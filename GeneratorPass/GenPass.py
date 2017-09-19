import string
import random
import datetime
import os
import sys
spec = '!@#$%&*?^'
today = str(datetime.date.today()).replace('-', '/')
filename = 'passwd.txt'
service = str(input('Введите ресурс: '))
name = str(input('Введите ФИО: '))

def randompassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + spec
    size = 8
    return ''.join(random.choice(chars) for x in range(size+1))

if not os.path.exists(filename):
    with open(filename, 'w') as logfile:
        logfile.write('{0:<12} {1:^15} {2:^20} {3:^10} {4}'.format('Пароль', 'Ресурс', 'Имя', 'Дата', '\n'))
        logfile.write('{0:-<12} {0:-^15} {0:-^20} {0:-^10} {1}'.format('-', '\n'))
        logfile.close()
else:
        with open(filename, 'r') as logfile:
            if not logfile.readline()[0:5] == 'Парол':
                with open(filename, 'w') as logfile:
                    logfile.write('{0:<12} {1:^15} {2:^20} {3:^10} {4}'.format('Пароль', 'Ресурс', 'Имя', 'Дата', '\n'))
                    logfile.write('{0:-<12} {0:-^15} {0:-^20} {0:-^10} {1}'.format('-', '\n'))
                    logfile.close()

with open(filename, 'a') as logfile:
    logfile.write('{0:<12} {1:^15} {2:^20} {3:^10} {4}'.format(randompassword(), service, name, today, '\n'))
    logfile.close()

print(name, 'пароль: ', randompassword())