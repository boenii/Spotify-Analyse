import json

filenumber = 0
m = 0
listened = 0
listened_time = 0
period_output = None


filepath_folder = 'd:\privat\Visual Studio Code\spotify-JSON-ANALyse\MyData'
period = "this year" # "this year" or "last 365 days"
artist = "Killstation"


while filenumber <= 5:
    filepath_json = filepath_folder+'\StreamingHistory'+str(filenumber)+'.json'

    with open(filepath_json, 'r', errors='ignore') as json_file:
        json_load = json.load(json_file)

    with open(filepath_json, errors='ignore') as f:
        data = len(json.load(f))
        for m in range(data):
            if artist in json_load[m]['artistName']:
                if period == "this year":
                    if "2022" in json_load[m]['endTime']:
                        if json_load[m]['msPlayed'] != 0:
                            listened = listened+1
                            listened_time = listened_time+json_load[m]['msPlayed']
                elif period == "last 365 days":
                    if json_load[m]['msPlayed'] != 0:
                        listened = listened+1
                        listened_time = listened_time+json_load[m]['msPlayed']
    
        m = m+1
    filenumber = filenumber+1 

if period == "this year":
    period_output = "Du hast dieses Jahr "
elif period == "last 365 days":
    period_output = "Du hast in den letzten 365 Tagen "

useroutput = period_output + str(listened) + " mal " + artist + " gehört" + "\ndas sind " + str(listened_time/1000/60/60) + " Stunden, das sind " + str(listened_time/1000/60/60/24) + " Tage"
print(useroutput)