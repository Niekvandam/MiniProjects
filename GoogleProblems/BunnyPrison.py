loopX = 1
loopY = 1
currentYAxis = 1
bunnyId = 1

def solution(x, y):
    global loopX
    global loopY
    global currentYAxis
    global bunnyId
    if isinstance(x, int) or isinstance(y, int):
        if x > 100000 or y > 100000 or x < 1 or y < 1:
            return
        while loopX != x or loopY != y:
            if (loopY - 1 != 0):
                loopX += 1
                loopY -= 1
            else:
                loopY = currentYAxis + 1
                currentYAxis = loopY
                loopX = 1
            bunnyId += 1
        return str(bunnyId)
    return


def solution2(x, y):
    left = (x + y)
    right = (x + y)
    full = left * right
    oof = full / 2
    return str(oof + x)



print(solution(3, 2))
print(solution2(3, 2))