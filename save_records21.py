from recentrecord2 import recentrecord21 as rr21
from recentrecord_digitization2 import recentrecord_digit21 as rd21
from starter2 import startrecord21 as sr21
from teamrank2 import relrank21 as rrk21

def save_records211(name):
    name_list1 = ['KIA', 'KT', 'LG', 'NC', 'SSG', '두산', '롯데', '삼성', '키움', '한화']
    teamlist = rr21(name)
    finddate = list(teamlist.values())
    num = 0
    for i in range(0, len(finddate)):
        
        num += 1
        if finddate[i][1] == "--":
            a = finddate[i-1]   
            break
    date = list(teamlist.keys())[num - 2]
    dm = date[:2]
    dm2 = date[2:]
    
    team_a = name_list1.index(a[0]) + 1
    team_h = name_list1.index(a[3]) + 1
    ateamd = rd21(rr21(team_a), team_a)
    hteamd = rd21(rr21(team_h), team_h)
    teamr = rrk21(a[0], a[3])
    starter_a = sr21(name)[0]
    starter_h = sr21(name)[1]
    ateam_n = ateamd['name']
    hteam_n = hteamd['name']
    ateam_st = ateamd['out_avrg']
    hteam_st = hteamd['home_avrg']
    team_gap = teamr[2]
    astart_dW = starter_a['WHIP']
    astart_dA = starter_a['AVG']
    hstart_dW = starter_h['WHIP']
    hstart_dA = starter_h['AVG']
    team_rec = date + " "
    team_rec += ateam_n + " "
    team_rec += str(ateam_st) + " "
    team_rec += str(astart_dW) + " "
    team_rec += str(astart_dA) + " "
    team_rec += hteam_n + " "
    team_rec += str(hteam_st) + " "
    team_rec += str(hstart_dW) + " "
    team_rec += str(hstart_dA) + " "
    return team_rec
