def main(table):
    # 1. Remove duplicates among columns
    # by leaving only the first occurrence of a duplicate column in the table.
    unique_columns = []
    unique_rows = []

    for col_index, col in enumerate(zip(*table)):
        if col not in unique_columns:
            unique_columns.append(col)
            unique_rows.append([row[col_index] for row in table])
    print(unique_rows, '\n', unique_columns)
    # 2. Remove empty columns.
    non_empty_cols = [col_index for col_index, col in enumerate(unique_columns) if any(col)]
    table = [[row[col_index] for col_index in non_empty_cols] for row in unique_rows]

    # 3. Remove duplicates among rows,
    # by leaving only the first occurrence of a duplicate row in the table.
    unique_rows = []
    [unique_rows.append(row) for row in table if row not in unique_rows]
    table = unique_rows

    # 4. Transform the contents of the cells according to the examples.
    for row_index, row in enumerate(table):
        for col_index, cell in enumerate(row):
            if cell.startswith("+7"):  # Fix phone numbers
                table[row_index][col_index] = cell[2:]
            elif cell == "Да" or cell == "Нет":  # Replace "Да" "Нет"
                table[row_index][col_index] = "1" if cell == "Да" else "0"
            elif "[at]" in cell:  # Remove "[at]" characters
                table[row_index][col_index] = cell[:cell.index('[at]')]

    table.insert(0, [i + 1 for i in range(len(table))])
    # 5. Transpose the table.
    table = [list(x) for x in zip(*table)]

    return table


def main2(table):
    # 1. Удалить дубли среди столбцов,
    # оставив только первое вхождение повторяющегося столбца в таблицу.
    unique_columns = []
    for col_index in range(len(table[0])):
        col = [row[col_index] for row in table][1::]
        if col not in unique_columns:
            unique_columns.append(col)
    table = [list(x) for x in zip(*unique_columns)]

    # 2. Удалить пустые столбцы.
    non_empty_cols = [col_index for col_index in range(len(table[0])) if
                      any(row[col_index] is not None for row in table)]
    table = [[row[col_index] for col_index in non_empty_cols] for row in table]

    # 3. Удалить дубли среди строк,
    # оставив только первое вхождение повторяющейся строки в таблицу.
    unique_rows = []
    for row in table:
        if row not in unique_rows:
            unique_rows.append(row)
    table = unique_rows

    # 4. Преобразовать содержимое ячеек по примерам.
    for row_index, row in enumerate(table):
        for col_index, cell in enumerate(row):
            # print(cell)
            if cell[:2:] == "+7":  # Исправление номеров
                table[row_index][col_index] = cell[2::]
            elif cell == "Да" or cell == "Нет":  # замена "Да" "Нет"
                table[row_index][col_index] = "1" if cell == "Да" else "0"
            elif "[at]" in cell:  # удаление символов "[at]"
                table[row_index][col_index] = cell[:cell.index('['):]
    # print('formatted', table)
    table.insert(0, [i + 1 for i in range(len(table))])

    # 5. Транспонировать таблицу.
    table = [list(x) for x in zip(*table)]

    return table


table = [
    ["1", "2", "3", "4", "5", "6"],
    ["zanin33[at]mail.ru", "+74961198774", None, "Да", None, "zanin33[at]mail.ru"],
    ["cozasin74[at]yahoo.com", "+72915442441", None, "Да", None, "cozasin74[at]yahoo.com"],
    ["sorberg30[at]rambler.ru", "+70918810293", None, "Нет", None, "sorberg30[at]rambler.ru"],
    ["sorberg30[at]rambler.ru", "+70918810293", None, "Нет", None, "sorberg30[at]rambler.ru"]
]

transformed_table = main(table)

for row in transformed_table:
    print("\t".join(str(x) for x in row))
