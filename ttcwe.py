# Source By FaLahAlanezi + WeeX + M3GON + J_Qatar And Edited By @t7ttt7

# Here You Put Your Bot Token In Telegram *Optinal*, If You Dont Want To "LEAVE IT"

token = "Token"

# And Here Put Your Telegram-ID *Optinal*, And like what i said If You Dont Want To "LEAVE IT"

tid = "Telegram-ID"

try:
	 import os,sys,time,base64,codecs,itertools,requests,json,random,user_agent,colorama,re,threading,uuid
	 from user_agent import *
	 from colorama import *
except Exception as F:
	print("[ModuleERROR]%s"%(F),"\n\nWait To Download The Modules It takes 1 or 2 minutes\nBe patient please\nDownloading...\n")
	os.system("pip install colorama")
	os.system("pip install json")
	os.system("pip install requests")
	os.system("pip install itertools")
	os.system("pip install user_agent")
	os.system("pip install re")
	os.system("pip install random")
	os.system("pip install os")
	os.system("pip install sys")
	os.system("pip install time")
	os.system("pip install threading")
	os.system("pip install base64")
	os.system("pip install codecs")
	os.system("pip install uuid")
	pass

os.system("clear")

b = '\033[30m'
re = '\033[31m'
g = '\033[32m'
ye = '\033[33m'
bl = '\033[34m'
ma = '\033[35m'
cy = '\033[36m'
wh = '\033[37m'
res = '\033[39m'

headerswol = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
"Connection": "close",
"Host": "www.tiktok.com",
"Accept-Encoding": "gzip, deflate",
"Cache-Control": "max-age=0"
}

# The Message Content, Chage It If You Want To

fa = """𖡦-------------------------------𖡦
𖡦    𝐓𝐢𝐤𝐓𝐨𝐤𝐂𝐡𝐞𝐜𝐤𝐞𝐫   𖡦
𖡦-------------------------------𖡦"""

ra = """
𖡦-›New User Hunted UP ✅
𖡦-------------------------------𖡦"""

k ="""𖡦-›User : """

an = """𖡦-------------------------------𖡦
𖡦-› @t7ttt7
𖡦-------------------------------𖡦"""

rad = """ ✓"""

FAQ = """𝙲𝚕𝚒𝚌𝚔 𝚃𝚑𝚎 𝚄𝚜𝚎𝚛 𝚃𝚘 𝙲𝚘𝚙𝚢!"""

boora = False

def animate1():
	        for c in itertools.cycle(['|', '/', '-', '\\']):
	        	if boora:
	        		break
	        	sys.stdout.write(b
	        	+ Style.BRIGHT + '\rLogging in '+c)
	        	time.sleep(0.1)
kir = threading.Thread(target=animate1)

def sessionIDcheck():
	from random import sample
	import string
	while True:
		for i in range(1):
			fls = (''.join(sample(string.ascii_lowercase, 8)))
			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		payload = ""
		headers = {
	"Accept": "text/html,application/xhtml+xml,applicationxml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"User-Agent": generate_user_agent(),
	"Connection": "close",
	"Host": "www.tiktok.com",
	"Accept-Encoding": "gzip, deflate",
	"Cache-Control": "max-age=0"
		}
		cookies = {'sessionid': sessionId}
		response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		post = str (response.json()["status_msg"])
		if post==""or"":
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+g+'✓'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Congrats Your SessionID Is Not Blocked')
			exit()
		else:
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+" Invalid SessionID")
			exit()
	

