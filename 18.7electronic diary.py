#ЭЛЕКТРОННЫЙ ДНЕВНИК ДЛЯ ШКОЛЬНОГО КЛАССА
import random
#список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
#отсортируем список учеников
students.sort()
#список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
#пустой словарь с оценками по каждому предмету
students_marks = {}
#сгенерируем данные по оценкам:
#цикл по ученикам
for student in students: #1 итерация: student = 'Александр'
    students_marks[student] = {} #1 итерация: students_marks['Александр'] = {}
    #цикл по предметам
    for class_ in classes: #1 итерация: class_ = 'Математика'
        marks = [random.randint(1,5) for i in range(3)] #генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks #studens_marks ['Александра']['Математика'] = [5, 5, 5]
#выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student} 
    {students_marks[student]}''')

#выводим список команд
#создаем функцию
def print_commands():
    print('''Список команд:
    1. Добавить оценки ученика по предмету.
    2. Вывести средний балл по всем предметам по каждому ученику.
    3. Вывести все оценки по всем ученикам.
    4. Добавить новый предмет.
    5. Редактировать название предмета.
    6. Удалить предмет.
    7. Добавить нового ученика.
    8. Редактировать имя ученика.
    9. Удалить ученика.
    10. Редактировать оценки ученика по предмету.
    11. Удалить оценки по предмету.
    12. Вывести все оценки по определенному ученику.
    13. Вывести средний балл по каждому предмету по определенному ученику.
    14. Количество учеников в школе.
    15. Список всех учеников.
    16. Список текущих предметов.
    17. Выход из программы.
    0 вывести список команд
    ''')

#выводим список команд
print_commands()

while True:
    print()
    print('Для вывода списка команд введите 0')
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценки ученика по предмету.')
        #считываем имя ученика
        student = input('Введите имя ученика: ')
        #считываем название предмета
        class_ = input('Введите предмет: ')
        #считываем оценку
        mark = int(input('Введите оценку: '))
        #если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            #добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        #неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику.')
        #цикл по ученикам
        for student in students:
            print(student)
            #цикл по предметам
            for class_ in classes:
                #находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                #находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                #выводим средний балл по предмету
                print(f'{class_} - {marks_sum//marks_count}')
                print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам.')
        #выводим словарь с оценками:
        #цикл по ученикам
        for student in students:
            print(student)
            #цикл по словарю
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()

    elif command == 4:
        print('4. Добавить новый предмет.')
        #считываем название предмета
        classes_ = input('Введите название нового предмета: ')
        #добавляем предмет в список
        classes.append(classes_)
        print(classes)

    elif command == 5:
        print('5. Редактировать название предмета.')
        print(f'Текущие предметы: {', '.join(classes)}')
        #считываем название предмета
        old_classes = input('Введите название предмета, которое нужно изменить: ')
        if old_classes not in classes:
            print('ОШИБКА: предмет не найден')
            continue
        else:
            #запрашиваем новое название
            new_classes = input('Новое название: ')
            #редактируем название предмета
            classes[classes.index(old_classes)] = new_classes
            #обновляем у всех студентов
            for marks in students_marks.values():
                if old_classes in marks:
                    marks[new_classes] = marks.pop(old_classes)
        #уведомляем
        print(f'Предмет {old_classes} переименован в {new_classes}')
        print(classes)

    elif command == 6:
        print('6. Удалить предмет.')
        #считываем название предмета, которое нужно удалить
        end_word = input('Введите предмет который хотите удалить: ')
        #если введенное слово есть в списке ключей словаря
        if end_word in classes:
            print(f'Удаляем из словаря: {end_word}')
            #удаляем элемент словаря с ключом eng_word
            classes.remove(end_word)
        else:
            print('ОШИБКА! Этого предмета нет.')
        print(classes)

    elif command == 7:
        print('7. Добавить нового ученика.')
        #считываем имя нового ученика
        students_ = input('Введите имя нового ученика: ')
        #добавляем новое имя в список
        students.append(students_)
        print(students)

    elif command == 8:
        print('8. Редактировать имя ученика.')
        print(f'Список учеников: {', '.join(students)}')
        #считываем имя ученика
        old_students = input('Введите имя ученика, которое нужно изменить: ')
        if old_students not in students:
            print('ОШИБКА: имя не найдено!')
            continue
        else:
            #запрашиваем новое имя
            new_students = input('Новое имя: ')
            #редактируем имя ученика
            students[students.index(old_students)] = new_students
            #обновляем во всех списках
            if old_students in students_marks:
                students_marks[new_students] = students_marks.pop(old_students)
        print(f'Обновленный список учеников: {students}')

    elif command == 9:
        print('9. Удалить ученика.')
        #считываем имя ученика, которого нужно удалить
        del_students = input('Введите имя ученика, которого хотите удалить: ')
        #если введенное имя есть в списке ключей словаря
        if del_students in students:
            print(f'Удаляем из словаря: {del_students}')
            #удаляем элемент словаря
            students.remove(del_students)
        else:
            print('ОШИБКА! Этого ученика нет!')
        print(students)

    elif command == 10:
        print('10. Редактировать оценки ученика по предмету.')
        for student in students:
            print(f'''{student} 
            {students_marks[student]}''')
        #считываем данные ученика
        students_ = input('Введите имя ученика: ')
        classes_ = input('Введите название предмета: ')
        #проверяем на наличие
        if students_ not in students and classes_ not in classes:
            print('ОШИБКА: имя или предмет не найден')
            continue
        else:
            #запрашиваем новые оценки
            new_students_marks = input('Введите оценки по предмету: ')
            #преобразуем введенные оценки в список чисел
            new_marks = list(map(int, new_students_marks.split()))
            #редактируем оценки
            students_marks[students_][classes_] = new_marks
            #уведомляем
            print(f'Оценки для {students_} по предмету {classes_} обновлены.')
            for student in students:
                print(f'''{student} 
                {students_marks[student]}''')

    elif command == 11:
        print('11. Удалить оценки по предмету.')
        for student in students:
            print(f'''{student} 
                    {students_marks[student]}''')
        # считываем данные ученика
        students_ = input('Введите имя ученика: ')
        classes_ = input('Введите название предмета: ')
        #проверяем на наличие
        if students_ not in students and classes_ not in classes:
            print('ОШИБКА: имя или предмет не найден')
            continue
        else:
            #удаляем оценки по предмету
            students_marks[students_].pop(classes_)
        print(f'Все оценки по предмету {classes_} для ученика {students_} удалены.')
        #показываем обновленные данные
        for student in students:
            print(f'''Обновленные данные: {student} 
            {students_marks[student]}''')

    elif command == 12:
        print('12. Вывести все оценки по определенному ученику.')
        #выводим словарь с оценками:
        #запрашиваем имя ученика ученикам
        students_ = input('Введите имя ученика: ')
        #цикл по словарю
        for class_ in classes:
             print(f'\t{class_} - {students_marks[students_][class_]}')

    elif command == 13:
        print('13. Вывести средний балл по каждому предмету по определенному ученику.')
        #выводим список всех учеников
        print('Список учеников:', ', '.join(students))
        #цикл по ученикам
        student_name = input('Введите имя ученика: ')
        #проверяем, что ученик существует
        if student_name not in students:
            print('ОШИБКА: такого ученика нет')
        else:
            print(f'\tСредние баллы для ученика {student_name}:')
            for classes, marks in students_marks[student_name].items():
                #проверяем, что есть оценка
                if marks:
                    #находим среднее значение
                    print(f'\t{classes} - {sum(marks) // len(marks)}.')
                else:
                    print(f'{student_name}: нет оценок.')

    elif command == 14:
        print('14. Количество учеников в школе.')
        print(f'Всего учеников: {len(students)}')

    elif command == 15:
        print('15. Список всех учеников.')
        print('Ученики:', ', '.join(students))

    elif command == 16:
        print('16. Список текущих предметов.')
        print('Предметы:', ', '.join(classes))

    elif command == 17:
        print('17. Выход из программы.')
        break

    elif command == 0:
        print('+ вывести список команд')
        print_commands()