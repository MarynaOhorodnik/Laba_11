'''
Дано текстовий файл f. Переписати у файл g всі рядки з вихідного файлу. Порядок рядків замінити на зворотній.
Огороднік Марина Олександрівна, І курс, група 122А
'''
import random
# створимо список, з якого рандомно буде заповнюватися файл
list = ['The best of both worlds', 'Speak of the devil', 'See eye to eye', 'Once in a blue moon', 'When pigs fly',
        'To cost an arm and a leg', 'A piece of cake', 'Let the cat out of the bag', 'To feel under the weather',
        'To kill two birds with one stone', 'To cut corners', 'To add insult to injury', 'Let someone of the hook']
f = open("f.txt", "wt")   # відкриваємо файл у режимі запису тексту
for i in range(random.randint(5, 10)):  # циклічно записуємо у файл рядки
    f.write(random.choice(list)+'\n')
f.close()  # закриваємо файл
f = open("f.txt", "rt")  # відкриваємо файл у режимі читання тексту
l = reversed(f.readlines())  # виписуємо рядки файлу у список, змінивши порядок на зворотній
g = open("g.txt", "wt")  # відкриваємо файл у режимі запису тексту
for j in l:  # циклічно записуємо у файл рядки
    g.write(j)
# переміщаємо покажчик файла f на початок, тому що при виконані функції readlines() покажчик перемістивмя в кінець
f.seek(0)
print(f'File F:\n{f.read()}')  # виводимо на екран зміст файлу
f.close()  # закриваємо файл
g.close()  # закриваємо файл
g = open("g.txt", "rt")  # відкриваємо файл у режимі читання тексту
print(f'File G:\n{g.read()}')  # виводимо на екран зміст файлу
g.close()  # закриваємо файл
