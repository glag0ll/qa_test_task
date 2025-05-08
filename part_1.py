def get_integer_input(prompt):
    while True:
        try:
            value = input(prompt)
            # Проверяем, является ли ввод целым числом
            if '.' in value:
                raise ValueError("введите целое число, а не дробное")
            return int(value)
        except ValueError as e:
            print(f"ошибка: {e}. введите целое число.")

def get_number_list():
    while True:
        try:
            print('\nвведите количество чисел в списке')
            count = get_integer_input('> ')
            if count <= 0:
                raise ValueError("количество должно быть больше нуля ")
            return count
        except ValueError as e:
            print(f"ошибка: {e}")


def sort():
    print('введите количество чисел которое будет в списке')
    nums = get_number_list()
    print(f'количество чисел в вашем списке = {nums}, введите числа в данном диапазоне, после каждого введённого числа нажмите "Enter"')
    numbers = []
    while len(numbers) < nums:
        try:
            num = get_integer_input(f'введите число #{len(numbers) + 1}: ')
            numbers.append(num)
        except ValueError as e:
            print(e)

    print(f'\nсписок целиком: {numbers}')

    if numbers:
        even_numbers = [x for x in numbers if x % 2 == 0]
        print(f'четные числа списка: {even_numbers}')
        print(f'максимальное число списка: {max(numbers)}')
        print(f'минимальное число списка: {min(numbers)}')
        print(f'отсортированный список: {sorted(numbers)}')
    else:
        print('список пуст, операции невозможны')


sort()