# 2. Замена всех вхождений в файле



import os, re

def workB(filename,was,become,prevwas):  #Замена вхождений в файле
    with open(filename,'r', encoding='utf-8') as filex:
        file=filex.read()
        if prevwas in file:
            file=re.sub(was,become,file)
        else:
            print('Данного выражения в файле нет')

    with open(filename,'w', encoding='utf-8') as filex:
        filex.write(file)

def work(filename,was,become):
    try:
        workB(filename,was,become,was)
    except re.error:
        was1="\\"+was #На случай,если введен символ по типу *
        return workB(filename,was1,become,was)

print('ЗАМЕНА ВСЕХ ВХОЖДЕНИЙ В ФАЙЛЕ')
print('_________________________')
where=input('Введите полное имя документа для поиска его в данной дериктории или полный путь для поиска по всему компьютеру:  ')
exist=os.access(where, os.F_OK)

if exist is False:
    print('Данного файла не существует')
else:
    if os.access(where, os.W_OK) is False:
        print('К сожалению, доступ к файлу для записи закрыт, поэтому дальнейшая замена вхождений невозможна')
    else:
        was = input('Какое выражение вы хотите заменить? ')
        become = input('На что вы хотите его заменить? ')

        work(where, was, become)
