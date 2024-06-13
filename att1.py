"""
Desenvolva uma aplicação Python que utilize ao menos 2 coleções e funções, para que seja possível realizar o cadastro de veículos
em um estacionamento com o seguinte menu:

1 - Estacionar veículo

2 - Retirar veículo

3 - Veículos estacionados

4 - Está estacionado?

0 - Sair

Deve gravar a placa do veículo que será a chave, marca, modelo, cor e proprietário.
"""

# Dicionário para armazenar os veículos estacionados (placa como chave)
veiculos_estacionados = {}

def estacionar_veiculo():
# Nessa etapa pederemos  para o usuario informar a placa do veiculo
    placa = input("Digite a placa do veículo: ").upper()
    
# Nessa etapa verificaremos para ver se o veiculo ja foi estacionado
    if placa in veiculos_estacionados:
        print("Veículo já está estacionado.")
    else:
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        proprietario = input("Digite o nome do proprietário: ")

# Aora precisamos solicitar ao usuario informar os dados do veiculo em dicionario
        veiculos_estacionados[placa] = {
            "marca": marca,
            "modelo": modelo,
            "cor": cor,
            "proprietario": proprietario
        }
        print(f"Veículo {placa} estacionado com sucesso.")

def retirar_veiculo():
# Agora iremos por uma funcao para retirar um veículo do estacionamento
    placa = input("Digite a placa do veículo a ser retirado: ").upper()
    
 # agora verificamos para ver se o veiculo foi estacionado
    if placa in veiculos_estacionados:
        del veiculos_estacionados[placa]
        print(f"Veículo {placa} retirado com sucesso.")
    else:
        print("Veículo não encontrado no estacionamento.")

# Aqui faremos uma função para listar todos os veiculos que ja foram estacionados
def listar_veiculos_estacionados():
    if veiculos_estacionados:
        print("Veículos estacionados:")
        for placa, dados in veiculos_estacionados.items():
            print(f"Placa: {placa}, Marca: {dados['marca']}, Modelo: {dados['modelo']}, Cor: {dados['cor']}, Proprietário: {dados['proprietario']}")
    else:
        print("Nenhum veículo estacionado.")

def verificar_estacionamento():

    placa = input("Digite a placa do veículo: ").upper()
    
# Verificaremos para ver se o veículo está estacionado
    if placa in veiculos_estacionados:
        print(f"O veículo {placa} está estacionado.")
    else:
        print(f"O veículo {placa} não está estacionado.")

def main():
# Aqui irmeos fazer uma função principal que exibe o menu e captura a escolha do usuário"""
    while True:
        print("Menu do Estacionamento")
        print("1 - Estacionar veículo")
        print("2 - Retirar veículo")
        print("3 - Veículos estacionados")
        print("4 - Está estacionado?")
        print("0 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue
# Solicitaremos ao usuario informar uma opçao:

        if opcao == 1:
            estacionar_veiculo()
        elif opcao == 2:
            retirar_veiculo()
        elif opcao == 3:
            listar_veiculos_estacionados()
        elif opcao == 4:
            verificar_estacionamento()
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
