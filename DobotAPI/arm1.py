from dobotapi.utils import get_coms_port
from dobotapi.effectors.suctioncup import SuctionCup
import time

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)

home = {'x': 215, 'y': 45, 'z': 135}
pickUp = {'x' : 130, 'y' : 185, 'z' : 115}
pickDown = {'x': 145, 'y': 175, 'z': -50}
placeUp = {'x': 230, 'y': 145, 'z': 90}
placeDown = {'x': 240, 'y': 150, 'z': 10}
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
