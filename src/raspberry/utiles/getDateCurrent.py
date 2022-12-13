import datetime


def getDate_Current():
    currentDatetime = datetime.datetime.now()
    formatDate = currentDatetime.strftime("%d-%m-%y")
    return formatDate
