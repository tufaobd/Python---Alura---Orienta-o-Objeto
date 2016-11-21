# -*- coding: utf-8 -*-
from datetime import date


class Item(object):

	def __init__(self, descricao, valor):
		self.__descricao = descricao
		self.__valor = valor

	@property
	def descricao(self):
		return self.__descricao

	@property
	def valor(self):
		return self.__valor

class Nota_fiscal(object):

	def __init__(self, razao_social, cnpj, itens, detalhes='', data_de_emissao=date.today(), observadores=[]):
		self.__razao_social = razao_social
		self.__cnpj = cnpj
		self.__itens = itens
		self.__data_de_emissao = data_de_emissao
		if len(detalhes) > 20:
			raise Exception('Detalhe da nota não pode ultrapassar 20 caracteres')
		self.__detalhes = detalhes

		for observador in observadores:
			observador(self)

	@property
	def razao_social(self):
		return self.__razao_social

	@property
	def cnpj(self):
		return self.__cnpj

	@property
	def data_de_emissao(self):
		return self.__data_de_emissao
		
	@property
	def detalhes(self):
		return self.__detalhes


if __name__ == '__main__':
	from criador_nota import Criador_de_nota_fiscal
	from observadores import imprime, enviar_nota, salvar_nota

	itens = [
		Item(
			'Arroz', 25,
			),
		Item(
			'Feijao', 35,
			),
		Item(
			'Carne', 60
			)
		]
	nota_fiscal = Nota_fiscal(
		razao_social='Supermercado Rafael', 
		cnpj='0114477885522',
		itens = itens,
		observadores=[imprime, enviar_nota,salvar_nota]
		)

	#nota_criada_com_builder = (Criador_de_nota_fiscal()
	#	.com_razao_social('Supermercado Rafaels')
	#	.com_cnpj('11223344')
	#	.com_itens(itens)
	#	.constroi()
	#	)
	#print nota_criada_com_builder.cnpj