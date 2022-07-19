from robot_t import *


Robot = robot()
Robot._home = [200,0,100,0]
Robot.A_base[2,3] = 95
Robot.A_herr[0,3] = 35
Robot.A_herr[2,3] = -135
Robot.inicar()
time.sleep(5)
Robot.moveJ([200,0,100,0])
time.sleep(2)


for i in range(0,5,1):
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


