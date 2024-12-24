def exit_game(var):
    if var == 'q':
        print("Kapatiliyor...")
        raise SystemExit


def amount_numbers():
    while True:
        amount = input('Cikis --> q\n Sayi Miktari Giriniz:')
        exit_game(amount)

        if amount.isdigit() != True or int(amount) < 2:
            print('Gecersiz Deger. En az 2 sayi kullanabilirsiniz.')
            continue

        return int(amount)


def collect_numbers(amount):
    numbers = []
    placeholder = 1
    while True:
        number = input(f'Cikis --> q / {placeholder}. Sayiyi Giriniz:')
        exit_game(number)

        if number.strip('-').isdigit() != True:
            print('Gecersiz Sayi. Tekrar Deneyiniz')
            continue

        numbers.append(number)
        placeholder += 1

        if amount == len(numbers):
            return numbers


def find_max_min(numbers_list):
    max_value, min_value = numbers_list[0], numbers_list[0]
    for i in numbers_list:

        if min_value > i:
            min_value = i

        if max_value < i:
            max_value = i

    return f'En Kucuk Sayi: {min_value}\nEn Buyuk Sayi: {max_value}'


def control_structure():
    target = input('Cikis --> q\n Baslamak Icin Herhangi Bir Karakter Girin:\n')
    target = target.lower()

    if target == 'q':
        exit_game(target)

    if target:
        count = amount_numbers()
        numbers = collect_numbers(count)
        max_min = find_max_min(numbers)
        print(max_min)
