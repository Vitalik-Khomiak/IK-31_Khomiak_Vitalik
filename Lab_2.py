#import library
import subprocess


#definition
def login(params):
    if len(params) != 2:
        print("Не виконано вхід. Потрібно два параметри: <login> <password>")
    else:
        print("Успішно виконано вхід.")
#----------------------------------------------------------------------------------------]

def echo(params):
    print(" ".join(params))
#----------------------------------------------------------------------------------------]

def splitter(text):
    text = text.split()
    command = text.pop(0)
    params = text
    return command, params
    #----------------------------------------------------------------------------------------]

def msg(params):
    if len(params) != 2:
        print("Лист не надіслано. Необхідно два параметри: <destinationUser> <text>")
    else:
        print(f"Лист надіслано користувачу {params[0]}.")
#----------------------------------------------------------------------------------------]

def ping(params):
    stroka = ''.join(params)
    result = subprocess.getoutput(f"ping {stroka}")
    print(result)
#----------------------------------------------------------------------------------------]

def list(params):
    stroka = ''.join(params)
    result = subprocess.getoutput(f"dir {stroka}")
    print(result)
#----------------------------------------------------------------------------------------]

def file(params):
    if len(params) != 2:
        print(
            "Файл не надіслано. Потрібно два параметри: <destinationUser> <filename>")
    else:
        print(f"Файл '{params[1]}' надіслано користувачу {params[0]}.")
#----------------------------------------------------------------------------------------]



#Main function
def main():
    command, params = splitter(input("Введіть команду\n"))
    print(f"Команда: {command}; Параметри: {params}")
    if command == 'ping':
        ping(params)
    elif command == 'login':
        login(params)
    elif command == 'list':
        list(params)
    elif command == 'msg':
        msg(params)
    elif command == 'echo':
        echo(params)
    elif command == 'file':
        file(params)
    elif command == 'exit':
        return False
    else:
        print("Невизначена команда, повторіть спробу")
    return True

if __name__ == "__main__":
    while True:
        if main() == False:
            break