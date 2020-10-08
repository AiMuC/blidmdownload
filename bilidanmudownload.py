import requests
import json
import xmltodict
BV = input("请输入BV号: ")
r = requests.get("https://api.bilibili.com/x/web-interface/view?bvid="+str(BV))
r.encoding = 'utf-8'
arr = json.loads(r.text)
avid=arr['data']['aid']
getcid="https://www.bilibili.com/widget/getPageList?aid="+str(avid)
r = requests.get(getcid)
r.encoding = 'utf-8'
arr = json.loads(r.text)
cid=arr[0]["cid"]
getdanmu="https://comment.bilibili.com/"+str(cid)+".xml"
r = requests.get(getdanmu)
r.encoding = 'utf-8'
o = xmltodict.parse(r.text)
danmu = json.dumps(o)
danmu = json.loads(danmu)
for index in range(len(danmu['i']['d'])):
    print(str(index)+":"+danmu['i']['d'][index]['#text'])
print("\r\n----------------------------\r\n")
print("本视频共"+str(len(danmu['i']['d']))+"条弹幕")
