import requests
import json
import dotenv
import os

dotenv.load_dotenv()

base_url = "https://www.kookapp.cn/api"

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Authorization": "Bot " + os.getenv("token"),
}

data = {
    "id": 453027
}
res = requests.post(
    base_url + "/v3/game/activity", headers=headers, data=json.dumps(data)
)
print(res.text)
