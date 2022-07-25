from math import degrees
from numbers import Real
from sympy import *
import sympy
from A_a2b import P2A, A_a2b
import serial,time
from empaquetador import empaquetar

class robot:
    _pos = [0,0,0,0] #pose del robot actual, no tocar
    _d = [0,0,0,0,0] #parametro de dh d
    _alfa = [-pi/2,0,0,pi/2,0] #parametro de dh alfa 
    _a = [0,115,117,25,0] #parametro de dh a
    _vth_max = (5/3)*pi
    _home = [50,0,0,0] #home del robot, tocar con cuidado

    Ts = 20*10**(-3) #sample time del ciclo de control, si se modifica modificar tambien en el arduino
    offsets_motores = [95,50,90,85] #cuan torcidos pusiste los motores, con esto se ajusta para calibrar los angulos
    theta = [0,0,0,0] #parametro de dh theta, que ademas es la posicion de los motores
    A04 = eye(4) #transformacion que representa la pose actual del robot, tocar con cuidadoy de preferencia no tocar
    A_base = eye(4) #transformacion que representa la base del robot, asi toma el 0 en el cruce entre los ejes 1 y 2
    A_herr = eye(4) #transformcacion que representa la herramienta
    gripper = 0 #estado del gripper, 1 andando, 0 apagado
    motors = 0 #estado de los motores, 1 andando, 0 apagados
    puerto = 'COM5' # esto va a cambiar segun donde se conecte y hasta ahora no se como hacer para autodetectarlo
    brate = 115200 #baudrate, no tocar o si se toca cambiar tambien del arduino
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
    # Metodo que me calcula la cinematica directa del robot con los Q pasados por argumento
    # me devuelve la transformacion entre la base del robot y la herramienta, pero tambien guarda el A04
    # Q0 theta_1
    # Q1 theta_2
    # Q2 theta_3
    # Q3 theta_4
    def dir_cinematics(self,Q):   

        A = eye(4) #inicializo A como la matriz de rototranslacion nula alias identidad

        A[0,0] = -sin(Q[0])*sin(Q[3]) + cos(Q[0])*cos(Q[3])
        A[0,1] = -sin(Q[0])*cos(Q[3]) - cos(Q[0])*sin(Q[3])
        A[0,2] = 0
        A[0,3] = (self._a[1]*cos(Q[1]) + self._a[2]*cos(Q[1]+Q[2]) + self._a[3])*cos(Q[0])

        A[1,0] =  sin(Q[0])*cos(Q[3]) + cos(Q[0])*sin(Q[3])
        A[1,1] = -sin(Q[0])*sin(Q[3]) + cos(Q[0])*cos(Q[3])
        A[1,2] = 0
        A[1,3] = (self._a[1]*cos(Q[1]) + self._a[2]*cos(Q[1]+Q[2]) + self._a[3])*sin(Q[0])

        A[2,3] = -self._a[1]*sin(Q[1]) - self._a[2]*sin(Q[1]+Q[2])

        #A = sympy.simplify(A)
        return self.A_base * A * self.A_herr

#-------------------------------------------------------------------------------------------------------
# Este metodo me devuelve la matriz A04 expresada en funcion de los th
    def A04sym(self):
        A04_sym = eye(4)
        Q = symbols('th1,th2,th3,thni,th4')

        for  i in  range(0,5,1):
            A04_sym = A04_sym * A_a2b(self._d[i],Q[i],self._alfa[i],self._a[i])
        
        A04_sym = sympy.simplify( A04_sym )
        A04_sym = Subs(A04_sym,Q[3],-(Q[1]+Q[2]))
        return sympy.simplify( A04_sym )
#-------------------------------------------------------------------------------------------------------
    # Metodo que me calcula la cinematica inversa del robot con la Abase-brida (Abb) pasado por argumento
    # me devuelve las posiciones de las articulaciones del robot, este robot por su mecanica tiene siempre
    # solo una configuracion valida (brazo hacia arriba) asi que no es necesario pasarle un vector de 
    # configuracion, pero se lo voy a agregar para generalizar el modelo, cfg=1 es brazo hacia arriba,
    # cfg=-1 es brazo hacia abajo
    # Q0 theta_1
    # Q1 theta_2
    # Q2 theta_3
    # Q3 theta_4
    def inv_cinematics_c(self,Abb,cfg):
        A = self.A_base.inv() * Abb * self.A_herr.inv()
        th = [0,0,0,0]

        th[0] = atan2(A[1,3],cfg*A[0,3]) # calculo th 0
    
        s1=sin(th[0])
        
        c1=cos(th[0])

        s4 = A[1,0]*c1 - A[0,0]*s1 

        if c1 == 0: # uso la expresion que no se rompa por la singularidad de la division
            b = A[1,3]/s1 - self._a[3]
            c4 = -(A[0,1] + s4*c1)/s1
        else:
            b = A[0,3]/c1 - self._a[3]
            c4 = (A[0,0] + s4*s1)/c1

        # calculo th 4     
        th[3] = atan2(s4,c4) 

        c3 = ((b)**2 + A[2,3]**2 - (self._a[1]**2 + self._a[2]**2))/(2*self._a[1]*self._a[2]) # ahora calculo th3
        s3 = sqrt(1-c3**2)
        th[2] = atan2(s3,c3)
        

        # por ultimo calculo th2

        s2=(self._a[2]*(-A[2,3]*c3-b*s3)-self._a[1]*A[2,3])/(b**2 + A[2,3]**2)
        c2=(self._a[2]*(-A[2,3]*s3+b*c3)+self._a[1]*b)/(b**2 + A[2,3]**2)

        th[1] = atan2(s2,c2)

        return th