def vpncheck():
	from random import sample
	import string
	for i in range(1):
		fls = (''.join(sample(string.ascii_lowercase, 26)))
		weblog = f'https://www.tiktok.com/@{fls}'
		rq = requests.get(weblog, headers=headerswol)
		if rq.status_code == 404:
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+g+'✓'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Congrats Your IP Not Blocked')
		elif rq.status_code == 200:
			print(Style.BRIGHT+"""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+''' Your IP Blocked''')

def ttrpn():
	done = 0
	error = 0
	import re as rep
	rpurl = f'https://www.tiktok.com/@{trgt}?is_copy_url=1&is_from_webapp=v1'
	HeadersUserId = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'tt_webid_v2=6931890936634443265; tt_webid=6931890936634443265; s_v_web_id=verify_0cddbd837c6e0df451b5cf3cf6ff5182; tt_csrf_token=4uNJGBn_ZzXhHYhSj3HbIQN0; bm_sz=6EF8376E5CFB32C01ECE75A0FA3C368D~YAAQl14zVviROxx3AQAAV4r4ywq5vtEk3rtDacDlheJxT03p4N1pg85sGK77KNKXfMOdbbluR4LkSMxoO/Gid5RizfsKYTW95j1ohsm+hvv4WiTWuI3Y/AmkvbX4IwbAXIRt96ajgIBthfsVZbZO8Dv7ovFmusOiw/8V6/x+U9P8elBMk2E9kbSQ5lekNFfG; csrf_session_id=2ee5d5b530b24bb28efbd674f0c8c88d; ak_bmsc=708DF909DAA3A8B972B9DE1C6303581156335E973B4200006F373460CEEDD27D~plZGd4T0oSlOh6wPNBFPeKMGOE6ZjQIGvTs9w2/7bfAh5hTH99sQPFqP9B9Dq9PG6RHTcnpl4mk03X9laadSVAhVFnNgEnz3NJvipdEPm8Mzfx3D5udHaQDInSt03uKImS72kIcvJB3Z0qsXMvfRKK0LKBD+XJ09MJhErybjt+OjDsz8zSm3/uiDJouHEjSfr/XWzH7jO6WawOfHpaIVGiA9UQnLrKA0Mhd2plCEdAraUeBLqAgAprdaI6MNyuykLK; ttwid=1%7CWf1epqHAd8sW5357XF9Dyy5P1xfJTD0lq_ycAc6mBwg%7C1614034971%7C942ab2f27a5f118fbc2e0793c7b9651a0617459cf422c9e3a1e4811fdea20217; passport_csrf_token=858080cf8140c4c62acba7ba040b8b83; passport_csrf_token_default=858080cf8140c4c62acba7ba040b8b83; _abck=B32AAB6B88AFAD7EDD5F8F43238D6289~0~YAAQjV4zVm9uYrl3AQAAZ6L8ywURQO1JkWzgk84A4ZwfDMQ8UVfOS3/KItiQLgE0yzyHhYexPZZ5w8hShvI35Zho1pF+Fo7uG6ueoSFw2gvlZB/g+zBikJciGupLJ720MaL8wb1/9ztrekyo5ObZG3kB1B0Vh+V70DGbWn9p3RzyFs5XlmTKuHlML/qwo4azpscxLg6aoMxxbO8tFMF4CBPIAoqikm3F9gtHCXPKcJ6hb4aesROJICXwac8oxfYKjQ2uzb/2gSYC+d3/sOdiZQCx1UTtNC33TQSP1bD/S+uSRPTsBj4YDXt22BlMluAJbbNmrI9Xc4v9hvhYdlitBOKDuI8jrw==~-1~-1~-1; MONITOR_WEB_ID=6931890936634443265; bm_sv=431EBC22FBA0B9E6654828B1BF07D9C4~d+AgKbhhH6iHfBJPadKHtTbJbUCnr5tqw/IF6gVcieTr3Dmk/iuM4cVGK8XlKH9NX/CKW0DtQGXrLi9zACZXHwBVKmdQ1iJ8sncYZdiXsrq9ZlK8Re3drCZiA+spFOHLAOFhaln9UU1z9Wa0C+Se2HasaD67JQmegmFvO7ZU7fc=',
	'Host': 'www.tiktok.com',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
	}
	ReqForUserId = requests.get(rpurl,headers=HeadersUserId).text
	kr = rep.findall('"seoProps":{"pageId":"(.*?)"', ReqForUserId)
	rk = "".join(kr)
	
	url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=&root_referer=https:%2F%2Fwww.tiktok.com%2F%40{trgt}%3Fis_copy_url%3D1%26is_from_webapp%3Dv1&user_agent=Mozilla%2F5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=en-US&browser_platform=Linux+x86_64&browser_name=Mozilla&browser_version=5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=America%2FNew_York&page_referer=https:%2F%2Fwww.tiktok.com%2F%40ksgf%3Fis_copy_url%3D1%26is_from_webapp%3Dv1&priority_region=SA&verifyFp=verify_0cddbd837c6e0df451b5cf3cf6ff5182&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=linux&did=6931890936634443265&tt-web-region=SA&uid=6930581757486040066'
	
	headers = {
	'Connection': 'close',
	'Content-Length': '102',
	'Accept': 'application/json, text/plain, */*',
	'x-secsdk-csrf-token': '0001000000012a8f40f370c5ae099b1a65c576cb480f5d1706c0dfdd8c7991aa1929ad3cbadc166634f9de3b1a91',
	'tt-csrf-token': '4uNJGBn_ZzXhHYhSj3HbIQN0',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
	'Content-Type': 'application/json',
	'Origin': 'https://www.tiktok.com',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': f'https://www.tiktok.com/@{trgt}?is_copy_url=1&is_from_webapp=v1',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cookie': f'tt_webid_v2=6931890936634443265; tt_webid=6931890936634443265; s_v_web_id=verify_0cddbd837c6e0df451b5cf3cf6ff5182; tt_csrf_token=4uNJGBn_ZzXhHYhSj3HbIQN0; bm_sz=6EF8376E5CFB32C01ECE75A0FA3C368D~YAAQl14zVviROxx3AQAAV4r4ywq5vtEk3rtDacDlheJxT03p4N1pg85sGK77KNKXfMOdbbluR4LkSMxoO/Gid5RizfsKYTW95j1ohsm+hvv4WiTWuI3Y/AmkvbX4IwbAXIRt96ajgIBthfsVZbZO8Dv7ovFmusOiw/8V6/x+U9P8elBMk2E9kbSQ5lekNFfG; csrf_session_id=2ee5d5b530b24bb28efbd674f0c8c88d; ak_bmsc=708DF909DAA3A8B972B9DE1C6303581156335E973B4200006F373460CEEDD27D~plZGd4T0oSlOh6wPNBFPeKMGOE6ZjQIGvTs9w2/7bfAh5hTH99sQPFqP9B9Dq9PG6RHTcnpl4mk03X9laadSVAhVFnNgEnz3NJvipdEPm8Mzfx3D5udHaQDInSt03uKImS72kIcvJB3Z0qsXMvfRKK0LKBD+XJ09MJhErybjt+OjDsz8zSm3/uiDJouHEjSfr/XWzH7jO6WawOfHpaIVGiA9UQnLrKA0Mhd2plCEdAraUeBLqAgAprdaI6MNyuykLK; ttwid=1%7CWf1epqHAd8sW5357XF9Dyy5P1xfJTD0lq_ycAc6mBwg%7C1614034971%7C942ab2f27a5f118fbc2e0793c7b9651a0617459cf422c9e3a1e4811fdea20217; passport_csrf_token=858080cf8140c4c62acba7ba040b8b83; passport_csrf_token_default=858080cf8140c4c62acba7ba040b8b83; odin_tt=13ca4edd431b0cf63c4cf86df8117cc220963d5fe1adedc5b500e7bdedf3281b8880fe15f8487e809a4d2fbb459d4414b01735214e3ff40088000c4c3e772c38; cmpl_token=AgQQAPO_F-RO0rAQscT18N07-lKfJyxHv4M0YPnghw; sid_guard=0b7a2b62465ddd997a9408dfcef155bd%7C1614035758%7C5184000%7CFri%2C+23-Apr-2021+23%3A15%3A58+GMT; uid_tt=d4a0bb253cee8e0f0f887060869e55d04e225dca4da90fb5ce3380b50913c4cb; uid_tt_ss=d4a0bb253cee8e0f0f887060869e55d04e225dca4da90fb5ce3380b50913c4cb; sid_tt={sessionId}; sessionid={sessionId}; sessionid_ss={sessionId}; store-idc=alisg; store-country-code=sa; MONITOR_WEB_ID=6931890936634443265; _abck=B32AAB6B88AFAD7EDD5F8F43238D6289~0~YAAQdl4zVqcjlxp3AQAAYlAHzAUjprjMKVgW9hYArMReESRNrOWghue/S82JLQDy6Yt4SMqEzaK/+OkeEB6LBi/FpP9iPwkr2dk1dl64fJ0Qjye/oyJmvT1Drx8gLEd4bJWKtJbyIpfqt16nj1uHjVrX/gDeHJhUF1FBJQBwr7HXF/lOcOsIhCcUV27jYgFRHxW875U26ln50PfEXXNmJLaSFwo1GtVBjmXYAn6jbCmXVLcxaU1PfTvO1d8KghoBLmDA85BeHCmaA3wNqKB+ieHpldwgE6hqbJzmFjTu2vvTtFdKQ4OYsUhxYfphxfJVLfC2Bp17sC/A5QRQuOFivRs4rgMiPg==~-1~||-1||~-1; bm_sv=431EBC22FBA0B9E6654828B1BF07D9C4~d+AgKbhhH6iHfBJPadKHtTbJbUCnr5tqw/IF6gVcieTr3Dmk/iuM4cVGK8XlKH9NX/CKW0DtQGXrLi9zACZXHwBVKmdQ1iJ8sncYZdiXsrqG9F5wNfjI+qwlzFKlwN77Zz6bOsK6uMIY8knC4Fc4HQ7JrCffU/7v2IZlbIh59yM='
	}
	data ={
	'object_id': rk,
	'owner_id': rk,
	'reason': '306',
	'report_type': "user"
	}
	count = 0
	while True:
		time.sleep(slep)
		rq = requests.post(url, json=data, headers=headers).text
		if '"errMsg":"Thanks for your feedback"' in rq:
			count += 1
			print(f"{Style.BRIGHT}{wh}│\n├─╼{b}[{wh}{count}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{g} Done ✓{res}")
		elif '{"statusCode":1,"errMsg":"parmas Missing"}' in rq:
			raise Exception;(f"{Style.BRIGHT}{wh}{b}[{wh}{re}!{b}]{wh} {re}Failed ✘{re} ❯{wh}❯{b}❯{wh} Invalid inputs{res}")
		else:
			count += 1
			print(f"{Style.BRIGHT}{wh}│\n├─╼{b}[{wh}{count}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{re} Failed ✘{res}")

def ttrpn():
	done = 0
	error = 0
	import re as rep
	rpurl = f'https://www.tiktok.com/@{trgt}?is_copy_url=1&is_from_webapp=v1'
	HeadersUserId = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'tt_webid_v2=6931890936634443265; tt_webid=6931890936634443265; s_v_web_id=verify_0cddbd837c6e0df451b5cf3cf6ff5182; tt_csrf_token=4uNJGBn_ZzXhHYhSj3HbIQN0; bm_sz=6EF8376E5CFB32C01ECE75A0FA3C368D~YAAQl14zVviROxx3AQAAV4r4ywq5vtEk3rtDacDlheJxT03p4N1pg85sGK77KNKXfMOdbbluR4LkSMxoO/Gid5RizfsKYTW95j1ohsm+hvv4WiTWuI3Y/AmkvbX4IwbAXIRt96ajgIBthfsVZbZO8Dv7ovFmusOiw/8V6/x+U9P8elBMk2E9kbSQ5lekNFfG; csrf_session_id=2ee5d5b530b24bb28efbd674f0c8c88d; ak_bmsc=708DF909DAA3A8B972B9DE1C6303581156335E973B4200006F373460CEEDD27D~plZGd4T0oSlOh6wPNBFPeKMGOE6ZjQIGvTs9w2/7bfAh5hTH99sQPFqP9B9Dq9PG6RHTcnpl4mk03X9laadSVAhVFnNgEnz3NJvipdEPm8Mzfx3D5udHaQDInSt03uKImS72kIcvJB3Z0qsXMvfRKK0LKBD+XJ09MJhErybjt+OjDsz8zSm3/uiDJouHEjSfr/XWzH7jO6WawOfHpaIVGiA9UQnLrKA0Mhd2plCEdAraUeBLqAgAprdaI6MNyuykLK; ttwid=1%7CWf1epqHAd8sW5357XF9Dyy5P1xfJTD0lq_ycAc6mBwg%7C1614034971%7C942ab2f27a5f118fbc2e0793c7b9651a0617459cf422c9e3a1e4811fdea20217; passport_csrf_token=858080cf8140c4c62acba7ba040b8b83; passport_csrf_token_default=858080cf8140c4c62acba7ba040b8b83; _abck=B32AAB6B88AFAD7EDD5F8F43238D6289~0~YAAQjV4zVm9uYrl3AQAAZ6L8ywURQO1JkWzgk84A4ZwfDMQ8UVfOS3/KItiQLgE0yzyHhYexPZZ5w8hShvI35Zho1pF+Fo7uG6ueoSFw2gvlZB/g+zBikJciGupLJ720MaL8wb1/9ztrekyo5ObZG3kB1B0Vh+V70DGbWn9p3RzyFs5XlmTKuHlML/qwo4azpscxLg6aoMxxbO8tFMF4CBPIAoqikm3F9gtHCXPKcJ6hb4aesROJICXwac8oxfYKjQ2uzb/2gSYC+d3/sOdiZQCx1UTtNC33TQSP1bD/S+uSRPTsBj4YDXt22BlMluAJbbNmrI9Xc4v9hvhYdlitBOKDuI8jrw==~-1~-1~-1; MONITOR_WEB_ID=6931890936634443265; bm_sv=431EBC22FBA0B9E6654828B1BF07D9C4~d+AgKbhhH6iHfBJPadKHtTbJbUCnr5tqw/IF6gVcieTr3Dmk/iuM4cVGK8XlKH9NX/CKW0DtQGXrLi9zACZXHwBVKmdQ1iJ8sncYZdiXsrq9ZlK8Re3drCZiA+spFOHLAOFhaln9UU1z9Wa0C+Se2HasaD67JQmegmFvO7ZU7fc=',
	'Host': 'www.tiktok.com',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
	}
	ReqForUserId = requests.get(rpurl,headers=HeadersUserId).text
	kr = rep.findall('"seoProps":{"pageId":"(.*?)"', ReqForUserId)
	rk = "".join(kr)
	
	url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=&root_referer=https:%2F%2Fwww.tiktok.com%2F%40{trgt}%3Fis_copy_url%3D1%26is_from_webapp%3Dv1&user_agent=Mozilla%2F5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=en-US&browser_platform=Linux+x86_64&browser_name=Mozilla&browser_version=5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=America%2FNew_York&page_referer=https:%2F%2Fwww.tiktok.com%2F%40ksgf%3Fis_copy_url%3D1%26is_from_webapp%3Dv1&priority_region=SA&verifyFp=verify_0cddbd837c6e0df451b5cf3cf6ff5182&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=linux&did=6931890936634443265&tt-web-region=SA&uid=6930581757486040066'
	
	headers = {
	'Connection': 'close',
	'Content-Length': '102',
	'Accept': 'application/json, text/plain, */*',
	'x-secsdk-csrf-token': '0001000000012a8f40f370c5ae099b1a65c576cb480f5d1706c0dfdd8c7991aa1929ad3cbadc166634f9de3b1a91',
	'tt-csrf-token': '4uNJGBn_ZzXhHYhSj3HbIQN0',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
	'Content-Type': 'application/json',
	'Origin': 'https://www.tiktok.com',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': f'https://www.tiktok.com/@{trgt}?is_copy_url=1&is_from_webapp=v1',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cookie': f'tt_webid_v2=6931890936634443265; tt_webid=6931890936634443265; s_v_web_id=verify_0cddbd837c6e0df451b5cf3cf6ff5182; tt_csrf_token=4uNJGBn_ZzXhHYhSj3HbIQN0; bm_sz=6EF8376E5CFB32C01ECE75A0FA3C368D~YAAQl14zVviROxx3AQAAV4r4ywq5vtEk3rtDacDlheJxT03p4N1pg85sGK77KNKXfMOdbbluR4LkSMxoO/Gid5RizfsKYTW95j1ohsm+hvv4WiTWuI3Y/AmkvbX4IwbAXIRt96ajgIBthfsVZbZO8Dv7ovFmusOiw/8V6/x+U9P8elBMk2E9kbSQ5lekNFfG; csrf_session_id=2ee5d5b530b24bb28efbd674f0c8c88d; ak_bmsc=708DF909DAA3A8B972B9DE1C6303581156335E973B4200006F373460CEEDD27D~plZGd4T0oSlOh6wPNBFPeKMGOE6ZjQIGvTs9w2/7bfAh5hTH99sQPFqP9B9Dq9PG6RHTcnpl4mk03X9laadSVAhVFnNgEnz3NJvipdEPm8Mzfx3D5udHaQDInSt03uKImS72kIcvJB3Z0qsXMvfRKK0LKBD+XJ09MJhErybjt+OjDsz8zSm3/uiDJouHEjSfr/XWzH7jO6WawOfHpaIVGiA9UQnLrKA0Mhd2plCEdAraUeBLqAgAprdaI6MNyuykLK; ttwid=1%7CWf1epqHAd8sW5357XF9Dyy5P1xfJTD0lq_ycAc6mBwg%7C1614034971%7C942ab2f27a5f118fbc2e0793c7b9651a0617459cf422c9e3a1e4811fdea20217; passport_csrf_token=858080cf8140c4c62acba7ba040b8b83; passport_csrf_token_default=858080cf8140c4c62acba7ba040b8b83; odin_tt=13ca4edd431b0cf63c4cf86df8117cc220963d5fe1adedc5b500e7bdedf3281b8880fe15f8487e809a4d2fbb459d4414b01735214e3ff40088000c4c3e772c38; cmpl_token=AgQQAPO_F-RO0rAQscT18N07-lKfJyxHv4M0YPnghw; sid_guard=0b7a2b62465ddd997a9408dfcef155bd%7C1614035758%7C5184000%7CFri%2C+23-Apr-2021+23%3A15%3A58+GMT; uid_tt=d4a0bb253cee8e0f0f887060869e55d04e225dca4da90fb5ce3380b50913c4cb; uid_tt_ss=d4a0bb253cee8e0f0f887060869e55d04e225dca4da90fb5ce3380b50913c4cb; sid_tt={sessionId}; sessionid={sessionId}; sessionid_ss={sessionId}; store-idc=alisg; store-country-code=sa; MONITOR_WEB_ID=6931890936634443265; _abck=B32AAB6B88AFAD7EDD5F8F43238D6289~0~YAAQdl4zVqcjlxp3AQAAYlAHzAUjprjMKVgW9hYArMReESRNrOWghue/S82JLQDy6Yt4SMqEzaK/+OkeEB6LBi/FpP9iPwkr2dk1dl64fJ0Qjye/oyJmvT1Drx8gLEd4bJWKtJbyIpfqt16nj1uHjVrX/gDeHJhUF1FBJQBwr7HXF/lOcOsIhCcUV27jYgFRHxW875U26ln50PfEXXNmJLaSFwo1GtVBjmXYAn6jbCmXVLcxaU1PfTvO1d8KghoBLmDA85BeHCmaA3wNqKB+ieHpldwgE6hqbJzmFjTu2vvTtFdKQ4OYsUhxYfphxfJVLfC2Bp17sC/A5QRQuOFivRs4rgMiPg==~-1~||-1||~-1; bm_sv=431EBC22FBA0B9E6654828B1BF07D9C4~d+AgKbhhH6iHfBJPadKHtTbJbUCnr5tqw/IF6gVcieTr3Dmk/iuM4cVGK8XlKH9NX/CKW0DtQGXrLi9zACZXHwBVKmdQ1iJ8sncYZdiXsrqG9F5wNfjI+qwlzFKlwN77Zz6bOsK6uMIY8knC4Fc4HQ7JrCffU/7v2IZlbIh59yM='
	}
	data ={
	'object_id': rk,
	'owner_id': rk,
	'reason': '310',
	'report_type': "user"
	}
	count = 0
	while True:
		time.sleep(slep)
		rq = requests.post(url, json=data, headers=headers).text
		if '"errMsg":"Thanks for your feedback"' in rq:
			count += 1
			print(f"{Style.BRIGHT}{wh}│\n├─╼{b}[{wh}{count}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{g} Done ✓{res}")
		elif '{"statusCode":1,"errMsg":"parmas Missing"}' in rq:
			raise Exception;(f"{Style.BRIGHT}{wh}{b}[{wh}{re}!{b}]{wh} {re}Failed ✘{re} ❯{wh}❯{b}❯{wh} Invalid inputs{res}")
		else:
			count += 1
			print(f"{Style.BRIGHT}{wh}│\n├─╼{b}[{wh}{count}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{re} Failed ✘{res}")

def ttrpn():
	done = 0
	error = 0
	import re as rep
	rpurl = f'https://www.tiktok.com/@{trgt}?is_copy_url=1&is_from_webapp=v1'
	HeadersUserId = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Cookie': 'tt_webid_v2=6931890936634443265; tt_webid=6931890936634443265; s_v_web_id=verify_0cddbd837c6e0df451b5cf3cf6ff5182; tt_csrf_token=4uNJGBn_ZzXhHYhSj3HbIQN0; bm_sz=6EF8376E5CFB32C01ECE75A0FA3C368D~YAAQl14zVviROxx3AQAAV4r4ywq5vtEk3rtDacDlheJxT03p4N1pg85sGK77KNKXfMOdbbluR4LkSMxoO/Gid5RizfsKYTW95j1ohsm+hvv4WiTWuI3Y/AmkvbX4IwbAXIRt96ajgIBthfsVZbZO8Dv7ovFmusOiw/8V6/x+U9P8elBMk2E9kbSQ5lekNFfG; csrf_session_id=2ee5d5b530b24bb28efbd674f0c8c88d; ak_bmsc=708DF909DAA3A8B972B9DE1C6303581156335E973B4200006F373460CEEDD27D~plZGd4T0oSlOh6wPNBFPeKMGOE6ZjQIGvTs9w2/7bfAh5hTH99sQPFqP9B9Dq9PG6RHTcnpl4mk03X9laadSVAhVFnNgEnz3NJvipdEPm8Mzfx3D5udHaQDInSt03uKImS72kIcvJB3Z0qsXMvfRKK0LKBD+XJ09MJhErybjt+OjDsz8zSm3/uiDJouHEjSfr/XWzH7jO6WawOfHpaIVGiA9UQnLrKA0Mhd2plCEdAraUeBLqAgAprdaI6MNyuykLK; ttwid=1%7CWf1epqHAd8sW5357XF9Dyy5P1xfJTD0lq_ycAc6mBwg%7C1614034971%7C942ab2f27a5f118fbc2e0793c7b9651a0617459cf422c9e3a1e4811fdea20217; passport_csrf_token=858080cf8140c4c62acba7ba040b8b83; passport_csrf_token_default=858080cf8140c4c62acba7ba040b8b83; _abck=B32AAB6B88AFAD7EDD5F8F43238D6289~0~YAAQjV4zVm9uYrl3AQAAZ6L8ywURQO1JkWzgk84A4ZwfDMQ8UVfOS3/KItiQLgE0yzyHhYexPZZ5w8hShvI35Zho1pF+Fo7uG6ueoSFw2gvlZB/g+zBikJciGupLJ720MaL8wb1/9ztrekyo5ObZG3kB1B0Vh+V70DGbWn9p3RzyFs5XlmTKuHlML/qwo4azpscxLg6aoMxxbO8tFMF4CBPIAoqikm3F9gtHCXPKcJ6hb4aesROJICXwac8oxfYKjQ2uzb/2gSYC+d3/sOdiZQCx1UTtNC33TQSP1bD/S+uSRPTsBj4YDXt22BlMluAJbbNmrI9Xc4v9hvhYdlitBOKDuI8jrw==~-1~-1~-1; MONITOR_WEB_ID=6931890936634443265; bm_sv=431EBC22FBA0B9E6654828B1BF07D9C4~d+AgKbhhH6iHfBJPadKHtTbJbUCnr5tqw/IF6gVcieTr3Dmk/iuM4cVGK8XlKH9NX/CKW0DtQGXrLi9zACZXHwBVKmdQ1iJ8sncYZdiXsrq9ZlK8Re3drCZiA+spFOHLAOFhaln9UU1z9Wa0C+Se2HasaD67JQmegmFvO7ZU7fc=',
	'Host': 'www.tiktok.com',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
	}
	ReqForUserId = requests.get(rpurl,headers=HeadersUserId).text
	kr = rep.findall('"seoProps":{"pageId":"(.*?)"', ReqForUserId)
	rk = "".join(kr)
	
	url = f'https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=&root_referer=https:%2F%2Fwww.tiktok.com%2F%40{trgt}%3Fis_copy_url%3D1%26is_from_webapp%3Dv1&user_agent=Mozilla%2F5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=en-US&browser_platform=Linux+x86_64&browser_name=Mozilla&browser_version=5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F88.0.4324.150+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=America%2FNew_York&page_referer=https:%2F%2Fwww.tiktok.com%2F%40ksgf%3Fis_copy_url%3D1%26is_from_webapp%3Dv1&priority_region=SA&verifyFp=verify_0cddbd837c6e0df451b5cf3cf6ff5182&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=linux&did=6931890936634443265&tt-web-region=SA&uid=6930581757486040066'
	
	headers = {
	'Connection': 'close',
	'Content-Length': '102',
	'Accept': 'application/json, text/plain, */*',
	'x-secsdk-csrf-token': '0001000000012a8f40f370c5ae099b1a65c576cb480f5d1706c0dfdd8c7991aa1929ad3cbadc166634f9de3b1a91',
	'tt-csrf-token': '4uNJGBn_ZzXhHYhSj3HbIQN0',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
	'Content-Type': 'application/json',
	'Origin': 'https://www.tiktok.com',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': f'https://www.tiktok.com/@{trgt}?is_copy_url=1&is_from_webapp=v1',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cookie': f'tt_webid_v2=6931890936634443265; tt_webid=6931890936634443265; s_v_web_id=verify_0cddbd837c6e0df451b5cf3cf6ff5182; tt_csrf_token=4uNJGBn_ZzXhHYhSj3HbIQN0; bm_sz=6EF8376E5CFB32C01ECE75A0FA3C368D~YAAQl14zVviROxx3AQAAV4r4ywq5vtEk3rtDacDlheJxT03p4N1pg85sGK77KNKXfMOdbbluR4LkSMxoO/Gid5RizfsKYTW95j1ohsm+hvv4WiTWuI3Y/AmkvbX4IwbAXIRt96ajgIBthfsVZbZO8Dv7ovFmusOiw/8V6/x+U9P8elBMk2E9kbSQ5lekNFfG; csrf_session_id=2ee5d5b530b24bb28efbd674f0c8c88d; ak_bmsc=708DF909DAA3A8B972B9DE1C6303581156335E973B4200006F373460CEEDD27D~plZGd4T0oSlOh6wPNBFPeKMGOE6ZjQIGvTs9w2/7bfAh5hTH99sQPFqP9B9Dq9PG6RHTcnpl4mk03X9laadSVAhVFnNgEnz3NJvipdEPm8Mzfx3D5udHaQDInSt03uKImS72kIcvJB3Z0qsXMvfRKK0LKBD+XJ09MJhErybjt+OjDsz8zSm3/uiDJouHEjSfr/XWzH7jO6WawOfHpaIVGiA9UQnLrKA0Mhd2plCEdAraUeBLqAgAprdaI6MNyuykLK; ttwid=1%7CWf1epqHAd8sW5357XF9Dyy5P1xfJTD0lq_ycAc6mBwg%7C1614034971%7C942ab2f27a5f118fbc2e0793c7b9651a0617459cf422c9e3a1e4811fdea20217; passport_csrf_token=858080cf8140c4c62acba7ba040b8b83; passport_csrf_token_default=858080cf8140c4c62acba7ba040b8b83; odin_tt=13ca4edd431b0cf63c4cf86df8117cc220963d5fe1adedc5b500e7bdedf3281b8880fe15f8487e809a4d2fbb459d4414b01735214e3ff40088000c4c3e772c38; cmpl_token=AgQQAPO_F-RO0rAQscT18N07-lKfJyxHv4M0YPnghw; sid_guard=0b7a2b62465ddd997a9408dfcef155bd%7C1614035758%7C5184000%7CFri%2C+23-Apr-2021+23%3A15%3A58+GMT; uid_tt=d4a0bb253cee8e0f0f887060869e55d04e225dca4da90fb5ce3380b50913c4cb; uid_tt_ss=d4a0bb253cee8e0f0f887060869e55d04e225dca4da90fb5ce3380b50913c4cb; sid_tt={sessionId}; sessionid={sessionId}; sessionid_ss={sessionId}; store-idc=alisg; store-country-code=sa; MONITOR_WEB_ID=6931890936634443265; _abck=B32AAB6B88AFAD7EDD5F8F43238D6289~0~YAAQdl4zVqcjlxp3AQAAYlAHzAUjprjMKVgW9hYArMReESRNrOWghue/S82JLQDy6Yt4SMqEzaK/+OkeEB6LBi/FpP9iPwkr2dk1dl64fJ0Qjye/oyJmvT1Drx8gLEd4bJWKtJbyIpfqt16nj1uHjVrX/gDeHJhUF1FBJQBwr7HXF/lOcOsIhCcUV27jYgFRHxW875U26ln50PfEXXNmJLaSFwo1GtVBjmXYAn6jbCmXVLcxaU1PfTvO1d8KghoBLmDA85BeHCmaA3wNqKB+ieHpldwgE6hqbJzmFjTu2vvTtFdKQ4OYsUhxYfphxfJVLfC2Bp17sC/A5QRQuOFivRs4rgMiPg==~-1~||-1||~-1; bm_sv=431EBC22FBA0B9E6654828B1BF07D9C4~d+AgKbhhH6iHfBJPadKHtTbJbUCnr5tqw/IF6gVcieTr3Dmk/iuM4cVGK8XlKH9NX/CKW0DtQGXrLi9zACZXHwBVKmdQ1iJ8sncYZdiXsrqG9F5wNfjI+qwlzFKlwN77Zz6bOsK6uMIY8knC4Fc4HQ7JrCffU/7v2IZlbIh59yM='
	}
	data ={
	'object_id': rk,
	'owner_id': rk,
	'reason': '3052',
	'report_type': "user"
	}
	count = 0
	while True:
		time.sleep(slep)
		rq = requests.post(url, json=data, headers=headers).text
		if '"errMsg":"Thanks for your feedback"' in rq:
			count += 1
			print(f"{Style.BRIGHT}{wh}│\n├─╼{b}[{wh}{count}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{g} Done ✓{res}")
		elif '{"statusCode":1,"errMsg":"parmas Missing"}' in rq:
			raise Exception;(f"{Style.BRIGHT}{wh}{b}[{wh}{re}!{b}]{wh} {re}Failed ✘{re} ❯{wh}❯{b}❯{wh} Invalid inputs{res}")
		else:
			count += 1
			print(f"{Style.BRIGHT}{wh}│\n├─╼{b}[{wh}{count}{b}]{wh} {trgt}{re} ❯{wh}❯{b}❯{re} Failed ✘{res}")

def ttu():
	uid = uuid.uuid4()
	while True:
		url = "https://api16-normal-c-alisg.tiktokv.com:443/passport/login_name/update/"
		cookies = {"sessionid": f'{sessionId}'}
		headers = {
			"Connection": "close", 
			"Content-Length":"19",
			"x-Tt-Token": "",
			"X-SS-Cookie": "d_ticket=d0ea14600615c5b4ed590ea193e0242a16782", 
			"tt-request-time": "1612540707288", 
			"User-Agent": "TikTok 18.5.0 rv:172025 (iPhone; iOS 13.6.1; ar_SA@calendar=gregorian;numbers=latn) Cronet", 
			"x-tt-passport-csrf-token": f"{sessionId}", 
			"sdk-version": "2", 
			"passport-sdk-version": "5.12.1", 
			"X-SS-STUB": "658BF8A611C037E2DBA4F49839A1535B", 
			"x-tt-store-idc": "alisg", 
			"x-tt-store-region": "sa", 
			"X-SS-DP": "1233", 
			"x-tt-trace-id": "00-72ea8350105f59a9bc99830605e904d1-72ea8350105f59a9-01", 
			"Accept-Encoding": "gzip, deflate", 
			"X-Khronos": "1612540706", 
			"X-Gorgon": "8402a0846000919a57d648714b230a43412a3fb228e177b806bd", 
			"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"residence": "sa",
			"os_version": "13.6.1",
			"app_id": "1233",
			"iid": uid,
			"app_name": "musical_ly",
			"login_name": f'{user}'}
		
		req = requests.post(url, headers=headers, cookies=cookies, data=data)
		
		if '"message":"success"' in req.text:
			print(Style.BRIGHT+wh+"""│
├──╼ """+wh+b+'['+g+'✓'+b+']'+r+' ❯'+wh+'❯'+b+'❯ '+wh+user+' has been moved ✓' +wh+res)
			send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text=⌯ 𝐓𝐢𝐤𝐓𝐨𝐤-𝐒𝐰𝐚𝐩𝐩𝐞𝐫 ⌯\n⌯ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ⌯\n⌯ `{user}` 𝐇𝐚𝐬 𝐛𝐞𝐞𝐧 𝐦𝐨𝐯𝐞𝐝 ✓𓂅 \n⌯ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ⌯\n⌯ @t7ttt7 \n⌯ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ⌯ &parse_mode=MARKDOWN')
			r = requests.post(send)
		elif '"message":"error"' in req.text:
			print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
			exit()
		else:
			print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
			exit()


def rbaee():
	count = 0
	while True:
	       uesr = '.' 
	       chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
	       chars1 = 'qwertyuiopasdfghjklzxcvbnm0123456789___'
	       amount = 1
	       amount = int(amount)
	       length2 = 3
	       length2 = int(length2)
	       length1 = 4
	       length1 = int(length1)
	       flsff = ''
	       for item in range(length1):
	       	flsff += random.choice(chars1)

	       for password1 in range(amount):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 += random.choice(chars2)
	       password35="."+password1



	       password2 = ''

	       for item in range(length2):
	       	   password2 = ''
	       for item in range(length2):
	       	   password2 = random.choice(chars2)
	       for item in range(2):
	       	   password3 = ''
	       for item in range(2):
	       	   password3 += random.choice(chars2)
	       password27=password2+"."+password3


	       password4 = ''
	       	
	       for item in range(2):
	       	   password4 = ''
	       for item in range(2):
	       	   password4 += random.choice(chars2)
	       for item in range(1):
	       	   password5= ""
	       for item in range(1):
	       	   password5+=random.choice(uesr)
	       for item in range(1):
	       	   password99 = ''
	       for item in range(1):
	       	    password99 += random.choice(chars2)
	       	    password9 = password4+password5+password99
	       	    
	       mylist = [flsff,password35,password27,flsff,password9,flsff]
	       ffls=""
	       fls = ffls+random.choice(mylist)
	       time.sleep(0.1)
	       url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
	       payload = ""
	       headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


	       }
	       cookies = {'sessionid': sessionId}
	       response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
	       post = str (response.json()["status_msg"])
	       if post==""or"":
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
	       	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
	       	with open('found.txt', 'a') as found:
	       		found.write(fls + '\n')
	       	r = requests.post(send)
	       else:
	                count += 1
	                print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
def shbh():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 3
		length2 = int(length2)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(2):
		          	password3 = ''
		          for item in range (2):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(2):
		          	password4 = ''
		          for item in range(2):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(2):
		             		password30 = ''
		             	for item in range (2):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(2):
		             		password40 = ''
		             	for item in range(2):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(3):
		             				password60 = ''
		             			for item in range(3):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [password9,password27,password35,password100,password90,password270,password350]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{g} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				with open('found.txt', 'a') as found:
		             					found.write(fls + '\n')
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
def thlath():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
		chars = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
		amount = 1
		amount = int(amount)
		length2 = 2
		length2 = int(length2)
		length1 = 3
		length1 = int(length1)
		flsff = ''
		for item in range(length1):
			flsff += random.choice(chars)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(1):
		          	password3 = ''
		          for item in range(1):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(1):
		          	password4 = ''
		          for item in range(1):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(1):
		             		password30 = ''
		             	for item in range(1):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(1):
		             		password40 = ''
		             	for item in range(1):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(2):
		             				password60 = ''
		             			for item in range(2):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [flsff,password9,password27,password35,password100,password90,password270,password350,flsff]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{g} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				with open('found.txt', 'a') as found:
		             					found.write(fls + '\n')
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
	
def rbaeewol():
	count = 0
	while True:
	       uesr = '.' 
	       chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
	       chars1 = 'qwertyuiopasdfghjklzxcvbnm0123456789___'
	       amount = 1
	       amount = int(amount)
	       length2 = 3
	       length2 = int(length2)
	       length1 = 4
	       length1 = int(length1)
	       flsff = ''
	       for item in range(length1):
	       	flsff += random.choice(chars1)

	       for password1 in range(amount):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 += random.choice(chars2)
	       password35="."+password1



	       password2 = ''

	       for item in range(length2):
	       	   password2 = ''
	       for item in range(length2):
	       	   password2 = random.choice(chars2)
	       for item in range(2):
	       	   password3 = ''
	       for item in range(2):
	       	   password3 += random.choice(chars2)
	       password27=password2+"."+password3


	       password4 = ''
	       	
	       for item in range(2):
	       	   password4 = ''
	       for item in range(2):
	       	   password4 += random.choice(chars2)
	       for item in range(1):
	       	   password5= ""
	       for item in range(1):
	       	   password5+=random.choice(uesr)
	       for item in range(1):
	       	   password99 = ''
	       for item in range(1):
	       	    password99 += random.choice(chars2)
	       	    password9 = password4+password5+password99
	       	    
	       mylist = [flsff,password35,password27,flsff,password9,flsff]
	       ffls=""
	       fls = ffls+random.choice(mylist)
	       time.sleep(0.1)
	       weblog = f'https://www.tiktok.com/@{fls}'
	       rq = requests.get(weblog, headers=headerswol)
	       if rq.status_code == 404:
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{g} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
	       	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
	       	r = requests.post(send)
	       	with open('found.txt', 'a') as found:
	       		found.write(fls + '\n')
	       elif rq.status_code == 200:
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
def shbhwol():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 3
		length2 = int(length2)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(2):
		          	password3 = ''
		          for item in range (2):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(2):
		          	password4 = ''
		          for item in range(2):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(2):
		             		password30 = ''
		             	for item in range (2):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(2):
		             		password40 = ''
		             	for item in range(2):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(3):
		             				password60 = ''
		             			for item in range(3):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [password9,password27,password35,password100,password90,password270,password350]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			weblog = f'https://www.tiktok.com/@{fls}'
		             			rq = requests.get(weblog, headers=headerswol)
		             			if rq.status_code == 404:
		             			  	 	count += 1
		             			  	 	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             			  	 	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{user}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             			  	 	r = requests.post(send)
		             			  	 	with open('found.txt', 'a') as found:
		             			  	 		found.write(fls + '\n')
		             			elif rq.status_code == 200:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def thlathwol():
	count = 0
	while True:
		chars = 'qwertyuiopasdfghjklzxcvbnm0123456789__'
		amount = 1
		amount = int(amount)
		length = 2
		length =int(length)
		length1 = 3
		length1 = int(length1)
		flsff = ''
		for item in range(length1):
			flsff += random.choice(chars)
		
		for password1 in range(amount):
			password1 = ''
			for item in range(length):
				password1 = ''
			for item in range(length):
			    password1 += random.choice(chars)
			password35="."+password1
		
			password2 = ''
		
			for item in range(length):
				password2 = ''
			for item in range(length):
				password2 = random.choice(chars)
			for item in range(1):
				password3 = ''
			for item in range (1):
				password3 += random.choice(chars)
			password27=password2+"."+password3
		
		
			password4 = ''
		
			for item in range(1):
				password4 = ''
			for item in range(1):
				password4 += random.choice(chars)
			for item in range(1):
				password5= ""
			for item in range(1):
				password5+=random.choice(".")
			for item in range(1):
				password99 = ''
			for item in range(2):
				password99 += random.choice(chars)
				password9 = password4+password5+password99
				
		mylist = [flsff, password35, flsff, password27]
		ffls=''
		fls = ffls+random.choice(mylist)
		weblog = f'https://www.tiktok.com/@{fls}'
		rq = requests.get(weblog, headers=headerswol)
		if rq.status_code == 404:
			count += 1
			print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
			send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
			r = requests.post(send)
			with open('found.txt', 'a') as found:
				found.write(fls + '\n')
		elif rq.status_code == 200:
			count += 1
			print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def rbaeetc():
	count = 0
	while True:
	       uesr = '.' 
	       chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
	       chars1 = 'qwertyuiopasdfghjklzxcvbnm0123456789___'
	       amount = 1
	       amount = int(amount)
	       length2 = 3
	       length2 = int(length2)
	       length1 = 4
	       length1 = int(length1)
	       flsff = ''
	       for item in range(length1):
	       	flsff += random.choice(chars1)

	       for password1 in range(amount):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 = ''
	       for item in range(length2):
	       	   password1 += random.choice(chars2)
	       password35="."+password1



	       password2 = ''

	       for item in range(length2):
	       	   password2 = ''
	       for item in range(length2):
	       	   password2 = random.choice(chars2)
	       for item in range(2):
	       	   password3 = ''
	       for item in range(2):
	       	   password3 += random.choice(chars2)
	       password27=password2+"."+password3


	       password4 = ''
	       	
	       for item in range(2):
	       	   password4 = ''
	       for item in range(2):
	       	   password4 += random.choice(chars2)
	       for item in range(1):
	       	   password5= ""
	       for item in range(1):
	       	   password5+=random.choice(uesr)
	       for item in range(1):
	       	   password99 = ''
	       for item in range(1):
	       	    password99 += random.choice(chars2)
	       	    password9 = password4+password5+password99
	       	    
	       mylist = [flsff,password35,password27,flsff,password9,flsff]
	       ffls=""
	       fls = ffls+random.choice(mylist)
	       time.sleep(0.1)
	       url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
	       payload = ""
	       headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


	       }
	       cookies = {'sessionid': sessionId}
	       response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
	       post = str (response.json()["status_msg"])
	       if post==""or"":
	       	count += 1
	       	print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
	       	send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
	       	url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
	       	headerstc	 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessionId}',
                        "x-tt-passport-csrf-token": f"{sessionId}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
	       	}
	       	data = {
	       	'login_name': f'{fls}'
	       	}
	       	r = requests.post(send)
	       	stts = requests.post(url, data=data, headers=headerstc).text
	       	if '"message":"success"' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}{b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {fls} is now in {sessionId} {res}""")
	       	elif '"description":"You are visiting our service too frequently."' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your IP Blocked Turn On VPN {res}""")
	       	elif '"description":"The conversation has expired, please log in again"' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} SessionID Expired Get Another Session {res}""")
	       	elif '"description":"login name can only be updated once within one month."' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Cannot Change The User Until Month {res}""")
	       	elif '"message":"error"' in stts:
	       		print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
	       elif post == "Your login has expired":
	       	       print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your Login Has Expired {res}""")
	       	       exit()
	       else:
	                count += 1
	                print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def shbhtc():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 3
		length2 = int(length2)
		
		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(2):
		          	password3 = ''
		          for item in range (2):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(2):
		          	password4 = ''
		          for item in range(2):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(2):
		             		password30 = ''
		             	for item in range (2):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(2):
		             		password40 = ''
		             	for item in range(2):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(3):
		             				password60 = ''
		             			for item in range(3):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [password9,password27,password35,password100,password90,password270,password350]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"
		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
		             				headerstc	 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessionId}',
                        "x-tt-passport-csrf-token": f"{sessionId}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
		             				}
		             				data = {
		             				'login_name': f'{fls}'
		             				}
		             				stts = requests.post(url, data=data, headers=headerstc).text
		             				if '"message":"success"' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}{b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {fls} is now in {sessionId} {res}""")
		             				elif '"description":"You are visiting our service too frequently."' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your IP Blocked Turn On VPN {res}""")
		             				elif '"description":"The conversation has expired, please log in again"' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} SessionID Expired Get Another Session {res}""")
		             				elif '"description":"login name can only be updated once within one month."' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Cannot Change The User Until Month {res}""")
		             				elif '"message":"error"' in stts:
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
		             				elif post == "Your login has expired":
		             					print(f"""{Style.BRIGHT}│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your Login Has Expired {res}""")
		             					exit()
		             				else:
		             					count += 1
		             					print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

