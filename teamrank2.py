import requests
import re

def relrank21(a, b):
    url = "https://www.koreabaseball.com/TeamRank/TeamRank.aspx"
    name_list = ['KIA 타이거즈','KT 위즈','LG 트윈스','NC 다이노스','SSG 랜더스','두산 베어스','롯데 자이언츠','삼성 라이온즈','키움 히어로즈','한화 이글스']
    txtall = requests.get(url).text
    rank1 = []
    rank = {}
    relative_rank = []

    i = 1
    team = re.compile('>(\d+)</td>\s+<td>(\D\D\D?)</td>')
    rank1 = team.findall(txtall)

    for m in range(0, len(rank1)):
        rank[rank1[m][1]] = m + 1

    relative_rank.append(a)
    relative_rank.append(b)
    relative_rank.append(rank[a] - rank[b])
    return relative_rank

