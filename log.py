import view
def get_data():

    with open('tex.txt', 'r') as file:
        data = file.read().split(f'\n')
        return data

def add_data(a):
    with open('tex.txt', 'a') as file:
        file.write(a)

def edit_data(a):
    with open('tex.txt', 'w') as file:
        file.write(str(a))
