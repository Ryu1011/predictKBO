from save_records21 import save_records211 as sr211

def save_records21():
    r1 = open("C:/Users/a0106/야구 언더오버 예측/records2.txt", 'r')
    record1 = r1.readlines()
    r1.close()
    date1 = sr211(1)[:4]
    recent = []

    for i in range(1, len(record1)):
        if record1[i][:4] == date1:
            recent.append(record1[i])

    r2 = open("C:/Users/a0106/야구 언더오버 예측/records2.txt", 'a')
    listst = ""
    for i in range(1, 10):
        print(i)
        if len(recent) == 5:
            break
        a = sr211(i)
        if a[5:7] not in "".join(recent):
            recent.append(a)
            r2.write(a + "\n")
            print(a)
   
    r2.close()
        
