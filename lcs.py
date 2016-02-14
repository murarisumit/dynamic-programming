def lcs_recursive(str1, str2):
    '''(str, str) -> list

    Return the list of chars of longest commen subsequence given two input
    string.


    >>>lcs_recursive("ABCDGH", "AEDFHR")
    ['A','D', 'H']
    >>>lcs_recursive("AGGTAB", "GXTXAYB")
    ['G', 'T', 'A', 'B']
    '''
    if not str1 or not str2:
        return []

    x, xs, y, ys = str1[0], str1[1:], str2[0], str2[1:]

    if x == y:
        return [x] + lcs_recursive(xs, ys)
    else:
        return max(lcs_recursive(str1, ys), lcs_recursive(xs, str2), key=len)


def lcs_len_recursive(str1, str2):
    out = lcs_recursive(str1,str2)
    print(out)
    return len(out)



def lcs_dp(str1, str2):
    '''(str, str) -> int

    Return the length of longest commen subsequence given two input
    string.


    >>>lcs_dp("ABCDGH", "AEDFHR")
    3
    >>>lcs_dp("AGGTAB", "GXTXAYB")
    4
    '''
    if not str1 or not str2:
        return []

    m = len(str1)
    n = len(str2)

    #Storing the calculated data
    L =[[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]


def test_lcs_len_recursive():
    assert lcs_len_recursive('abc', 'aeb') == 2
    assert lcs_len_recursive("ABCDGH", "AEDFHR") == 3
    assert lcs_len_recursive("AGGTAB", "GXTXAYB") == 4
    assert lcs_dp('abc', 'aeb') == 2
    assert lcs_dp("ABCDGH", "AEDFHR") == 3
    assert lcs_dp("AGGTAB", "GXTXAYB") == 4
