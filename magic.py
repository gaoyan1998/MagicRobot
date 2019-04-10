import sys

import fire

from robot import config
from robot.Conversation import Conversation
from server import server
from wukong import Wukong

wukong = None
conversation = None

if __name__ == '__main__':
    if len(sys.argv) == 1:
        conversation = Conversation(False)
        wukong = Wukong(conversation)
        config.init()

        server.run(conversation, wukong)
        # wukong.run()
    else:
        fire.Fire(Wukong)
