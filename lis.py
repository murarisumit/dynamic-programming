def lis(input):
    alis=[1] * len(input)
    for i in range(0, len(input)):
        for j in range(0, i):
            if input[j] < input[i] and alis[i] < alis[j] +1:
                alis[i] = alis[j] + 1

    maxi = 0
    for i in range(len(input)):
        maxi = max(maxi, alis[i])

    return maxi

def test_lis():
    assert lis([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert lis([3,4, -1, 0, 6, 2, 3]) == 4

