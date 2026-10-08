def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("Cписок пуст")
    min_num = nums[0]
    max_num = nums[0]
    for i in nums:
        if i > max_num: max_num = i
        if i < min_num: min_num = i
    return min_num, max_num

test_array_1 = [
    [3, -1, 5, 5, 0],
    [42],
    [-5, -2, -9],
    [1.5, 2, 2.0, -3.1],
    [] #для удобства и ошибки(raisevalue) пустой список был пермещен в конец вывода
]
#for array in test_array_1:
    #print(min_max(array))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = list(set(nums))
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1] : nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

test_array_2 = [
    [3, 1, 2, 1, 3],
    [],
    [-1, -1, 0, 2, 2],
    [1.0, 1, 2.5, 2.5, 0]
]
#for array in test_array_2:
    #print(unique_sorted(array))

def flatten(mat: list[list | tuple]) -> list:
    s = []
    for i in mat:
        if type(i) == list or type(i) == tuple: 
            for j in i:
                s.append(j)
        else:
            raise TypeError("Элемент не является списком/кортежем")
    return s

test_array_3 = [
    [[1, 2], [3, 4]],
    [[1, 2], (3, 4, 5)],
    [[1], [], [2, 3]],
    #[[1, 2], "ab"]
]

for array in test_array_3:
    print(flatten(array))
