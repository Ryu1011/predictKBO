import requests
import re

def recentrecord21(name):
    recentrecord = {}
    start = {}
    url="https://search.naver.com/search.naver?sm=tab_sug.mbk&where=nexearch&query="
    
    name_list = ['KIA 타이거즈','KT 위즈','LG 트윈스','NC 다이노스','SSG 랜더스','두산 베어스','롯데 자이언츠','삼성 라이온즈','키움 히어로즈','한화 이글스']
    name_list1 = ['KIA', 'KT', 'LG', 'NC', 'SSG', '두산', '롯데', '삼성', '키움', '한화']
    txtall = requests.get(url+"{}".format(name_list[int(name)-1])).text

    left_team = re.compile('<em class="team_lft">(\w+)<')
    right_team = re.compile('<em class="team_rgt">(\w+)<')
    left_score = re.compile('<span class="(score_lft)?(vs)?">(<strong>)?(\d+)?(\w+)?<')
    right_score = re.compile('<span class="(score_rgt)?(vs)?">(<strong>)?(\d+)?(\w+)?<')
    date = re.compile('tr class="schedule_2022(\d+)')
    cancel = re.compile('schedule_2022\d\d\d\d.+우천취소<')
    cancel2 = re.compile('schedule_2022(\d\d\d\d)')
    playing = re.compile('schedule_2022\d\d\d\d.+경기중">')
    playing2 = re.compile('schedule_2022(\d\d\d\d)')
    starter = re.compile('(?<=schedule_2022)(\d\d\d\d)|(선발)')
    left_team_list = left_team.findall(txtall)
    right_team_list = right_team.findall(txtall)
    left_score_list = left_score.findall(txtall)
    right_score_list = right_score.findall(txtall)
    date_list = date.findall(txtall)
    cancel_list = cancel.findall(txtall)
    cancel_list2 = []
    playing_list = playing.findall(txtall)
    playing_list2 = []
    for i in range(0, len(cancel_list)):
        cancel_list2.append(cancel2.findall(cancel_list[i])[-1])
    starter_list = starter.findall(txtall)
    
    for i in range(0, len(playing_list)):
        playing_list2.append(playing2.findall(playing_list[i])[-1])

    for i in range(0, len(starter_list)):
         if '선발' in starter_list[i][1]:
            if '선발' in starter_list[i + 1][1]:
                start[starter_list[i-1][0]] = "선발"
                break
            else:
                continue
   
    for a in range(0, len(date_list)):
        listst = []
        listst.append(left_team_list[a])
        if date_list[a] in playing_list2:    listst.append("경기")
        elif left_score_list[a][3] != '':    listst.append(left_score_list[a][3])
        elif date_list[a] in cancel_list2:    listst.append("취")
        elif date_list[a] in start.keys():    listst.append("선")
        else:   listst.append("--")
        if date_list[a] in playing_list2:    listst.append("중")
        elif right_score_list[a][3] != '':    listst.append(right_score_list[a][3])
        elif date_list[a] in cancel_list2:    listst.append("소")
        elif date_list[a] in start.keys():    listst.append("발")
        else: listst.append("--")
        listst.append(right_team_list[a])
        recentrecord[date_list[a]] = listst
        listst = []
   
    return recentrecord
