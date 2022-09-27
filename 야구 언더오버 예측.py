from textlist import print_choose, print_teamlist, print_teamlist2
from recentrecord_digitization import recentrecord_digit
from recentrecord2 import recentrecord21
from save_records2 import save_records21
from recentrecord import recentrecord1
from save_records import save_records1
from underover import underover1
from starter import startrecord
from teamrank import relrank

while True:
    a = int(input(print_choose()))
    if a == 1  :
        print_teamlist()
        b = int(input("선택: "))
        recentrecord1(b)
    elif a == 2:
        print_teamlist()
        b = int(input("선택: "))
        recentrecord_digit(recentrecord21(b), b)
    elif a == 3:
        print_teamlist2()
        b = input("선택: ")
        c = b.split(" ")
        c1 = c[0]
        c2 = c[1]
        relrank(c1, c2)
    elif a == 4:
        print_teamlist()
        b = int(input("선택: "))
        startrecord(b)
    elif a == 5:
        print_teamlist()
        b = int(input("선택: "))
        underover1(b)
    elif a == 6:
        save_records1()
    elif a == 7:
        save_records21()
