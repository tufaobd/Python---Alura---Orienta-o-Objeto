# -*- coding: utf-* -*-

def imprime(nota_fiscal):
	print 'Imprimindo nota %s ...Aguarde' %(nota_fiscal.cnpj)

def enviar_nota(nota_fiscal):
	print 'Enviando nota %s por email .... Aguarde' %(nota_fiscal.cnpj)

def salvar_nota(nota_fiscal):
	print 'Salvando nota %s no banco de dados ... Aguarde' %(nota_fiscal.cnpj)