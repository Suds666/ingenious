from django.shortcuts import render

# Create your views here.
import urllib.request
import json
import http.client
import re



def index(request):
    
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen()
        season = request.POST['season']


    conn = http.client.HTTPSConnection("visual-crossing-weather.p.rapidapi.com")

    headers = {
        'content-type': "application/octet-stream",
        'X-RapidAPI-Key': "936e1ac239msh7df431a948dca44p16d75djsn762b9335897d",
        'X-RapidAPI-Host': "visual-crossing-weather.p.rapidapi.com"
    }
    def split_string(s):
    # use regular expression to find quoted substrings
        quoted_substrings = re.findall('"[^"]*"|\'[^\']*\'', s)
        # replace the quoted substrings with placeholders
        for i, substr in enumerate(quoted_substrings):
            s = s.replace(substr, f'__QUOTED{i}__')
        # split the string by commas
        parts = s.split(',')
        # replace the placeholders with the original quoted substrings
        for i, substr in enumerate(quoted_substrings):
            parts = [p.replace(f'__QUOTED{i}__', substr) for p in parts]
        # strip leading and trailing whitespace from each part
        parts = [p.strip() for p in parts]
        return parts
    
    def bigbang(n):
        conn.request("GET", n, headers=headers)
        res = conn.getresponse()
        data = res.read()

        a = data.decode("utf-8")
        b = a[314:]
        c = b.split('\n')
        c.pop()
        l3 = []

        for i in c:
            l3.append(split_string(i))

        l3.pop(0)
        string1 = 'Address,Date time,Minimum Temperature,Maximum Temperature,Temperature,Dew Point,Relative Humidity,Heat Index,Wind Speed,Wind Gust,Wind Direction,Wind Chill,Precipitation,Precipitation Cover,Snow Depth,Visibility,Cloud Cover,Sea Level Pressure,Weather Type,Latitude,Longitude,Resolved Address,Name,Info,Conditions'
        l1 = []
        l2 = []
        for string2 in l3:
        # Split string1 by comma to get keys
            keys = string1.strip().split(',')

                # Split string2 by comma to get values

            dictionary = dict(zip(keys, string2))

            l1.append(dictionary)
        for i in l1:
            l2.append(i['Precipitation'])
        
        for i in l2:
            l2[l2.index(i)] = float(i)
        return sum(l2)
    if season == 'kharif':
        

        
        p1 = f"/history?startDateTime=2022-06-01&aggregateHours=24&location={city}&endDateTime=2022-06-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        p2 = f"/history?startDateTime=2022-07-01&aggregateHours=24&location={city}&endDateTime=2022-07-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        p3 = f"/history?startDateTime=2022-08-01&aggregateHours=24&location={city}&endDateTime=2022-08-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        p4 = f"/history?startDateTime=2022-09-01&aggregateHours=24&location={city}&endDateTime=2022-09-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        df1 = bigbang(p1)
        df2 = bigbang(p2)
        df3 = bigbang(p3)
        df4 = bigbang(p4)

        dl = df1+df2+df3+df4
        return render(request, 'main/index.html', dl)

    if season == 'rabi':
        

        
        p5 = f"/history?startDateTime=2022-09-01&aggregateHours=24&location={city}&endDateTime=2022-09-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        p6 = f"/history?startDateTime=2022-10-01&aggregateHours=24&location={city}&endDateTime=2022-10-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        p7 = f"/history?startDateTime=2022-11-01&aggregateHours=24&location={city}&endDateTime=2022-11-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        p8 = f"/history?startDateTime=2022-12-01&aggregateHours=24&location={city}&endDateTime=2022-12-30&unitGroup=us&dayStartTime=8%3A00%3A00&contentType=csv&dayEndTime=17%3A00%3A00&shortColumnNames=0"
        df5 = bigbang(p5)
        df6 = bigbang(p6)
        df7 = bigbang(p7)
        df8 = bigbang(p8)

        dl2 = df5+df6+df7+df8
        return render(request, 'main/index.html', dl2)

