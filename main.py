import sys  # library for working with files

default_my_ip_list = []  # array of ip addresses


# reading function
def read_my_file(name, version):
    my_ip_list = default_my_ip_list.copy()  # array of ip addresses
    if version == "4":
        try:
            with open(name + '.txt', 'r') as f:
                for line in f:
                    if not line:  # checking for an empty file
                        if len(my_ip_list) == 0:
                            raise ValueError("Файл пустой")
                        break
                    temp = line.rstrip().split(".")
                    if len(temp) == 4:  # block counter + presence of digits
                        if all(x.isdigit() for x in temp):
                            # Interval from 0 to 255
                            if all(0 <= int(x) < 256 for x in temp):
                                my_ip_list.append(temp)
                            else:
                                raise ValueError("Не все блоки попадают в размерность")
                                sys.exit()

                        else:
                            raise ValueError("Не все блоки являются цифрами")
                            sys.exit()

                    else:
                        raise ValueError("Неправильное к-во блоков в IP")
                        sys.exit()
        except FileNotFoundError:
            print("Фвйл", name, "не найден")
            sys.exit()
    elif version == "6":
        print("6 there is no version")
    else:
        print("Версия не определена.")
        sys.exit()
    return my_ip_list


# def conclusion(my_ip_list):
#     if len(my_ip_list) > 10:
#         print('Содержимое файла слишком большой, вывод не рентабельный')
#     else:
#         print('Содержимое файла \n', my_ip_list)


def convert_number(num):
    temp = str(bin(num))[2:]
    # at the output we can get a number that does not fit the format ####_####
    while len(temp) < 8:
        # we correct the injustice if it is present
        temp = "0" + temp
    return temp


# bytes per page
def byte_to_str(num):
    # bytes(num) -_- ....
    num = int(num, 2)
    return num


def find_type(my_min, ny_max, level):
    # int name_pref -_- ....
    name_pref = ["31", "30", "29", "28", "27", "26", "25", "24", "23", "22", "21", "20", "19", "18", "17", "16", "15",
                 "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    my_min = convert_number(my_min)
    ny_max = convert_number(ny_max)

    # Берем 2 числа и ведем поиск отличий 160 и 166
    # 1 0 1 0 0 0 1 1
    # 1 0 1 0 0 1 1 0
    # _ _ _ _ _ * * * <-отличия чисел
    # 1 1 1 1 1 0 0 0 <- первый  IP 160

    # collect a postfix
    deep = 0  # defining the base IP
    my_pref = ""
    for my_i in range(len(my_min)):
        if my_min[my_i] != ny_max[my_i]:
            my_pref = name_pref[7 - my_i + level]
            deep = my_i
            break
    # collect the number and return it
    num = ""
    for my_j in range(deep):
        num += my_min[my_j]
    for my_j in range(8 - deep):
        num += "0"
    return byte_to_str(num), my_pref


def print_result_net(my_ip_list):
    m_stat = [[255, 0], [255, 0], [255, 0], [255, 0]]  # array with the minimum number
    for i in range(len(my_ip_list)):
        # проверка на максимум в 1 октете
        for j in range(4):
            if int(my_ip_list[i][j]) < m_stat[j][0]:
                m_stat[j][0] = int(my_ip_list[i][j])
            # проверка на минимум в 1 октете
            if int(my_ip_list[i][j]) > m_stat[j][1]:
                m_stat[j][1] = int(my_ip_list[i][j])
    # проверка на отличающиеся IP в 1 и т.д. октете
    print("Result net:")
    if m_stat[0][0] != m_stat[0][1]:  # for 1 octats
        mint, pref = find_type(m_stat[0][0], m_stat[0][1], 24)
        print(str(mint) + ".0.0.0/" + str(pref))
    elif m_stat[1][0] != m_stat[1][1]:  # for 2 octats
        mint, pref = find_type(m_stat[1][0], m_stat[1][1], 16)
        print(str(m_stat[0][0]) + "." + str(mint) + "." + ".0.0/" + str(pref))
    elif m_stat[2][0] != m_stat[2][1]:  # for 3 octats
        mint, pref = find_type(m_stat[2][0], m_stat[2][1], 8)
        print(str(m_stat[0][0]) + "." + str(m_stat[1][0]) + "." + str(mint) + ".0/" + str(pref))
    elif m_stat[3][0] != m_stat[3][1]:  # for 4 octats
        mint, pref = find_type(m_stat[3][0], m_stat[3][1], 0)
        print(str(m_stat[0][0]) + "." + str(m_stat[1][0]) + "." + str(m_stat[2][0]) + "." + str(mint) + "/" + str(pref))
        # to exclude octate
    elif m_stat[0][0] == m_stat[0][1] and m_stat[1][0] == m_stat[1][1] and m_stat[2][0] == m_stat[2][1] \
            and m_stat[3][0] == m_stat[3][1]:
        print(str(m_stat[0][0]) + "." + str(m_stat[1][0]) + "." + str(m_stat[2][0]) + "." + str(m_stat[3][0]) + "/32")


def main(p1, p2):
    # reading function
    my_ip_list = read_my_file(p1, p2)

    # output of source data:
    # conclusion(my_ip_list)

    # the actual response is being generated print_result_net()
    return print_result_net(my_ip_list)


if __name__ == '__main__':
    # Идея приложения найти максимальный и минимальный IP указанный в текстовом файле
    # найденные IP разобрать и подобрать подсеть так, чтобы все влезли
    # the program starts: main.py ipv4 "4" (where 2 arguments are used: txt file name and ip version)
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        raise ValueError("Неверные параметры запуска")
