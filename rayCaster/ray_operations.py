import math
'''
https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
'''


def ccw(A, B, C):
    '''Counterclockwise'''
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersects(a, b, c, d):
    '''Checks if lines are overlapping'''
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


def intersect_point(ray_start, ray_end, barrier_start, barrier_end):
    rs_x, rs_y = ray_start[0], ray_start[1]
    re_x, re_y = ray_end[0], ray_end[1]
    bs_x, bs_y = barrier_start[0], barrier_start[1]
    be_x, be_y = barrier_end[0], barrier_end[1]

    p1_x = int((rs_x * re_y - rs_y * re_x)
               * (bs_x - be_x) - (rs_x - re_x)
               * (bs_x * be_y - bs_y * be_x))
    p2_x = int((rs_x - re_x) * (bs_y - be_y) - (rs_y - re_y) * (bs_x - be_x))

    p1_y = int((rs_x * re_y - rs_y * re_x)
               * (bs_y - be_y) - (rs_y - re_y)
               * (bs_x * be_y - bs_y * be_x))
    p2_y = int((rs_x - re_x) * (bs_y - be_y) - (rs_y - re_y) * (bs_x - be_x))

    return (p1_x / p2_x, p1_y / p2_y)


def points_distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def translate(value, origin_min, origin_max, map_min, map_max):
    origin_span = origin_min - origin_max
    map_span = map_min - map_max
    scaled_value = float(value - origin_min) / float(origin_span)
    return int(map_min + (scaled_value * map_span))


def get_closest_intersection(ray, barriers):
    distance_to_closest_intersection = math.inf
    closest_intersection = None
    ray_start = (ray.parent.x, ray.parent.y)
    ray_end = ray.endpoint()
    for barrier in barriers:
        if not intersects(ray_start, ray_end, barrier.start_pos, barrier.end_pos):
            continue
        found_intersect = intersect_point(ray_start, ray_end,
                                          barrier.start_pos, barrier.end_pos)
        distance = points_distance(ray_start, found_intersect)
        if distance > distance_to_closest_intersection:
            continue
        distance_to_closest_intersection = distance
        closest_intersection = found_intersect
    return closest_intersection, distance_to_closest_intersection
