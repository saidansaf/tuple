mevalar = ("olma", "anor", "banan", "uzum")
print(mevalar[0])
print(mevalar[2])
print(mevalar[1:3])

mevalar = ("olma", "anor", "banan", "uzum")
i = mevalar.index("banan")
print(i)

sonlar = {1, 2, 3, 4}
yangi = int(input("Son kiriting: "))
sonlar.add(yangi)
print(sonlar)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))
print(A.difference(B))

sonlar = {5, 10, 15, 20}
for i in sonlar:
    print(i)