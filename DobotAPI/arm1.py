from dobotapi.utils import get_coms_port
from dobotapi.dobot import Dobot
from dobotapi.effectors.suctioncup import SuctionCup
import time
from csv import DictReader

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)

with open("coordinates_for_arm_1.csv", 'r') as f:
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)

home = list_of_dict[0]
pickUp = list_of_dict[1]
pickDown = list_of_dict[2]
placeUp = list_of_dict[3]
placeDown = list_of_dict[4]

r1 = 10
r2 = 47

def main():
    bot.move_to(int(home['x']),int(home['y']),int(home['z']))
    bot.move_to(int(pickUp['x']),int(pickUp['y']),int(pickUp['z']))
    bot.move_to(int(pickDown['x']),int(pickDown['y']),int(pickDown['z']))
    cup.suck()
    bot.move_to(int(pickUp['x']),int(pickUp['y']),int(pickUp['z']))
    bot.move_to(int(placeUp['x']),int(placeUp['y']),int(placeUp['z']),r2)
    bot.move_to(int(placeDown['x']),int(placeDown['y']),int(placeDown['z']))
    cup.idle()
    bot.move_to(int(placeUp['x']),int(placeUp['y']),int(placeUp['z']),r1)
    bot.move_to(int(home['x']),int(home['y']),int(home['z']))

while True:
        try:
                main()
        except KeyboardInterrupt:
                bot.close()
                print("Dobot disconnected")
        time.sleep(5)
