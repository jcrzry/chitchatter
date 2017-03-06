#parses messages and inserts html tags if necessary.

def checkForLink(message):
    valueList = message.split()
    for i in valueList:
        if len(i) > 4:
            if i[:4] == 'http':
                link = i
                return link
            
    
                
def isImage(link):
    comparisonList = ['.jpg','.png','.jpeg','.gif']
    if link[-4:] in comparisonList or link[-5:] in comparisonList:
        b = True
    else:
        b = False
    return b
    
def returnLink(link, flag):
    if flag == True:
        return "<img class ='submittedImg' src='" + link + "'/>"
    else:
        return "<a href='" + link +"'>"+ link +"</a>"

def getWrappedMessage(message):
    link = checkForLink(message)
    if link != None:
        b = isImage(link)
        return message.replace(link,returnLink(link,b))
    else:
        return message