import requests
import json
import time
import random

def get_message(auth,chanel_id):

    headr = {
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = random.choice(chanel)
    discord_url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    print(discord_url)
    res = requests.get(url=discord_url, headers=headr)

    result = json.loads(res.content)
    res_list = []
    for context in result:
        if ('<') not in context['content'] :
            if ('@') not in context['content'] :
                if ('http') not in context['content']:
                    if ('?') not in context['content']:
                        res_list.append(context['content'])
    return random.choice(res_list)


def chat(chanel,authorization):
      header = {
          "Authorization": authorization,
          "Content-Type": "application/json",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
      }
      for chanel_id in chanel:
          msg = {
              "content": get_message(authorization,chanel_id),
              "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
              "tts": False,
          }
          discord_url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
          try:
              res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
              print(res.content)
          except:
              pass
          continue
      time.sleep(random.randrange(15, 35))


if __name__ == "__main__":
    chanel = [""]
    authorization = ""
    while True:
        try:
            chat(chanel,authorization)
            sleeptime = random.randrange(600, 1200) #发送间隔时间(秒)
            time.sleep(sleeptime)
        except:
            break
