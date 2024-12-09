N_R = input("Ievadiet vielu un recepšu skaitu: ")
N_R = N_R.split()
N = N_R[0]
R = N_R[1]
R = int(R)

izej = input(f"Ievadiet {N} sastāvdaļas: ")
izej = izej.split()
izej = [int(cip) for cip in izej]

r = 1
recep = []
while r <= R:
    recepsuSk = input(f"Ievadiet {r}. receptes vielas: ").split()
    recepsuSk = [int(sk) for sk in recepsuSk]
    recep.append(recepsuSk)
    r += 1
#print(recep)

for rec in recep:
    rezul = []
    for x, y in zip(izej, rec):
        if y != 0:
            rezul.append(x // y)
    rezult = min(rezul)
    print(rezult)