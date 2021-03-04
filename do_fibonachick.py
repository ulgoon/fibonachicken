def memo(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return wrapper

@memo
def do_fibo(num):
    """
    do_fibo(num: positive integer)
    return fibonacci sequence
    if num is same or less than 1, return num
    """
    if num<=1:
        return num
    else:
        return do_fibo(num-1) + do_fibo(num-2)

# This function execute only on __main__
if __name__=='__main__':
    user_num = int(input('Type any positive integer: '))
    result = do_fibo(user_num)
    print(result)
