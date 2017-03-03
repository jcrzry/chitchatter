#parses messages and inserts html tags if necessary.

def checkForLink(message):
    valueList = message.split()
    for i in valueList:
        if len(i) > 4:
            if i[:4] == 'http':
                link = i
    return i
    
                
def isImage(link):
    comparisonList = ['.jpg','.png','.jpeg','.gif']
    for i in comparisonList:
        if link[-4:] == i or link[-5:] == i:
            b = True
        else:
            b = False
    return b
    
def returnLink(link, flag):
    if flag == True:
        return "<img src =' " + link + "'/>"
    else:
        return "<a href='" + link +"'> Link </a>"
    