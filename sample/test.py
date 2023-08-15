import requests
import json
import dotenv



config = {
    **dotenv.dotenv_values(".env"),
    **dotenv.dotenv_values(".env.dev"),
}


base_url = "https://www.kookapp.cn/api"

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Authorization": "Bot " + config["token"],
}

data = {
    "id": 453027,
    "icon": "https://img.kookapp.cn/assets/2022-07/zW0oz6ZUma0a00a0.png/icon"
}
res = requests.post(
    base_url + "/v3/game/update", headers=headers, data=json.dumps(data)
)
print(res.text)
