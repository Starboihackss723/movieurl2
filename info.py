import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '15599295'))
API_HASH = environ.get('API_HASH', '4ce42998f7df4a64934294dadca28ae0')
BOT_TOKEN = environ.get('BOT_TOKEN', '5901655383:AAEhLlefUzFSeLw0BH9Ae9CDbOxaFWdZWuY')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/4bbe7d02c370327912a24.jpg https://telegra.ph/file/6eea2995ca264212c8375.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5463205082').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001863651025').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5463205082').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001863651025')
auth_grp = environ.get('AUTH_GROUP', '-1001666282080')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://movies:7234049299@cluster0.mc1he3h.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1001553184345'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Best_FriendsFor_Ever')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "📁 ➜ {file_name} @Star_MoviesHub\n🦋 𝗙𝗶𝗿𝘀𝘁 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 🦋\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐘𝐨𝐮𝐫 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐞𝐫𝐞 𝐀𝐧𝐝 𝐆𝐞𝐭 𝐈𝐧 1 𝐌𝐢𝐧𝐮𝐭𝐞 100℅ 👇\nhttps://t.me/Star_MoviesHub\nयहां अपनी फिल्मों का अनुरोध करें और 1 मिनट में प्राप्त करें 100℅ 👇\nhttps://t.me/Star_MoviesHub\n\n╔══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╗\nᴏғғɪᴄɪᴀʟ @star_x_network\nMᴏᴠɪᴇs @Star_X_Movies\nsᴜᴘᴘᴏʀᴛ @Best_FriendsFor_Ever\n╚══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╝\n✯ ━━━━━ ✧ ━━━━━ ✯")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "📁 ➜ {file_name} @Star_MoviesHub\n🦋 𝗙𝗶𝗿𝘀𝘁 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 🦋\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐘𝐨𝐮𝐫 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐞𝐫𝐞 𝐀𝐧𝐝 𝐆𝐞𝐭 𝐈𝐧 1 𝐌𝐢𝐧𝐮𝐭𝐞 100℅ 👇\nhttps://t.me/Star_MoviesHub\nयहां अपनी फिल्मों का अनुरोध करें और 1 मिनट में प्राप्त करें 100℅ 👇\nhttps://t.me/Star_MoviesHub\n\n╔══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╗\nᴏғғɪᴄɪᴀʟ @star_x_network\nMᴏᴠɪᴇs @Star_X_Movies\nsᴜᴘᴘᴏʀᴛ @Best_FriendsFor_Ever\n╚══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╝\n✯ ━━━━━ ✧ ━━━━━ ✯")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [𝚂𝚃𝙰𝚁 𝙱𝙾𝙸](https://t.me/Star_X_Movies)")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##

      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'shareus.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', 'FXugaKcy3GNNLmZty8F02G5FMv82')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 120))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/Star_X_Movies/5"

   # Custom Caption Under Button #
CAPTION_BUTTON = "UPDATES"
CAPTION_BUTTON_URL = "https://t.me/Star_X_Network"

   # Auto Delete For Bot Sending Files #
