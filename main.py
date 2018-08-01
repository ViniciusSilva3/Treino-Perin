class Menu:
	def start(self):
		print("*********************")
		print("MENU BANCO")
		print("Selecione a opcao:")
		print("1")
		print("2")
		print("3\n")
		while(1):
			escolha = raw_input("Entre com a opcao desejada:\n")
			if escolha == '1':
				self.met1()
				break
			elif escolha == '2':
				self.met2()
				break
			elif escolha == '3':
				self.met3()
				break
			else:
				print("Opcao Invalida\n")
		return escolha

	def met1(self):
		print("escolha a quantidade a ser depositada: ")

	def met2(self):
		print("Escolha a quantidade a ser transferida: ")

	def met3(self):
		print("Escolha a quantidade a ser sacada: ")


class Conta:
	def __init__(self, numero):
		self.num = numero
		self.saldo = 0

	def getSaldo(self):
		print(self.saldo)

	def depositar(self, x):
		self.saldo = self.saldo + x

	def retirar(self, x):
		self.saldo = self.saldo - x



a = Conta(13)
a.getSaldo()
a.depositar(100)
a.getSaldo()
b = a.saldo
print b

