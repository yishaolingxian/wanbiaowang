# -*- coding: utf-8 -*-
import scrapy
import math,json
from scrapy_redis.spiders import RedisSpider
from wanbiaomarket.items import WanbiaomarketItem
from lxml import etree


class WanbiaoSpider(RedisSpider):
	name = 'wanbiao'
	allowed_domains = ['wbiao.cn']
	# start_urls = ['http://https://www.wbiao.cn//']

	redis_key = 'wanbiao_urls'
	custom_settings = {
		# 'DOWNLOADER_MIDDLEWARES': {
		 #    'okbuymarket.mymiddlerware.ProxySpiderMiddleware': 1,
		 #    'okbuymarket.mymiddlerware.UaSpiderMiddlerware': 2
		# },
	
		'DOWNLOAD_DELAY': 0,
	
		'CONCURRENT_REQUESTS': 30,
		# 下载超时 5- 10 秒
		'DOWNLOAD_TIMEOUT': 10,
		# 下载重试次数 2 -3 次
		'RETRY_TIMES': 2,
	
		# -----------------------scrapy redis 配置---------------------------------------
	
		# url指纹过滤器
		'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
	
		# 调度器
		'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
	
		# 设置爬虫自动清空队列和去重指纹集合，全部爬取完成后会自动清空，
		# 如果强制中断爬虫的运行，爬取队列和去重指纹集合是不会被清空的
		'SCHEDULER_PERSIST': True,
	
		# 爬虫重新启动时候，是否清空队列和指纹
		'SCHEDULER_FLUSH_ON_START': False,
	
		# 设置请求队列类型
		# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
		# 'SCHEDULER_QUEUE_CLASS': "scrapy_redis.queue.SpiderQueue",  # 按照队列模式，先进先出
		'SCHEDULER_QUEUE_CLASS': "scrapy_redis.queue.SpiderStack",  # 按照栈进行请求的调度，先进后出
	
		# 配置redis管道文件，权重数字相对最大
		'ITEM_PIPELINES': {
			'scrapy_redis.pipelines.RedisPipeline': 300,  # redis管道文件，自动把数据加载到redis
		},
	
		# redis 连接配置
		'REDIS_HOST': '127.0.0.1',
		'REDIS_PORT': 6379,
		'REDIS_PARAMS': {
			'password': None,
			'db': 2
		},
	}



	def parse(self, response):
		title_url_list = response.xpath('//div[@class="nav_left_menu"]/div[contains(@class,"menu_box")]/dl/dd[contains(@class,"sub_menu")]//a/@href').extract()
		for title_url in title_url_list:
			print("分类链接===========", title_url)
			yield scrapy.Request(url=title_url, callback=self.parse_list_first, encoding='utf-8')
			
	def parse_list_first(self, response):
		# 解析商品详情页链接
		product_url_list = response.xpath('//div[@id="s_goods_list"]/ul/li//a[contains(@class,"s_goods_name")]/@href').extract()
		# print("product_url_list", product_url_list)
		# for product_url in product_url_list:
		# 	print("商品链接=============", product_url)
			# yield scrapy.Request(url=product_url, callback=self.parse_product, encoding='utf-8')
		
		# 解析分页信息, 获取总商品数，以及手表品牌
		total_goods = response.xpath('//input[@id="total_goods"]/@value').extract()[0]
		# product_name = response.xpath('//script[@type="text/javascript"]/text()')[0]
		product_name = response.xpath('//script[@type="text/javascript"]/text()')[0].re('"brandEnName":"(.*?)"')[0]
		# 构建分页链接
		total_pages = math.ceil(int(total_goods) / 48)
		print('total_pages', total_pages)
		base_url = 'https://www.wbiao.cn/'
		if total_pages >= 2:
			for page in range(2, total_pages + 1):
				print('page',page)
				page_url = base_url + product_name + '-watches/index-p' + str(page) + '.html'
				yield scrapy.Request(url=page_url, callback=self.parse_list_other, encoding='utf-8')
	
	def parse_list_other(self,response):
		# 解析商品详情页链接
		product_url_list = response.xpath('//div[@id="s_goods_list"]/ul/li//a[contains(@class,"s_goods_name")]/@href').extract()
		print("product_url_list", product_url_list)
		for product_url in product_url_list:
			print("商品链接=============", product_url)
			yield scrapy.Request(url=product_url, callback=self.parse_product, encoding='utf-8')
		
	def parse_product(self, response):
		item = WanbiaomarketItem()
		
		# 获取详情描述
		desc = response.xpath('//div[@class="format_content"]/div[contains(@class,"format_content_container")]/div[contains(@class,"right")]/div[contains(@class,"right_a")]//text()').extract()[1:]
		# 拼接构造最终值
		if desc is not None:
			index_list = [index for index, value in enumerate(desc) if value == ' ']
			for index, value in enumerate(index_list):
				if index % 2 == 0:
					desc[value] = ':'
				if index % 2 != 0:
					desc[value] = ';'
			desc = ''.join(desc)
		else:
			desc = ''
		item['desc'] = desc
		# 获取店铺名称
		store = response.xpath('//div[@class="Bread_content"]/div[contains(@class,"Bread_content_right")]/span[@class="right_b"]/a/text()').extract()[0]
		item['store'] = store if store is not None else ''
		print(item['store'])
		
		# 构造ajax请求获取 title, modelnumber, pid, sales, brand, price
		ajax_url = response.url.split('/')[-1].split('.')[0]
		ajax_url = 'https://www.wbiao.cn/goods/goodsData?goodsCode=' + ajax_url
		yield scrapy.Request(url=ajax_url,callback=self.parse_detail,encoding='utf-8', meta={'data':item})

	def parse_detail(self, response):
		item = response.meta['data']
		html = json.loads(response.text)
		html_json = html['html']
		selector = etree.HTML(html_json)
		model_number = selector.xpath('//div[contains(@class, "upper_model_a")]/span[2]/text()')[0]
		pid = selector.xpath('//div[contains(@class, "upper_model_b")]/span[2]/text()')[0]
		brand = selector.xpath('//div[contains(@class, "upper_model_c")]/span[2]/text()')[0]
		sales = selector.xpath('//div[contains(@class, "upper_model_d")]/span[2]/text()')[0]
		price = selector.xpath('//div[@class="upper_price"]//span[contains(@class, "js_price")]/text()')[0].replace(',',                                                                                       '')
		title = selector.xpath('//div[@class="upper_title"]/text()')[0]
		item['price'] = price
		item['title'] = title
		item['modelnumber'] = model_number
		item['pid'] = pid
		item['brand'] = brand
		item['sales'] = sales
		yield item

