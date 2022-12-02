"""Robot."""
from FollowerBot import FollowerBot


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
    # drives to a line on a white surface
    robot.set_wheels_speed(30)
    robot.sleep(1)

    turn = 0
    # follows the black line with "u" pattern
    for i in range(5000):
        left_line_sensor = robot.get_left_line_sensor()
        right_line_sensor = robot.get_right_line_sensor()

        if left_line_sensor == 0 and right_line_sensor == 0:
            robot.set_wheels_speed(100)
            robot.sleep(0.03)
            robot.set_wheels_speed(0)
        elif left_line_sensor != 0 and right_line_sensor == 0:
            robot.set_left_wheel_speed(50)
            robot.sleep(0.01)
            robot.set_left_wheel_speed(0)
        elif left_line_sensor == 0 and right_line_sensor != 0:
            robot.set_right_wheel_speed(50)
            robot.sleep(0.01)
            robot.set_right_wheel_speed(0)
        else:
            # for "п" pattern
            if turn == 3:
                break
            turn += 1
            if not robot.get_third_line_sensor_from_left() and robot.get_third_line_sensor_from_right() > 0:
                robot.set_left_wheel_speed(-50)
                robot.sleep(0.1)
                robot.set_left_wheel_speed(0)
                color3 = robot.get_third_line_sensor_from_left()
                if color3 == 1024:
                    robot.set_left_wheel_speed(40)
                    robot.sleep(0.1)
                    robot.set_left_wheel_speed(0)
            elif robot.get_third_line_sensor_from_left() > 0 and not robot.get_third_line_sensor_from_right():
                robot.set_right_wheel_speed(-50)
                robot.sleep(0.1)
                robot.set_right_wheel_speed(0)
                color3 = robot.get_third_line_sensor_from_right()
                if color3 == 1024:
                    robot.set_right_wheel_speed(40)
                    robot.sleep(0.1)
                    robot.set_right_wheel_speed(0)
            elif robot.get_second_line_sensor_from_left() and robot.get_second_line_sensor_from_right():
                break

    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    pass


if __name__ == "__main__":
    follow_the_line(robot=FollowerBot())
