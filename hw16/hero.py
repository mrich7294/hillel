import configparser


def hero_update(**kwargs):
    filename = 'hero.ini'

    config = configparser.ConfigParser()
    config.read(filename)

    # додавати персонаж
    # try:
    #     section_name = input('Введіть найменування секції для персонажа: ')
    #     config.add_section(section_name)
    # except configparser.DuplicateSectionError:
    #     pass

    keys = ["hero", "power", "alive", "speed", "x", "y"]
    section_name = 'heroes'  # закоментувати при додаванні персонажа
    try:
        lst_help = []
        for key, value in kwargs.items():
            for i in keys:
                if i != key:
                    continue
                else:
                    lst_help.append(key)
                    config.set(section_name, key, value)

        # додавати персонаж, присвоєння значення по замовчуванню
        # lst_help = set(keys) - set(lst_help)
        # if lst_help != '':
        #     for j in lst_help:
        #         config.set(section_name, j, 'default_value')

    except TypeError:
        print(f"Ключ та його значення повинні були типом 'str'!")
    finally:
        with open(filename, "w") as config_file:
            config.write(config_file)

    return hero_update


if __name__ == "__main__":
    my_dict = {"hero": "Batman", "power": "130", "y": "2", "gfd": "23"}
    hero_update(**my_dict)
