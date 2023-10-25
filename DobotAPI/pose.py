import time

from dobotapi.dobot import Dobot
from dobotapi.utils import get_coms_port
from dobotapi.effectors.suctioncup import SuctionCup

bot = Dobot()
bot.connect()
cup = SuctionCup(bot = bot)

def main():
    print('dobot connected')
    while True:
        pose = bot.get_pose()
        print(pose.position.x,' ',pose.position.y,' ',pose.position.z)
        time.sleep(2)

try:
    main()
except KeyboardInterrupt:
    bot.close()
    print("Dobot disconnected")