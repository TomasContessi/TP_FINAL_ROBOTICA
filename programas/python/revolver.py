from robot_t import *


Robot = robot()
Robot._home = [50,0,0,0]

Robot.inicar()

Robot.homeJ()
input("start")
Robot.moveJ([100,0,140,0])

for i in range(0,8,1):
    #time.sleep(0.7)
    Robot.moveL([200,0,140,0],0.5)
    #time.sleep(0.7)
    Robot.moveL([200,0,0,0],0.5)
    

time.sleep(0.7)
Robot.homeJ()
time.sleep(2)
Robot.shutdown()