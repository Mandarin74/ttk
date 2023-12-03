import logger

def menu():
    print('Выберите действие \
        \n 1 - Поиск сотрудника \
        \n 2 - Добавление нового сотрудника \
        \n 3 - Редактирование сотрудника')
    res = int(input('Введите число: '))
    return res

def info():
    return input('введите информацию о сотруднике')

def new_emp():
    fio = input('ФИО: ')
    date = input('Дата рождения: ')
    work = input('Должность: ')
    zp = input('Зарплата: ')
    phone = input('Телефон: ')

    try:
        zap = '\n' + fio + '|' + date + '|' + work + '|' + zp + '|' + phone
        logger.log_logger('new_emp', True)
    
    except:
        logger.log_logger('new_emp', False)

    return zap
