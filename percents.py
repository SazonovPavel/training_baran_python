


def percents (x, y):
    """What  percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    return result


def print_percents (x, y):
    """Print what  percantage of x is y"""
    print (str(y) + " is " + str(percents(x, y)) + " % of " + str(x))

print_percents(200, 50)