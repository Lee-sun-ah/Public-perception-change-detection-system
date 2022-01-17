from django.shortcuts import render
from .models import Twitter
from .models import News
import pandas as pd
# Create your views here.

def index(request):
    datas=Twitter.objects.all()
    for i in datas:
        i.date=str(i.date).replace('2021-','')
        i.date=str(i.date).replace('-','월 ')
        i.date=i.date+"일"
    datas2=News.objects.all()
    for j in datas2:
        j.date=str(j.date).replace('2021-','')
        j.date=str(j.date).replace('-','월 ')
        j.date=j.date+"일"
    df=pd.read_excel(r'D:\과제\개별연구\project\main\datalab.xlsx')
    date=[]
    interest=[]
    for i in range(len(df)):
        date.append(str(df.loc[i][0][5:7])+"월 "+str(df.loc[i][0][8:10])+"일") 
        interest.append(float(df.loc[i][1]))
    return render(request,'main/index.html',{"datas":datas,"datas2":datas2,"date":date,"interest":interest})