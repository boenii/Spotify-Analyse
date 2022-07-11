import json

filenumber = 0
m = 0
listened = 0
listened_time = 0


while filenumber<=5:
    filepath_json = 'd:\privat\Visual Studio Code\spotify-JSON-ANALyse\MyData\StreamingHistory'+str(filenumber)+'.json'

    with open(filepath_json, 'r', errors='ignore') as json_file:
        json_load = json.load(json_file)


    with open(filepath_json, errors='ignore') as f:
        data = len(json.load(f))
        for m in range(data):
            if "2022" in json_load[m]['endTime']:
                if json_load[m]['msPlayed'] != 0:
                    listened = listened+1
                    listened_time = listened_time+json_load[m]['msPlayed']
    
        m = m+1
    filenumber = filenumber+1 

useroutput = "Du hast dieses Jahr " + str(listened) + " Songs gehört," + "\ndas sind " + str(listened_time/1000/60/60) + " Stunden, oder " + str(listened_time/1000/60/60/24) + " Tage"
print(useroutput)