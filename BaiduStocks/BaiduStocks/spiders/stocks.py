# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock=re.findall(r"[s][hz]\d{6}",href)[0]
                url='https://gupiao.baidu.com/stock/'+stock+'.html'
                yield scrapy.Request(url,callback=self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        infodict={}
        stockinfo=response.css('.stock-bets')
        name=stockinfo.css('bets-name').extract()[0]
        keyList=stockinfo.css('dt').extract()
        valuelist=stockinfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>',keyList[i])[0][1:-5]
            try:
                val=re.findall(r'\d+\.?.*</dd>',valuelist[i])[0][0:-5]
            except:
                val='--'
            infodict[key]=val
            infodict.update(
                {'股票名称':re.findall(r'\s.*\(',name)[0].split()[0] + \
                    re.findall(r'\>.*\<',name)[0][1:-1]}
            )
        pass
