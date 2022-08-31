import datetime
from time import strptime
filename="input.txt"
fileobj=open(filename)
params={}
dicts={}
for line in fileobj:
    line=line.strip()
    key_value=line.split()
    if len(key_value)==3:
        subscription=key_value[0]
        item=key_value[1]
        plan=key_value[2]
        if subscription not in params:
            params[subscription] = []
        params[subscription].append(item)
        params[subscription].append(plan)
    if len(key_value)==2:
        subscription=key_value[0]
        item=key_value[1]
        dicts[subscription] = []
        dicts[subscription].append(item)

dates=dicts["START_SUBSCRIPTION"]
dates_string = ' '.join([str(elem) for elem in dates])
fileobj.close
filen="output.txt"
fileob=open(filen, "a")

def change_date(given_list,dates_string):
    ci=given_list[0]
    dates_val=dates_string.split("-")
    day_val=int(dates_val[0])
    month_val=int(dates_val[1])
    year_val=int(dates_val[2])


    if "PERSONAL" in given_list:
        month_val+=1
        if(month_val>12):
            month_val%=12
            year_val+=1
        mo_val=str(month_val)
        ye_val=str(year_val)
        da_val=str(day_val)
            
    if "FREE" in given_list:
        month_val+=1
        if(month_val>12):
            month_val%=12
            year_val+=1
        mo_val=str(month_val)
        ye_val=str(year_val)
        da_val=str(day_val)

    if "PREMIUM" in given_list:
        month_val+=3
        if(month_val>12):
            month_val%=12
            year_val+=1
        mo_val=str(month_val)
        ye_val=str(year_val)
        da_val=str(day_val)
    dates_values=""  
    dates_values=dates_values+da_val+"-"+mo_val+"-"+ye_val
    fileob.write("RENEWAL_REMINDER ")
    fileob.write(ci)
    fileob.write("\t")
    fileob.write(dates_values)
    fileob.write("\n")
    print("RENEWAL_REMINDER",ci,dates_values,"\n")


def price(give_list,mon):
    if "MUSIC" in give_list:
        if "PERSONAL" in give_list:
            mon+=100
        if "FREE" in give_list:
            mon+=0
        if "PREMIUM" in give_list:
            mon+=250
    if "VIDEO" in give_list:
        if "PERSONAL" in give_list:
            mon+=200
        if "FREE" in give_list:
            mon+=0
        if "PREMIUM" in give_list:
            mon+=500
    

    if "PODCAST" in give_list:
        if "PERSONAL" in give_list:
            mon+=100
        if "FREE" in give_list:
            mon+=0
        if "PREMIUM" in give_list:
            mon+=300
    return mon


    subscription_list=[]
subscription_list=params["ADD_SUBSCRIPTION"]
add_topup=[]
add_topup=params["ADD_TOPUP"]
length_subscription_list=len(subscription_list)
music_list=[]
video_list=[]
podcast_list=[]

if "MUSIC" in subscription_list:
    m=subscription_list.index("MUSIC")
for i in range(m,m+2):
    music_list.append(subscription_list[i])

if "VIDEO" in subscription_list:
    v=subscription_list.index("VIDEO")
for i in range(v,v+2):
    video_list.append(subscription_list[i])

if "PODCAST" in subscription_list:
    p=subscription_list.index("PODCAST")
for i in range(p,p+2):
    podcast_list.append(subscription_list[i])


dates_val=dates_string.split("-")
day_val=int(dates_val[0])
month_val=int(dates_val[1])
if(month_val>12):
        fileob.write("INVALID_DATE")
        fileob.write("\n")
        fileob.write("ADD_SUBSCRIPTION_FAILED")    
        fileob.write("\t")
        fileob.write("INVALID_DATE")
        
if(month_val<=12):
    money=0
    if "MUSIC" in music_list:
        change_date(music_list,dates_string)
        money=price(music_list,money)
    if "VIDEO" in video_list:    
        change_date(video_list,dates_string)
        money=price(video_list,money)
    if "PODCAST" in podcast_list:
        change_date(podcast_list,dates_string)
        money=price(podcast_list,money)
    if ("FOUR_DEVICE" in add_topup) or ("TEN_DEVICE" in add_topup):
        ki=int(add_topup[1])
        if ("MUSIC" in music_list) or ("VIDEO" in video_list) or ("PODCAST" in podcast_list):
            if "FOUR_DEVICE" in add_topup:
                money=money+ki*50
            if "TEN_DEVICE" in add_topup:
                money=money+ki*100  
    ka=str(money)
    fileob.write("RENEWAL_AMOUNT")
    fileob.write("\t")
    fileob.write(ka)
    print("RENEWAL_AMOUNT\t",ka)
