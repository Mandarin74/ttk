import log
import view
import logger

def search(emp):
    try:
        book = log.get_data()
        an = []
        flag = False
        for i in book:
            if i.find(emp) != -1:
                flag = True
                an.append(i)
        if flag == True:
            return an
        else:
            return 'Сотрудник не найден'
        logger.log_logger('search', True)
    except:
        logger.log_logger('search', False)

def edit():
    try:    
        book = log.get_data()
        emp = view.info()
        for i in book:
            if i.find(emp) != -1:
                i = view.new_emp()
        log.edit_data(book)
        logger.log_logger('edit', True)
    except:
        logger.log_logger('edit', False)
