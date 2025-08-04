def time (generation, year, month,day, hour):
    hour += 1
    if hour >24:
        day +=1
        hour = 0
    if day > 30:
        month +=1
    if month > 12:
        year +=1
        month = 0  
    if year > 30:
        generation +=1

    return generation, year, month,day,hour    