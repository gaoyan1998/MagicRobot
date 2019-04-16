# -*- coding: utf-8-*-
from robot.sdk.AbstractPlugin import AbstractPlugin
from robot import weatherGet


class Plugin(AbstractPlugin):

    def handle(self, text, parsed):
        # self.say('', cache=True)
        data = weatherGet.get_weather_data()
        message = "早安!愿你又是美好一天。"
        message += data['basic']['location'] + data['now']['cond_txt'] + ",室外温度" + data['now']['hum'] + "," + \
                   data['now']['wind_dir'] + data['now']['wind_spd'] + "级," + data['lifestyle'][0]['txt']
        message += "，您今天有什么安排呢？"
        # self.con.doResponse(query=message)
        self.say(message, cache=False)

    def isValid(self, text, parsed):
        return "早安" in text