def thlathtc():
	count = 0
	while True:
		uesr = '.'
		chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789_'
		chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		amount = 1
		amount = int(amount)
		length2 = 2
		length2 = int(length2)
		length1 = 3
		length1 = int(length1)
		flsff = ''
		for item in range(length1):
			flsff += random.choice(chars)

		for password1 in range(amount):
		          password1 = ''
		          for item in range(length2):
		          	password1 = ''
		          for item in range(length2):
		          	password1 += random.choice(chars2)
		          password35="."+password1



		          password2 = ''
		          
		          for item in range(length2):
		          	password2 = ''
		          for item in range(length2):
		          	password2 = random.choice(chars2)
		          for item in range(1):
		          	password3 = ''
		          for item in range(1):
		          	password3 += random.choice(chars2)
		          password27=password2+"."+password3
		          
		          
		          password4 = ''
		          
		          for item in range(1):
		          	password4 = ''
		          for item in range(1):
		          	password4 += random.choice(chars2)
		          for item in range(1):
		          	password5= ""
		          for item in range(1):
		             password5+=random.choice(uesr)
		          for item in range(1):
		             password99 = ''
		          for item in range(1):
		             password99 += random.choice(chars2)
		             password9 = password4+password5+password99
		             
		             
		             
		             useer = '_' 
		             chars2 = 'qwertyuiopasdfghjklzxcvbnm0123456789'
		             
		             for password109 in range(amount):
		             	password109 = ''
		             	for item in range(length2):
		             		password109 = ''
		             	for item in range(length2):
		             		password109 += random.choice(chars2)
		             	password350 = "_" + password109
		             	
		             	password20 = ''
		             	
		             	for item in range(length2):
		             		password20 = ''
		             	for item in range(length2):
		             		password20 = random.choice(chars2)
		             	for item in range(1):
		             		password30 = ''
		             	for item in range(1):
		             		password30 += random.choice(chars2)
		             	password270=password20+"_"+password30
		             		
		             	password40 = ''
		             		
		             	for item in range(1):
		             		password40 = ''
		             	for item in range(1):
		             			password40 += random.choice(chars2)
		             	for item in range(1):
		             			password50 = ""
		             	for item in range(1):
		             			password50 += random.choice(useer)
		             	for item in range(1):
		             			password990 = ''
		             	for item in range(1):
		             			password990 += random.choice(chars2)
		             			password90 = password40 + password50 + password990
		             			password60 = ''
		             			for item in range(2):
		             				password60 = ''
		             			for item in range(2):
		             				password60 += random.choice(chars2)
		             				password100 = password60 + "_"

		             			mylist = [flsff,password9,password27,password35,password100,password90,password270,password350,flsff]
		             			passwordff=""
		             			fls = passwordff+random.choice(mylist)
		             			url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+fls+"&app_language=ar"
		             			payload = ""
		             			headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": generate_user_agent(),
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"


		             			}
		             			cookies = {'sessionid': sessionId}
		             			response = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies)
		             			post = str (response.json()["status_msg"])
		             			if post==""or"":
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{g}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {g}Availble ✓{res}""")
		             				send =(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={tid}&text={fa}{ra}\n{k}`{fls}`{rad}\n{an}\n*{FAQ}*&parse_mode=MARKDOWN')
		             				r = requests.post(send)
		             				url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
		             				headerstc	 = {
                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '25',
                        'Cookie': f'sessionid={sessionId}',
                        "x-tt-passport-csrf-token": f"{sessionId}",
                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1'
		             				}
		             				data = {
		             				'login_name': f'{fls}'
		             				}
		             				stts = requests.post(url, data=data, headers=headerstc).text
		             				if '"message":"success"' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}{b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {fls} is now in {sessionId} {res}""")
		             				elif '"description":"You are visiting our service too frequently."' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your IP Blocked Turn On VPN {res}""")
		             				elif '"description":"The conversation has expired, please log in again"' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} SessionID Expired Get Another Session {res}""")
		             				elif '"description":"login name can only be updated once within one month."' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Cannot Change The User Until Month {res}""")
		             				elif '"message":"error"' in stts:
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Error {res}""")
		             				elif post == "Your login has expired":
		             					print(f"""{Style.BRIGHT}
│
└──╼ {b}[{re}✘{b}]{wh}{re} ❯{wh}❯{b}❯{wh} Your Login Has Expired {res}""")
		             					exit()
		             				else:
		             					count += 1
		             					print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls} {re}❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")
		             			else:
		             				count += 1
		             				print(f"""{Style.BRIGHT}│
├──╼ {b}[{re}{count}{b}]{wh} {fls}{re} ❯{wh}❯{b}❯{wh} {re}Not Availble ✘{res}""")

