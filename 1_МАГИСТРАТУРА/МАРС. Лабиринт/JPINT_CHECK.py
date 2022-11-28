import time
from math import pi, fabs
from zmqRemoteApi import RemoteAPIClient

print('Program started')

client = RemoteAPIClient()
sim = client.getObject('sim')


youbot = sim.getObject('./youBot')
wheel_Joints=[-1,-1,-1,-1] #front left, rear left, rear right, front right
wheel_Joints[0]=sim.getObject('./rollingJoint_fl')
wheel_Joints[1]=sim.getObject('./rollingJoint_rl')
wheel_Joints[2]=sim.getObject('./rollingJoint_rr')
wheel_Joints[3]=sim.getObject('./rollingJoint_fr')

'''

def setMovement(Vx, Vy, W):
    #Apply the desired wheel velocities:
    sim.setJointTargetVelocity(wheel_Joints[0],-Vx - Vy - W)
    sim.setJointTargetVelocity(wheel_Joints[1],-Vx + Vy - W)
    sim.setJointTargetVelocity(wheel_Joints[2],-Vx - Vy + W)
    sim.setJointTargetVelocity(wheel_Joints[3],-Vx + Vy + W)

    return Vy, Vx, W
'''
#SetMovement с м/c
def setMovement(Vy, Vx, W):
    w0 = (Vy + Vx + (0.242 + 0.15) * W) / 0.05
    w1 = (Vy - Vx + (0.242 + 0.15) * W) / 0.05
    w2 = (Vy + Vx - (0.242 + 0.15) * W) / 0.05
    w3 = (Vy - Vx - (0.242 + 0.15) * W) / 0.05

    sim.setJointTargetVelocity(wheel_Joints[0], -w0)
    sim.setJointTargetVelocity(wheel_Joints[1], -w1)
    sim.setJointTargetVelocity(wheel_Joints[2], -w2)
    sim.setJointTargetVelocity(wheel_Joints[3], -w3)

    return Vy, Vx, W


# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)


# Run a simulation in stepping mode:
client.setStepping(True)
sim.startSimulation()
orientation = 0.0
pos = 0.0
pos_CS = sim.getObjectPosition(youbot, -1)
while (t := sim.getSimulationTime()) <= 10:
    V, _, W = setMovement(0.3, 0, 0)

    pos += V * 0.05
    s = f'Simulation time: {t:.2f} [s] (simulation running synchronously '\
        'to client, i.e. stepped)'


    sim.addLog(sim.verbosity_scriptinfos, s)
    client.step()  # triggers next simulation step
#youBot stop
pos_CF = sim.getObjectPosition(youbot, -1)
ITOG = fabs(pos_CF[1] - pos_CS[1])

print(f'\n\nРасстояние из копеллии = {ITOG}\n\nРасстояние по одометрии = {pos}')

sim.stopSimulation()


# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

print('\n\nProgram ended')