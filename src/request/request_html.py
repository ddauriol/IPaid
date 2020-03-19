import requests
from bs4 import BeautifulSoup


class GetDadosProdutos():
    def __init__(self, GTIN_EAN):
        self.url = 'https://cosmos.bluesoft.com.br/produtos/'
        self.GTIN_EAN = GTIN_EAN
        self.dados_produto = {}
        self.i = 0
        self.RequestURL()
        self.GetNoneProduto()
        self.GetInformacao()

    def RequestURL(self):
        r = requests.get(self.url + self.GTIN_EAN).text
        self.html_text = BeautifulSoup(r, 'html.parser')

    def GetNoneProduto(self):
        h1 = str(self.html_text.findAll("h1", {"class": "page-header"}))
        self.dados_produto[self.i] = {
            'Nome do Produto': h1[24:h1.find('<img')].replace('\n', '')
            }
        self.i = self.i + 1
        self.dados_produto[self.i] = {
            'img': 'https://cdn-cosmos.bluesoft.com.br/products/'
            + self.GTIN_EAN
            }
        self.i = self.i + 1

    def GetInformacao(self):
        dl = self.html_text.findAll("dl", {"class": "dl-horizontal"})
        dts = self.html_text.findAll("dt")
        dds = self.html_text.findAll("dd")
        inf_produto = []
        desc_produto = []

        for tag in dts:
            inf_produto.append((tag.text).replace('\n', '').replace(':', ''))

        for tag in dds:
            desc_produto.append((tag.text).replace('\n', ''))

        if len(desc_produto) == len(inf_produto):
            while self.i < len(desc_produto):
                self.dados_produto[self.i] = {
                    inf_produto[self.i]: desc_produto[self.i]
                    }
                self.i = self.i + 1


id_7896102584189 = GetDadosProdutos('7894000050034')
print(id_7896102584189.dados_produto)
