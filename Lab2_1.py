# Rassam Yazdi
# 1006019425
# Section 0102
# ESC180 Lab 2

import math

def vector_from_points(p1, p2):                                                                                                              
    ''' 
    Description:
    Returns the an n dimensional vector with its tail at p1 and head at p2.
    Returns an empty list if any of the points are empty lists.
    
    Type contract:
    (list) -> list
    
    Example:
    >>>vector_from_points([0, 0], [1, 2]) 
    [1, 2]
    >>>vector_from_points([3, -1, 0], [10, 0, 1])
    [7, 1, 1]
    ''' 
    vector = []
    if len(p1) == 0 or len(p2) == 0:
        return vector
    
    else:   
        for index in range(0, len(p1)):
            vector.append(p2[index] - p1[index])
       
        return vector

def vector_length(v):                                                                                                                        
    ''' 
    Description:
    Returns the length of a vector v unless vector v is an empty list, in which case it will return -1
    
    Type contract:
    (list) -> num
    
    Example:
    >>>vector_length([2, 1]) 
    2.23606797749979
    >>>vector_length([]) 
    -1
    ''' 
    if len(v) == 0:
        return -1
    
    else:
        sqlength = 0
        for index in range(0, len(v)):
            sqlength += (v[index])**2  
        
        return sqlength**0.5
    
def angle_between(v, w):                                                                                                                     
    ''' 
    Description:
    This function returns the angle between two n dimensional vectors in degrees
    
    Type contract:
    (list) -> num
    
    Example:
    >>>angle_between([-1], [2])  
    180.0
    >>>angle_between([0, 1, 0, 1], [1, 3, 4, 5])
    37.61611202673532
    '''                    
    return (180/math.pi)*math.acos((dot_product(v,w))/(vector_length(v) * vector_length(w)))
    
def dot_product(v,w):                                                                                                                        
    ''' 
    Description:
    Thid function returns the dot product between two vn dimensional vectors
    
    Type contract:
    (list) -> num
    
    Example:
    >>>dot_product( [-1], [2])   
    -2
    >>>dot_product( [0, 1, 0, 1], [1, 3, 4, 5])    
    8
    >>>dot_product([0, 0], [0, 0])    
    0
    '''
    product= 0
    
    for index in range(0, len(v)):
        product += (v[index] * w[index])
   
    return product  
    
def unit_vector(v):
    ''' 
    Description:
    This function finds the unit vector of a given vector v and returns it as a list.
    Returns an empty list if vector is an emplty list.
    
    Type contract:
    (list) -> list
    
    Example:
    >>>unit_vector([2, 1])
    [0.8944271909999159, 0.4472135954999579]
    >>>unit_vector([])
    []
    ''' 
    vector = []
    if len(v) == 0:
        return vector
    
    else:   
        for index in range(0, len(v)):
            vector.append(v[index]/vector_length(v))
       
        return vector    
    
def cross_product(v,w):                                                                                                                      
    ''' 
    Description:
    This function returns the cross product of two vectors of 3 dimensions v and w. (assume 0 for unstated components)
    If either of the vectors has greater than 3 dimensions, an empty list is returned.
    
    Type contract:
    (list) -> list
    
    Example:
    >>>cross_product([], [2])
    [0, 0, 0]
    >>>cross_product([2, 8], [1, 4, 3])
    [24, -6, 0]
    >>>cross_product([1, 1, 1], [5.5, 5.5, 5.5])
    [0.0, -0.0, 0.0]
    >>>cross_product( [1, 1, 1, 0], [1, 5.5])
    []
    '''
    if len(v) > 3 or len(w) > 3:
        return []
    
    else:
        while len(v) < 3:
            v.append(0)
        while len(w) < 3:
            w.append(0)
            
        vector = [0,0,0]
        vector[0] = v[1]*w[2]-v[2]*w[1]
        vector[1] = v[2]*w[0]-v[0]*w[2]
        vector[2] = v[0]*w[1]-v[1]*w[0]
        
        return vector
    
def scalar_projection(v,w):                                                                                                                  
    ''' 
    Description:
    Returns scalar projection of w onto v
    
    Type contract:
    (list) -> num
    
    Example:
    >>> scalar_projection([-2], [1.5])
    -1.5
    >>> scalar_projection([0, 3], [1.5, 2])    
    2.0
    '''
    return dot_product(v,w)/vector_length(v)
    
def vector_projection(v,w):                                                                                                            
    ''' 
    Description:
    This function returns the vector projection of w on to v
    
    Type contract:
    (list) -> list
    
    Example:
    >>> vector_projection([-2], [1.5])
    [1.5]
    >>> vector_projection([0, 3], [1.5, 2])    
    [0.0, 2.0]
    '''
    vector = []
    
    for index in range(0,len(v)):
        vector.append((dot_product(v,w)/vector_length(v)**2)*v[index])    
    
    return vector

      