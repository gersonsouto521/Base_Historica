import sqlite3


class HistoricalSummarySqlitePipeline(object):
    def process_item(self, item, spider):
        self.conn.execute(
            'insert into historical_summary(title, codigo_da_acao, ativo, periodo, abe, maximo, minimo, preco_med, vol_med, variacao, porcentagem) values (:title, :codigo_da_acao, :ativo, :periodo, :abe, :maximo, :minimo, :preco_med, :vol_med, :variacao, :porcentagem)',
            item
        )
        self.conn.commit()
        return item
 
    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name ="historical_summary" '
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                'create table historical_summary(id integer primary key, title text, codigo_da_acao text, ativo text, periodo text, abe text, maximo text, minimo text, preco_med text, vol_med text, variacao text, porcentagem text)'
            )
    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()
 
    def close_spider(self, spider):
        self.conn.close()

