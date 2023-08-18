import random
import config
from robot.loader import bot
from enum import Enum
from loguru import logger

logger.info("Loading tasks...")
class UpdateState(Enum):
    NO_UPDATE = "no update"
    PLAY_GAME = "play game"
    LISTEN_MUSIC = "listen music"
    SLEEP = "sleep"

CUR_STATE = None
@bot.task.add_interval(minutes=1)
async def update_status():
    if random.random() > config.STATE_UPDATE_POSSIBILITY:
        return
    state = random.choices(
        [
            UpdateState.NO_UPDATE,
            UpdateState.PLAY_GAME,
            UpdateState.SLEEP,
        ],
        weights=[5, 3, 2],
    )
    global CUR_STATE
    log_channel = await bot.client.fetch_public_channel(config.LOG_CHANNEL_ID)
    match state[0]:
        case UpdateState.PLAY_GAME:
            game = random.choice(config.PLAYING_GAMES)
            if CUR_STATE != game[0]:
                await bot.client.send(log_channel, f"开始玩: {game[1]}")
                logger.info(f"开始玩: {game[1]}")
                await bot.client.update_playing_game(game[0])
                CUR_STATE = game[0]
            return
        case UpdateState.SLEEP:
            if CUR_STATE != None:
                try:
                    await bot.client.stop_listening_music()
                except:
                    pass
                try:
                    await bot.client.stop_playing_game()
                except:
                    pass
                logger.info("休息一下")
                await bot.client.send(log_channel, "休息一下")
                CUR_STATE = None
            return