#-------------------------------------------------------------------------------------------------------
# el mismo metodo pero para no tener que poner siempre el cfg que no se necesita 
# (el brazo siemre mira arriba)
    def inv_cinematics(self,Abb):
        return self.inv_cinematics_c(Abb,1)
#-------------------------------------------------------------------------------------------------------
# metodo que inicia la posicion del robot y lo manda a home, no se por que pero cuando se establece la coneccion
# algo raro le pasa al arduino y el motor se mueve para cualquier lado o en el mejor de los casos apaga los motores
    def inicar(self):
        self.A04 = P2A (self._home)
        self._pos = self._home
        self.theta = self.inv_cinematics(self.A04)
        self.arduino = serial.Serial(self.puerto,self.brate)
        self.arduino.flushInput()
        self.arduino.flushOutput()
        time.sleep(0.7)
        self.motors = 1
        self.homeJ()

        
#-------------------------------------------------------------------------------------------------------
# metodo que manda al robot a hacer un home
    def homeJ(self):
        self.moveJ(self._home)
#-------------------------------------------------------------------------------------------------------
# metodo que hace al robot hacer un movimiento joint entre su pose actual y la pose deseada

# por ahora no le puse velocidad
    def moveJ(self,pose):
        A = P2A(pose)
        Q = self.inv_cinematics(A)
        self.stream(Q)
        self.A04 = A
        self._pos = pose
        self.theta = Q
#-------------------------------------------------------------------------------------------------------
# metodo que hace los movimientos lineales, los hace con muchos movimientos joint chiquitos
    def moveL(self,pose,tiempo):
        N_steps = tiempo/self.Ts
        for i in range(0,int(N_steps),1):
            dx = (pose[0] - self._pos[0])/(N_steps - i)
            dy = (pose[1] - self._pos[1])/(N_steps - i)
            dz = (pose[2] - self._pos[2])/(N_steps - i)
            dth= (pose[3] - self._pos[3])/(N_steps - i)
            
            #self._pos = self._pos + [dx,dy,dz,dth]
            self._pos[0] = self._pos[0] + dx
            self._pos[1] = self._pos[1] + dy
            self._pos[2] = self._pos[2] + dz
            self._pos[3] = self._pos[3] + dth

            
            self.A04 = P2A(self._pos)
            self.theta = self.inv_cinematics(self.A04)

            self.stream(self.theta)

#-------------------------------------------------------------------------------------------------------
# metodo que envia el comando al robot, se podria hacer tambien que ademas de recibir un echo reciba informacion de sensores
    def stream(self,Q):
        startMarker = "."
        x = "z"

        paquete = empaquetar(self.dh2rob(Q),self.gripper,self.motors)


        print (paquete.encode())

        self.arduino.write(paquete.encode())

        while  x != startMarker.encode(): #me quedo esperando el echo (por ahora no hay timeout)
            x = self.arduino.read()

        return 
#-------------------------------------------------------------------------------------------------------
# metodo que apaga el robot, en si lo que hace es liberar el puerto
    def shutdown(self):
        self.motors = 0
        self.gripper = 0
        self.stream(self.theta)
        self.arduino.flushInput()
        self.arduino.flushOutput()
        time.sleep(1)
        print("apagado")
        self.arduino.close()
#-------------------------------------------------------------------------------------------------------
# metodo que me pasa de los angulos en radianes de la cinematica a los angulos en grados que necesita el robot
    def dh2rob(self,Q):
        V = [0,0,0,0]
        V[0] = int(self.offsets_motores[0] + degrees(Q[0]))
        V[1] = int(self.offsets_motores[1] - degrees(Q[1]))
        V[2] = int(self.offsets_motores[2] + degrees(Q[2]) - V[1])
        V[3] = int(self.offsets_motores[3] + degrees(Q[3]))
        return V