# -*- coding: utf-8 -*-
import scrapy
from historical_summary.run import *

class AdvfnSpider(scrapy.Spider):
    name = 'advfn'
    start_urls = ['https://br.advfn.com/bolsa-de-valores/bovespa/%s/historico'%acao_escolhida2]

    def parse(self, response):
        title = response.xpath('.//h1/strong').extract()
        ativo = response.xpath('//*[@id="quoteElementPiece1"]/text()').extract()
        historicos = response.xpath('//div[2]/table[@class="table_element_class"]//tr')
        for historico in historicos:
            base = historico.xpath('.')
            periodo = base.xpath('.//td[@class="String Column1"]/text()').extract_first()
            abe = base.xpath('.//td[@class="Numeric Column2"]/text()').extract_first()
            max_ = base.xpath('.//td[@class="Numeric Column3"]/text()').extract_first()
            min_ = base.xpath('.//td[@class="Numeric Column4"]/text()').extract_first()
            preco_med = base.xpath('.//td[@class="Numeric Column5"]/text()').extract_first()
            vol_med = base.xpath('.//td[@class="Numeric Column6"]/text()').extract_first()
            variacao = base.xpath('.//td[@class="Numeric Column7"]/text()').extract_first()
            porcentagem = base.xpath('//td[@class="Numeric Column8 ColumnLast"]/text()').extract_first()
            yield{
                'title':title,
                'ativo':ativo,
                'periodo':periodo,
                'abe':abe,
                'max_':max_,
                'min_':min_,
                'preco_med':preco_med,
                'vol_med':vol_med,
                'variacao':variacao,
                'porcentagem':porcentagem,
            }

