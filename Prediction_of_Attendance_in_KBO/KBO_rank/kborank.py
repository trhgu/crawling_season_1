import pandas as pd
import requests


def KBO_rank(date):
    data1 = []

    for i in date:
        pre, pro = i
        url = "https://www.koreabaseball.com/ws/TeamRank.asmx/GetTeamRankDaily?startDate={}&endDate={}".format(
            pre, pro)
        response = requests.get(url)
        data = response.json()
        for num in range(0, 10):
            team = data['data'][num]["name"]
            rank = data['data'][num]["data"]

            for i in rank:
                if len(str(i[1])) == 1:
                    a = "0" + str(i[1] + 1)
                else:
                    a = i[1]

                if len(str(i[2])) == 1:
                    b = "0" + str(i[2])
                else:
                    b = i[2]
                
                data1.append({team:
                          {"date": str(i[0])+ "/" + str(a) + "/" + str(b),
                           "rank": i[3],
                           }})

    date = []
    hw = []
    kia = []
    kt = []
    lg = []
    ld = []
    nc = []
    ob = []
    sk = []
    ss = []
    kw = []

    for dic in data1:
        for key, value in dic.items():
            if key == "한화":
                date.append(value["date"])
            if key == "한화":
                hw.append(value["rank"])
            if key == "KIA":
                kia.append(value["rank"])
            if key == "KT":
                kt.append(value["rank"])
            if key == "LG":
                lg.append(value["rank"])
            if key == "롯데":
                ld.append(value["rank"])
            if key == "NC":
                nc.append(value["rank"])
            if key == "두산":
                ob.append(value["rank"])
            if key == "SK":
                sk.append(value["rank"])
            if key == "삼성":
                ss.append(value["rank"])
            if key == "넥센":
                kw.append(value["rank"])
            if key == "키움":
                kw.append(value["rank"])

    gg = pd.DataFrame(columns=("date", "hw", "kia", "kt", "lg",
                               "ld", "nc", "ob", "sk", "ss", "kw"))

    gg["date"] = date
    gg["hw"] = hw
    gg["kia"] = kia
    gg["kt"] = kt
    gg["lg"] = lg
    gg["ld"] = ld
    gg["nc"] = nc
    gg["ob"] = ob
    gg["sk"] = sk
    gg["ss"] = ss
    gg["kw"] = kw
    
    return gg
