import os
import dotenv
PLAYING_GAMES = [
    (3,  "英雄联盟"),
    (9624,  "泰拉瑞亚"),
    (16301,  "原神"),
    (579379,  "星际争霸2"),
    (18,  "Dota 2"),
    (10976,  "雀魂麻将"),
    (193096,  "星露谷物语"),
    (11213,  "生化危机2：重制版"),
    (32876,  "生化危机5"),
    (81307,  "生化危机8：村庄"),
    (449860,  "生化危机：启示录"),
    (527718,  "生化危机"),
    (528143,  "生化危机6"),
    (898114,  "生化危机3：重制版"),
    (1027611,  "生化危机4：重制版"),
    (1042874,  "生化危机7"),
    (139331,  "极限国度"),
    (21, "地下城与勇士"),
]

dotenv.load_dotenv()
KOOK_TOKEN = os.getenv('KOOK_TOKEN')
STATE_UPDATE_POSSIBILITY = float(os.getenv('STATE_UPDATE_POSSIBILITY', 0.5))
WEB_HOST = os.getenv('WEB_HOST', '0.0.0.0')
WEB_PORT = int(os.getenv('WEB_PORT', 4396))
LOG_CHANNEL_ID = os.getenv('LOG_CHANNEL_ID', '5906997479983282')

# OpenAI API Config
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ENDPOINT = os.getenv('OPENAI_ENDPOINT')
OPENAI_DEPLOYMENT_NAME = os.getenv('OPENAI_DEPLOYMENT_NAME')