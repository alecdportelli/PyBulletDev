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
p.setGravity(0, 0, -10)
angle = p.addUserDebugParameter('Steering', -0.5, 0.5, 0)
throttle = p.addUserDebugParameter('Throttle', 0, 20, 0)
car = p.loadURDF('simplecar.urdf', [0, 0, 0.1])
plane = p.loadURDF('simpleplane.urdf')
sleep(3)

wheel_indices = [1, 3, 4, 5]
hinge_indices = [0, 2]

while True:
    user_angle = p.readUserDebugParameter(angle)
    user_throttle = p.readUserDebugParameter(throttle)
    for joint_index in wheel_indices:
        p.setJointMotorControl2(car, joint_index,
                                p.VELOCITY_CONTROL,
                                targetVelocity=user_throttle)
    for joint_index in hinge_indices:
        p.setJointMotorControl2(car, joint_index,
                                p.POSITION_CONTROL, 
                                targetPosition=user_angle)
    p.stepSimulation()

