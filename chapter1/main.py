

def check_relation(net, first, second):
    i = 0

    while i <= len(net):
        for tuples in net:
            if first in tuples:
                a = tuples.index(first)

                if a == 1:
                    second_name_in_t = tuples[0]
                else:
                    second_name_in_t = tuples[1]

                if second_name_in_t == second:
                    return True
                else:
                    first = second_name_in_t

        i += 1

    return False


if __name__ == '__main__':

    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )


assert check_relation(net, "Петя", "Стёпа") is True
assert check_relation(net, "Маша", "Петя") is True
assert check_relation(net, "Ваня", "Дима") is False
assert check_relation(net, "Лёша", "Настя") is False
assert check_relation(net, "Стёпа", "Маша") is True
assert check_relation(net, "Лена", "Маша") is False
assert check_relation(net, "Вова", "Лена") is True