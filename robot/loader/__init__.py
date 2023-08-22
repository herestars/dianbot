from khl import Bot, Message
import config
import redis as R

bot = Bot(token=config.KOOK_TOKEN)
redis = R.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
