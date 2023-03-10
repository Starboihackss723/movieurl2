#### This Code Was Devloped By @AM_ROBOTS ####

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

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://paisakamalo.in/')
    START_TXT = environ.get("START_TXT", "š·š“š»š¾ {}")
    HELP_TXT = """š·š“š {}
š·š“šš“ šøš š¼š š·š“š»šæ š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """<b>āÆ š¼š š½š°š¼š“: {}</b>
<b>ā® š²šš“š°šš¾š: <a href=https://t.me/star_x_network>ššš°š š±š¾šø</a></b>
<b>ā® š»šøš±šš°šš: šæššš¾š¶šš°š¼</b>
<b>ā® š»š°š½š¶šš°š¶š“: šæššš·š¾š½ š¹</b>
<b>ā® š³š°šš° š±š°šš“: š¼š¾š½š¶š¾-š³š±</b>
<b>ā® š±š¾š šš“ššš“š: į“į“_į“į“į“Ź</b>
<b>ā® š±ššøš»š³ ššš°ššš: š1.0.43 [ š±š“šš° ]</b>
<b>ā® š¼š¾ššøš“š š²š·š°š½š½š“š»: <a href=https://t.me/star_x_movies>š¹š¾šøš½</a></b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Source - https://t.me/best_friendsfor_ever

<b>DEVS:</b>
- <a href=https://t.me/its_star_boi>ššš°š š±š¾šø</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and įÆāUāįÆį¶ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/star_x_network)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of įÆāUāįÆį¶

<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specified user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban  - <code>to ban a user.</code>
ā¢ /unban  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ā šš¾šš°š» šµšøš»š“š: <code>{}</code>
ā šš¾šš°š» ššš“šš: <code>{}</code>
ā šš¾šš°š» š²š·š°šš: <code>{}</code>
ā ššš“š³ ššš¾šš°š¶š“: <code>{}</code> š¼šš±
ā šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> š¼šš±"""
    LOG_TEXT_G = """#ššš°šš«šØš®š©
    
<b>įāŗ šš«šØš®š© āŖ¼ {}(<code>{}</code>)</b>
<b>įāŗ ššØš­šš„ ššš¦ššš«š¬ āŖ¼ <code>{}</code></b>
<b>įāŗ ššššš šš² āŖ¼ {}</b>
"""
    LOG_TEXT_P = """#ššš°šš¬šš«  
    
<b>įāŗ šš - <code>{}</code></b>
<b>įāŗ ššš¦š - {}</b>
"""
