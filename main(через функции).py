from itertools import chain
from functools import reduce
import operator


def clean(x):
    return x.replace('-', '').replace('(', '').replace(')','')

def clean_and_count (x):
    clean_and_count.countet += 1
    return clean_and_count.countrt, x.replace('-', '').replace('(', '').replace(')', '')

clean_and_count.counter = 0
###counter - самодельный аттрибут
phone = input('Введите номер телефона=>')
phone_book = [phone, '8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', '8-495-430', '+79185238495']
print('phone_book =', phone_book)
for i in range(len(phone_book)):
    phone_book[i] = clean(phone_book[i])
    if (len(phone_book[i])==7) :
        phone_book[i]='+7495'+ phone_book[i]
    elif phone_book[i][0] == '8':
        phone_book[i] = '+7' + phone_book[i][1:]
print('phone_book =', phone_book)
#for i in phone_book:
#    print (len(i))
for i in range(1, len(phone_book)):
    if phone_book[0]==phone_book[i]:
        print('YES')
    else:
        print('NO')
