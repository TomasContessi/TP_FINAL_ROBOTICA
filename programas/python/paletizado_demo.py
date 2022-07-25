from robot_t import *


Robot = robot()
Robot._home = [200,0,100,0]
Robot.inicar()

input("start")

Robot.moveJ([200,0,100,0])
time.sleep(2)


for i in range(0,1,1):
    Robot.moveL([200,0,0,0],1)
    time.sleep(0.7)
    Robot.moveL([200,0,100,0],1)
    time.sleep(0.7)
    Robot.moveJ([0,-200,100,0])
    time.sleep(0.7)
    Robot.moveL([0,-200,0,0],1)
    time.sleep(0.7)
    Robot.moveL([0,-200,100,0],1)
    time.sleep(0.7)
    Robot.moveJ([200,0,100,0])
    time.sleep(0.7)

Robot.homeJ()
time.sleep(2)
Robot.shutdown()


