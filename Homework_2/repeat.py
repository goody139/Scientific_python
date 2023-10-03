from pyparsing import empty


def repeat(string, num):
    """
    Returns a string which comprises every character 
    of the string multiplied by num, e.g. 
    repeat(ja, 2) - returns jjaa
    - assumes that at least one character (string) and one number(int) is inserted -

    Args:
        string (str): string which should be changed
        num (int) : number by which characters should be multiplied
    Returns:
        new_string (str): the inserted string with repeated characters

    """ 
    
    new_string = string[0]*num

    if(len(string) == 0):
        return new_string
    
    else: 
    
        # for character in string...
        for i in range(1,len(string)): 
            # add amount of character to new string
            new_string += string[i]*num

        return new_string 

