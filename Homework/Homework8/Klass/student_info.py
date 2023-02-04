import pandas as pd

print('----'*30)
print('Табель учащихся в средней школе # 1285')

stud_card = {
        'ID': ['01','02','03','04','05'],
        'Имя' : ['Иван','Сергей','Екатерина','Ольга','Мария'],
        'Фамилия': ['Петров','Бойко','Литовченко','Мессинг','Пастернак'],
        'Дата рождения' : ['17.08.2000','04.05.2001','01.04.1999','23.02.2002','08.03.2004'],
        'Успеваемость' : ['Отличник','Троечник','Хорошист','Отличник','Хорошист']
}
    
sc = pd.DataFrame(data = stud_card)

with open('students.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)
