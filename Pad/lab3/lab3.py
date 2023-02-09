from pathlib import Path
import csv


# folder_name = input("folder name: ")
# folder = Path(folder_name)
# if folder.is_dir():
#     folder_count = len([1 for file in folder.iterdir()])
#
# print(f"В папке {folder_name} есть {folder_count} объектов")


def main():
    def write_csv():  # функция записи новыой строки в файл
        key_inp = input('Enter key: ')
        date_inp = input('Enter date: ')
        price_inp = input('Enter price: ')
        name_inp = input('Enter name: ')
        all_data[key_inp] = [date_inp, price_inp, name_inp]
        with open('data.csv', 'w') as f:
            for elem in all_data:
                f.write(elem + "," + all_data[elem][0] + "," + all_data[elem][1] + "," + all_data[elem][2] + "\n")
        f.close()

    all_data = {}
    # чтение данных из файла и их занесение в словарь
    with open("data.csv", "r") as f:
        # reader = csv.DictReader(f)
        reader = csv.reader(f)
        for line in reader:
            all_data[line[0]] = line[1:]

    print("ID, Date, Price, Product Name")
    for elem in all_data:
        print(elem, *all_data[elem])
    print("\n")

    # Сортировка по числовому полю
    print("Сортировка словаря по цене:")
    for elem in sorted(all_data.items(), key=lambda para: int(para[1][1])):
        print(elem[0], *elem[1])
    print("")
    # Сортировка по строковому полю
    print("Сортировка словаря по названию товара:")
    for elem in sorted(all_data.items(), key=lambda para: para[1][2]):
        print(elem[0], *elem[1])
    print("")

    # Вывод строк словаря в которых наименование товара = 'pizza'
    print("Строки, в которых имя товара 'pizza': ")
    for elem in all_data:
        if all_data[elem][2] == 'pizza':
            print(elem, *all_data[elem])

    print("")
    check = input('Add newline to file? Enter y/n: ')
    if check == 'y':
        write_csv()
        print("Данные успешно сохранены!")
    else:
        print("Программа остановлена")


if __name__ == "__main__":
    main()
