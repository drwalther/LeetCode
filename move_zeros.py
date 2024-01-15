# Дан массив из чисел, все нули нужно переместить в конец списка
# Нужно решить за O(n) по времени и O(1) по памяти
def move_zeroes(arr: list[int]) -> list[int]:
    zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[zero], arr[i] = arr[i], arr[zero]
            zero += 1
    return arr


if __name__ == "__main__":
    a = [1, 2, 2, 0, 4, 6, 0, 0, 8]
    print(move_zeroes(a))
