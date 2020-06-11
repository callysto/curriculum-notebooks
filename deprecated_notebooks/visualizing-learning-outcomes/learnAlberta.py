#!/usr/bin/env python
# learnAlberta.py

'''
What a mess!

This is where I dumped the ugly and unpolished bits to
achieve a bareknuckle recovery of Alberta Education learning outcomes.

Deadlines must be met.

Assembled by Eric Easthope
MIT License
'''

from requests import get
from bs4 import BeautifulSoup as bs
from bs4.dammit import EncodingDetector
url = 'http://www.learnalberta.ca/ProgramsOfStudy.aspx'

def removeBrackets(string):
    start = string.find('(')
    end = string.find(')')
    if start != -1 and end != -1:
        return (string[:start] + string[end+1:]).strip();

# parse corresponding page HTML for a subject
def soupForField(field):
    params = {
        "lang": "en",
        "posLang": "en",
        "Core": field
    }
    
    r = get(url, params=params)
    httpEncoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
    htmlEncoding = EncodingDetector.find_declared_encoding(r.content, is_html=True)
    encoding = htmlEncoding or httpEncoding; encoding
    return bs(r.content, "lxml", from_encoding=encoding)

# parse corresponding page HTML for a program
def soupForProgram(programID):
    import json
    url = 'http://www.learnalberta.ca/ProgramOfStudy.aspx'
    params = {
        "lang": "en",
        "ProgramId": programID
    }
    r = get(url, params=params)
    httpEncoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
    htmlEncoding = EncodingDetector.find_declared_encoding(r.content, is_html=True)
    encoding = htmlEncoding or httpEncoding; encoding
    return bs(r.content, "html5lib", from_encoding=encoding)

def getSpecificOutcomes(generalOutcome):
    specificOutcomes = generalOutcome.find_all('div', class_='formalp')
    specificOutcomeData = []
    for outcome in specificOutcomes:
        outcomeList = []
        # get enumeration for specific outcome
        outcomeNumber = ''.join(c for c in outcome.find('div').text if c.isdigit())

        # get specific outcome description
        description = outcome.find('p').text.strip().replace('\r', ' ').replace(':', '').replace('.', '').replace('\n', ' ')
        descriptionEnding = outcome.find(text=True, recursive=False)

        # if they exist, distinguish bullet points
        bullets = []
        bulletList = outcome.find('ul')
        if bulletList is not None:
            for b in bulletList.find_all('li'):
                bullets.append(b.text.replace('.', ''))

        bulletDescriptions = [description+' '+b+' '+descriptionEnding.strip().replace('.', '') for b in bullets]

        # learning processes: "critical aspects of learning, doing and understanding"
        processes = [a.text for a in outcome.find_next_sibling().find_all('a')]
        if len(processes) == 0:
            processes = [a.text for a in outcome.find_next_sibling().find_next_sibling().find_all('a')]

        fullDescription = description + (descriptionEnding if descriptionEnding is not None else '')
        if len(bulletDescriptions) != 0:
            for description in bulletDescriptions:
                outcomeList.append(description.strip())
        else:
            outcomeList.append(fullDescription)
        specificOutcomeData.append({
            'name': 'Specific Outcome'+' '+outcomeNumber,
            'outcomes': outcomeList,
            'processes': processes
        })
    return specificOutcomeData;

def getOutcomesByIndex(index):
    outcomes = []
    generalOutcome = rationaleSections[index].find_next_sibling().parent
    outcomeTitleText = generalOutcome.find('div', class_='title').text # first title instance
    outcomeTitle = removeBrackets(outcomeTitleText)

    outcomeDescriptionText = generalOutcome.find('div', class_='subtitle').text # first subtitle instance
    colonIndex = outcomeDescriptionText.find(':')
    outcomeDescription = outcomeDescriptionText[colonIndex+1:].replace('.', '').strip()

    outcomeCode = ''.join(c for c in outcomeTitle if c.isupper())
    identifier = topic[:2].upper()+course+'.'+outcomeCode
    
    # append general outcome
    outcomes.append([identifier, ' - '.join([outcomeTitle, outcomeDescription]), []])
    
    for i, outcome in enumerate(getSpecificOutcomes(generalOutcome)):
        for j, o in enumerate(outcome['outcomes']):
            if len(outcome['outcomes']) > 1:
                outcomes.append([identifier + str(i+1) + chr(ord('A') + j), o, outcome['processes']])
            else:
                outcomes.append([identifier + str(i+1), o, outcome['processes']])
    return outcomes;
    
