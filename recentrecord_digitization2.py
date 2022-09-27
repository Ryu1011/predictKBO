def recentrecord_digit21(recentrecord, name):
    name_list1 = ['KIA', 'KT', 'LG', 'NC', 'SSG', '두산', '롯데', '삼성', '키움', '한화']
    digit1 = {}
    i = len(recentrecord)
    rrv = list(recentrecord.values())
    digit1["name"] = (name_list1[name-1])
    homesum = []
    outsum = []
    avrg_home = 0
    avrg_out = 0
    for m in range(0, i - 1):
        if rrv[m][1] not in ['--', '취', '선', '경기']:
            if digit1["name"] == rrv[m][0]:    outsum.append(int(rrv[m][1]))
            else:    homesum.append(int(rrv[m][2]))
        else: continue
    for a in homesum:
        avrg_home += a
    for b in outsum:
        avrg_out += b
    digit1["home_points"] = homesum
    digit1["out_points"] = outsum
    digit1["home_avrg"] = float("%0.2f"%(avrg_home/len(homesum)))
    digit1["out_avrg"] = float("%0.2f"%(avrg_out/len(outsum)))

    return digit1
