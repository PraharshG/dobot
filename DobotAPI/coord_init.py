import time
import csv
from dobotapi.dobot import Dobot
from dobotapi.utils import get_coms_port
from dobotapi.effectors.suctioncup import SuctionCup

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)
fields = ['pos','x','y','z']
def main():
    print('dobot connected')
    for x in range(4):
        print('Select option:')
        if(input() == '1'):
            home = bot.get_pose()
        elif(input() == '2'):
            PickUP = bot.get_pose()
        elif(input() == '3'):
            pickDown = bot.get_pose()
        elif(input() == '4'):
            placeUp = bot.get_pose()
        elif(input() == '5'):
            placeDown = bot.get_pose()
    filename = "coords.csv"
 
    mydict =[{'pos': 'home', 'x': home.position.x, 
            'y': home.position.y, 'z': home.position.y},
            {'pos': 'PickUP', 'x': PickUP.position.x, 
            'y': PickUP.position.y, 'z': PickUP.position.z},
            {'pos': 'pickDown', 'x': pickDown.position.x, 
            'y': pickDown.position.y, 'z': pickDown.position.z},
            {'pos': 'placeUp', 'x': placeUp.position.x, 
            'y': placeUp.position.y, 'z': placeUp.position.z},
            {'pos': 'placeDown', 'x': placeDown.position.x, 
            'y': placeDown.position.y, 'z': placeDown.position.z}]

# writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
     
    # writing headers (field names)
        writer.writeheader()
     
    # writing data rows
        writer.writerows(mydict)
    time.sleep(2)

try:
    main()
except KeyboardInterrupt:
    bot.close()
    print("Dobot disconnected")
