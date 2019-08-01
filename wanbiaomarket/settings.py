# -*- coding: utf-8 -*-

# Scrapy settings for wanbiaomarket project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wanbiaomarket'

SPIDER_MODULES = ['wanbiaomarket.spiders']
NEWSPIDER_MODULE = 'wanbiaomarket.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wanbiaomarket (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Cookie':'wsess_id=MjAxODA2MjgyMjMyMDE=; acw_tc=AQAAADM7iQHoqgMAIhdDfJZ+m8QG80TV; w_info=eyJlbnYiOiJwcm9kIn0=; _ga=GA1.2.20674272.1530196323; _gid=GA1.2.293933105.1530196323; Hm_lvt_d8e95c635d8135c55060c556fd69e039=1530196324; NTKF_T2D_CLIENTID=guest8CB3DE47-8E24-07B0-3678-46CEF241BEF6; nTalk_CACHE_DATA={uid:wx_1000_ISME9754_guest8CB3DE47-8E24-07,tid:1530196324929918}; Qs_lvt_93213=1530196325; mediav=%7B%22eid%22%3A%22221303%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%226AD%3D%3DFO)%3D8%3C%25zBx7oj%3Ds%22%2C%22ctn%22%3A%22%22%7D; __lnkrntdmcvrd=wbiao.cn; wTk=OrJhM1B3kyQ0A4KqKX3CxVUe; wbiaoid=91558367345c0c568b71f25870aa28bd; wbiaoid.sig=Q7fEn5_SXpzVHLrAOJwjaKA4JJ4uQjySQFDi7h0T1Yc; Hm_lpvt_d8e95c635d8135c55060c556fd69e039=1530196449; Qs_pv_93213=476284887625091800%2C3752561769283351000%2C4102247614687463400%2C3239285301165129000%2C4310371804085287000; WBIAOID=b5811345a210a3477fe0269d36896defc23f0528%7Ee41038cca77140b070717dac4de203f2; c0265ed028d0e4c247e1d4b026e2bc6a=43ebaec88b54b5091455584368dc7b5f4c34399f%7E11; OZ_SI_2037=sTime=1530196686&sIndex=1; OZ_1U_2037=vid=vb34f2ce919e29.0&ctime=1530196686&ltime=0; OZ_1Y_2037=erefer=-&eurl=https%3A//www.wbiao.cn/goods/goodsdata.html&etime=1530196686&ctime=1530196686&ltime=0&compid=2037; isntips1=1530196686681; has_checkd_login_status=1; session3=574f837f3df3ddbf7471f0eb781b17972f9618d9%7Ewww3f8ea375e39d6ec2949e17060222fb7ed',
	'Host':'www.wbiao.cn',
	'Referer':'https://www.wbiao.cn/',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wanbiaomarket.middlewares.WanbiaomarketSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wanbiaomarket.middlewares.WanbiaomarketDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wanbiaomarket.pipelines.WanbiaomarketPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
