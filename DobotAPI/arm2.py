import keyboard
import time
from dobotapi.dobot import Dobot
from dobotapi.utils import get_coms_port
from dobotapi.effectors.suctioncup import SuctionCup

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)

def pickPlace(bot):
    print('picking and placing')

    home = {'x': 285, 'y': 15, 'z': 80}
    pickDown = {'x': 293, 'y': 45, 'z': 15}
    placeUp = {'x': 65, 'y': 230, 'z': 70}
    placeDown = {'x': 65, 'y': 230, 'z': -40}
    r = -29.7

    bot.move_to(home['x'], home['y'], home['z'], r)
    bot.move_to(pickDown['x'], pickDown['y'], pickDown['z'], r)
    cup.suck()
    bot.move_to(home['x'], home['y'], home['z'], r)
    bot.move_to(placeUp['x'], placeUp['y'], placeUp['z'], r)
    bot.move_to(placeDown['x'], placeDown['y'], placeDown['z'], r)
    cup.idle()
    bot.move_to(placeUp['x'], placeUp['y'], placeUp['z'], r)
    bot.move_to(home['x'], home['y'], home['z'], r)

def main():
    print("Dobot connected")
    while True:
        bot.conveyor_belt.move(-0.25)

        lis = []
        while True:  # Loop to capture keys continuously
            event = keyboard.read_event()
            num = str(event)[14]
            if num in ['0','1','2','3','4','5','6','7','8','9']:
                lis.append(int(num))
            
            if event.name == 'enter' and event.event_type == 'down':
                #print(lis[1:-1])
                bot.conveyor_belt.move(0)
                pickPlace(bot)
                break


        number = ''.join(str(digit) for digit in lis[1:-1])
        print(number)

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
