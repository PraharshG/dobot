from dobotapi.utils import get_coms_port
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
    bot.move_to(home['x'],home['y'],home['z'])
    bot.move_to(pickUp['x'],pickUp['y'],pickUp['z'])
    bot.move_to(pickDown['x'],pickDown['y'],pickDown['z'])
    cup.suck()
    bot.move_to(pickUp['x'],pickUp['y'],pickUp['z'])
    bot.move_to(placeUp['x'],placeUp['y'],placeUp['z'],r2)
    bot.move_to(placeDown['x'],placeDown['y'],placeDown['z'])
    cup.idle()
    bot.move_to(placeUp['x'],placeUp['y'],placeUp['z'],r1)
    bot.move_to(home['x'],home['y'],home['z'])

while True:
        try:
                main()
        except KeyboardInterrupt:
                bot.close()
                print("Dobot disconnected")
        time.sleep(5)
