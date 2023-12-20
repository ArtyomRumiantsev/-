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
phone_book = list(map(clean, phone_book))
print('phone_book =', phone_book)
shorts = filter(lambda x: len(x[1]) == 7, phone_book)
m1 = map(lambda x: '+7495' + x, shorts)

start_with_8 = filter(lambda x: len(x[1]) == 11, phone_book)
m2 = map(lambda x: '+7' + x[1][1:], start_with_8)

m3 = filter(lambda x: len (x[1]) == 12, phone_book)

phone_book1 = sorted(chain(m1, m2, m3))

phone1 = phone_book.pop(0)[1]

yes_no = {True: 'YES\n', False: 'NO\n'}

m4 = map(lambda x: yes_no[phone1 == x[1]], phone_book1)

print('m4 first use', *m4)

#answer = ''.join(m4)
answer = reduce(operator.add, m4)
print(answer)