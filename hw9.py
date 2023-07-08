def remove_empty_columns(x):
    res = []
    for row in x:
        if row[0] is None:
            continue
        temp = []
        for cell in row:
            if cell is None:
                continue
            temp.append(cell)
        res.append(temp)
    return res


def divide(table):
    new_table = []
    for row in table:
        email, phone = row[0].split("#")
        new_row = [email, phone] + row[1:]
        new_table.append(new_row)
    return new_table


def transform(table):
    for row in table:
        # заменяем "@" на "[at]"
        row[0] = row[0].replace("@", "[at]")

        # убираем "+7 " и заменяем пробелы на "-"
        row[1] = row[1].replace("+7 ", "").replace(" ", "-")

        # убираем имя инициалы в третьем столбце
        names = row[2].split(" ")
        row[2] = f"{names[0]} {names[2]}"

        # заменяем "выполнено" на "да" и "не выполнено" на "нет"
        if row[3] == "Выполнено":
            row[3] = "да"
        elif row[3] == "Не выполнено":
            row[3] = "нет"

    return table


def transpose(table):
    return [[row[i] for row in table] for i in range(len(table[0]))]


def transform2(table):
    table[0], table[1] = table[1], table[0]
    table[1], table[2] = table[2], table[1]
    return table


def main(x):
    res = remove_empty_columns(x)
    res = divide(res)
    res = transform(res)
    res = transpose(res)
    res = transform2(res)
    return res
