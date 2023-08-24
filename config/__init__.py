import os
import dotenv
PLAYING_GAMES = [
    (3,  "英雄联盟"),
    (32,  "我的世界"),
    (1070120,  "我的世界：传奇"),
    (46655,  "我的世界：基岩版"),
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
    (14852, "奥日与黑暗森林"),
    (5900, "叛乱：沙漠风暴"),
    (38, "荒野大镖客2"),
    (167570, "植物大战僵尸"),
    (238951, "地铁 2033"),
    (428112, "红色警戒 2：尤里的复仇"),
    (1284197, "红色警戒3"),
    (9, "无主之地3"),
    (38417, "Apex 英雄"),
    (10896, "雨中冒险2"),
    (14852, "奥日与黑暗森林"),
    (8873, "文明 VI"),
    (190783, "Mirror 2"),
    (490903, "NEKOPARA Extra")
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


# Redis Config
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))
