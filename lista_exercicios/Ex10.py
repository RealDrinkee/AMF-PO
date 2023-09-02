# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# 1. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# 1. tipoCombustivel.
# 2. valorLitro
# 3. quantidadeCombustivel
# 2. Possua no mínimo esses métodos:
# 1. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
# quantidade de litros que foi colocada no veículo
# 2. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
# mostra o valor a ser pago pelo cliente.
# 3. alterarValor( ) – altera o valor do litro do combustível.
# 4. alterarCombustivel( ) – altera o tipo do combustível.
# 5. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.


class BombaCombustivel():

    def __init__(self):
        self.__tipoCombustivel = {
            1: "Gasolina",
            2: "Etanol",
            3: "Diesel",
        }
        self.__valorLitro = {
            self.__tipoCombustivel[1]: 5.00,
            self.__tipoCombustivel[2]: 3.50,
            self.__tipoCombustivel[3]: 4.00,
        }
        self.__quantidadeCombustivel = {
            self.__tipoCombustivel[1]: 500,
            self.__tipoCombustivel[2]: 500,
            self.__tipoCombustivel[3]: 500,
        }

    def getTipoCombustivel(self):
        return self.__tipoCombustivel

    def getValorLitro(self):
        return self.__valorLitro

    def getQuantidadeCombustivel(self):
        return self.__quantidadeCombustivel

    def tipoCombustivel(self):
        print("1 - Gasolina\n2 - Etanol\n3 - Diesel")
        opcaoCombustivel = int(input("Qual combustível deseja? "))
        return opcaoCombustivel


    def abastecerValorGasolina(self):
        valorAbastecerGasolina = float(input("Qual o valor deseja abastecer? "))
        somar = valorAbastecerGasolina / self.__valorLitro[self.__tipoCombustivel[1]]
        if somar > self.__quantidadeCombustivel[self.__tipoCombustivel[1]]:
            print("Não há combustível suficiente para abastecer!")
        else:
            self.__quantidadeCombustivel[self.__tipoCombustivel[1]] = self.__quantidadeCombustivel[self.__tipoCombustivel[1]] - somar
            print(f"Você abasteceu {somar} litros de gasolina")
            print(f"O valor a ser pago é: {valorAbastecerGasolina}\n")
            pagar = float(input("Efetue o pagamento: R$"))
            if pagar < valorAbastecerGasolina:
                print("Valor insuficiente!")
            else:
                print(f"Seu troco é: {pagar - valorAbastecerGasolina}")

        return self.__quantidadeCombustivel[self.__tipoCombustivel[1]]

    def abastecerValorEtanol(self):
        valorAbastecerEtanol = float(input("Qual o valor deseja abastecer? "))
        somar = valorAbastecerEtanol / self.__valorLitro[self.__tipoCombustivel[2]]
        if somar > self.__quantidadeCombustivel[self.__tipoCombustivel[2]]:
            print("Não há combustível suficiente para abastecer!")
        else:
            self.__quantidadeCombustivel[self.__tipoCombustivel[2]] = self.__quantidadeCombustivel[self.__tipoCombustivel[2]] - somar
            print(f"Você abasteceu {somar} litros de etanol")
            print(f"O valor a ser pago é: {valorAbastecerEtanol}\n")
            pagar = float(input("Efetue o pagamento: R$"))
            if pagar < valorAbastecerEtanol:
                print("Valor insuficiente!")
            else:
                print(f"Seu troco é: {pagar - valorAbastecerEtanol}")

        return self.__quantidadeCombustivel[self.__tipoCombustivel[2]]

    def abastecerValorDiesel(self):
        valorAbastecerDiesel = float(input("Qual o valor deseja abastecer? "))
        somar = valorAbastecerDiesel / self.__valorLitro[self.__tipoCombustivel[3]]
        if somar > self.__quantidadeCombustivel[self.__tipoCombustivel[3]]:
            print("Não há combustível suficiente para abastecer!")
        else:
            self.__quantidadeCombustivel[self.__tipoCombustivel[3]] = self.__quantidadeCombustivel[self.__tipoCombustivel[3]] - somar
            print(f"Você abasteceu {somar} litros de diesel")
            print(f"O valor a ser pago é: {valorAbastecerDiesel}\n")
            pagar = float(input("Efetue o pagamento: R$"))
            if pagar < valorAbastecerDiesel:
                print("Valor insuficiente!")
            else:
                print(f"Seu troco é: {pagar - valorAbastecerDiesel}")

        return self.__quantidadeCombustivel[self.__tipoCombustivel[3]]
    def combustivelGasolina(self):
        quantidadeGasolina = int(input("Quantos litros de gasolina deseja? "))
        if quantidadeGasolina > self.__quantidadeCombustivel[self.__tipoCombustivel[1]]:
            print("Não há combustível suficiente para abastecer!")
        else:
            quantidadeGasolina = self.__quantidadeCombustivel[self.__tipoCombustivel[1]] - quantidadeGasolina
            print(f"Você abasteceu {quantidadeGasolina} litros de gasolina")
            soma = quantidadeGasolina * self.__valorLitro[self.__tipoCombustivel[1]]
            print(f"O valor a ser pago é: {quantidadeGasolina * self.__valorLitro[self.__tipoCombustivel[1]]}\n")
            pagar = float(input("Efetue o pagamento: R$"))
            if pagar < soma:
                print("Valor insuficiente!")
            else:
                print(f"Seu troco é: {pagar - soma}")

        return self.__quantidadeCombustivel[self.__tipoCombustivel[1]]

    def combustivelEtanol(self):
        quantidadeEtanol = int(input("Quantos litros de etanol deseja? "))
        if quantidadeEtanol > self.__quantidadeCombustivel[self.__tipoCombustivel[2]]:
            print("Não há combustível suficiente para abastecer!")
        else:
            quantidadeEtanol = self.__quantidadeCombustivel[self.__tipoCombustivel[2]] - quantidadeEtanol
            print(f"Você abasteceu {quantidadeEtanol} litros de etanol")
            soma = quantidadeEtanol * self.__valorLitro[self.__tipoCombustivel[2]]
            print(f"O valor a ser pago é: {quantidadeEtanol * self.__valorLitro[self.__tipoCombustivel[2]]}\n")
            pagar = float(input("Efetue o pagamento: R$"))
            if pagar < soma:
                print("Valor insuficiente!")
            else:
                print(f"Seu troco é: {pagar - soma}")

        return self.__quantidadeCombustivel[self.__tipoCombustivel[2]]

    def combustivelDiesel(self):
        quantidadeDiesel = int(input("Quantos litros de diesel deseja? "))
        if quantidadeDiesel > self.__quantidadeCombustivel[self.__tipoCombustivel[3]]:
            print("Não há combustível suficiente para abastecer!")
        else:
            quantidadeDiesel = self.__quantidadeCombustivel[self.__tipoCombustivel[3]] - quantidadeDiesel
            print(f"Você abasteceu {quantidadeDiesel} litros de diesel")
            soma = quantidadeDiesel * self.__valorLitro[self.__tipoCombustivel[3]]
            print(f"O valor a ser pago é: {quantidadeDiesel * self.__valorLitro[self.__tipoCombustivel[3]]}\n")
            pagar = float(input("Efetue o pagamento: R$"))
            if pagar < soma:
                print("Valor insuficiente!")
            else:
                print(f"Seu troco é: {pagar - soma}")

        return self.__quantidadeCombustivel[self.__tipoCombustivel[3]]

    def alterarValorGasolina(self):
        novoValorGasolina = float(input("Qual o novo valor da gasolina? "))
        self.__valorLitro[self.__tipoCombustivel[1]] = novoValorGasolina
        return self.__valorLitro[self.__tipoCombustivel[1]]

    def alterarValorEtanol(self):
        novoValorEtanol = float(input("Qual o novo valor do etanol? "))
        self.__valorLitro[self.__tipoCombustivel[2]] = novoValorEtanol
        return self.__valorLitro[self.__tipoCombustivel[2]]

    def alterarValorDiesel(self):
        novoValorDiesel = float(input("Qual o novo valor do diesel? "))
        self.__valorLitro[self.__tipoCombustivel[3]] = novoValorDiesel
        return self.__valorLitro[self.__tipoCombustivel[3]]

    def alterarQuantidadeCombustivel(self):
        novaQuantidadeGasolina = int(input("Qual a nova quantidade de gasolina? "))
        self.__quantidadeCombustivel[self.__tipoCombustivel[1]] = novaQuantidadeGasolina
        return self.__quantidadeCombustivel[self.__tipoCombustivel[1]]

    def alterarQuantidadeEtanol(self):
        novaQuantidadeEtanol = int(input("Qual a nova quantidade de etanol? "))
        self.__quantidadeCombustivel[self.__tipoCombustivel[2]] = novaQuantidadeEtanol
        return self.__quantidadeCombustivel[self.__tipoCombustivel[2]]

    def alterarQuantidadeDiesel(self):
        novaQuantidadeDiesel = int(input("Qual a nova quantidade de diesel? "))
        self.__quantidadeCombustivel[self.__tipoCombustivel[3]] = novaQuantidadeDiesel
        return self.__quantidadeCombustivel[self.__tipoCombustivel[3]]


    def menu(self):
        print("1 - Abastecer por valor\n2 - Abastecer por litro\n3 - Alterar valor\n4 - Alterar combustível\n5 - Alterar quantidade de combustível\n6 - Sair")
        opcao = int(input("Qual opção deseja? "))
        return opcao

    def main(self):
        opcao = 0
        while opcao != 6:
            opcao = self.menu()
            try:
                if opcao == 1:
                    tipoCombustivel = self.tipoCombustivel()
                    if tipoCombustivel == 1:
                        self.abastecerValorGasolina()
                    elif tipoCombustivel == 2:
                        self.abastecerValorEtanol()
                    elif tipoCombustivel == 3:
                        self.abastecerValorDiesel()
                    else:
                        print("Opção inválida")
                elif opcao == 2:
                    tipoCombustivel = self.tipoCombustivel()
                    if tipoCombustivel == 1:
                        self.combustivelGasolina()
                    elif tipoCombustivel == 2:
                        self.combustivelEtanol()
                    elif tipoCombustivel == 3:
                        self.combustivelDiesel()
                    else:
                        print("Opção inválida")
                elif opcao == 3:
                    tipoCombustivel = self.tipoCombustivel()
                    if tipoCombustivel == 1:
                        self.alterarValorGasolina()
                    elif tipoCombustivel == 2:
                        self.alterarValorEtanol()
                    elif tipoCombustivel == 3:
                        self.alterarValorDiesel()
                    else:
                        print("Opção inválida")
                elif opcao == 4:
                    tipoCombustivel = self.tipoCombustivel()
                    if tipoCombustivel == 1:
                        self.alterarQuantidadeCombustivel()
                    elif tipoCombustivel == 2:
                        self.alterarQuantidadeEtanol()
                    elif tipoCombustivel == 3:
                        self.alterarQuantidadeDiesel()
                    else:
                        print("Opção inválida")
                elif opcao == 5:
                    tipoCombustivel = self.tipoCombustivel()
                    if tipoCombustivel == 1:
                        self.alterarQuantidadeCombustivel()
                    elif tipoCombustivel == 2:
                        self.alterarQuantidadeEtanol()
                    elif tipoCombustivel == 3:
                        self.alterarQuantidadeDiesel()
                    else:
                        print("Opção inválida")
                elif opcao == 6:
                    break
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)
            opcao = self

classBombaCombustivel = BombaCombustivel()
classBombaCombustivel.main()



