# -*-coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Estado_orcamento(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def aplica_desconto_extra(self, orcamento):
		pass
	
	@abstractmethod
	def aprova(self, orcamento):
		pass

	@abstractmethod
	def reprova(self, orcamento):
		pass

	@abstractmethod
	def finaliza(self, orcamento):
		pass

class Em_aprovacao(Estado_orcamento):

	def aplica_desconto_extra(self,orcamento):
		orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

	def aprova(self, orcamento):
		orcamento.estado_atual = Aprovado()

	def reprova(self, orcamento):
		orcamento.estado_atual = Reprovado()

	def finaliza(self, orcamento):
		raise Exception('Orcamento em aprovação não pode ser finalizado')


class Aprovado(Estado_orcamento):

	def aplica_desconto_extra(self,orcamento):
		orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

	def aprova(self, orcamento):
		raise Exception('Orcamento já em estado de Aprovado')

	def reprova(self, orcamento):
		raise Exception('Orcamento Aprovado não pode ser Reprovado')

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()

class Reprovado(Estado_orcamento):

	def aplica_desconto_extra(self,orcamento):
		raise Exception('Orçamentos reprovados não recebe desconto extra')

	def aprova(self, orcamento):
		raise Exception('Orcamento reprovados não podem ser Aprovado')

	def reprova(self, orcamento):
		raise Exception('Orcamento já se encontra em situação reprovado')

	def finaliza(self, orcamento):
		orcamento.estado_atual = Finalizado()



class Finalizado(Estado_orcamento):

	def aplica_desconto_extra(self,orcamento):
		raise Exception('Orçamentos Finalizados não recebe desconto extra')

	def aprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser aprovados novamente')
	
	def reprova(self, orcamento):
		raise Exception('Orçamentos finalizados não podem ser reprovados')

	def finaliza(self, orcamento):
		raise Exception('Orçamento finalizados não podem ser finalizados novamente')

class Orcamento(object):

	def __init__(self):
		self.__itens = []
		self.estado_atual = Em_aprovacao()
		self.__desconto_extra = 0

	def aprova(self):
		self.estado_atual.aprova(orcamento)

	def reprova(self):
		self.estado_atual.reprova(orcamento)

	def finaliza(self):
		self.estado_atual.finaliza(orcamento)

	def aplica_desconto_extra(self):
		self.estado_atual.aplica_desconto_extra(self)

	def adiciona_desconto_extra(self, desconto):
		self.__desconto_extra += desconto

	@property
	def valor(self):
		total = 0.0
		for item in self.__itens:
			total += item.valor
		return total - self.__desconto_extra

	def obter_itens(self):
		return tuple(self.__itens)

	@property
	def total_itens(self):
		return len(self.__itens)

	def adiciona_item(self, item):
		self.__itens.append(item)

class Item(object):
	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor = valor

	@property
	def valor(self):
		return self.__valor

	@property
	def nome(self):
		return self.__nome

if __name__ == '__main__':

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Arroz', 150))
	orcamento.adiciona_item(Item('Feijão', 300))
	orcamento.adiciona_item(Item('Carne', 20))

	print 'R$ ', orcamento.valor
	orcamento.aprova()


	orcamento.aplica_desconto_extra()
	#print 'Estado atual',orcamento
	#print 'R$ ', orcamento.valor
	
	
	