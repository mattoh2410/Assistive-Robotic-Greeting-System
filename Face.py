import asyncio
import sys

import cozmo
from cozmo import robot


class Face:
    def __init__(self, robot):
        self.r = robot
        self.person = self.person = ["matthew", "Glasgow,GB"], ["jennifer", "Edinburgh,GB"]
        self.name = None
        self.city = None

    def find_person(self, ):
        self.r.move_lift(-3)
        self.r.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
        try:
            self.r.world.wait_for_observed_face(timeout=30)
        except asyncio.TimeoutError:
            "exit"
        for visible_face in self.r.world.visible_faces:
            if visible_face.name is not None:
                for i in self.person:
                    if i[0] == visible_face.name:
                        self.name = i[0]
                        print(self.name)
                        self.city = i[1]
                        print(self.city)

        if self.name is None:
            print("Can't recognise any faces")
            exit

