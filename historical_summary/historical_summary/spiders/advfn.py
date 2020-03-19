# -*- coding: utf-8 -*-
import scrapy


class AdvfnSpider(scrapy.Spider):
    name = 'advfn'
    allowed_domains = ['https://br.advfn.com/bolsa-de-valores/bovespa/itausa-pn-ITSA4/historico']
    start_urls = ['http://https://br.advfn.com/bolsa-de-valores/bovespa/itausa-pn-ITSA4/historico/']

    def parse(self, response):
        pass
