import datetime

x = datetime.datetime.now()
def __index(b,a):
    c=[]
    i=0
    a=str(a)
    for i in range(len(a)):
        if a[i]==b:
            c.append(i)
    return c

def __test(time):
    c=(__index(':',time)[0])
    hours=time[0:c]
    minute=time[c+1:]
    return int(hours) ,int(minute)
    
def __chech_month(month):
    if month==2:
        return 0
    elif month==4 or month==6 or month==9 or month==11:
        return 1
    else :
        return 2

def __process_date(date,pos,space,hours):
    slash=__index("-",date)
    year=int(date[0:slash[0]])
    month=int(date[slash[0]+1:slash[1]])
    day=int(date[slash[1]+1:space[0]])
    if int(hours)>=24:
        day+=1
        hours-=24
        if day>30 and __chech_month(month)==1:
            month=+1
            day-=30
        elif day>29 and __chech_month(month)==0:
            month+=1
            day-=28
        elif day>31 and __chech_month(month)==2:
            month+=1
            day-=31
        if month>12:
            year+=1
            month-=12
    elif int(hours)<0:
        day-=1
        hours+=24
        if day==0 and __chech_month(month-1)==1:
            day=30
            month-=1
        elif day==0 and __chech_month(month-1)==0:
            day=28
            month-=1
        elif day==0 and __chech_month(month-1)==2:
            day=31
            month-=1
        if month==0:
            month=12
            year-=1
    
    date_made=str(year)+'-'+str(month)+'-'+str(day)+" "+str(hours)+date[pos[0]:]
    return date_made

def __edit_time(delta,to_from):
    current_utc = datetime.datetime.utcnow()
    print("british time : ",current_utc)
    pos=__index(':',current_utc)
    space=__index(' ',current_utc)
    current_utc=str(current_utc)
    hours_edited=current_utc[space[0]+1:pos[0]]
    minute_edited=current_utc[pos[0]+1:pos[1]]
    if to_from=='+':
        minute_edited=int(minute_edited)+delta[1]
        hours_edited=int(hours_edited)+delta[0]
        if minute_edited>=60:
            hours_edited +=1
            minute_edited=minute_edited-60
        
    elif to_from=="-":
        hours_edited=int(hours_edited)-delta[0]
        minute_edited=int(minute_edited)-delta[1]
        if minute_edited<0:
            hours_edited -=1
            minute_edited=minute_edited+60
        
    edited_date=current_utc[0:space[0]+1]+str(hours_edited)+":"+str(minute_edited)+current_utc[pos[1]:]
    new_date=__process_date(edited_date,pos,space,hours_edited)
    
    return new_date
    

def time(enter_your_delta_time,posative_or_negative):
    delta=__test(enter_your_delta_time)
    new_time=__edit_time(delta,posative_or_negative)
    print("your time :    ",new_time)
country={
    'IRAQ':["03:00","+"],
    'UAE' :["04:00","+"],
    'KSA' :["03:00","+"],
}
def time_country(name):
    time(country[name][0],country[name][1])
