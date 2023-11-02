#import keyboard
import time
from dobotapi.dobot import Dobot
from dobotapi.utils import get_coms_port
from dobotapi.effectors.suctioncup import SuctionCup
from csv import DictReader

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)

def pickPlace(bot):
    print('picking and placing')

    with open("coordinates_for_arm_2.csv", 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader) 
    r = -29.7
    home = list_of_dict[0]
    pickDown = list_of_dict[1]
    placeUp = list_of_dict[2]
    placeDown = list_of_dict[3]

    bot.move_to(int(home['x']), int(home['y']), int(home['z'], r))
    bot.move_to(int(pickDown['x']), int(pickDown['y']), int(pickDown['z'], r))
    cup.suck()
    bot.move_to(int(home['x']), int(home['y']), int(home['z'], r))
    bot.move_to(int(placeUp['x']), int(placeUp['y']), int(placeUp['z']), r)
    bot.move_to(int(placeDown['x']), int(placeDown['y']), int(placeDown['z']), r)
    cup.idle()
    bot.move_to(int(placeUp['x']), int(placeUp['y']), int(placeUp['z']), r)
    bot.move_to(int(home['x']), int(home['y']), int(home['z'], r))

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
