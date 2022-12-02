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
            # hardcode for "п" pattern with 2 turns. turn == 6 because robot does 2 turns in 6 rotations.
            if turn == 6:
                break
            turn += 1
            # for "п" pattern
            if not robot.get_third_line_sensor_from_left() and robot.get_third_line_sensor_from_right() > 0:
                turn_left(robot)
            elif robot.get_third_line_sensor_from_left() > 0 and not robot.get_third_line_sensor_from_right():
                turn_right(robot)
            elif robot.get_second_line_sensor_from_left() and robot.get_second_line_sensor_from_right():
                break

    robot.done()


# 4. osa
# ----------------------------------------------------------------------------------------------------------------------


def drive_to_line_for_last_function(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    color = robot.get_left_line_sensor()
    while color != 0:
        robot.set_wheels_speed(100)
        robot.sleep(0.01)
        robot.set_wheels_speed(0)
        color = robot.get_left_line_sensor()


def follow_the_line_for_last_function(robot: FollowerBot):
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
            # hardcode for "п" pattern with 2 turns. turn == 6 because robot does 2 turns in 6 rotations.
            if turn == 8:
                break
            turn += 1
            # for "п" pattern
            if not robot.get_third_line_sensor_from_left() and robot.get_third_line_sensor_from_right() > 0:
                turn_left(robot)
            elif robot.get_third_line_sensor_from_left() > 0 and not robot.get_third_line_sensor_from_right():
                turn_right(robot)
            elif robot.get_second_line_sensor_from_left() and robot.get_second_line_sensor_from_right():
                break

    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    drive_to_line_for_last_function(robot)
    follow_the_line_for_last_function(robot)


if __name__ == "__main__":
    the_true_follower(robot=FollowerBot())
