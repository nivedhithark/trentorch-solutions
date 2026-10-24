def product(f, lo, hi):
    """
    f:  a function taking a single integer and returning a number
    lo: the starting index (inclusive)
    hi: the ending index (inclusive)

    Returns:
        Prod_{i=lo}^{hi} f(i), the product of f(i) for every integer i
        from lo to hi, both ends included. If hi < lo, the product is
        empty (1).
    """
    # TODO: Implement the product from Theory as an explicit loop.
    result = 1;
    print("lo is ", lo, " and hi is ", hi);
    for i in range(lo, hi + 1):
        if (hi < lo):
            return result;
        function_i = f(i);
        print("f(i) is ", function_i);
        result = result * function_i;
    print("result is ", result);
    return result;
