import time
import multiprocessing
from dobotapi.dobot import Dobot
from dobotapi.utils import get_coms_port
from dobotapi.effectors.suctioncup import SuctionCup

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)

def pickPlace(bot):
    print('picking and placing')

    home = {'x': 200, 'y': -60, 'z': 95}
    pickDown = {'x': 225, 'y': -195, 'z': 5}
    placeUp = {'x': 160, 'y': 205, 'z': 60}
    placeDown = {'x': 160, 'y': 205, 'z': -45}
    r = -29.7

    bot.move_to(home['x'], home['y'], home['z'], r)
    bot.move_to(pickDown['x'], pickDown['y'], pickDown['z'], r)
    cup.suck()
    bot.move_to(placeUp['x'], placeUp['y'], placeUp['z'], r)
    bot.move_to(placeDown['x'], placeDown['y'], placeDown['z'], r)
    cup.idle()
    bot.move_to(placeUp['x'], placeUp['y'], placeUp['z'], r)
    bot.move_to(home['x'], home['y'], home['z'], r)

def main():
    print("Dobot connected")
    bot.ir_toggle(True)
    forpnp(bot)
    #pnp = multiprocessing.Process(target = forpnp , args = (bot,))
    #gp = multiprocessing.Process(target = getpose , args = (bot,))
    #pnp.start()
    #gp.start()
    #pnp.join()
    #gp.join()

def forpnp(bot):
    while True:
        if not bot.get_ir():
            bot.conveyor_belt.move(0.25)
            time.sleep(1)
        else:
            bot.conveyor_belt.move(0)
            pickPlace(bot)
        time.sleep(0.1)

def getpose(bot):
    while True:
        pose = bot.get_pose()
        print(pose.position.x,' ',pose.position.y,' ',pose.position.z)
        time.sleep(2)

try:
    main()
except KeyboardInterrupt:
    bot.close()
    print("Dobot disconnected")
