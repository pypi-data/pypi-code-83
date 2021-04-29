import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

import quick_hull.utils as utils

def quick_hull(points, p1, p2, side, bisectors):        
    farthest_point_idx = -1
    max_dist = 0
  
    # Find the farthest point (on the specified side )from the line [p1, p2]
    for index in range(len(points)):
        maybe_farthest = utils.get_dist(p1, p2, points[index])
        # If this point is on the correct side of the line and farther than our max
        # it becomes our new farest point
        if utils.get_side(p1, p2, points[index]) == side and maybe_farthest > max_dist:
            farthest_point_idx = index
            max_dist = maybe_farthest
    
    # flag to indicate that the line [p1, p2] has no
    # further point, therefore it is part of the hull!
    no_further_point = farthest_point_idx == -1

    # add visualization components
    bisectors.append([p1, p2, farthest_point_idx, no_further_point])

    # if the line itself is the furthest, add the line
    # endpoints to the convex hull
    if no_further_point:
        return [p1, p2]

    farthest_point = points[farthest_point_idx]
    
    hull = []

    # Recur on the line forming the triangle between p1 and farthest point
    side_1_hull = quick_hull(points, farthest_point, p1, -utils.get_side(farthest_point, p1, p2), bisectors)
    # Recur on the line forming the triangle between p2 and farthest point
    side_2_hull = quick_hull(points, farthest_point, p2, -utils.get_side(farthest_point, p2, p1), bisectors)
    
    if side_1_hull != None:
        hull.extend(side_1_hull)
    if side_2_hull != None:
        hull.extend(side_2_hull)

    return hull



def compute_convex_hull(points):
    # copy the point list to not alter the original
    input_points = points[:]

    # get the initial min_x and max_x to bisect the input points
    min_idx, max_idx = utils.get_min_max(points)

    # container for the visualization components
    bisectors = []
    # list of points defining the convex hull
    convex_hull = []
    
    # start recursively searching for the hull on one side of the bisector
    first_half_hull = quick_hull(input_points, input_points[min_idx], input_points[max_idx], 1, bisectors)
    
    if first_half_hull != None:
        convex_hull.extend(first_half_hull)

     # start recursively searching for the hull on the other side of the bisector
    second_half_hull = quick_hull(input_points, input_points[min_idx], input_points[max_idx], -1, bisectors)
    
    if second_half_hull != None:
        convex_hull.extend(second_half_hull)

    convex_hull_no_duplicate_points = []
    [convex_hull_no_duplicate_points.append(x) for x in convex_hull if x not in convex_hull_no_duplicate_points]
    
    # return the computed hull and the visualization components
    return convex_hull_no_duplicate_points, bisectors


def visualize(points, bisectors):
    fig, _ = plt.subplots()
    ln, = plt.plot([], [], 'ro')
    convex_hull = []
    filtered_out_inputs = []
    input_points = points[:]

    xs = [p[0] for p in input_points]
    ys = [p[1] for p in input_points]

    def init():
        convex_hull.clear()
        return ln,

    def update(frame, bisectors, convex_hull, filtered_out_inputs, xs, ys):
        
        plt.clf()
        
        # For the last iteration, only plot the convex hull
        if frame == len(bisectors)+1:
            for ch_segment in convex_hull:
                p1 = ch_segment[0]
                p2 = ch_segment[1]
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', alpha=1.0)
        # For the first iteration, only plot the initial input points
        elif frame == 0:
            plt.scatter(xs, ys, color='blue', alpha=0.2)
        else:
            frame -= 1
            bisector = bisectors[frame]
            p1, p2, farthest_idx, is_farthest = bisector

            if is_farthest:
                convex_hull.append([p1, p2])

            for bisector_idx in range(frame+1):
                bisector = bisectors[bisector_idx]
                p1, p2, farthest_idx, is_farthest = bisector
                
                alpha = 0.3
                if bisector_idx == frame:
                    alpha=1.0
                    if farthest_idx != -1:
                        plt.scatter(points[farthest_idx][0], points[farthest_idx][1], color='red')
                        if points[farthest_idx] in input_points:
                            input_points.remove(points[farthest_idx])
                        filtered_out_inputs.append(points[farthest_idx])

                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='blue', alpha=alpha)

                if farthest_idx == -1:
                    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='green')
                else:
                    farthest_point = points[farthest_idx]
                    plt.plot([p1[0], farthest_point[0]], [p1[1], farthest_point[1]], 'b--', alpha=0.3)
                    plt.plot([p2[0], farthest_point[0]], [p2[1], farthest_point[1]], 'b--', alpha=0.3)
                    filtered_out_inputs.extend(utils.filter_points(input_points, p1, p2, farthest_point))
                    
            for ch_segment in convex_hull:
                p1 = ch_segment[0]
                p2 = ch_segment[1]
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', alpha=1.0)
        
        input_xs = [point[0] for point in input_points]
        input_ys = [point[1] for point in input_points]
        # plot all the input points
        plt.scatter(input_xs, input_ys, color='blue', alpha=1.0)
        
        filtered_xs = [point[0] for point in filtered_out_inputs]
        filtered_ys = [point[1] for point in filtered_out_inputs]
        plt.scatter(filtered_xs, filtered_ys, color='blue', alpha=0.2)
        
        return ln,

    ani = FuncAnimation(fig, update, frames=range(len(bisectors)+2), fargs=(bisectors, convex_hull, filtered_out_inputs, xs, ys, ),
                        init_func=init, blit=True)

    return ani