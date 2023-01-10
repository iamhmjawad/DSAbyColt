def product_of_array(arr):
    result = 1

    def helper(helper_input):
        nonlocal result
        if len(helper_input) == 0:
            return
        result = result * helper_input[0]
        helper(helper_input[1:])
    helper(arr)
    return result


print(product_of_array([1, 2, 3, 4]))
