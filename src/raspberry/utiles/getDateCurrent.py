import datetime 

def getDate_Current():
    currentDatetime = datetime.datetime.now()
    formatDate = currentDatetime.strftime("%y-%m-%d")
    return formatDate
