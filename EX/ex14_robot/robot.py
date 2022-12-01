"""Robot."""
from FollowerBot import FollowerBot


# robot = FollowerBot()
# color1 = robot.get_left_line_sensor()
# while color1 != 0:
#     robot.set_wheels_speed(100)
#     robot.sleep(0.01)
#     robot.set_wheels_speed(0)
#     if robot.get_line_sensors().count(0) == 6:
#         color2 = robot.get_left_line_sensor()
#         while color2 != 1024:
#             robot.set_wheels_speed(100)
#             robot.sleep(0.01)
#             robot.set_wheels_speed(0)
#             if robot.get_line_sensors().count(0) != 6 and robot.get_left_line_sensors().count(0) != 3:
#                 robot.set_left_wheel_speed(20)
#             elif robot.get_line_sensors().count(0) != 6 and robot.get_right_line_sensors().count(0) != 3:
#                 robot.set_right_wheel_speed(20)
#             color2 = sum(robot.get_line_sensors()) / 6
#         break
#     else:
#         color1 = robot.get_left_line_sensor()
# robot.done()
def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(20)
    robot.sleep(5)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    color = robot.get_left_line_sensor()
    print(color)
    while color != 0:
        print(robot.get_position())
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
        color = robot.get_left_line_sensor()
    robot.set_wheels_speed(20)
    robot.sleep(1)
    robot.set_wheels_speed(0)
    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    color1 = robot.get_third_line_sensor_from_left()
    while color1 != 0:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
        color1 = robot.get_third_line_sensor_from_left()

    color2 = robot.get_left_line_sensor()
    while color2 == 0:
        if robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() == 0:
            robot.set_wheels_speed(100)
            robot.sleep(0.01)
            robot.set_wheels_speed(0)
        if robot.get_left_line_sensor() != 0 and robot.get_right_line_sensor() == 0:
            robot.set_left_wheel_speed(50)
            robot.sleep(0.01)
            robot.set_left_wheel_speed(0)
        elif robot.get_left_line_sensor() == 0 and robot.get_right_line_sensor() != 0:
            robot.set_right_wheel_speed(50)
            robot.sleep(0.01)
            robot.set_right_wheel_speed(0)
        else:
            color2 = 1

    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass
