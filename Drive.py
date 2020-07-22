import cozmo
from cozmo.util import Pose, degrees
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id


class Drive:

    def __init__(self, robot):
        self.robot = robot
        self.shorts = robot.world.get_light_cube(LightCube1Id)
        self.sun_glasses = robot.world.get_light_cube(LightCube2Id)
        self.jacket = robot.world.get_light_cube(LightCube3Id)
        self.cube_number = 3

    def find(self, number):
        print(number)
        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cubes = self.robot.world.wait_until_observe_num_objects(num=self.cube_number,
                                                                object_type=cozmo.objects.LightCube,
                                                                timeout=10)
        print("Found %s cubes" % len(cubes))

        lookaround.stop()
        if number == 1:
            for i in cubes:
                if i == self.jacket:
                    action = self.robot.pickup_object(self.jacket, num_retries=3)
                    action.wait_for_completed()
                    self.robot.go_to_pose(Pose(0, 0, 0, angle_z=degrees(180)),
                                          relative_to_robot=False).wait_for_completed()
                    self.robot.say_text("here is your jacket").wait_for_completed()
                    action = self.robot.place_object_on_ground_here(i)
                    action.wait_for_completed()
                    break
        elif number == 2:
            for i in cubes:
                if i == self.shorts:
                    action = self.robot.pickup_object(self.shorts, num_retries=3)
                    action.wait_for_completed()
                    self.robot.go_to_pose(Pose(-9.3, -173, 0, angle_z=degrees(180)),
                                          relative_to_robot=False).wait_for_completed()
                    self.robot.say_text("here are your shorts").wait_for_completed()
                    action = self.robot.place_object_on_ground_here(i)
                    action.wait_for_completed()

        elif number == 3:
            for i in cubes:
                if i == self.shorts:
                    action = self.robot.pickup_object(self.shorts, num_retries=3)
                    action.wait_for_completed()
                    self.robot.go_to_pose(Pose(-9.3, -173, 0, angle_z=degrees(180)),
                                          relative_to_robot=False).wait_for_completed()
                    self.robot.say_text("here are your shorts").wait_for_completed()
                    action = self.robot.place_object_on_ground_here(i)
                    action.wait_for_completed()
                    self.robot.turn_in_place(degrees(180)).wait_for_completed()
                    self.find(4)
                    break

        elif number == 4:
            for i in cubes:
                if i == self.sun_glasses:
                    action = self.robot.pickup_object(self.sun_glasses, num_retries=3)
                    action.wait_for_completed()
                    self.robot.go_to_pose(Pose(0, 0, 0, angle_z=degrees(180)),
                                          relative_to_robot=False).wait_for_completed()
                    self.robot.say_text("here are your sun glasses").wait_for_completed()
                    action = self.robot.place_object_on_ground_here(i)
                    action.wait_for_completed()
                    break
        else:
            print("unknown item")


