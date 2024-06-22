
# pip install pyzmq cbor keyboard

import keyboard
from zmqRemoteApi import RemoteAPIClient
from zmqRemoteApi_IPv6 import RemoteAPIClient

import random
import math



client = RemoteAPIClient('localhost', 23000)
#client = RemoteAPIClient('2001:288:6004:17:2023:cda:4:6', 23000)

print('Program started')
sim = client.getObject('sim')
#sim.startSimulation()
print('Simulation started')

v=4
a=40

#選擇控制的球員
player='/qqqq'



def setVelocity(lfwV, rfwV,lbwV, rbwV):
    leftMotor1 = sim.getObject(player+'/1')
    rightMotor1 = sim.getObject(player+'/2')
    leftMotor2 = sim.getObject(player+'/3')
    rightMotor2 = sim.getObject(player+'/4')
    sim.setJointTargetVelocity(leftMotor1, lfwV)
    sim.setJointTargetVelocity(rightMotor1, rfwV)
    sim.setJointTargetVelocity(leftMotor2, lbwV)
    sim.setJointTargetVelocity(rightMotor2, rbwV)
    #輸入四個變數分別給四個軸速度
    

def turnover():
    floor= sim.getObject('/Floor')
    player1 = sim.getObject(player)
    a=sim.getObjectOrientation(player1,floor)
    b=sim.getObjectPosition(player1,floor)
    a[0]=0
    a[1]=0
    b[2]=0.3
    sim.setObjectPosition(player1,floor,b)
    sim.setObjectOrientation(player1,floor,a)
def playercontrol(x):
    if keyboard.is_pressed('w'):
        setVelocity(-x, -x, -x, -x)
    elif keyboard.is_pressed('s'):
        setVelocity(x, x, x, x)
    elif keyboard.is_pressed('space'):
        turnover()
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setVelocity(0, 0, 0, 0)

while True:
    if keyboard.is_pressed('shift'):
        playercontrol(v + 4)
    else:
        playercontrol(v)