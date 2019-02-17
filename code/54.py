def compute():
    try:
        5/0
    except ZeroDivisionError:
        print('division by zero!')

compute()