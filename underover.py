from recentrecord2 import recentrecord21 as rr21
from recentrecord_digitization2 import recentrecord_digit21 as rd21
from starter2 import startrecord21 as sr21
from teamrank2 import relrank21 as rrk21
import random

def underover1(name):
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
    if astart_dW != "--":
        ascore = round(ateam_st - team_gap * 0.7 - ((astart_dW * 5 / 3.5) + (astart_dA * 25 / 3.5)) / 2 + random.randrange(1, 3))
    else:
        ascore = round(ateam_st - team_gap * 0.9 - (( 2 * 5 / 3.5) + (0.3 * 25 / 3.5)) / 2 + random.randrange(1, 3))
    if hstart_dW != "--":
        hscore = round(hteam_st + team_gap * 0.7 - ((hstart_dW * 5 / 3.5) + (hstart_dA * 25 / 3.5)) / 2 + random.randrange(1, 3))
    else:
        hscore = round(hteam_st + team_gap * 0.9 - ((2 * 5 / 3.5) + (0.3 * 25 / 3.5)) / 2 + random.randrange(1, 3))
    if ascore > 5.5:    a = "오버"
    else:   a = "언더"
    if hscore > 5.5:    h = "오버"
    else:   h = "언더"
    if ascore < 0:  ascore = 0
    else:   ascore = ascore
    if hscore < 0: hscore = 0
    else:   hscore = hscore
    if ascore - hscore > 0:
        wint = ateam_n
        gaps = ascore - hscore
    elif ascore - hscore < 0:
        wint = hteam_n
        gaps = hscore - ascore
    else:
        wint = hteam_n
        gaps = "?"
    print("{}팀의 예상 점수: {}점".format(ateam_n, ascore))
    print("{}팀의 예상 점수: {}점".format(hteam_n, hscore))
    print("{}월 {}일 {} 대 {} 경기는 {}점차로 {}가 승리할 것으로 예측됩니다.".format(dm, dm2, ateam_n, hteam_n, gaps, wint))
    print("5.5점 기준, {}팀 {}, {}팀 {}".format(ateam_n, a, hteam_n, h))
