#swansonbot.py
# import models
import requests
import os
import json

botID = 7

def botResponses(message):
    if message[:2] != '!!':
        #do nothingr
        return ""
    if(len(message.split())) == 2:
        prompt, command = message.split(" ",2)
    else:
        prompt, command, argu = message.split(" ", 2)
    if command.lower() == 'about':
        reply = "Welcome all! You are amongst a fine group of people here in Pawnee. In this message \
        we talk about all things wood, parks, or recreation. We occasionally dable with the cones of dunshire! Also,\
        if you have any pictures of little sebastion, please share!"
    elif command.lower() == 'help':
        reply = "Try one of these commands: about, \n say (i'll repeat something), \n neigh, \n notknope, \n parkInfo [State abreviation] [name]"
    elif command.lower() == 'say':
        reply = argu
    elif command.lower() == "neigh":
        reply = "Here's a wiki for poor lil' sebastian. http://parksandrecreation.wikia.com/wiki/Li'l_Sebastian"
    elif command.lower() == 'notknope':
        reply = "Leslie Knope 2012!"
    elif command.lower() == 'park info':
        state, query = argu.split(" ",2)
        reply = get_parks(state,query)
    else:
        reply = "I'm not sure what you're trying to say...You must be from Eagleton."
    return reply
    
def get_parks(state, query):
    parksKey = os.getenv('parksKey')
    header = {'Authorization': '313A6491-C8D5-4791-B9EC-B236856FCDEB'}
    print('parksKey:',os.getenv('parksKey'))
    queryString = 'https://developer.nps.gov/api/v0/parks?limit=10&stateCode=' + state + '&q'+query
    apiResponse = requests.get(queryString, headers=header)
    json2 = apiResponse.json()
    formattedResult = "Please Try again Eagletonian."
    for i in json2['data']:
        if i['name'].lower() == query.lower():
            result = i
            formattedResult = \
            "Here's some info on " + result['fullName'] + "\n directions: <a href = '" +  result['directionsUrl'] + "'> Get Directions</a> \
            \n Website: <a href='" + result['url'] + "'>" + result['url'] + "</a> \n Weather: " + result['weatherInfo']
    return formattedResult

