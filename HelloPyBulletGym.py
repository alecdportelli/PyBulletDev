'''
Hello Open AI gym PyBullet file
Code is courtesy of: https://gerardmaggiolino.medium.com/creating-openai-gym-environments-with-pybullet-part-1-13895a622b24

Author: Alec Portelli
alecportelli@icloud.com
alecdportelli.com
'''

import pybullet as p
import time
import pybullet_data
import gym
from time import sleep

p.connect(p.GUI)
car = p.loadURDF('simplecar.urdf')
number_of_joints = p.getNumJoints(car)
for joint_number in range(number_of_joints):
    info = p.getJointInfo(car, joint_number)
    print(info)