def getSpecificOutcomes(generalOutcome):
    specificOutcomes = generalOutcome.find_all('div', class_='formalp')
    specificOutcomeData = []
    for outcome in specificOutcomes:
        outcomeList = []
        # get enumeration for specific outcome
        outcomeNumber = ''.join(c for c in outcome.find('div').text if c.isdigit())

        # get specific outcome description
        description = outcome.find('p').text.strip().replace('\r', ' ').replace(':', '').replace('.', '').replace('\n', ' ')
        descriptionEnding = outcome.find(text=True, recursive=False)

        # if they exist, distinguish bullet points
        bullets = []
        bulletList = outcome.find('ul')
        if bulletList is not None:
            for b in bulletList.find_all('li'):
                bullets.append(b.text.replace('.', ''))

        bulletDescriptions = [description+' '+b+' '+descriptionEnding.strip().replace('.', '') for b in bullets]

        # learning processes: "critical aspects of learning, doing and understanding"
        processes = [a.text for a in outcome.find_next_sibling().find_all('a')]
        if len(processes) == 0:
            processes = [a.text for a in outcome.find_next_sibling().find_next_sibling().find_all('a')]

        fullDescription = description + (descriptionEnding if descriptionEnding is not None else '')
        if len(bulletDescriptions) != 0:
            for description in bulletDescriptions:
                outcomeList.append(description.strip())
        else:
            outcomeList.append(fullDescription)
        specificOutcomeData.append({
            'name': 'Specific Outcome'+' '+outcomeNumber,
            'outcomes': outcomeList,
            'processes': processes
        })
    return specificOutcomeData;

def getOutcomesByIndex(subject, course, sections, index):
    outcomes = []
    generalOutcome = sections[index].find_next_sibling().parent
    outcomeTitleText = generalOutcome.find('div', class_='title').text # first title instance
    outcomeTitle = removeBrackets(outcomeTitleText)

    outcomeDescriptionText = generalOutcome.find('div', class_='subtitle').text # first subtitle instance
    colonIndex = outcomeDescriptionText.find(':')
    outcomeDescription = outcomeDescriptionText[colonIndex+1:].replace('.', '').strip()

    outcomeCode = ''.join(c for c in outcomeTitle if c.isupper())
    identifier = subject[:2].upper()+course+'.'+outcomeCode
    
    # append general outcome
    outcomes.append([identifier, ' - '.join([outcomeTitle, outcomeDescription]), []])
    
    for i, outcome in enumerate(getSpecificOutcomes(generalOutcome)):
        for j, o in enumerate(outcome['outcomes']):
            if len(outcome['outcomes']) > 1:
                outcomes.append([identifier + str(i+1) + chr(ord('A') + j), o, outcome['processes']])
            else:
                outcomes.append([identifier + str(i+1), o, outcome['processes']])
    return outcomes;

def groupByOutcomeGroup(subject, course, sections, outcomeGroups):
    vertices = []
    outcomeProcesses = {}
    maxTarget = 0
    for i, (sectionIndex, group) in enumerate(outcomeGroups):
        outcomes = getOutcomesByIndex(subject, course, sections, sectionIndex)
        for outcome in outcomes:
            for p in outcome[2]:
                try:
                    outcomeProcesses[p].append(outcome[0])
                except KeyError:
                    outcomeProcesses[p] = []
                    outcomeProcesses[p].append(outcome[0])

        for idx, outcome in enumerate(outcomes):
            if outcome[0].split('.')[1] != group:
                vertices.append({
                    'name': outcome[0],
                    'description': outcome[1],
                    'group': i,
                    'processes': outcome[2]
                })
    return vertices, outcomeProcesses