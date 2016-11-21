# -*- coding: utf-8 -*-
from descontos import Desconto_por_cinco_itens, Desconto_por_quinhentos_reais, Sem_desconto
class Calculador_de_descontos(object):

	def calcula(self, orcamento):
		desconto = Desconto_por_cinco_itens(
			Desconto_por_quinhentos_reais(
				Sem_desconto()
				)
			).calcula(orcamento)
		return desconto


if __name__ == '__main__':
	
	from orcamento import Orcamento, Item

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Arroz', 150))
	orcamento.adiciona_item(Item('Feijão', 300))
	orcamento.adiciona_item(Item('Carne', 20))
	
	calculador = Calculador_de_descontos()
	desconto = calculador.calcula(orcamento)
	
	print '|----------------------------------------- |'
	print '|-- Bem vindo ao Supermercado do Rafael -- |'
	print '| ', (' '*39), '|'
	for itens in orcamento.obter_itens():
		print '|--', itens.nome , (' ' * (37-len(itens.nome))) , ''
		print '|--------------- R$', itens.valor , (' ' * 19) , ''
	print '| ', (' '*39), '|'
	print '|-- Total de itens ', (orcamento.total_itens), (' ' * 19), ' |'
	print '|-- Valor sem desconto R$ ', orcamento.valor, (' ' * 8), ' |'
	print '|-- Desconto R$ ', desconto, (' ' * 22),  ' |'
	print '|-- Valor com Desconto R$ ', orcamento.valor - desconto, (' ' * 8),  ' |'
	print '| ', (' '*39), '|'
	print '|-------------- Volte Sempre --------------|'


