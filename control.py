import view
import log
import model

def button():
    a = view.menu()
    if a == 1:
        print(model.search(view.info()))
    elif a == 2:
        log.add_data(view.new_emp())
    elif a == 3:
        model.edit()
        print(log.get_data())