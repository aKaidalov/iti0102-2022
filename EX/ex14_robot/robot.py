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


# 2. osa
# ----------------------------------------------------------------------------------------------------------------------


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


# 3. osa
# ----------------------------------------------------------------------------------------------------------------------


def turn_left(robot: FollowerBot):
    """Follower bot turn left."""
    robot.set_left_wheel_speed(-50)
    robot.sleep(0.1)
    robot.set_left_wheel_speed(0)
    color3 = robot.get_third_line_sensor_from_left()
    if color3 == 1024:
        robot.set_left_wheel_speed(40)
        robot.sleep(0.1)
        robot.set_left_wheel_speed(0)


def turn_right(robot: FollowerBot):
    """Follower bot turn right."""
    robot.set_right_wheel_speed(-50)
    robot.sleep(0.1)
    robot.set_right_wheel_speed(0)
    color3 = robot.get_third_line_sensor_from_right()
    if color3 == 1024:
        robot.set_right_wheel_speed(40)
        robot.sleep(0.1)
        robot.set_right_wheel_speed(0)


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
            # hardcode for "??" pattern with 2 turns. turn == 6 because robot does 2 turns in 6 rotations.
            if turn == 6:
                break
            turn += 1
            # for "??" pattern
            if not robot.get_third_line_sensor_from_left() and robot.get_third_line_sensor_from_right() > 0:
                turn_left(robot)
            elif robot.get_third_line_sensor_from_left() > 0 and not robot.get_third_line_sensor_from_right():
                turn_right(robot)
            elif robot.get_second_line_sensor_from_left() and robot.get_second_line_sensor_from_right():
                break

    robot.done()


# 4. osa
# ----------------------------------------------------------------------------------------------------------------------


def follow_the_curve(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    # to get on the line
    robot.set_wheels_speed(30)
    robot.sleep(1)

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
            break


def follow_the_turn_left(robot: FollowerBot):
    """
    Create a FollowerBot that will turn on a corner.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_left_wheel_speed(-100)
    robot.set_right_wheel_speed(100)
    robot.sleep(0.14)
    robot.set_wheels_speed(0)


def follow_the_turn_right(robot: FollowerBot):
    """
    Create a FollowerBot that will turn on a corner.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_right_wheel_speed(-100)
    robot.set_left_wheel_speed(100)
    robot.sleep(0.14)
    robot.set_wheels_speed(0)


def jump(robot: FollowerBot):
    """
    Create a FollowerBot that will jump through squares.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(100)
    robot.sleep(0.8)
    robot.set_wheels_speed(0)


def turnaround(robot: FollowerBot):
    """
    Create a FollowerBot that will turn around.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_left_wheel_speed(-100)
    robot.set_right_wheel_speed(100)
    robot.sleep(0.28)
    robot.set_wheels_speed(0)


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    # start -> finish
    follow_the_curve(robot)  # section 1
    follow_the_turn_left(robot)  # section 2
    follow_the_curve(robot)  # section 3
    jump(robot)  # section 4
    follow_the_curve(robot)  # section 5
    follow_the_turn_left(robot)  # section 6
    follow_the_curve(robot)  # section 7
    follow_the_turn_left(robot)  # section 8
    follow_the_curve(robot)  # section 9

    turnaround(robot)

    # finish -> start
    follow_the_curve(robot)  # section 1
    follow_the_turn_right(robot)  # section 2
    follow_the_curve(robot)  # section 3
    follow_the_turn_right(robot)  # section 4
    follow_the_curve(robot)  # section 5
    jump(robot)  # section 6
    follow_the_curve(robot)  # section 7
    follow_the_turn_right(robot)  # section 8
    follow_the_curve(robot)  # section 9

    robot.done()


if __name__ == "__main__":
    the_true_follower(robot=FollowerBot())
