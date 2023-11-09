def hour_min(time):
    l=time.split(':')
    return [int(l[0]),int(l[1])] 
    
def calcDays(timeStart):
    if(timeStart[1]>59):
        addMinuts=timeStart[1]%59
        addHoures=timeStart[1]//59
        timeStart[0]=timeStart[0]+addHoures
        timeStart[1]=addMinuts
    jourAded=0
    hoursAded=0
    if(timeStart[0]>23):
        jourAded=timeStart[0]//23
        timeStart[0]=timeStart[0]%23-1

    return[jourAded,timeStart[0],timeStart[1]]
        
        
    
  def add_time(timeNow,timeAded,dayNow=0):
    AM=['00:00','11:59']
    PM=['12:00','23:59']
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    l1=timeNow.split()
    hourAndMinutNow=hour_min(l1[0])
    if(l1[1]=='PM'):
        hourAndMinutNow[0]=hourAndMinutNow[0]+12

    hourAndMinutAded=hour_min(timeAded)

    totalHourAndMinut =[hourAndMinutNow[0]+hourAndMinutAded[0],hourAndMinutNow[1]+hourAndMinutAded[1]]
    result=calcDays(totalHourAndMinut)

    dayAded=result[0]
    partOfDay='AM'
    if(result[1]>11):
        partOfDay='PM'
    hour=str(result[1])
    minut=str(result[2])
    if(len(minut)==1):
        minut='0'+minut
    if(len(hour)==1):
        hour='0'+hour

    if(dayNow!=0):
        nbDay=(days.index(dayNow)+dayAded)%7
        endDay=days[nbDay]
        if(dayAded==0):
            print (hour +':'+minut+' '+partOfDay+' '+endDay)
        else :
            print (hour +':'+minut+' '+partOfDay+' '+endDay+' ('+str(dayAded)+' days later)' )
            
        
    else :
        print (hour +':'+minut+' '+partOfDay)

      
  
add_time("11:30 AM", "25:32", "Monday")
