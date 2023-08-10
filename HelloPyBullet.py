import pybullet as p
import time
import pybullet_data

# p.DIRECT for non-graphical version
physicsClient = p.connect(p.GUI)

# Get data path
p.setAdditionalSearchPath(pybullet_data.getDataPath()) 

# Set gravity 
p.setGravity(0,0,-9.8)

# Load ground
planeId = p.loadURDF('plane.urdf')

# Init start position
cubeStartPos = [0,0,1]

# Init rotation
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])

# Create ID for scripting 
boxId = p.loadURDF('r2d2.urdf',cubeStartPos, cubeStartOrientation)

# Run sim for certain amount of time 
for i in range (10000):
   p.stepSimulation()
   time.sleep(1./240.)

# Get position and rotation
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)

# Print the information
print(cubePos,cubeOrn)

# Disconnect from GUI
p.disconnect()


