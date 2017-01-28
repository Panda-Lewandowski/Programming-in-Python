# This Python file uses the following encoding: utf-8
text_file = open('data.txt')
print("""-----------------------------------------------------------------
                ЛЮДИ И ИХ ВЕЛИКИЕ ДОСТИЖЕНИЯ
-----------------------------------------------------------------
Ученый           | Достижение                              | Год
-----------------------------------------------------------------""")
while 1:
    l = text_file.readline()
    print(l, end='')
    if l == '':
        break
text_file.close()


r = int(input("""\nВыберите режим поиска:
1 - по одному фильтру
2 - по двум фильтрам\n"""))
if r == 1:
    fil = input("\nВведите нужную характеристику: ")
    fil = fil.lower()
    text_file = open('data.txt')
    text_result = open('result.txt', 'w+')
    text_result.write('Результаты поиска:\n')                   
    flag = 0
    while 1:
        line = text_file.readline()
        line_buf = line.replace('  ','')
        line_buf = line_buf.replace('|','\t')
        line = line.lower()
        if line.find(fil) != -1:
            text_result.write(line_buf)
            flag = 1
        elif line == '':
            break
    if flag == 0:
        text_result.write('Не нашлось подходящих результатов :(')
    text_file.close()
    text_result.close()
elif r == 2:
    fil1 = input("\nВведите нужную характеристику #1: ")
    fil2 = input("Введите нужную характеристику #2: ")
    fil1 = fil1.lower()
    fil2 = fil2.lower()
    text_file = open('data.txt')
    text_result = open('result.txt', 'w+')
    text_result.write('Результаты поиска:\n')                   
    flag = 0
    while 1:
        line = text_file.readline()
        line_buf = line.replace('  ','')
        line_buf = line_buf.replace('|','   ')
        line = line.lower()
        m = line.find(fil1)
        n = line.find(fil2)
        if m != -1 and n != -1:
            text_result.write(line_buf)           
            flag = 1
        elif line == '':
            break
    if flag == 0:
        text_result.write('Не нашлось подходящих результатов :(')               
    text_file.close()
    text_result.close()
else:
    print("Такого варианта нет")
text_result = open('result.txt')
while 1:
    l = text_result.readline()
    print(l)
    if l == '':
        break
text_file.close()
print('Вы можете также найти результаты поиска в файле "result.txt"')










