from robot_t import *

Robot = robot()
Robot._home = [180,0,50,0]
Robot.A_base[2,3] = 100
Robot.A_base[0,3] = -60

Robot.A_herr[0,3] = -7
Robot.A_herr[2,3] = -115


Robot.inicar()
Robot.homeJ()

input("start")

for i in range(0,30,1):
    Robot.moveJ([150,0,70,0])
    time.sleep(0.7)
    Robot.moveL([150,0,0,0],1)
    Robot.moveL([150,0,70,0],1)
    Robot.moveJ([100,0,70,0])
    time.sleep(0.7)
    Robot.moveL([100,0,0,0],1)
    Robot.moveL([100,0,50,0],1)
    Robot.moveJ([100,100,50,0])
    time.sleep(0.7)
    Robot.moveL([100,100,0,0],1)
    Robot.moveL([100,100,50,0],1)
    Robot.moveJ([100,-100,50,0])
    time.sleep(0.7)
    Robot.moveL([100,-100,0,0],1)
    Robot.moveL([100,-100,50,0],1)
    
Robot.homeJ()
time.sleep(0.7)
Robot.shutdown()