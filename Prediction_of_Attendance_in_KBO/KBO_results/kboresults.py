import requests
import pandas as pd

def kboresults(year, month, team):
    game_dic = []
    
    # json url search and Query pattern search
    for y in year:
        for m in month:
            for t in team:
                url = "https://www.koreabaseball.com/ws/Schedule.asmx/GetScheduleList?leId=1&srIdList=0%2C9&seasonId={}&gameMonth={}&teamId={}".format(y, m, t)
                # Request response
                response = requests.get(url)
                # Parsing
                data = response.json()["rows"]
                
                # Data select
                for n in range(0,31):
                    try:
                        year_c = y 
                        date = data[n]['row'][0]['Text'] #날짜
                        time = data[n]['row'][1]['Text'] #시간
                        result = data[n]['row'][2]['Text'] #경기결과
                        park = data[n]['row'][7]['Text']  #구장
                        etc = data[n]['row'][8]['Text'] #비고
                                
                        game_dic.append({
                            "year" : year_c,
                            "dates" : date,
                            "times" : time,
                            "results" : result,
                            "parks" : park,
                            "etcs" : etc,            
                            })
                    
                    except:
                        break
    
    #Data processing
    game = pd.DataFrame(game_dic)
    game['times'] = game['times'].str.replace('<b>',' ').str.replace('</b>',' ')
    game['results'] = game['results'].str.replace('<span class="win">',' win ').str.replace('<span class="lose">',' lose ').str.replace('<span class="same">',' same ').str.replace('</span><span>',' ').str.replace('</span></em><span>',' ').str.replace('<span>','').str.replace('</span>','').str.replace('<em>','').str.replace('</em>','')
    results_split = pd.DataFrame([x.split(' ') for x in sum([list([x]) for x in game["results"]], [])])
    dates_split = pd.DataFrame([x.split('(') for x in sum([list([x]) for x in game["dates"]], [])])
    game["away"] = results_split[0]
    game["homewin"] = results_split[4]
    game["home"] = results_split[6]
    game["weekday"] = dates_split[1].str.replace(")","")
    game = game.drop(["results"],axis = 1)
    game["dates"] = game["year"]+'/' + game["dates"].str[:2] +"/" + game["dates"].str[3:5]
    game = game.drop(["year"],axis = 1)
    game = game[["dates", "parks", "away", "home", "homewin", "etcs", "times" ]]
    game['dates'] = game['dates'].str.replace(".","/")
    game = game.drop_duplicates(subset=['dates','parks'], keep='first')
    game.reset_index(drop=True, inplace=True)
    
    return game                
