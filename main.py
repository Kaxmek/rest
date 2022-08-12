import time
import requests
import telebot
from time import sleep
token = "5550350888:AAEL2LRRBPtSVSchi6DEQZIn6-xBJ_eXm_g"
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
	msg=(f"𝑤𝑒𝑙𝑐𝑜𝑚𝑒 D𝑒𝑎𝑟 Tℎ𝑖𝑠 𝑏𝑜𝑡 𝑖𝑠 𝑖𝑛𝑡𝑒𝑛𝑑𝑒𝑑 𝑡𝑜 𝑐𝑟𝑒𝑎𝑡𝑒 𝑎 𝑝𝑎𝑠𝑠𝑤𝑜𝑟𝑑 f𝑜𝑟 I𝑛𝑠𝑡𝑎𝑔𝑟𝑎𝑚, 𝑝𝑙𝑒𝑎𝑠𝑒 𝑑𝑜 𝑛𝑜𝑡 𝑟𝑒𝑝𝑒𝑎𝑡 𝑜𝑟 𝑜𝑣𝑒𝑟𝑢𝑠𝑒\n\n\r                       ارسل اليوزر الان.\n\nBY : @MVMVP")
	bot.send_message(message.chat.id, msg)
	sleep(1)
	
	
	@bot.message_handler(func=lambda followinG:True )
	
	def com(message):
		iip=(message.text)
		url22 = f'https://www.instagram.com/{iip}/?__a=1&__d=dis'
		head1 = {
			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			                'accept-encoding': 'gzip, deflate, br',
			                'accept-language': 'en-US,en;q=0.9',
			                'cookie': 'sessionid=45480830288%3AjJWzjhVCd2XlfI%3A22%3AAYfC05qKCv-7xV0wIlNMG_6FCtAxzF-CSnQvqo2z0Q;ds_user_id=45480830288;csrftoken=fxIwfahUyKwEVBlZ9V3qwmGsInqtWQ59',
			                'referer': 'https://www.instagram.com/{}/'.format(iip),
			                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			                'sec-ch-ua-mobile': '?1',
			                'sec-fetch-dest': 'document',
			                'sec-fetch-mode': 'navigate',
			                'sec-fetch-site': 'snone',
			                'upgrade-insecure-requests': '1',
			                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
		}
		rr =requests.get(url22,headers=head1).json()
		try:
			
			iddd = str(rr['graphql']['user']['id'])
		except KeyError as error:
			bot.send_message(message.chat.id, f"😢 - Username Error\n🇮🇶 - @MVMVP - @W_Y67")
			
		headers = {
        # 'Content-Length': '305',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
        # Requests sorts cookies= alphabetically

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
		}
		data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
		}
		res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
		rs =str(res['obfuscated_email'])
		bot.send_message(message.chat.id, f"Rest User True\nUser : {iip}\nEmail : {rs}\nID : {iddd}\nBy : @MVMVP - @W_Y67")
			
		
				
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       sleep(10)
