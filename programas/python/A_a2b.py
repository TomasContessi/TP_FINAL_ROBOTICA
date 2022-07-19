from sympy import sin,cos,eye

#-------------------------------------------------------------------------------------------------------
# Esta funcion usa los parametros de DH del robot para darme la matriz de rototranslacion de un eje al otro
# son dos rotaciones en cadena extendidas con una translacion
def A_a2b(d,theta,alfa,a):
    A = eye(4) #inicializo A como la matriz de rototranslacion nula alias identidad

    A[0,0] = cos(theta)
    A[0,1] =-sin(theta)*cos(alfa)
    A[0,2] = sin(theta)*sin(alfa)
    A[0,3] = a*cos(theta)

    A[1,0] = sin(theta)
    A[1,1] = cos(theta)*cos(alfa)
    A[1,2] =-cos(theta)*sin(alfa)
    A[1,3] = a*sin(theta)

    A[2,1] = sin(alfa)
    A[2,2] = cos(alfa)
    A[2,3] = d

    return A
#-------------------------------------------------------------------------------------------------------
# esta funcion me pasa se pose vector a matrz de rototranslacion
# pos[0] = x
# pos[0] = y
# pos[0] = z
# pos[0] = theta
def P2A(pos):
    A = eye(4)
    A[0,0] = cos(pos[3])
    A[0,1] =-sin(pos[3])

    A[0,3] = pos[0]

    A[1,0] = sin(pos[3])
    A[1,1] = cos(pos[3])

    A[1,3] = pos[1]

    A[2,3] = pos[2]

    return A
#-------------------------------------------------------------------------------------------------------
