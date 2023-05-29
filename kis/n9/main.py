def pr(table):
    for row in table:
        print("\t".join(str(x) for x in row))


def remove_duplicates_cols(table):
    # Создаем список для хранения уникальных столбцов
    unique_columns = []

    # Перебираем столбцы таблицы
    for column in zip(*table):
        # Если столбец не встречался ранее,
        # добавляем его в список уникальных столбцов
        if column not in unique_columns:
            unique_columns.append(column)

    # Транспонируем список уникальных столбцов
    # для получения таблицы без повторов
    unique_table = list(zip(*unique_columns))
    return unique_table


def remove_duplicates_rows(x):
    # Создаем список для хранения уникальных строк
    unique_rows = []

    # Перебираем строки таблицы
    for row in x:
        # Если строка не встречалась ранее,
        # добавляем ее в список уникальных строк
        if row not in unique_rows:
            unique_rows.append(row)

    return unique_rows
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def remove_empty(x):
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


def formater(table):
    for row_index, row in enumerate(table):
        for col_index, cell in enumerate(row):
            # print(cell)
            if cell[:2:] == "+7":  # Исправление номеров
                table[row_index][col_index] = cell[2::]
            elif cell == "Да" or cell == "Нет":  # замена "Да" "Нет"
                table[row_index][col_index] = "1" if cell == "Да" else "0"
            elif "[at]" in cell:  # удаление символов "[at]"
                table[row_index][col_index] = cell[:cell.index('['):]
    return table


def transpose(A):
    C = []
    for i in range(len(A[0])):
        ci = []
        for j in range(len(A)):
            a = A[j][i]
            ci.append(a)
        C.append(ci)
    return (C)


def main(table):
    table = remove_duplicates_cols(table)
    table = remove_empty(table)
    table = remove_duplicates_rows(table)
    table = formater(table)
    table = transpose(table)
    return table


table = [
    ["1", "2", "3", "4", "5", "6"],
    ["zanin33[at]mail.ru", "+74961198774", None, "Да", None, "zanin33[at]mail.ru"],
    ["cozasin74[at]yahoo.com", "+72915442441", None, "Да", None, "cozasin74[at]yahoo.com"],
    ["sorberg30[at]rambler.ru", "+70918810293", None, "Нет", None, "sorberg30[at]rambler.ru"],
    ["sorberg30[at]rambler.ru", "+70918810293", None, "Нет", None, "sorberg30[at]rambler.ru"]
]

table2 = [['zanin33[at]mail.ru', '+74961198774', None, 'Да', None, 'zanin33[at]mail.ru'],
          ['cozasin74[at]yahoo.com', '+72915442441', None, 'Да', None, 'cozasin74[at]yahoo.com'],
          ['sorberg30[at]rambler.ru', '+70918810293', None, 'Нет', None, 'sorberg30[at]rambler.ru'],
          ['sorberg30[at]rambler.ru', '+70918810293', None, 'Нет', None, 'sorberg30[at]rambler.ru']]

transformed_table = main(table2)
pr(transformed_table)
