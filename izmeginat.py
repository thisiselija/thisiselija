i = input("Ievadiet skaitļus a, b, c un d ar atstarpi starp tiem: ")
a, b, c, d = map(i)
print(list(a, b, c, d))

kreis = a * d
lab = b * c

if kreis < lab:
    print(-1)
elif kreis == lab:
    print(0)
else:
    print(1)