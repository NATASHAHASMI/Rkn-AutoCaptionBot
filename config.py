# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    # Rkn client config
    API_ID = os.environ.get("API_ID", "23171051")
    API_HASH = os.environ.get("API_HASH", "10331d5d712364f57ffdd23417f4513c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7161447840:AAHijbJ3wANZcgdElBe2kkxYOsOaeS7wFUs")

    #start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")


    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))
    FORCE_SUB = os.environ.get("FORCE_SUB", "-1001868502293") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "Lucifer")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://tmr624062:2fS3ifhHtKRaLWQZ@cluster0.3gpzrlg.mongodb.net/?retryWrites=true&w=majority")

    #caption
    DEF_CAP = os.environ.get("DEF_CAP",
                             "<b><a href='https://t.me/TMR_update_channel'>{file_name} Telegram : @TMR_DEVELOPER\n\nForward the file before Downloading.</a></b>",
    )

    #sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAKjYmZkRgOAtKRZ1d8LHnLAKUtus9noAAIjAAMoD2oUJ1El54wgpAY1BA")

    #admin id
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6987799874').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
