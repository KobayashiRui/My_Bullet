import pybullet as p
import time

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally p.setGravity(0,0,-10)
#planeId = p.loadURDF("../data/plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
#boxId = p.loadSDF("../data/two_cubes.sdf",cubeStartPos, cubeStartOrientation) 
boxId = p.loadSDF("../data/two_cubes.sdf")
p.setGravity(0, 0, -10)

print("boxid")
print(boxId)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()