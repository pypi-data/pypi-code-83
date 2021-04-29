from numpy import array, append
from numpy.linalg import det

def get_min_max(points):
    min_idx = 0
    min_val = 9999
    max_idx = 0
    max_val = 0

    for pt_idx, pt in enumerate(points):
        if pt[0] < min_val:
            min_val = pt[0]
            min_idx = pt_idx
        if pt[0] > max_val:
            max_val = pt[0]
            max_idx = pt_idx
    
    return min_idx, max_idx

# Returns the side of point p with respect to line
# joining points p1 and p2.
def get_side(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
  
    if (val > 0):
        return 1
    
    if (val < 0):
        return -1
    
    return 0

# returns a value proportional to the distance
# between the point p and the line joining the
# points p1 and p2
def get_dist(p1, p2, p):
    return abs(((p[1] - p1[1]) * (p2[0] - p1[0])) - ((p2[1] - p1[1]) * (p[0] - p1[0])))


def Point(*coords, z = 1):
    return append(coords, z)


def orient(*points):
    d = det(array(points))
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


def filter_point(point, v1, v2, v3):
    if orient(Point(v1[0], v1[1]), Point(v2[0], v2[1]), Point(v3[0], v3[1])) == -1:
        v1_tmp = v1[:]
        v1 = v2[:]
        v2 = v1_tmp[:]
    
    query_point = Point(point[0], point[1])
    v1_point = Point(v1[0], v1[1])
    v2_point = Point(v2[0], v2[1])
    v3_point = Point(v3[0], v3[1])
    
    in_triangle = True
    in_triangle &= (orient(v1_point, v2_point, query_point) == 1)
    in_triangle &= (orient(v2_point, v3_point, query_point) == 1)
    in_triangle &= (orient(v3_point, v1_point, query_point) == 1)
    
    return in_triangle

def filter_points(inputs, v1, v2, v3):
    filtered = []
    pts = inputs[:]
    for point in pts:
        if filter_point(point, v1, v2, v3):
            filtered.append(point)
            inputs.remove(point)
    return filtered


        