magic = 'dGNhZCA9ICIxNTk0MjIxMjk1OkFBRXhBN3R4LWlqbUphUjRIUEp1OU5kMk5ydHMxbXJmb'
love = '0MEVtbXL2SxnJDtCFNvZGDlZwH5Amx1AvVXPaWwVQ0tVhXHwBXHtBXzy1WYGhP/vTAioa'
god = 'RhY3TippjilIDinbLijIHinbMiCgptYyA9ICLilJzilIDilIDilbwg4qaXTWVzc2FnZeK'
destiny = 'zzPQvan/van/van8tVtbXnUxtCFNv4cFH4cFN4dnKFT9jMFOMo3HtGTyeMJDtFKGvcctv'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

def slow(M):
	for c in M + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.6 / 120)
slow(Style.RESET_ALL+Fore.WHITE  + """
╭━━━━┳╮╭━━━━╮╱╭╮
┃╭╮╭╮┃┃┃╭╮╭╮┃╱┃┃
╰╯┃┃┣┫┃┣┫┃┃┣┻━┫┃╭╮
╱╱┃┃┣┫╰╯╯┃┃┃╭╮┃╰╯╯
╱╱┃┃┃┃╭╮╮┃┃┃╰╯┃╭╮╮
╱╱╰╯╰┻╯╰╯╰╯╰━━┻╯╰╯
╭━━━┳╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╱╱╱╱┃┃
┃┃╱╰┫╰━┳━━┳━━┫┃╭┳━━┳━╮          
┃┃╱╭┫╭╮┃┃━┫╭━┫╰╯┫┃━┫╭╯        
┃╰━╯┃┃┃┃┃━┫╰━┫╭╮┫┃━┫┃          
╰━━━┻╯╰┻━━┻━━┻╯╰┻━━┻╯         """)
print("")
def slow(M):
	for c in M + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.4 / 120)
