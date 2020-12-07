import re

class LinkClass:
    def __init__(self, name, link, time):
        self.name = name
        self.link = link
        self.time = time

urls = []
names = []
times = []
with open('D:\\git\\Python\\Day 4\\links.txt', 'r') as txt_file:
    data = txt_file.read()
    urls = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', data)
    names = re.findall("(?<=from )(.*)(?=to)", data)
    times = re.findall("[0-1][0-2]:[0-5][0-9] AM|[0-1][0-2]:[0-5][0-9] PM", data)


list_links = []

for (x,y,z) in zip(names, urls, times):
    l = LinkClass(x,y,z)
    list_links.append(l)

for link in list_links:
    print(f'Sent By: {link.name} \n Link: {link.link} \n At: {link.time}')
