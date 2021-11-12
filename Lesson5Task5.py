src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = []


# def unique_nums():
    # for i in range(len(src)):
        # if src.count(src[i]) == 1:
            # result.append(src[i])
    # print(result)s


# print(unique_nums())

# или
result = [num for num in src if src.count(num) == 1]
print(result)
