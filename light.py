def light_period(light_readings):
    length=len(light_readings)
    count=[1]*length
    a=0
    for i in range(length):
        if(light_readings[i]>=70):
            if(light_readings[i+1]>=light_readings[i] or light_readings[i+1]>=70):
                count[a]=count[a]+1
        else:
            a=a+1
    on_period=max(count)    
    actual_period=0
    for j in count:
        if(j>=5 and j<on_period):
            actual_period=on_period+j
    
    if(actual_period==0):
        return(on_period)
    else:
        return(actual_period)
# light_readings=[4,4,5,5,4,3,3,4,5,77,77,77,78,79,80,81,88,90,95,100,100,110,115,135,145,158,158,190,200,200,200,200,200, 7,8,8,8]
# light_readings=[4,5,100,8, 9, 11, 2, 3,4,5,6,5,4,5,4,100,110,115,135,145,158,158,190,200,200,200,200,7,8,8,8,4,5,11,2,12,24,25,26,27,28,29,30,30,30,30,30,30,30]
light_readings=[40,50,100,80, 90, 110, 20, 30,40,50,60,50,40,50,40,200,210,215,235,245,250,250,230,240,200,200,200,190,190,200,150,70,80,80,80,40,50,110,20,120,40,25,26,27,28,29,30,30,30,30,30,31,30]
print (str(light_period(light_readings))+' ms')

