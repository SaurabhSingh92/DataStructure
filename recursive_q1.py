def get_match(str1, str2, idx1=0, idx2=0):
    if len(str1) == idx1 or len(str2) == idx2:
        return 0

    elif str1[idx1] == str2[idx2]:
        print("Match", str1[idx1], str2[idx2])
        return 1 + get_match(str1, str2, idx1+1, idx2+1)

    else:
        print("Not Match", str1[idx1], str2[idx2])
        opt1 = get_match(str1, str2, idx1+1, idx2)
        opt2 = get_match(str1, str2, idx1, idx2+1)
        return max(opt1, opt2)

if __name__ == "__main__":
    str1 = "bacd"
    str2 = "bded"
    print(get_match(str1, str2))
