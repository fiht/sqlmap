mongo_host = 'wordpress.fiht.me'
mongo_port = 60000
from multiprocessing.dummy import Pool
from pymongo import MongoClient
p = Pool(processes=10)
def i(x):
    c = MongoClient(host=mongo_host,port=mongo_port)['txxx']['tx']
    for i in range(1,10000):
        c.insert({'t':i})
p.map(i,range(1,10000))