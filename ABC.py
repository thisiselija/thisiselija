try:    
    ievadSk = input("Ievadiet 4 skaitļus: ").split()
    a, b, c, d = (float(cip) for cip in ievadSk)
    hama = a, b, d, c


    if all(-10**9 <= x <= 10**9 for x in hama):
        if a/b > c/d:
            print(1)
        elif a/b < c/d:
            print(-1)
        else:
            print(0)  
    else:
        print("Skaitļi ir ārpus intervāla!")
except:
    print("Kļūda!")
    
    # ufhiusagflioudflkausgflikagflikaugfiluf
    