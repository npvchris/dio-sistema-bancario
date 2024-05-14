import datetime

class SistemaBancarioCLI:
    def __init__(self):
        self.saldo = 0
        self.saques = []
        self.contador_saques_diarios = 0

    def deposito(self, valor):
        if valor >= 100:
            self.saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior ou igual a R$ 100.')

    def saque(self, valor):
        if valor <= 500:
            if self.contador_saques_diarios < 3:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques.append(valor)
                    self.contador_saques_diarios += 1
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                else:
                    print('Saldo insuficiente para realizar o saque.')
            else:
                print('Limite de 3 saques diários alcançado.')
        else:
            print('O valor máximo de saque diário é R$ 500.')

    def extrato(self):
        print('--- Extrato ---')
        print('Data e Hora:', datetime.datetime.now())
        print('Depósitos:')
        for saque in self.saques:
            print(f'Saque de R$ {saque:.2f}')
        print(f'Saldo atual: R$ {self.saldo:.2f}')

        salvar = input("Deseja salvar o extrato em um arquivo de texto? (S/N): ").upper()
        if salvar == 'S':
            self.salvar_extrato_txt()

    def salvar_extrato_txt(self):
        data_hora = datetime.datetime.now()
        nome_arquivo = f"extrato_{data_hora.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write('--- Extrato ---\n')
            arquivo.write(f'Data e Hora: {data_hora}\n')
            arquivo.write('Depósitos:\n')
            for saque in self.saques:
                arquivo.write(f'Saque de R$ {saque:.2f}\n')
            arquivo.write(f'Saldo atual: R$ {self.saldo:.2f}\n')
        print(f'Extrato salvo em {nome_arquivo}')

# Função principal para interação com o usuário
def main():
    sistema = SistemaBancarioCLI()
    while True:
        print("\nOpções:")
        print("D - Depositar")
        print("S - Sacar")
        print("E - Extrato")
        print("Q - Sair")

        opcao = input("Escolha uma opção: ").upper()

        if opcao == 'D':
            valor = float(input("Digite o valor do depósito: "))
            sistema.deposito(valor)
        elif opcao == 'S':
            valor = float(input("Digite o valor do saque: "))
            sistema.saque(valor)
        elif opcao == 'E':
            sistema.extrato()
        elif opcao == 'Q':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
