
id=0                    #Индексы объектов класса анализы
idr=0                   #Индексы запросов на консультацию
employee={}                     #хранение данных о работниках
clients={}                  #хранение данных о клиентах
vitaminlist={}                  #запись всех заказанных анализов на витамины
oamoak={}                   #хранение всех заказанных общих анализов
requests={}                 #хранение всех оставленных заявок на консультацию

def end(self):
    print('******************************\n ')
    what = input(
        'Если желаете вернуться в предыдущее меню, введите 1. В противном случае введите любой другой символ: ')
    if what == "1":
        self.start()
    else:
        print('******************')

def requestagain():
    print('Заявки от клиентов')
    for i in requests:                  #вывод всех заявок на консультацию
        print(i,'.  ',requests[i]['name'],requests[i]['surname'],requests[i]['number'])
    answer=input('Для отработки заявки введите ее номер: ')
    try:
        requests.pop(answer)                    #удаление отработанной заяки
    except KeyError:
        print('Заявки с номерм '+answer+' не существует')

    answer=input('Для отработки еще одной заявки введите 1: ')
    if answer=='1':
        requestagain()

class User:                 #Все пользователи
    def __init__(self, name, surname, login, password):
        self.__surname=surname
        self.__name=name
        self.__login=login
        self.__password=str(password)

    def __str__(self):
        return f'{self.__name}, {self.__login}, {self.__password}'
    
    def getlogin(self):
        return self.__login
    def getpassword(self):
        return self.__password

    def setlogin(self,login):
        self.__login=login
    def setpassword(self,pasword):
        self.__password=pasword

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self,surname):
        self.__surname=surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

class Client(User):                 #Клиенты

    def __init__(self,name, surname, login, password, number=None,result=None):
        super().__init__(name, surname, login, password)
        self.__number=number
        self.__result=result
        clients[str(self.getlogin())] = {'password': self.getpassword(), 
        'name': self.name, 'surname': self.surname, 'result': self.result}

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self,number):
        self.__number=number
    @property
    def result(self):
        return self.__result
    @result.setter
    def result(self, result):
        self.__result = result

    def analizy(self):                  #Выбор услуги для сдачи анализов и получение результатов
        global id
        print('******************************\n '
        'Перечень услуг:\n'
              '1. ОАК 1500тг\n'
              '2. ОАМ 1200тг\n'
              '3. витамин Д 4000тг')
        answer =input('Введите номер выбранной услуги: ')
        if answer == "1":
            self.result = 'ОАК выполнен: Все хорошо:)'
            id+=1
            globals()[id]=Generals(name='ОАК', result=self.result, id=id)                   #Создание объекта класса анализы
            print('Ваша заявка принята')
            end(self)
        elif answer == "2":
            self.result = 'ОАМ выполнен: Все хорошо:)'
            id += 1
            globals()[id] = Generals(name='ОАМ', result=self.result, id=id)
            print('Ваша заявка принята')
            end(self)
        elif answer=="3":
            self.result = 'витамин Д выполнен: значения входят в норму:)'
            id += 1
            globals()[id] = Vitamins(name='витамин Д', result=self.result, id=id)
            print('Ваша заявка принята')
            end(self)
        else:
            print('******************************\n ',
            'Необходимо ввести 1,2 или 3. Попробуйте снова')
            return self.analizy()


    def start(self):                    #Основное меню для клиентов
        global number, startvar, idr
        startvar=None
        
        print('******************************\n '
            ' Если желаете сдать анализы введите 1,\n'
            ' Если желаете получить консультацию введите 2,\n Для получения результатов введите 3 \n '
            'Введите 4 для входа в другой аккаунт')
        answer = input()
        if answer=='1':
            self.analizy()
        elif answer=='2':
            number = input('Оставьте свой номер, с вами свяжется наш оператор: ')
            self.number=number
            clients[self.getlogin()]['number']=number
            idr+=1
            requests[str(idr)]={'name': self.name, 'surname': self.surname, 'number': number}
            print('Благодарим за обращение!')
            end(self)
        elif answer=='3':
            if self.result!=None:
                    print('Ваши результаты:\n',self.result)
            else:
                    print('Данных пока нет')
            end(self)
        elif answer=='4':
            print('*************************')
            startvar=True
        
        else:
            print('Необходимо ввести 1, 2, 4 или 3.')
            return self.start()
        return startvar
      
        

class Employee(User):                   # Работники
    def __init__(self,name, surname, login, password):
        super().__init__(name, surname, login, password)
        employee[str(self.getlogin())] = {'password': self.getpassword(), 
        'name': self.name, 'surname': self.surname}
    
    def start(self):
        global startvar
        startvar=None
        print('******************************\n '
        ' 1. Список клиентов\n','2. Cписок всех анализов\n',
        '3. Список оставленных заявок')
        print(' 4. Вход в другой аккаунт')
        answer=input('Ваш выбор:')
        while answer != "1" and answer != "2" and answer !="3"  and answer !="4":
            answer = input('Необходимо ввести 1, 2 или 3. Введите еще раз:')
        match answer:
            case "1":
                print('Клиенты:')
                c=0
                for i in clients:
                    c+=1
                    print(c,'.  ',i,clients[i]['surname'])
                end(self)
            case "2":
                print('Анализы')
                for i in oamoak:
                    print( i,'.  ',oamoak[i]['name'], ' (',oamoak[i]['price'],') ')
                for i in vitaminlist:
                    print( i,'.  ',vitaminlist[i]['name'], ' (',vitaminlist[i]['price'],') ')
                end(self)
            case "3":
                requestagain()
                
                end(self)
            case '4':
                print('*************************')
                startvar=True
        return startvar




class Analizy:                  #Все анализы
    def __init__(self, name, id=None,price=None,result=None):
        
        match name:
            case 'ОАК':
                price='1500тг'
            case 'ОАМ':
                price='1200тг'
            case 'витамин Д':
                price='4000тг'
        
        self.name=name
        self.price=price
        self.result=result
        self.id=id

    def __add__(self, other):                   #Перегрузка функции сложения для рассчета стоимости услуг
        x=int(self.price[:-2])
        y=int(other.price[:-2])
        return x+y
    def __radd__(self, other):
        y=int(self.price[:-2])
        return y+other


   
        

class Vitamins(Analizy):                    #Витамины
    def __init__(self,name, price=None, result=None, id=None):
        super().__init__(name, id,price, result)
        vitaminlist[str(self.id)] = {'name': self.name, 'price': self.price}
    
class Generals(Analizy):                    #Общие анализы
    def __init__(self,name, price=None, result=None, id=None):
        super().__init__(name, id,price, result)
        oamoak[str(self.id)] = {'name': self.name, 'price': self.price}


