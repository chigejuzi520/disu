import requests,random,json
from modules.log import logger


headers=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12','Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0','Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0;Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3','Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1','Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3']


def virustotal_get(domain,virustotal_key):
	url="https://www.virustotal.com/vtapi/v2/domain/report?domain={}&apikey={}".format(domain,virustotal_key)
	header1=random.choice(headers)
	header1={'user-agent':header1}
	i=0
	while i<3:
		try:
			response = requests.get(url=url, headers=header1,verify=False,timeout=5)
			if response.status_code==403:
				logger.log('ERROR',"	VirusTotal api 错误.")
				return []
			elif response.status_code==200:
				ret=response.json()
				if 'subdomains' in ret.keys():
					virustotal_domains=ret['subdomains']
					return virustotal_domains
			else:
				logger.log('ERROR','	VirusTotal API No Subdomains.')
				return []
		except requests.exceptions.RequestException:
			i=i+1