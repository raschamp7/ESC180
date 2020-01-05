# Rassam Yazdi
# 1006019425
# Section 0102
# ESC180 Lab 2

from Lab2_2 import error_indices

def dec_to_bin_list(dec_num):
    # DO NOT modify this function
    """
    (num)-> List[num]

    Function that converts decimal integer number to binary

    Usage: bin_list = dec_to_bin_list( dec_num )
    Input: dec_num is an integer number
    Output: bin_list is a list with four elements (0's and 1's), in the order of most significant bit to least significant bit

    The function assumes that dec_num is an integer.

    Inputs that are not in the range 0 to 15 will produce the same output as dec_num - 16*k where
    k is an integer that makes dec_num - 16*k attain a value from 0 to 15.

    >>> dec_to_bin_list(8)
    [1, 0, 0, 0]

    >>> dec_to_bin_list(16)
    [0, 0, 0, 0]
    """

    bin_list = []
    # start building the bin_list from the least significant bit
    # only need 4 bits
    while len(bin_list) < 4:
        curr_bit = dec_num % 2
        bin_list.append(int(curr_bit))
        dec_num = (dec_num - curr_bit)/2

    return list(reversed(bin_list))

def bin_list_to_dec(bin_list):
    # DO NOT modify this function
    '''
    (List[int]->int)

    Returns the decimal value of the input 4-bit number represented by bin_list.

    >>> bin_list_to_dec([1, 0, 0, 0])
    8
    '''
    dec = 0
    for i in range(len(bin_list)-1,-1, -1):
        dec += bin_list[i]*2**(len(bin_list)-i-1)
    return int(dec)

def add_two_bin_nums(four_bit_num1, four_bit_num2):
    """
    Description:
    This function returns the result of the addition of two four bit numbers as a four element list
    
    Type contract:
    (list) -> list
    
    Examples:
    >>> add_two_bin_nums([0,0,1,1], [0,1,0,1])
    [1, 0, 0, 0]
    >>> add_two_bin_nums([0,1,1,0], [1,1,0,0])
    [0, 0, 1, 0]
    >>> add_two_bin_nums([1,1,1,0], [1,1,0,0])
    [1,0, 1, 0]
    """
    carry = 0
    sum = [0,0,0,0]
    for i in range(len(four_bit_num1)-1, -1,-1):
        sum[i] += (carry + four_bit_num1[i] + four_bit_num2[i])
              
        carry = 0
        
        if sum[i] == 2:
            sum[i] = 0
            carry +=1
        elif sum[i] == 3:
            sum[i] = 1
            carry += 1
            
    return sum      
    
    
def check_bit_add(four_bit_num1, four_bit_num2, result):
    """
    Description:
    This function checks if the bit addition of the two bits above produces the result given in the "result".
    Returns an empty list if the two results are the same, and returns the indices of the differences between the two bits if they are different.
    
    Type contract:
    (list) -> list
    
    Examples:
    >>>check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [1,1,1,1])
    []
    >>>check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [0,1,0,1])
    [0, 2]
    >>>check_bit_add([1, 1, 1, 1],[1, 1, 1, 1], [1,1,1,0])
    []
    """
    
    if add_two_bin_nums(four_bit_num1, four_bit_num2) != result:
        return error_indices(add_two_bin_nums(four_bit_num1, four_bit_num2), result)
    else:
        return []

def check_dec_add(four_bit_num1, four_bit_num2):
    """
    Description:
    This function checks if the bit addition between the above bits results in the correct decimal result
    Returns 0 if they do not match (overflow), returns 1 if they do.
    
    Type contract:
    (list) -> num
    
    Examples: 
    >>>check_dec_add([1,0,0,0], [1,0,0,0])
    0
    >>>check_dec_add([0,0,1,1], [0,1,0,1])
    1
    """
    if bin_list_to_dec(add_two_bin_nums(four_bit_num1, four_bit_num2)) != (bin_list_to_dec(four_bit_num1) + bin_list_to_dec(four_bit_num2)):
        return 0
    else:
        return 1
    
def get_error_source(four_bit_num1, four_bit_num2, result):
    """
    Description:
    This function describes the type of error present, if any, in the binary addition. 
    If no errors made, returns 0, if there is an overflow error, return 1, if there is an error from another source, returns 2
    
    Type contract: 
    (list) -> num
    
    Examples:
    >>>get_error_source([0,0,0,0], [0,0,0,0], [0,0,0,0])
    0
    >>>get_error_source([1,0,0,1], [1,0,0,1], [0,0,1,0])
    1
    >>>get_error_source([1,0,0,1], [1,0,0,1], [1,0,1,0])
    2
    """    
    if check_dec_add(four_bit_num1, four_bit_num2) == 1:
        return 0
    elif check_bit_add(four_bit_num1, four_bit_num2, result) == []:
        return 1
    else: 
        return 2
    


