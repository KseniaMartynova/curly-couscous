from numpy import array, concatenate

def gauss(a, b):
    ab = concatenate((a, array([b]).T), axis=1)
    d = len(ab)



    for i in range(d):
        ab_ii = ab[i, i]
        ab[i] = ab[i] / ab_ii
        for j in range(i+1, d):
            ab[j] -= ab[i] * ab[j, i]


    for i in range(d - 1, -1, -1):
        sum = 0
        for j in range(i+1, d):
            sum = sum + ab[j] * ab[i, j]
        ab[i] = ab[i] - sum


    x = ab[:, -1]
    return x
