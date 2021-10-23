def dynamic_code(str1, str2):
    n = len(str1)
    m = len(str2)
    mtx = [[0 for y in range(m+1)] for x in range(n+1)]

    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                mtx[i+1][j+1] = 1 + mtx[i][j]
            else:
                mtx[i+1][j+1] = max(mtx[i+1][j], mtx[i][j+1])

    # for i in range(n+1):
    #     for j in range(m+1):
    #         print(mtx[i][j], end=" ")
    #     print("\n")

    return mtx[-1][-1]


if __name__ == "__main__":
    str1 = "abc"
    str2 = "avb"

    print(dynamic_code(str1, str2))
