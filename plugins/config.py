import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7842208500:AAGIE8C41yZ4fJeTd-VDa2SpTr6tiJ6NvLI")
    
    API_ID = int(os.environ.get("API_ID", "25888462"))
    
    API_HASH = os.environ.get("API_HASH", "50620d85a99c79e74972df60f0a11da1")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = ""
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Unique:n219219219@unique.p4hpd.mongodb.net/?retryWrites=true&w=majority&appName=Unique")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "NothingBots")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002206709779"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002446244647")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "7766469355"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "nothing_url_uploader_bot")
                                  
