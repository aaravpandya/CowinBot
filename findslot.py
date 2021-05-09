import requests
import json
import webbrowser

""" PARAMETERS """
district_id = "773"
date = "09-05-2021"
url_session = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+district_id+"&date="+date
url_getReCaptcha = "https://cdn-api.co-vin.in/api/v2/auth/getRecaptcha"
url_schedule = "https://cdn-api.co-vin.in/api/v2/appointment/schedule"
edgepath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
beneficiaries = ["ID_HERE"]
slot_index = 0
Token = "TOKEN_HERE"
path_to_html = "ABSOLUTE_PATH_TO_HTML" # Not sure if relative works 

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgepath))
edge = webbrowser.get("edge")
payload={}
headers = {
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
  'Accept': 'application/json, text/plain, */*',
  'Authorization': 'Bearer '+Token,
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'
}

def checkSessions():
    response = requests.request("GET", url_session, headers=headers, data=payload)
    print(response.status_code)
    response = json.loads(response.text)
    for center in response["centers"]:
        for session in center["sessions"]:
            if(session["available_capacity"]>0 and session["min_age_limit"]==18):
                return [True, center["center_id"], session["session_id"], session["slots"]]
    return [False,None,None,None]

def getRecaptcha():
    payload = json.dumps({})
    headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'Bearer '+Token,
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url_getReCaptcha, headers=headers, data=payload)
    print(response.text)
    svg = json.loads(response.text)["captcha"].replace("\\","")
    return svg

def schedule(center_id,captcha,session_id,slots):
    payload = json.dumps({
    "center_id": center_id,
    "session_id": session_id,
    "beneficiaries": beneficiaries,
    "slot": slots[slot_index],
    "captcha": captcha,
    "dose": 1
    })
    headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'Bearer '+Token,
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url_schedule, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    return response.status_code

while(True):
    Available,center_id, session_id, slots = checkSessions()
    if(Available):
        svg = getRecaptcha()
        with open("template.html",'r') as fp:
            html = fp.read()
        html = html.replace("Token", svg)
        with open(path_to_html,'w') as fp:
            fp.write(html)
        edge.open_new_tab(path_to_html)
        captcha = input()
        schedule(center_id,captcha,session_id,slots)
        break
