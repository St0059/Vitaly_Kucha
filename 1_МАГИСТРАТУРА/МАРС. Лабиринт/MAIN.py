import time
import random

from zmqRemoteApi import RemoteAPIClient

print('Program started')

client = RemoteAPIClient()
sim = client.getObject('sim')

l_sens = sim.getObject('./LEFT')
r_sens = sim.getObject('./RIGHT')

wheelJoints=[-1,-1,-1,-1] #front left, rear left, rear right, front right
wheelJoints[0]=sim.getObject('./rollingJoint_fl')
wheelJoints[1]=sim.getObject('./rollingJoint_rl')
wheelJoints[2]=sim.getObject('./rollingJoint_rr')
wheelJoints[3]=sim.getObject('./rollingJoint_fr')

vx=12
vy=0
w=0

def setMovement(forwBackVel,leftRightVel,rotVel):
    #Apply the desired wheel velocities:
    sim.setJointTargetVelocity(wheelJoints[0],-forwBackVel-leftRightVel-rotVel)
    sim.setJointTargetVelocity(wheelJoints[1],-forwBackVel+leftRightVel-rotVel)
    sim.setJointTargetVelocity(wheelJoints[2],-forwBackVel-leftRightVel+rotVel)
    sim.setJointTargetVelocity(wheelJoints[3],-forwBackVel+leftRightVel+rotVel)

def control_move(l_sens, r_sens):
    _, out_l, _, _, _ = sim.readProximitySensor(l_sens)
    _, out_r, _, _, _ = sim.readProximitySensor(r_sens)
    mid = (out_l + out_r) / 2
    setMovement(vx, vy, w)
    if out_l < mid:   setMovement(vx, vy , 5)
    elif out_r < mid: setMovement(vx, vy , -5)
    if out_l == out_r == 0.0: setMovement(0, 0, w - 3)
    print('Левый борт: ', out_l, '\nПравый борт: ', out_r)


# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)



# Run a simulation in asynchronous mode:
sim.startSimulation()
while (t := sim.getSimulationTime()) < 3:
    s = f'Simulation time: {t:.2f} [s] (simulation running asynchronously '\
        'to client, i.e. non-stepped)'
    print(s)
    sim.addLog(sim.verbosity_scriptinfos, s)
sim.stopSimulation()
# If you need to make sure we really stopped:
while sim.getSimulationState() != sim.simulation_stopped:
    time.sleep(0.1)

# Run a simulation in stepping mode:
client.setStepping(True)
sim.startSimulation()
while (t := sim.getSimulationTime()) < 50:
    s = f'Simulation time: {t:.2f} [s] (simulation running synchronously '\
        'to client, i.e. stepped)'
    print(s)
    sim.addLog(sim.verbosity_scriptinfos, s)


    control_move(l_sens, r_sens)
    #youBot motion

    client.step()  # triggers next simulation step

#youBot stop
setMovement(0, 0, 0)

sim.stopSimulation()


# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

print('Program ended')