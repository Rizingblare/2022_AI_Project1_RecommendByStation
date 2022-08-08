import os
import re
import csv
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import StationInfo

# Create your views here.

def index(request):
    return render(request, 'recommendByStation\index.html')

def csv2Model(request):
    path = 'recommendByStation\data\부산교통공사_도시철도역정보_20211020.csv'
    container = []
    with open(path,'r') as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            container.append(StationInfo(
                stationNum = row[0],
                stationKor = row[1],
                stationEng = row[2],
                stationTel = row[3],
                stationBikeStorage = (row[6] == 'O'),
                stationItemStorage = (row[7] == 'O'),
                stationTip = row[12],
            ))
    StationInfo.objects.bulk_create(container)
    return HttpResponse('Success to create model ~~ !!')

def DadaepoBeach(request):
    target = 'Dadaepo Beach'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }
    return render(request, f'recommendBystation\stations\\{target}.html', context)

def DadaepoHarbor(request):
    target = 'Dadaepo Harbor'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }
    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Natgae(request):
    target = 'Natgae'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Sinjangnim(request):
    target = 'Sinjangnim'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Jangnim(request):
    target = 'Jangnim'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Dongmae(request):
    target = 'Dongmae'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Sinpyeong(request):
    target = 'Sinpyeong'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Hadan(request):
    target = 'Hadan'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Dangni(request):
    target = 'Dangni'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Saha(request):
    target = 'Saha'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Goejeong(request):
    target = 'Goejeong'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Daeti(request):
    target = 'Daeti'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Seodaesin(request):
    target = 'Seodaesin'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Dongdaesin(request):
    target = 'Dongdaesin'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Toseong(request):
    target = 'Toseong'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Jagalchi(request):
    target = 'Jagalchi'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Nampo(request):
    target = 'Nampo'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Jungang(request):
    target = 'Jungang'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def BusanStation(request):
    target = 'Busan Station'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Choryang(request):
    target = 'Choryang'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Busanjin(request):
    target = 'Busanjin'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Jwacheon(request):
    target = 'Jwacheon'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Beomil(request):
    target = 'Beomil'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Beomnaegol(request):
    target = 'Beomnaegol'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Seomyeon(request):
    target = 'Seomyeon'

    targetInfo = StationInfo.objects.get(stationKor='서면(1)')
    print(targetInfo)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Bujeon(request):
    target = 'Bujeon'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Yangjeong(request):
    target = 'Yangjeong'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def CityHall(request):
    target = 'City Hall'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    target = target.replace(r"[ .]","")
    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Yeonsan(request):
    target = 'Yeonsan'

    targetInfo = StationInfo.objects.get(stationKor='연산(1)')
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def BusanNatlUnivEdu(request):
    target = 'Busan Natl Univ. Edu.'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }
    
    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Dongnae(request):
    target = 'Dongnae'

    targetInfo = StationInfo.objects.get(stationKor='동래(1)')
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Myeongnyun(request):
    target = 'Myeongnyun'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Oncheonjang(request):
    target = 'Oncheonjang'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def PusanNatlUniv(request):
    target = 'Pusan Natl Univ'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    
    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Jangjeon(request):
    target = 'Jangjeon'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Guseo(request):
    target = 'Guseo'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Dusil(request):
    target = 'Dusil'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Namsan(request):
    target = 'Namsan'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Beomeosa(request):
    target = 'Beomeosa'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)

def Nopo(request):
    target = 'Nopo'

    targetInfo = StationInfo.objects.get(stationEng=target)
    target = re.sub("[ .]","", target)
    csvDF = pd.read_csv(f'recommendByStation\data\stations\\{target}.csv')
    top10 = csvDF.sort_values(by=['평점'], ascending = False).head(10).to_numpy().tolist()
    context = {
        'stationInfo' : targetInfo,
        'top10Store' : top10,
    }

    return render(request, f'recommendBystation\stations\\{target}.html', context)
