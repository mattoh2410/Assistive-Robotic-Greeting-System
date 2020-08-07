import datetime
import sys

from Drive import Drive
from Weather import Weather
from Face import Face
from Lights import Lights
import cozmo
import asyncio


class Welcome:
    def __init__(self, robot):
        self.robot = robot
        self.time = datetime.datetime.now()
        self.hour = self.time.strftime("%I")
        self.min = self.time.strftime("%M")
        self.day = self.time.strftime("%A")
        self.day_no = self.time.strftime("%d")
        self.month = self.time.strftime("%B")

    def set_date(self):
        if self.day_no == 1:
            self.day_no = "1st"
        elif self.day_no == 21:
            self.day_no = "21st"
        elif self.day_no == 2:
            self.day_no = "2nd"
        elif self.day_no == 22:
            self.day_no = "22nd"
        elif self.day_no == 3:
            self.day_no = "3rd"
        elif self.day_no == 23:
            self.day_no = "23rd"
        elif self.day_no == 31:
            self.day_no = "31st"
        else:
            self.day_no = self.day_no + "th"

    def hello(self, w, outfit, city, name):
        self.set_date()
        if self.time.strftime("%p") == "AM":
            m = "Good Morning"
        else:
            m = "Good Afternoon"

        self.robot.say_text("Hello" + m).wait_for_completed()
        self.robot.say_text(m + name + "the current time is" + self.hour + self.min).wait_for_completed()
        self.robot.say_text("the date is " + self.day + "the" + self.day_no +
                            "of" + self.month).wait_for_completed()
        self.robot.say_text("Your outfit will be displayed on the printout message")
        self.robot.say_text("Press Enter of you want me to collect them for you, or type exit to exit")
        print(m, name, "the current time is", self.hour, self.min)
        print("the date is ", self.day, "the", self.day_no, "of", self.month)
        print("in", city, "the weather will be", w.get_detailed_status(), "with temperatures around",
              w.get_temperature('celsius')['temp'], "celsius")
        print("Based on the current temperature, I think you should wear your", outfit,
              "Press Enter of you want me to collect them for you, or type exit to exit")


def cozmo_program(robot: cozmo.robot.Robot):
    f = Face(robot)
    f.find_person()
    d = Drive(robot)
    weather = Weather(f.city)
    weather.set_outfit()
    welcome = Welcome(robot)
    welcome.hello(weather.w, weather.outfit, f.city, f.name)
    e = input()
    if e == "exit":
        robot.say_text("Goodbye")
    else:
        l = Lights()
        l.set_lights(d, weather.number)
        d.find(weather.number)


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=False)

