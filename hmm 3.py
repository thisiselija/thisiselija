def add(x,y):
    rezultats = x + y
    return rezultats

def minus(x,y):
    rezultats = x - y
    return rezultats

def reiz(x,y):
    rezultats = x * y
    return rezultats

def dal(x,y):
    rezultats = x / y
    return rezultats

while True:
    vienad = input("Ko šodien aprēķināsi? ")
    try:    
        num1 = int(vienad.split()[0])
        oper = vienad.split()[1]
        num2 = int(vienad.split()[2])       

        if oper == ('-'):
            print(minus(num1, num2))
        elif oper == ('+'):
            print(add(num1, num2))
        elif oper == ('*'):
            print(reiz(num1, num2))
        elif oper == ('/'):
            print(dal(num1, num2))   
        else:
            print("nederīga zīme")
    except ValueError:
        kluda = print("Ievadiet atstarpes starp dažādām vērtībām")
    except ZeroDivisionError:
        print("Ar nulli nedala")
        open("https://www.ss.lv/msg/lv/real-estate/flats/riga/tornjakalns/cnmoh.html#photo-4")
    continue


    # https://www.ss.lv/msg/lv/real-estate/flats/riga/tornjakalns/cnmoh.html#photo-4



    