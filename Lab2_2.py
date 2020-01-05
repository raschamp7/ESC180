# Rassam Yazdi
# 1006019425
# Section 0102
# ESC180 Lab 2

def packet_size(packet):
    ''' 
    Description:
    This function returns the size of the packet in bits.
    
    Type Contract:
    (list) -> num
    
    Examples:
    >>> packet_size([0,1,0,1])
    4
    '''
    return len(packet)

def error_indices(packet1, packet2):
    ''' 
    Description:
    This function returns the indices of all the differences between packets1 and 2 in a list.
    Returns an empty list if both packets are the same.
    
    Type contract:
    (list) -> list
    
    Examples:
    >>> error_indices([0,1,1,1], [1,1,0,1])
    [0, 2]
    >>> error_indices([1,1,0,1], [1,1,0,1])
    []
    
    '''
    indices = []
    for i in range(0,len(packet1)):
        if packet1[i] != packet2[i]:
            indices.append(i)   
    
    return indices
                   
    
def packet_diff(packet1, packet2):
    ''' 
    Description: 
    Return the number of bit errors that have happened in the transmission of packet1 to 2
    
    Type contract:
    (list1) -> num
    
    Examples:
    >>>packet_diff([0,1,0,1], [1,1,0,1])
    1
    >>> packet_diff([0,1,1,0], [0,1,1,0])    
    0
    '''
    count = 0
    for i in range(0,len(packet1)):
        if packet1[i] != packet2[i]:
            count+=1    
    return count

