from math import pi

from zmqRemoteApi import RemoteAPIClient

print('Program started')

client = RemoteAPIClient()
sim = client.getObject('sim')


wheel_Joints=[-1,-1,-1,-1] #front left, rear left, rear right, front right
wheel_Joints[0]=sim.getObject('./rollingJoint_fl')
wheel_Joints[1]=sim.getObject('./rollingJoint_rl')
wheel_Joints[2]=sim.getObject('./rollingJoint_rr')
wheel_Joints[3]=sim.getObject('./rollingJoint_fr')


#SetMovement с м/c и рад/с
def setMovement(Vy, Vx, W):
    w0 = (Vy + Vx + 0.385 * W) / 0.05
    w1 = (Vy - Vx + 0.385 * W) / 0.05
    w2 = (Vy + Vx - 0.385 * W) / 0.05
    w3 = (Vy - Vx - 0.385 * W) / 0.05

    sim.setJointTargetVelocity(wheel_Joints[0], -w0)
    sim.setJointTargetVelocity(wheel_Joints[1], -w1)
    sim.setJointTargetVelocity(wheel_Joints[2], -w2)
    sim.setJointTargetVelocity(wheel_Joints[3], -w3)

    return Vy, Vx, W


x, y, orientation = 0.0, 0.0, 0.0
def calc_ODOMETRY(v, w):
    global x, y, orientation
    dt = 0.05
    orientation += round(w * dt * 180 / pi, 4)

    x += round((v * dt), 4)

    return x, orientation

l_sens = sim.getObject('./LEFT')
r_sens = sim.getObject('./RIGHT')
hole = []
i = 0
def control_move(l_sens, r_sens, t):
    global hole, i
    Vy, Vx, W = setMovement(0.25, 0, 0)
    pos, orientation = calc_ODOMETRY(Vy, W)
    _, out_l, _, _, _ = sim.readProximitySensor(l_sens)
    _, out_r, _, _, _ = sim.readProximitySensor(r_sens)
    mid = (out_l + out_r) / 2
    if out_l < mid:   setMovement(Vy, Vx + 0.1, W)
    elif out_r < mid: setMovement(Vy, Vx - 0.1, W)
    elif out_l == out_r: setMovement(Vy, 0, 0)
    if t > 0 and (out_l == 0.0 or out_r == 0.0):
        if i == 0: print(f'Появилось отверстие\n позиция = {pos}')
        hole.append(pos)
        i=1
    elif i > 0 and (out_l != 0.0 or out_r != 0.0):
        distance = hole[-1] - hole[0]
        i = 0
        hole = []
        if distance > 0.6 : print(f'Ширина отверстия = {distance}\n Текущая позиция = {pos}') # 0.6 - безопасное расстояние

    print(f'Текущая позиция : {pos}')



# When simulation is not running, ZMQ message handling could be a bit
# slow, since the idle loop runs at 8 Hz by default. So let's make
# sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)


# Run a simulation in stepping mode:
client.setStepping(True)
sim.startSimulation()

while (t := sim.getSimulationTime()) < 16:
    if t > 0: control_move(l_sens, r_sens, t)

    s = f'Simulation time: {t:.2f} [s] (simulation running synchronously ' \
        'to client, i.e. stepped)'
    print(s)
    sim.addLog(sim.verbosity_scriptinfos, s)
    client.step()  # triggers next simulation step



#youBot stop


sim.stopSimulation()


# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

print('Program ended')