import requests
from bs4 import BeautifulSoup


dataStr = """method: search
searchMethod: true
searchTarget: ATM
orgName: jcvkxlhzv
orgId: reqtres
hid_1: 1
tenderName: vcxzv
tenderId: ytgfn
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/05/15
awardAnnounceEndDate: 110/05/15
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: vcxzvcxzvtr
hid_2: 1
gottenVendorName: tr
gottenVendorId: 765ytrhgf
hid_3: 1
submitVendorName: rewq
submitVendorId: ewrfsdvxc
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""
data = dict()
for row in dataStr.split('\n'):
    data[row.split(': ')[0]] = row.split(': ')[1]

data = {row.split(': ')[0]: row.split(': ')[1] for row in dataStr.split('\n')}

print(data)