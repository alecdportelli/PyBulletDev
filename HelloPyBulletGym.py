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

# Init Env
client = p.connect(p.GUI)
p.setGravity(0, 0, -9.8, physicsClientId=client) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Import assets 
planeId = p.loadURDF("plane.urdf")
carId = p.loadURDF("racecar/racecar.urdf", basePosition=[0,0,0.2])

# Get car position and rotation
position, orientation = p.getBasePositionAndOrientation(carId)

# Run sim
for _ in range(300): 
    pos, ori = p.getBasePositionAndOrientation(carId)
    p.applyExternalForce(carId, 0, [50, 0, 0], pos, p.WORLD_FRAME)
    p.stepSimulation()




