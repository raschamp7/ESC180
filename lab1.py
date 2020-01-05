# Rassam Yazdi
# 1006019425
# Section 0102
# ESC180 Lab 1
# Connected Cows

import math

def find_euclidean_distance(x1, y1, x2, y2):
    """
    Type contract: (float, float, float, float) -> float
    
    Description:   returns the euclidean distance between two points in 2D
    
    Example:       >>>find_euclidean_distance (3.0, 3.0, 2.0, 5.0)
                   2.24

    """
    return round(((y1-y2)**2 + (x1-x2)**2)**0.5,2)


def is_cow_within_bounds(cow_position, boundary_points):
    """
    Type contract: (float list, float embedded list) -> int
    
    Description:   returns 1 if cow is within bounds, 0 if the cow is beyond them
    
    Example:       >>>is_cow_within_bounds([3, 3], [[2, 5], [5, 5], [5, 1], [2, 1]])
                   1  
    
    """
    if cow_position[0] > boundary_points[0][0] and cow_position[0] < boundary_points[1][0]:
         
         if cow_position[1] > boundary_points[2][1] and cow_position[1] < boundary_points[0][1]:
             return 1
         
         else:
             return 0
    
    else:
        return 0
    
    return 0

def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    Type contract: (float list, float list) -> float
    
    Description:   returns the distance distance from the cow to a boundary point
    
    Example:       >>> find_cow_distance_to_boundary([3, 3], [2, 5])
                   2.24 
    """
    return round(((cow_position[1]-boundary_point[1])**2 + (cow_position[0]-boundary_point[0])**2)**0.5,2)
    


def find_time_to_escape(cow_speed, cow_distance):
    """
    Type contract: (float, float) -> float
    
    Description:   returns the time needed for the cow to escape given a speed and distance
    
    Example:       >>>  find_time_to_escape(2.0, 8.0)
                   4.0 
    """
    if cow_speed == 0:
        return -1
    
    else:
        return round(cow_distance/cow_speed,2)
    

def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    """
    Type contract: (float list, float list, float, float embedded list) -> float
    
    Description:   returns information about either how much time it will take for the cow to escape, or if it is inside or outside the boundaries
    
    Example:       >>>  report_cow_status ([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2,1]])
                   7.09
    """
    if is_cow_within_bounds(cow_position1, boundary_points) and is_cow_within_bounds(cow_position2, boundary_points):
        
        shortest_distance = min([abs(cow_position2[0] - boundary_points[0][0]), abs(cow_position2[0] - boundary_points[1][0]), abs(cow_position2[1] - boundary_points[0][1]), abs(cow_position2[1] - boundary_points[2][1])])
        
        return find_time_to_escape((find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1])/delta_t),shortest_distance)
    
    elif is_cow_within_bounds(cow_position1, boundary_points) == 0 and is_cow_within_bounds(cow_position2, boundary_points) == 0:
        
        return find_time_to_escape((find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1])/delta_t), find_cow_distance_to_boundary(cow_position2, boundary_points[0]))
    
    elif is_cow_within_bounds(cow_position2, boundary_points) and is_cow_within_bounds(cow_position1, boundary_points) == 0: 
        
        return -1
    
    elif is_cow_within_bounds(cow_position1, boundary_points) and is_cow_within_bounds(cow_position2, boundary_points) == 0: 
        
        return 0
    