import datetime as dt

def is_anagram(x,y):
    
    """is it an anagram?
    Inputs:
        2 * Strings
    
    Steps:
        checks the length of both strings
        if they are equal, then sort both strings
        if both sorted are equal, then return True
        Else False
    

    Returns:
        Boolean: True or False
    """
    
    x = x.lower()
    y = y.lower()
    
    if len(x) == len(y):
        s_x = sorted(x)
        s_y = sorted(y)
        
        if s_x == s_y:
            return True
        else:
            return False
    else:
        return False
    
if __name__ == '__main__':
    print(is_anagram('racecar','racecar'))