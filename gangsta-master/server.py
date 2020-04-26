from bot import telegram_chatbot
import gizoogle
import re
import urllib
import urllib.request
bot = telegram_chatbot("config.cfg")

def Find(msg): 
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg) 
    return bool(url)
	
	
def make_reply(msg):
	reply = None
	a = Find(msg)
	print(a)
	
	if a == 1:
		reply = "is a link"
		return reply
	elif a == 0:
		reply = msg
		return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
