# 1. Просмотр дел на сегодняшний день(Список дел должен выводится с датой и временем когда необходимо сделать)
# 2. Просмотр дел на завтрашний день
# 3. Просмотр дел на любой выбранный день, вводится с клавиатуры.
# 4. Возможность записать в ежедневник список дел на любой выбранный день.



# Основные требования:
# 1. Использование Базы данных (sqlite3, MySQL, postgreSQL) - 50
# 2. Вывод списка дел из ежедневника - 30
# 3. Запись списка дел в ежедневник - 20  

import sqlite3 as sql3
all='*'
notes='notes'
date='date'
bad='Введен неверный номер, попробуйте еще раз.' #Переменные для упрощения запросов

mydb = sql3.connect("C:/Users/aiman/Desktop/justcode/HW/project_sql/mydairy.db") 
mycursor = mydb.cursor()

def menu():     #Главное меню
    print('''
1.Оставить новую запись
2.Дела на сегодня
3.Дела на завтра
4.Посмотреть записи на конкретную дату
5.Редактирование''')

def show(query, texttitle='\n'):            #Вывод данных
  
  mycursor.execute(query)

  result=mycursor.fetchall()
  print('\n'+str(texttitle))
  for i in result:
    for j in i:
        print(j, end=' ')
    print('\n',end='')

def commit(query, texttitle='\n'):          #сохранение данных в бд
   print('\n'+str(texttitle))
   mycursor.execute(query)

   mydb.commit()

def select(what, table=notes, x=''):            #выборка данных из бд
    request=f'select {what} from {table} {x};'
    return request

def insert(columns, values, table=notes):           #добавление данных в бд
    request=f'''insert into {table}({columns}) VALUES ({values})'''
    return request

def delete(where, table=notes):         #удаление строк из бд
    request=f'''delete from {table} where {where}'''
    return request

def update(values, where, table=notes):             #изменение данных в бд
    request=f'''update {table} set {values} where {where}'''
    return request
   

def case5():            #редактирование бд
    dd=input('Введите дату в формате YYYY-MM-DD: ')
    dd=dd+'\''
    show(select('ID,date,time,text',notes,'where date=\''+dd))
    id=input('Выберите запись:')
    show(select('date,time,text',notes,'where ID='+id))
    wtd=int(input('Удалить(1) или изменить значение(2)? Для отмены введите 0: '))
    while wtd>2 or wtd<0:
                wtd=input(bad+' Удалить(1) или изменить значение(2)? Для отмены введите 0: ')
                wtd=int(wtd)
    match wtd:
                case 1:
                    commit(delete('id='+id))
                    print('Запись удалена')
                    exit()
                case 2:
                    wtd=int(input('Изменить текст записи(1), дату (2) или время(3)? '))
                    match wtd:
                        case 1:
                            text1=input("Введите текст записи: ")
                            commit(update('text=\''+text1+'\'','id='+id))
                        case 2:
                            date1=input('Введите планируемую дату в формате YYYY-MM-DD: ')
                            commit(update('date=\''+date1+'\'','id='+id))
                        case 3:
                            time1=input('Введите время в формате HH:MM:SS ')
                            commit(update('time=\''+time1+'\'','id='+id))
                    print('Изменения внесены')
                    show(select('date,time,text',notes,'where ID='+id))
                    exit()
                case 0:
                    menu()
                    choose()


def case1():            #добавление записей
    text1=input("Введите текст записи: ")
    date1=input('Введите планируемую дату в формате YYYY-MM-DD: ')
    time1=input('Введите время в формате HH:MM:SS ')
    commit(insert('text,date,time',f"\'{text1}\',\'{date1}\',\'{time1}\'"))
    print('Запись добавлена')
    show(select('date,time,text',notes,'where id=(select max(id) from notes)'))
    
    exit()
    

def exit():         #выход в главное меню
    wtd=input('Для выхода в главное меню введите 0, иначе нажмите enter: ')
    if wtd=="0":
        menu()
        choose()    
    else:
        print('****')  
    
def choose():       #функционал основного меню
    number=int(input('Выполнить: '))
    if 5<number<1:
        print(bad)
        return choose()
    match number:
        case 1:
            case1()
        case 2:
            show(select('date,time,text',notes,'where date=current_date'))  
            exit()      
        case 3:
            show(select('date,time,text',notes,'where date=date(current_date,\'1 days\')'))   
            exit()        
        case 4:
            dd=input('Введите дату в формате YYYY-MM-DD: ')
            dd=dd+'\''
            show(select('date,time,text',notes,'where date=\''+dd))         
            exit()      
        case 5:
            case5()


#*********************************запуск программы**************************
            
print('''Добро пожаловать в ежедневник)''')
menu()
choose()
