import csv

#Trabalho prático de Introdução à Ciência da computação/ INE5201-07236 / Leonardo dias Gutterres

#É importante ressaltar que as ''amostras'' nestas anotações(e no código) são tratadas como listas, portanto sempre que a expressão ''lista de amostras''
#For utilizada, pode-se entender como''lista de listas'' ou ''matriz''.

#Etapa de registramento de funções
def tela_de_opcoes():  #Função para acessar a tela de opções. Será utilizada após o final de cada opção, exceto "FIM". Retorna resposta do Usuário
    print('Escolha uma opção: ')
    print(('1- Novo registro; 2 - N novos registros; 3 - Calcular propriedades; 4 - Gravar em arquivo; 5 - Carregar de arquivo; 6 - Visualizar registros: '))
    opcao = input(('Digite uma opção ou FIM para sair: '))
    if opcao == 'FIM': #Verifica se o usuário quer encerrar o programa
        return opcao
    else:
        opcao = int(opcao) #Converter para inteiro pois irei utilizar operadores de comparação para esta variável

    while opcao < 1 or opcao > 6: #Certificar de que o usuário digitará uma opção válida
        print()
        print('Você não digitou uma opção válida, por favor tente de novo')
        print('Escolha uma opção: ')
        print(('1- Novo registro; 2 - N novos registros; 3 - Calcular propriedades; 4 - Gravar em arquivo; 5 - Carregar de arquivo; 6 - Visualizar registros: '))
        opcao = input(('Digite uma opção ou FIM para sair: '))
        if opcao == 'FIM':
            return opcao
        else:
            opcao = int(opcao)

    return opcao

def registrar_amostras(lista_de_amostras): #Função para registrar amostras, que será utilizada nas opções 1 e 2. Não retorna nenhuma informação, mas modifica a lista de amostras
        amostra_atual = []
        
        num_ponto = int(input('Informe o número do ponto:(37, 38, 39 ou 62): '))
        while num_ponto != 62 and (num_ponto < 37 or num_ponto > 39): #Certifica de que o usuário digite um ponto válido
            print()
            num_ponto = int(input('Digite um ponto válido(37, 38, 39 ou 62): '))
            
        concentracao = int(input('Informe a concentração de E. coli: '))
        while concentracao < 0: #Certifica de que o usuário digite uma concentração válida
            print()
            print('A concentração deve ser um valor positivo.Por favor, digite novamente')
            concentracao = int(input('Informe a concentração de E. coli: '))
        
        amostra_atual.append(num_ponto)
        amostra_atual.append(concentracao)
        lista_de_amostras.append(amostra_atual) #Adiciona a amostra informada à lista total de amostras
        print()
        
#Início
resultado_tela = tela_de_opcoes()  #Variável que registra a opção escolhida pelo usuário na tela de opções
lista_de_amostras = [] #Lista contendo todas as amostras([ponto,concecntração])

while resultado_tela != 'FIM': #Verifica se o usuário quer encerrar o programa na tela inicial
    
    if resultado_tela == 1: #Novo Registro
        registrar_amostras(lista_de_amostras) #Chama a função para registrar amostras na lista utilizada como parâmetro
        
        resultado_tela = tela_de_opcoes() #Utiliza a função para armazenar a proxima opção do usuário na tela inicial

    elif resultado_tela == 2: #N novos registros
        continuar = 'NOT_OK' #Variável para verificar se o usuário quer continuar inserindo amostras
        
        while continuar != 'OK': #Verifica se o usuário quer continuar inserindo amostras
            registrar_amostras(lista_de_amostras) #Chama a função para registrar amostras na lista utilizada como parâmetro
            
            continuar = input('Pressione qualquer tecla para inserir mais um registro ou OK para retornar: ')
        
        resultado_tela = tela_de_opcoes() #Utiliza a função para armazenar a proxima opção do usuário na tela inicial
        
    elif resultado_tela == 3: #Calcular Propriedades
        
        #variáveis para guardar informações-chave
        maiorponto = 0 
        maior_concentracao = 0
        soma_concentracoes = 0
            
        for amostra in lista_de_amostras: #Loop que passa por todas as amostras e guarda a maior concentração na variável 'maior_concentracao'
            if amostra[1] > maior_concentracao: 
                maiorponto = amostra[0]
                maior_concentracao = amostra[1] #Loop também guarada o ponto contendo a amostra de maior concentração
            soma_concentracoes += amostra[1] #Guarda a soma das concentrações da lista de amostras que será utilizada na média
        
        media_concentracoes = soma_concentracoes / len(lista_de_amostras)
            
        print(f'Ponto com maior concentração de bactérias: {maiorponto}. Concentração: {maior_concentracao}')
        print(f'Média das concentrações de todas as amostras: {media_concentracoes:.2f}')
            
        print()
        resultado_tela = tela_de_opcoes() #Utiliza a função para armazenar a proxima opção do usuário na tela inicial
        
    elif resultado_tela == 4: #Gravar em Arquivo
        
        with open('amostras.csv', 'w', newline='') as dados_salvos: #Salva a lista total de amostras em um arquivo chamado "amostras.csv"
            escritor = csv.writer(dados_salvos)
            escritor.writerows(lista_de_amostras)
        
        print('Dados de amostras atuais salvos com sucesso.')
            
        print()
        resultado_tela = tela_de_opcoes() #Utiliza a função para armazenar a proxima opção do usuário na tela inicial
    
    elif resultado_tela == 5: #Carregar de Arquivo
        
        ler_arquivo = input('Digite o nome do arquivo CSV a ser lido(Exemplo: "arquivo.csv"): ')
        novas_amostras_int = [] #Lista vazia que posteriormente conterá as amostras recebidas convertidas em numeros inteiros

        with open(ler_arquivo, 'r') as arquivo_csv: #Recebe amostras em csv e converte para uma lista
            leitor = csv.reader(arquivo_csv)
            novas_amostras_str = list(leitor) #Armazena as amostras em uma lista de strings
                    
            for linha in novas_amostras_str: #Processo para converter a lista de strings em uma lista de inteiros
                nova_amostra = []
                for elemento in linha:
                    numero = int(elemento)
                    nova_amostra.append(numero)
                novas_amostras_int.append(nova_amostra) 
                    
                
            lista_de_amostras += novas_amostras_int #Registra as novas amostras recebidas na lista total de amostras

        print('Amostras adicionadas.')
        
        print()
        resultado_tela = tela_de_opcoes() #Utiliza a função para armazenar a proxima opção do usuário na tela inicial
    
    else: #Visualizar Registros
        print(f'Ponto Concentração')
        for elemento in lista_de_amostras: #Loop que passa por todas as amostras registradas
            print(f'{elemento[0]} {elemento[1]}') #Imprime a amostra atual do loop
        
        print()
        resultado_tela = tela_de_opcoes() #Utiliza a função para armazenar a proxima opção do usuário na tela inicial

print()
print('Programa Encerrado.') #Avisa o usuário de que o procrama encerrou