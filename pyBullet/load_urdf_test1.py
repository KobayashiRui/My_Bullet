import pybullet as p
import time

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally p.setGravity(0,0,-10)
planeId = p.loadURDF("../data/plane.urdf")
#boxId = p.loadSDF("../data/two_cubes.sdf",cubeStartPos, cubeStartOrientation) 
#boxId = p.loadURDF("../my_data/test_data_v8/model.urdf") 
boxId = p.loadURDF("../my_data/mini_v3/model.urdf") 
p.setGravity(0, 0, -10)
maxForce = 0
mode = p.VELOCITY_CONTROL
#p.setJointMotorControl2(boxId, 0, controlMode=mode, force=maxForce)
for joint in range(p.getNumJoints(boxId)):
  info = p.getJointInfo(boxId, joint)
  p.setJointMotorControl2(boxId, joint, controlMode=mode, force=maxForce)
  print("info")
  print(info)
for i in range (100000):
    p.stepSimulation()
    time.sleep(1./1000.)
p.disconnect()