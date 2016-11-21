from impostos import ISS, ICMS, IKCV, ICPP

class Calculador_de_impostos(object):

	def realiza_calculo(self, calculo, imposto):
		imposto_calculado = imposto.calcula(orcamento)
		print 'R$ ',imposto_calculado


if __name__ == '__main__':

	from orcamento import Orcamento, Item

	calculador = Calculador_de_impostos()
	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Arroz', 30))
	orcamento.adiciona_item(Item('Feijao', 59))
	orcamento.adiciona_item(Item('Carne', 350))
	print '---Total da compra-- '
	print '-------------------- R$ ', orcamento.valor

	print 'ISS e ICMS'
	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())

	print 'ISS com ICMS' 
	calculador.realiza_calculo(orcamento, ISS(ICMS()))

	print 'IKCV e ICPP'
	calculador.realiza_calculo(orcamento, ICPP())
	calculador.realiza_calculo(orcamento, IKCV())

	print 'ICPP com IKCV' 
	calculador.realiza_calculo(orcamento, ICPP(IKCV()))