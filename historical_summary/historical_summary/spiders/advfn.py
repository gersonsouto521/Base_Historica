# -*- coding: utf-8 -*-
import scrapy
from historical_summary.run import *
import csv

class AdvfnSpider(scrapy.Spider):
    name = 'advfn'
    start_urls = ['https://br.advfn.com/bolsa-de-valores/bovespa/%s/historico'%acao_escolhida2]

    def parse(self, response):
        with open('../historical_summary/db.csv', 'a', newline='', encoding='utf-8') as saida:
            writer = csv.writer(saida)
            title = response.xpath('.//h1/strong/text()').extract_first()
            codigo_da_acao = response.xpath('.//tr[2]/td[2]/b/text()').extract_first()
            ativo = response.xpath('//*[@id="quoteElementPiece1"]/text()').extract_first()
            historicos = response.xpath('//div[2]/table[@class="table_element_class"]//tr')
            for historico in historicos:
                base = historico.xpath('.')
                periodo = base.xpath('.//td[@class="String Column1"]/text()').extract_first()
                abe = base.xpath('.//td[@class="Numeric Column2"]/text()').extract_first()
                maximo = base.xpath('.//td[@class="Numeric Column3"]/text()').extract_first()
                minimo = base.xpath('.//td[@class="Numeric Column4"]/text()').extract_first()
                preco_med = base.xpath('.//td[@class="Numeric Column5"]/text()').extract_first()
                vol_med = base.xpath('.//td[@class="Numeric Column6"]/text()').extract_first()
                variacao = base.xpath('.//td[@class="Numeric Column7"]/text()').extract_first()
                porcentagem = base.xpath('//td[@class="Numeric Column8 ColumnLast"]/text()').extract_first()
                writer.writerow([title, codigo_da_acao, ativo, periodo, abe, maximo, minimo, preco_med, vol_med, variacao, porcentagem])
                yield{
                    'title':title,
                    'codigo_da_acao':codigo_da_acao,
                    'ativo':ativo,
                    'periodo':periodo,
                    'abe':abe,
                    'maximo':maximo,
                    'minimo':minimo,
                    'preco_med':preco_med,
                    'vol_med':vol_med,
                    'variacao':variacao,
                    'porcentagem':porcentagem,
                }