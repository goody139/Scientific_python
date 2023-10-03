def is_prime(n):
    """
    Checks if n is a prime number.
    
    Args:
        n (int) : number to be checked
    Returns:
        True : if n is prime
        False : if n is not prime

    """ 

    if n>1:

        # Iteration
        for i in range(2,int(n/2)+1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if(n%i)==0:
                return False
                
        else:
            return True
    else: 
        return False