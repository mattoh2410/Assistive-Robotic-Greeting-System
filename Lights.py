import cozmo


class Lights:
    # method to set the cube lights
    @staticmethod
    def set_lights(d, number):
        if d.jacket is not None and number == 1:
            d.shorts.set_lights(cozmo.lights.red_light)
        if d.shorts is not None and number == 2:
            d.shorts.set_lights(cozmo.lights.green_light)
        if d.shorts is not None and number == 3:
            d.sun_glasses.set_lights(cozmo.lights.blue_light)
        if d.sun_glasses is not None and number == 3:
            d.sun_glasses.set_lights(cozmo.lights.green_light)
