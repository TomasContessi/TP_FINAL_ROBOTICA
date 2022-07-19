from sympy import *
from robot_t import *
import re

Robot = robot()

Robot.inicar()


pose = [90,90,90,0]
s1 = "100,0,0,0"

while s1 != "end":
    
    pose=[int(x) for x in re.findall(r'[^,.]+', ''.join(s1.split()))]
    if len(pose) != 4:
        pose = [120,0,90,0]
    
    pose[3] = rad(pose[3])
    Robot.moveJ(pose)
    
    s1 = input("pose = ")
    

Robot.shutdown()



