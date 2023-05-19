from classes import *

current_user=None                   #текущий пользователь
currentdb=None                  #текущая база данных

def logerror():                 
    print('Неверные логин или пароль, поробуйте еще раз:')
    return loginfunc()
def logpas():
    global login, password
    login = input('Введите логин:')
    password = input('Введите пароль:')
def name():
    global name,surname
    name = input('Имя: ')
    surname=input('Фамилия: ')

def loginfunc():                    #Вход в аккаунт
    global current_user, lgn, currentdb
    print('******************************\n '
          'Выберите форму для входа:\n '
          '1. Работник\n '
          '2. Клиент')
    who=input()
    if who=="1":
        currentdb=employee
        logpas()
    elif who=="2":
        currentdb=clients
        logpas()
    else:
        print('******************************\n '
        'Необходимо ввести 1 или 2. Попробуйте снова')
        return loginfunc()
    if login in currentdb:
        lgn=eval(login)                 #конвертация входных данных в объект класса
        if password==lgn.getpassword():
            print(f'Добро пожаловать в систему, {lgn.name} {lgn.surname}')
            current_user=lgn
        else:
            logerror()
    else:
        logerror()


def registration():                 #регистрация новых пользователей
    global current_user,player
    print('******************************\n '
    'Выберите форму для регистрации:\n '
          '1. Работник\n '
          '2. Клиент')
    who = input()
    
    if who=='1':
        logpas()
        name()
        globals()[login] = Employee(name, surname, login, password)
        employee[str(login)] = {'password': password, 'name': name, 'surname': surname}
    elif who=="2":
        logpas()
        name()
        globals()[login] = Client(name, surname, login, password)
        clients[str(login)] = {'password': password, 'name': name, 'surname': surname, 'results':None}
    else:
        print('******************************\n ','Необходимо ввести 1 или 2. Попробуйте снова')
        return registration()
    player=eval(login)
    print(f'Добро пожаловать в систему, {player.name} {player.surname}')
    current_user = player

def pricef():                   #Рассчет итоговой стоимости услуг
    print('******************************\n '
    'Перечень услуг:\n'
              '1. ОАК 1500тг\n'
              '2. ОАМ 1200тг\n'
              '3. витамин Д 4000тг')
    answer=input('Введите без пробелов и запятых номера интересубщих услуг:')
    if answer!=None:
        k=0
        for i in answer:
            if i=="1":
                i=g1
            elif i=="2":
                i=g2
            elif i=='3':
                i=v1
            else:
                i=0
            
            k=k+i
        print(f'Итого: {k}тг'  )
    else:
        print('Вы ничего не ввели, тогда продолжим') 

        
def startmenu():                    #Стартовое меню программы
    choice=input(''' Если у вас уже есть аккаунт введите 1, если хотите зарегестрироваться нажмите 2.\n Для рассчета стоимости сдачи анализов нажмите 3: ''')
    while choice!="1" and choice!="2" and choice!="3":
            choice=input('Необходимо ввести 1 или 2. Введите еще раз:')
    match choice:
        case "2":
            registration()
        case "1":
            loginfunc()
        case '3':
            pricef()
            startmenu()

    startvar=current_user.start()
    
    if startvar==True:
        # print(app)
        return startmenu()
    return print('******************************\n ','Благодарим за использование нашего сервиса!')

####################################################################################


samm=Client('sam','smitt','samm','123')
sal=Client('sal','smitt','sal','123')
ann=Employee('Ann','Gony','ann',123)
v1=Vitamins('витамин Д')
g1=Generals('ОАК')
g2=Generals('ОАМ')
vitaminlist.pop('None')
oamoak.pop('None')

#Вход в систему

print('******************************\n ',"Здравствуйте! ")
startmenu()


