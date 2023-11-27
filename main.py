from datetime import datetime, date, timedelta

def sortSecond(val): 
    return val['birthday'] 


def get_birthdays_per_week (list1):
    birthdays = {}
    weekDaysMapping = ("Monday", "Tuesday", 
                   "Wednesday", "Thursday",
                   "Friday")
    t_date = date.today()
    
    for el in list1:
        birth = el['birthday'].replace(year = t_date.year)
        if birth  < t_date:
            birth =  el['birthday'].replace(year = t_date.year + 1)
        el['birthday'] = birth

    list1 = list(list1) 
    list1.sort(key=sortSecond)    
    week_interval = timedelta(days=8) 
    f_date = t_date + week_interval
    
    for el in list1:    
        birth = el['birthday']
        if  birth < f_date:            
            if  birth.weekday() == 5 or birth.weekday() == 6:  
                birthdays["Monday"] = birthdays.get('Monday', []) + [el['name']]     
            else: 
                dayOfTheWeek = weekDaysMapping[birth.weekday()]
                birthdays[dayOfTheWeek] = birthdays.get(dayOfTheWeek, []) + [el['name']]
    
    return birthdays  


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    print(list(result))
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")                  