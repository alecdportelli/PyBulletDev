import pybullet as p
import time
import pybullet_data

# p.DIRECT for non-graphical version
physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF('plane.urdf')
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF('r2d2.urdf',cubeStartPos, cubeStartOrientation)

for i in range (10):
   p.stepSimulation()
   time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print("GLEE")
print(cubePos,cubeOrn)

p.disconnect()


