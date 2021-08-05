import math

def rotate_point(centerPoint, point, angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is clockwise"""
    angle = math.radians(angle)
    temp_point = (point[0] - centerPoint[0], point[1] - centerPoint[1])
    temp_point = (
            temp_point[0] * math.cos(angle) - temp_point[1] * math.sin(angle),
            temp_point[0] * math.sin(angle) + temp_point[1] * math.cos(angle)
            )
    temp_point = (temp_point[0]+centerPoint[0], temp_point[1]+centerPoint[1])
    return temp_point

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

def vector_average_angle(array_of_angles):
    """
    Calculates average between N angles

    For 2 it works like this (generalized to more):
    Calculated angle between 2 angles using vectors.
    This means that it gets always closer angle to these 2 (not one on the other side)
    10,30 => 20
    0,90 => 45
    0,180 => 90
    270,360 => 315 (360-45)
    """

    # calculate array of cartesian tuples
    cartesian_coordinates = [
            (
                math.cos(math.radians(a)),
                math.sin(math.radians(a))
                ) for a in array_of_angles
            ]
    average_x, average_y = 0,0
    for (x,y) in cartesian_coordinates:
        average_x += x
        average_y += y
    average_x /= len(cartesian_coordinates)
    average_y /= len(cartesian_coordinates)

    return average_x, average_y

    tangle = round(math.degrees(math.atan2(average_y, average_x)))
    if tangle < 0:
        return 360 + tangle
    return tangle

def two_angles_step_direction(a,b):
    """
    returns 1 or -1 depending if angle a should be incremented
    or decremented to get to angle b
    10, 350 => -1 (we should decrement angles to get to 350)
    10, 30 => 1 (we should increment angles to get to 30)
    """

    xa = math.cos(math.radians(a))
    ya = math.sin(math.radians(a))
    xb = math.cos(math.radians(b))
    yb = math.sin(math.radians(b))

    average_x = (xa + xb) / 2
    average_y = (ya + yb) / 2

    tangle = math.degrees(math.atan2(average_y, average_x))
    if tangle < 0:
        return -1
    return 1


def move_point_with_angle(x, y, angle, step_size):
    """
    Returns new location of point as pair (x,y) moved 
    step_size far to direction defined by angle
    """
    x += math.sin(math.radians(angle)) * step_size;
    y -= math.cos(math.radians(angle)) * step_size;
    return x,y

