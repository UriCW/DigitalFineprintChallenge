from math import sqrt
def is_factor(integer,divisor):
    """ Check if whole integer factor

        Args:
            integer (int): The number to check
            divisor (int): The divisor to try
        Returns:
            bool: True if 'divisor' is a whole integer divisor of 'integer', False otherwise
    
    """
    if (integer % divisor == 0) :return True
    else: return False 

def get_factors(integer):
    """ Get factors of a positive integer
      
        Generate a set of positive factors up to 'integer' - 1
        
        Args:
            integer (int): number to find factors, must be a positive integer >= 1.
    
        Returns:
            set: A set of unique factors, or an empty set if 'integer' <= 1

    """
    if integer <= 1: return set()
    ret=set()
    ret.add(1)
    for i in range(2,round(sqrt(integer)+1)):
        if (is_factor(integer,i)):
            ret.add(i)
            ret.add(int(integer/i) )
    return ret

def classify(integer):
    """ Classify number

    Args:
        integer (int): number to classify, must be an integer >= 1
    
    Returns:
        "perfect", "abundant" or "deficient"

    Raises:
        ValueError: if 'integer' is not of type int , if it is arbitrarily large or less then 1

    """
    if(type(integer) != int ):
        raise ValueError("%s is not an integer"%(integer))
    if (integer >= 9999999999999):
        raise ValueError("%s is too big"%(integer))
    if (integer < 1):
        raise ValueError("I only work on positive integers")

    factors=get_factors(integer)
    total=sum(factors)
    if (total==integer): return "perfect"
    elif (total>integer): return "abundant"
    else: return "deficient"
