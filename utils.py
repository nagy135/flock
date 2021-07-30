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

    tangle = round(math.degrees(math.atan2(average_y, average_x)))
    if tangle < 0:
        return 360 + tangle
    return tangle
