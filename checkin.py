import requests,json,os

#填入glados账号对应cookie
COOKIES = os.environ["COOKIES"]
cookies=COOKIES.split('&&')



def start():    
    url= "https://glados.one/api/user/checkin"
    url2= "https://glados.one/api/user/status"
    referer = 'https://glados.one/console/checkin'
    origin = "https://glados.one"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    payload={
        'token': 'glados.network'
    }
    for cookie in cookies:
        checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
        print("finish")
def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
