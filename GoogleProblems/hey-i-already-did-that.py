def solution(n,b):
    k = len(n)
    minion_id = n
    ids = []
    while minion_id not in ids:
        ids.append(minion_id)
        s = sorted(minion_id)

        # Append array to varaible, in ascending or descending order
        x_descend = ''.join(s[::-1])
        y_ascend = ''.join(s)

        # If the base is 10, perform a default calculation
        if b == 10:
            int_m = int(x_descend) - int(y_ascend)
            minion_id = str(int_m)

        # If the base is not equal to 10, execute a base convert
        else:
            int_m_10 = int(x_descend, b) - int(y_ascend, b)
            minion_id = convert_base(int_m_10, b)
        minion_id = str(minion_id).zfill(k)
    return len(ids) - ids.index(minion_id)


def convert_base(number, base):
    if base < 2:
        return False
    remainders = []
    while number > 0:
        remainders.append(str(number % base))
        number //= base
    remainders.reverse()
    return ''.join(remainders)


# returns 1
print(solution('1211', 10))

# returns 3
print(solution('210022', 3))