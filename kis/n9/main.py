def main(table):
    # 1. Удалить дубли среди столбцов,
    # оставив только первое вхождение повторяющегося столбца в таблицу.
    print(table)
    unique_columns = []
    for col_index in range(len(table[0])):
        col = [row[col_index] for row in table][1::]
        if col not in unique_columns:
            unique_columns.append(col)
    table = [list(x) for x in zip(*unique_columns)]
    print(unique_columns)
    unique_candr = [col if "Да" in col or "Нет" in col or None in col else [*set(col)] for col in unique_columns]
    print(unique_candr)
    table = [list(x) for x in zip(*unique_candr)]
    print(table)

    # 2. Удалить пустые столбцы.
    non_empty_cols = [col_index for col_index in range(len(table[0])) if
                      any(row[col_index] is not None for row in table)]
    table = [[row[col_index] for col_index in non_empty_cols] for row in table]

    # 3. Удалить дубли среди строк,
    # оставив только первое вхождение повторяющейся строки в таблицу.
    # unique_rows = []
    # for row in table:
    #     if row not in unique_rows:
    #         unique_rows.append(row)
    # table = unique_rows

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
    # table = [list(x) for x in zip(*table)]
    header = table[0]
    table = [list(x) for x in zip(*table[1:])]
    table.insert(0, header)
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

# def main(table):
#     # step 1
#     print(table)
#     # Transpose the input table to simplify operations
#     table_T = list(map(list, zip(*table)))

#     # Remove duplicate columns, preserving the first occurrence of each duplicate
#     unique_cols = []
#     visited_cols = set()
#     for col in table_T:
#         col_str = str(col)  # Convert each column to a string for hashing
#         if col_str not in visited_cols:
#             visited_cols.add(col_str)
#             unique_cols.append(col)
#     table_T = unique_cols

#     # Remove empty columns
#     non_empty_cols = []
#     for col in table_T:
#         if any(col):
#             non_empty_cols.append(col)
#     table_T = non_empty_cols

#     # Transpose the table back to the original form
#     result = list(map(list, zip(*table_T)))

#     # Remove duplicate rows, preserving the first occurrence of each duplicate
#     unique_rows = []
#     for row in result:
#         if row not in unique_rows:
#             unique_rows.append(row)
#     result = unique_rows

#     print()
#     print(result)
#     return result

#     unique_columns = []
#     for row in table:
#         unique_row = []
#         for val in row:
#             if val not in unique_row:
#                 unique_row.append(val)
#                 if row.index(val) not in unique_columns:
#                     unique_columns.append(row.index(val))

#     # step 2
#     transformed_table = []
#     for row in table:
#         transformed_row = []
#         for col_index in unique_columns:
#             if row[col_index] != None:
#                 transformed_row.append(row[col_index])
#         transformed_table.append(transformed_row)

#     # step 3
#     unique_rows = []
#     for row in transformed_table:
#         if row not in unique_rows:
#             unique_rows.append(row)
#     # # step 4
#     # transformation_rules = {}
#     # for row in unique_rows[1:]:
#     #     for i, val in enumerate(row):
#     #         if i not in transformation_rules:
#     #             transformation_rules[i] = {}
#     #         if val not in transformation_rules[i]:
#     #             transformation_rules[i][val] = len(transformation_rules[i])

#     # for row in transformed_table[1:]:
#     #     for i, val in enumerate(row[3:]):
#     #         if val != None:
#     #             row[i+3] = transformation_rules[i+3][val]

#     # step 5
#     transposed_table = []
#     for i in range(len(transformed_table[0])):
#         transposed_row = []
#         for row in transformed_table:
#             transposed_row.append(row[i])
#         transposed_table.append(transposed_row)


#     transposed_table.insert(0, unique_rows[0])
#     transposed_table[0] += unique_columns[1:]

#     return transposed_table


# def main3(table):
#     # 1. Remove duplicates among columns
#     # by leaving only the first occurrence of a duplicate column in the table.
#     unique_columns = []
#     unique_rows = []

#     for col_index, col in enumerate(zip(*table)):
#         if col not in unique_columns:
#             unique_columns.append(col)
#             unique_rows.append([row[col_index] for row in table])
#     print(unique_rows, '\n', unique_columns)
#     # 2. Remove empty columns.
#     non_empty_cols = [col_index for col_index, col in enumerate(unique_columns) if any(col)]
#     table = [[row[col_index] for col_index in non_empty_cols] for row in unique_rows]

#     # 3. Remove duplicates among rows,
#     # by leaving only the first occurrence of a duplicate row in the table.
#     unique_rows = []
#     [unique_rows.append(row) for row in table if row not in unique_rows]
#     table = unique_rows

#     # 4. Transform the contents of the cells according to the examples.
#     for row_index, row in enumerate(table):
#         for col_index, cell in enumerate(row):
#             if cell.startswith("+7"):  # Fix phone numbers
#                 table[row_index][col_index] = cell[2:]
#             elif cell == "Да" or cell == "Нет":  # Replace "Да" "Нет"
#                 table[row_index][col_index] = "1" if cell == "Да" else "0"
#             elif "[at]" in cell:  # Remove "[at]" characters
#                 table[row_index][col_index] = cell[:cell.index('[at]')]

#     table.insert(0, [i + 1 for i in range(len(table))])
#     # 5. Transpose the table.
#     table = [list(x) for x in zip(*table)]

#     return table
