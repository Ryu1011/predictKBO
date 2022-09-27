import requests
import re
from pandas import DataFrame as df
from recentrecord2 import recentrecord21

def startrecord(name):
    result = []
    url="https://search.naver.com/search.naver?sm=tab_sug.mbk&where=nexearch&query="
    url2 = "https://www.google.com/search?q="
    url3 = "https://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId="
    name_list = ['KIA 타이거즈','KT 위즈','LG 트윈스','NC 다이노스','SSG 랜더스','두산 베어스','롯데 자이언츠','삼성 라이온즈','키움 히어로즈','한화 이글스']
    name_list1 = ['KIA', 'KT', 'LG', 'NC', 'SSG', '두산', '롯데', '삼성', '키움', '한화']
    txtall = requests.get(url+"{}".format(name_list[int(name)-1])).text

    startm = re.compile('<span class="name">(\w+)<')
    startm_list = startm.findall(txtall)[-2 : ]
    
    finddate1 = list(recentrecord21(name).values())
    for i in range(0, len(finddate1)):
        if finddate1[i][1] == ('선' or '경기'):
            break
        elif finddate1[i][1] == '--':
            i += -1
            break
    startmt_list = []
    startmt_list.append(finddate1[i][0])
    startmt_list.append(finddate1[i][3])

    mid = []
    for j in range(0, 2):
        txtall2 = requests.get(url2+"{} {} kbo 기록".format(startmt_list[j], startm_list[j])).text
        startm1 = re.compile('playerId%3D(\d+)')
        startm12 = startm1.findall(txtall2)
        mid.append(startm12[0])
      
    for m in range(0, 2):
        record = {}
        txtall3 = requests.get(url3+"{}".format(mid[m])).text
        
        record1 = re.compile('<td>(\d*[ ]?[.]?[-]?[\d*]?/?\d*)</td>')
        record2 = record1.findall(txtall3)
        record["name"] = startm_list[m]
        if len(record2) > 20:
            record["WHIP"] = float(record2[26])
            record["AVG"] = float(record2[27])
        else :
            record['WHIP'] = "--"
            record["AVG"] = " --"
        result.append(record)
        record = {}
    out = df(result, columns=["name", "WHIP", "AVG"], index = [startmt_list[0], startmt_list[1]])
    print(out)
    return result