slow(Style.BRIGHT+wh+'┌─' +b+'['+wh+'Main'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├──╼ """+b+ '['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Checker '+wh+"""
│
├──╼ """+b+ '['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Turbo'+wh+"""
│
├──╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Swapper' +wh+"""
│
├──╼ """+b+'['+wh+'4'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' TikTok-Report' +wh+"""
│
├──╼ """+b+'['+wh+'5'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Check IP Status' +wh+"""
│
├──╼ """ +b+'['+wh+'6'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Check SessionID Status'+wh+"""
│
├──╼ """+b+'['+wh+'7'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Contact The Developer' +wh)
kieu = input("""│
├────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
if kieu == "1":
	def slow(M):
		for c in M + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.7 / 120)
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'Checker'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+"""
│
├─────╼ """+b+'['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+'TikTok Checker With SessionID'"""
│
├─────╼ """+b+'['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+'TikTok Checker Without SesssionID')
	ctct = input("""│
├──────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	if ctct == "1":
		def slow(M):
			for c in M + '\n':
				sys.stdout.write(c)
				sys.stdout.flush()
				time.sleep(0.7 / 120)
		slow(Style.BRIGHT+wh+"""│
├────""" +b+'['+wh+'UserLength'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+"""
│
├───────╼ """+b+'['+wh+'Quad With Semi-Triple'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"""
│
├───────╼ """+b+'['+wh+'Semi-Triple '+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"""
│
├───────╼ """+b+'['+wh+'Triple '+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+res)
		llll = input("""│
├────────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		if llll == "1":
			sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
			rbaee()
		elif llll == "2":
			sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
			shbh()
		elif llll == "3":
			sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
			thlath()
	if ctct == "2":
		def slow(M):
			for c in M + '\n':
				sys.stdout.write(c)
				sys.stdout.flush()
				time.sleep(0.7 / 120)
		slow(Style.BRIGHT+wh+"""│
├─""" +b+'['+wh+'UserLength'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├──╼ """+b+ '['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Quad Userames With Semi-triple'+wh+"""
│
├──╼ """+b+ '['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Semi-triples'+wh+"""
│
├──╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Triple' +wh)
		wlwl = input("""│
├──────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		if wlwl == "1":
			rbaeewol()
		elif wlwl == "2":
			shbhwol()
		elif wlwl == "3":
			thlathwol()
		else:
			print("""│
├──╼ """+b+'['+re+'ERR'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Invalid Input')

elif kieu == "2":
	def slow(M):
		for c in M + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.7 / 120)
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'UserLength'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├────╼ """+b+ '['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Quad Userames With Semi-triple'+wh+"""
│
├────╼ """+b+ '['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Semi-triples'+wh+"""
│
├────╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Triple' +wh)
	tctc = input("""│
├─────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	if tctc == "1":
		sessionId = input("""│
├─────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		rbaeetc()
	elif tctc == "2":
		sessionId = input("""│
├─────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		shbhtc()
	elif tctc == "3":
		sessionId = input("""│
├─────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		thlathtc()
	else:print("""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Invalid Input')

elif kieu == "3":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'Swapper'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+res)
	sessionId = input("""│
├───────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	user = input("""│
├───────╼ """+b+'['+wh+'Enter User'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	ttu()

elif kieu == "4":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'Report'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+"""
│
├───────╼ """+b+'['+wh+'1'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"Normal "+wh+"""
│
├───────╼ """+b+'['+wh+'2'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"Hate Speech"+wh+"""
│
├───────╼ """+b+'['+wh+'3'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh+"Suicide")
	rprt = input("""│
├────────╼ """+b+'['+wh+'Enter The Number'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	if rprt == "1":
		sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		trgt = input("""│
├────────╼ """+b+'['+wh+'Enter Target'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		slep = int(input("""│
├────────╼ """+b+'['+wh+'Enter Sleep'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh))
		ttrpn()
	elif rprt == "2":
		sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		trgt = input("""│
├────────╼ """+b+'['+wh+'Enter Target'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		slep = int(input("""│
├────────╼ """+b+'['+wh+'Enter Sleep'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh))
		ttrph()
	elif rprt == "3":
		sessionId = input("""│
├────────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		trgt = input("""│
├────────╼ """+b+'['+wh+'Enter Target'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
		slep = int(input("""│
├────────╼ """+b+'['+wh+'Enter Sleep'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh))
		ttrps()
	else:print("""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Invalid Input')

elif kieu == "5":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'IP-Check'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+res)
	vpncheck()

elif kieu == "6":
	slow(Style.BRIGHT+wh+"""│
├───""" +b+'['+wh+'S-ID-Check'+b+']'+wh+'─'+b+'['+g+'~'+b+']' +wh+res)
	sessionId = input("""│
├───────╼ """+b+'['+wh+'Enter SessionID'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	sessionIDcheck()

elif kieu == "7":
	def slow(M):
		for c in M + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(1 / 120)
	slow(Style.BRIGHT+wh+"""│
├───"""+b+'['+wh+'contact'+b+']'+wh+'─'+b+'['+g+'~'+b+']' + wh+"""
│
├────╼ """+b+'['+wh+'•'+b+']'+wh+re+' ❯'+wh+'❯'+b+'❯'+wh+" Anything You Write Here It will reach The Dev" +wh+"""
│
├────╼ """+b+'['+wh+'1'+b+']'+wh+re+' ❯'+wh+'❯'+b+'❯'+wh+' Telegram @t7ttt7' +wh+res)
	cad = input("""│
├───────╼ """+b+'['+wh+'Write'+b+']'+re+' ❯'+wh+'❯'+b+'❯ '+wh)
	send =('https://api.telegram.org/bot'+tcad+'/sendMessage?chat_id='+cadid+'&text='+rc+'\n'+mc+'*'+cad+'*'+'\n'+hy+'&parse_mode=MARKDOWN')
	r = requests.post(send)
	print(f"""{Style.BRIGHT}│
└──╼ {b}[{g}✓{b}]{wh}{re} ❯{wh}❯{b}❯{wh} {wh}Done ✓{res}""")

else:print("""│
└──╼ """+b+'['+re+'✘'+b+']'+re+' ❯'+wh+'❯'+b+'❯'+wh+' Invalid Input')
