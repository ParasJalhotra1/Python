import re
with open('D:\\git\\Python\\Day 4\\links.txt') as myFile:
    for line in myFile.readlines():
        links = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', line)
        print(links)