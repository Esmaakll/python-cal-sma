import random as r
import time  as t

"""
    2 adet zar atılsın ve her iki zarın değeri de 6 olduğunda program dursun.
    İki zar da 6 gelene kadar kaç kez zar atıldığını bildiren programı yazınız.
"""

i = 1
while True:
    zar_1 = r.randint(1, 6)
    zar_2 = r.randint(1, 6)

    if zar_1 == 6 and zar_2 == 6:
        print("""Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2))
        t.sleep(2)
        break

    print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
    i += 1
    t.sleep(0.5)

print("""\n*** {}. denemede (6,6) geldi ***""".format(i))