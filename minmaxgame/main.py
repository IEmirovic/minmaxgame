from func import control_structure


def main():
    while True:
        try:
            control_structure()

        except Exception as error:
            print(f'Beklenmeyen Hata: {error}')


if __name__ == "__main__":
    main()
