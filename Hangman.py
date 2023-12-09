import random

hasla = ["domek","placek","zamek"]
x = random.choice(hasla)
x = list(x)
print(f"słowo składa się z {len(x)} liter")
n = 0
slowo = []
while x != slowo:
    while x != slowo:
        if slowo == x:
            break
        else:
            n = n + 1
            y = input(f"zgadnij {n} literke: ")
            if y in x:
                print("dobrze")
                slowo.insert(x.index(y), y)
                print(slowo)
                print(f"literka znajduje się na {x.index(y) + 1} miejscu w slowie")
            else:
                print("źle")

print("SŁOWO ODGADNIĘTE!!!")




