from robot_t import *


Robot = robot()
Robot._home = [-10,0,100,0]
Robot.A_base[2,3] = 100
Robot.A_base[0,3] = -60
Robot.inicar()

input("start")

Robot.moveJ([150,100,100,0])
time.sleep(2)


for i in range(0,1,1):
    Robot.moveJ([150,100,50,0])
    time.sleep(0.7)
    Robot.moveL([170,100,50,0],1)
    Robot.moveL([170,100,100,0],1)
    Robot.moveL([170,-100,100,0],1)
    Robot.moveL([170,-100,50,0],1)
    Robot.moveL([150,-100,50,0],1)
    Robot.moveJ([150,-100,100,0])
    time.sleep(0.7)

    Robot.moveJ([100,100,50,0])
    time.sleep(0.7)
    Robot.moveL([120,100,50,0],1)
    Robot.moveL([120,100,100,0],1)
    Robot.moveL([170,100,100,0],1)
    Robot.moveL([170,100,50,0],1)
    Robot.moveL([150,100,50,0],1)
    Robot.moveJ([150,100,100,0])
    time.sleep(0.7)

    Robot.moveJ([100,-100,50,0])
    time.sleep(0.7)
    Robot.moveL([120,-100,50,0],1)
    Robot.moveL([120,-100,100,0],1)
    Robot.moveL([120,100,100,0],1)
    Robot.moveL([120,100,50,0],1)
    Robot.moveL([100,100,50,0],1)
    Robot.moveJ([100,100,100,0])
    time.sleep(0.7)

    Robot.moveJ([150,-100,50,0])
    time.sleep(0.7)
    Robot.moveL([170,-100,50,0],1)
    Robot.moveL([170,-100,100,0],1)
    Robot.moveL([120,-100,100,0],1)
    Robot.moveL([120,-100,50,0],1)
    Robot.moveL([100,-100,50,0],1)
    Robot.moveJ([100,-100,100,0])
    time.sleep(0.7)
    
Robot.homeJ()
time.sleep(2)
Robot.shutdown()