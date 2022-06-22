from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
import pandas as pd
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

def Beomnaegol(request):
    station = 'Beomnaegol'
    stationInfo = StationInfo.objects.get(stationNum=118)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Beomil(request):
    station = 'Beomil'
    stationInfo = StationInfo.objects.get(stationNum=117)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수','블로그 리뷰 수']] = top10Df[['방문자 리뷰 수','블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Jwacheon(request):
    station = 'Jwacheon'
    stationInfo = StationInfo.objects.get(stationNum=116)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Busanjin(request):
    station = 'Busanjin'
    stationInfo = StationInfo.objects.get(stationNum=115)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Choryang(request):
    station = 'Choryang'
    stationInfo = StationInfo.objects.get(stationNum=114)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def BusanStation(request):
    station = 'BusanStation'
    stationInfo = StationInfo.objects.get(stationNum=113)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Jungang(request):
    station = 'Jungang'
    stationInfo = StationInfo.objects.get(stationNum=112)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Nampo(request):
    station = 'Nampo'
    stationInfo = StationInfo.objects.get(stationNum=111)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)

def Jagalchi(request):
    station = 'Jagalchi'
    stationInfo = StationInfo.objects.get(stationNum=110)
    path = f'recommendByStation\data\\{station}.csv'
    csvDf = pd.read_csv(path)
    top10Df = csvDf.sort_values(by=['평점'], ascending = False).head(10)
    top10Df[['방문자 리뷰 수', '블로그 리뷰 수']] = top10Df[['방문자 리뷰 수', '블로그 리뷰 수']].astype(int)
    top10Arr = top10Df.to_numpy()
    top10List = top10Arr.tolist()

    context = {
        'stationInfo' : stationInfo,
        'top10Store': top10List,
    }

    return render(request, f'recommendByStation\\{station}.html', context)