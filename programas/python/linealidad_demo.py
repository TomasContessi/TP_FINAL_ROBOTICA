from robot_t import *

Robot = robot()
Robot._home = [80,0,50,0]
Robot.A_base[2,3] = 100
Robot.A_base[0,3] = -60

Robot.A_herr[0,3] = -7
Robot.A_herr[2,3] = -135


Robot.inicar()
Robot.homeJ()

input("start")
Robot.moveJ([80,100,30,0])
time.sleep(0.7)
for i in range(0,10,1):
    Robot.moveL([80,100,0,0],10)
    Robot.moveL([80,-100,0,0],10)

    
Robot.homeJ()
time.sleep(0.7)
Robot.shutdown()