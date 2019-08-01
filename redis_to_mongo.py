import redis,pymongo,json

# redis 配置项
redis_url = '127.0.0.1'
redis_port = 6379
redis_db = 2
redis_passwd = None

# mongo 配置项
mongo_url = '127.0.0.1'
mongo_port = 27017
mongo_dbname = 'admin'
mongo_table = 'wbproduct'
mongo_user = 'alice'
mongo_passwd = 123456



def process_item():
	redis_cli = redis.StrictRedis(host=redis_url, port=redis_port, db=redis_db, password=redis_passwd)
	mongo_cli = pymongo.MongoClient(host=mongo_url, port=mongo_port, username=mongo_user, password=mongo_passwd)
	mongo_DB = mongo_cli[mongo_dbname]
	mongo_TB = mongo_DB[mongo_table]
	while True:
		try:
			source, data_json = redis_cli.blpop('wanbiao:items')
			data = json.loads(data_json.decode('utf-8'))
		except:
			print('redis 获取数据失败')
			break
		try:
			mongo_TB.insert(data)
		except:
			print('mongo插入失败')
			break
		
		
if __name__ == '__main__':
	process_item()
			
	
	
