from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests, zipfile, io
"""File for creating Person objects
just open this python file to run. If all the python files in floder run together
, this may not work or work extreamly slow"""
class Crawler:
    """get data
    """
    def __init__(self,endpage):
        """endpage must less than 10"""
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            'Connection': 'keep-alive',
            'Referer': 'http://www.baidu.com/'
            }        
        website_num_a = {'a_2012' : '322709', 'a_2013': '322672', 
                       'a_2014' : '322669', 'a_2015': '322667',
                       'a_2016' : '322649', 'a_2017': '327550',
                       'a_2018' : '327550'}
        website_num_b = {'b_2012' : '1424890', 'b_2013': '1424891', 
                       'b_2014' : '1424893', 'b_2015': '1424894',
                       'b_2016' : '1424895', 'b_2017': '1424896',
                       'b_2018' : '1424903'}
        self.website_num_a = website_num_a
        self.website_num_b = website_num_b
        if (10 - int(endpage)) < 0:
            raise ValueError('You have to choose a number less or equal 10')
        else:
            self.endpage = int(endpage)
        
    def post_request(self):
        """Post request, return data"""
        for i in range(1,self.endpage):
            if i == 1:
                url = 'http://stats.gd.gov.cn/zyhygyzjz/index'  + '.html'
            else:
                page = i
                url = 'http://stats.gd.gov.cn/zyhygyzjz/index_' + str(i) + '.html'
            
            req = urllib.request.Request(url, headers=self.headers)
            data = urllib.request.urlopen(req).read().decode()
            print(url)
            soup = BeautifulSoup(data, 'lxml')
            urllist = soup.select('li a[target="_blank"]')
            self.urllist = urllist
            return self.urllist
    
    def get_zip_url(self,k,j):
        """Get zip download address from 2012 to 2018"""
        if k not in ['a_2017', 'a_2018']:
            url_1 = 'http://stats.gd.gov.cn/attachment/0/322/' + str(self.website_num_a[k]) + '/' + str(self.website_num_b[j]) + '.zip?ref=spec'  
        else:
            url_1 = 'http://stats.gd.gov.cn/attachment/0/327/' + str(self.website_num_a[k]) + '/' + str(self.website_num_b[j]) + '.zip?ref=spec'
        self.website_num_b = self.website_num_b[j]
        self.url_1 = str(url_1)
        print(self.url_1)
    
    def get_zip_by_url(self):
        """Download zip to local"""
        print ("downloading with requests")
        r = requests.get(self.url_1,stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        print ("downloading finish")
            


abc = Crawler('9')                ###test
print(abc.post_request())         ###test
abc.get_zip_url('a_2017','b_2017')###test
abc.get_zip_by_url()              ###test


