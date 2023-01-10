def recursive_range(x):
    if x == 0:
        return 0
    return x + recursive_range(x - 1)


print(recursive_range(5))
