import math
import random
#Generator liczb pseudolosowych dla rozkładu jednostajnego(metoda Linear Congruential Generator)
seed = 123456
a = 132615312
c = 123123123
m = 1212684125635128
n = 1000
def lcg_random_generator(seed, a, c, m, n):
    random_numbers = []
    x = seed

    for i in range(n):
        x = (a * x + c) % m
        random_numbers.append(x)

    return random_numbers
random_numbers = lcg_random_generator(seed, a, c, m, n)
for i, number in enumerate(random_numbers):
    print(f"Liczba losowa {i + 1}: {number}")
#Generator liczb pseudolosowych dla rozkładu jednostajnego(metoda middle square random)
seed = 765396141934646123407
num_digits = 40
n = 1000
def middle_square_random_generator(seed:int, n: int) -> int: #Middle-square method
    l = []
    length = len(str(seed))//2
    for _ in range(n):
        seed_sq = seed**2
        length_sq = len(str(seed_sq))//2
        rint = int(str(seed_sq)[length_sq-length:length_sq+length])
        l.append(rint)
        seed = rint
    return l


random_numbers = middle_square_random_generator(seed,n)

for i, liczba in enumerate(random_numbers):
    print(f"Liczba losowa {i + 1}: {liczba}")
# Generator liczb pseudolosowych dla rozkładu normalnego(Box-Muller transform)
n = 1000
def box_muller_normal_distribution(n):
    random_numbers = []
    for i in range(n):
        u1 = random.random()
        u2 = random.random()

        z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)

        random_numbers.extend([z1, z2])

    return random_numbers
random_numbers = box_muller_normal_distribution(n)
for i in range(0, len(random_numbers), 2):
    print(f"Liczba losowa {i // 2 + 1}: {random_numbers[i]:.6f}")
# Generator liczb pseudolosowych dla rozkładu normalnego(Marsaglia polar method)
n = 1000
def marsaglia_polar_normal_distribution(n):
    random_numbers = []
    for i in range(n):
        while True:
            u1 = random.uniform(-100, 100)
            u2 = random.uniform(-100, 100)
            s = u1 * u1 + u2 * u2
            if 0 < s <= 1:
                break

        factor = math.sqrt(-2 * math.log(s) / s)
        z1 = u1 * factor
        random_numbers.append(z1)

    return random_numbers


random_numbers = marsaglia_polar_normal_distribution(n)

for i, number in enumerate(random_numbers):
    print(f"Random Number {i + 1}: {number:.6f}")