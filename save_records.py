from recentrecord2 import recentrecord21 as rr21

def save_records1():
    date = ""
    date_rec = ""
    for i in range(1, 11):
        relist = list(rr21(i).values())
        datelist = list(rr21(i).keys())
        for j in range(0, len(relist)):
            date_rec1 = ""
            if relist[j][1] == "선" or relist[j][1] == "--":
                if relist[j-1][0] not in date_rec:
                    date_rec1 = " ".join(relist[j-1])
                    date_rec += date_rec1
                    date_rec += " "
                date = datelist[j-1]
                break
    records = open("C:/Users/a0106/야구 언더오버 예측/records.txt", 'r')
    re1 = records.read()
    if date not in re1:
        records.close()
        records = open("C:/Users/a0106/야구 언더오버 예측/records.txt", 'a')
        records.write("\n")
        records.write(date)
        records.write(" ")
        records.write(date_rec)
        records.close()
    else:
        records.close()

    
