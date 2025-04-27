import json


def getLineOf(lines, text):
    for i, line in enumerate(lines):
        if line.strip() == text:
            return i
    return -1

def addLines(lines, identifier, linesToAdd):
    lineIndex = getLineOf(identifier)
    
    for index, line in enumerate(linesToAdd):
        if (index == 0):
            lines[lineIndex] = linesToAdd[index]
        else:
            lines.insert(lineIndex + index, linesToAdd[index])

