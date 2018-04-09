import calendar
'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

def week():
    index=0
    
    while index < 7:
        
        yield list(calendar.day_name)[index]
        index +=1

Week  = week()
for x in Week:
    print(x)