import random

#inicializar um vetor sorteio com 6 numeros
#inicializar um vetor aposta com 6 numeros
sorteio = [0,0,0,0,0,0]
aposta = [0,0,0,0,0,0]
indice = 0

#de forma didática vou criar um while somente para a aposta e outro para o sorteio
while indice < len(aposta):
    #criamos uma variável para receber o input do usuário
    num_aposta = int(input(f"Informe o {indice+1}° numero: "))
    #verificamos se esse número é valido no intervalo possível da mega sena
    if num_aposta < 1 or num_aposta > 60:
        print("Opção inválida.. informe novamente")
        continue
    #verificamos se esse número já está no vetor aposta ( in = pertence ao vetor ?)
    elif num_aposta in aposta:
        print("Esse número já foi apostado... Informe novamente")
        continue
    #Caso esteja tudo certo, colocamos o número no vetor e incrementamos o indice
    #Já aproveitamos esse loop para criar o vetor de sorteio
    else:
        aposta[indice] = num_aposta
        indice += 1

#zeramos o indice para iniciarmos o loop do sorteio
indice = 0
while indice < len(sorteio):
    num_sorteio = random.randint(1,60)
    #Aqui faço a verificação oposta do que feito no vetor aposta, para vocês verem outra forma
    #se o numero não estiver no vetor de sorteio, adicione, se não aponte erro
    if not num_sorteio in sorteio:
        sorteio[indice] = num_sorteio
        indice += 1
    else:
        print("Número já sorteado, repita sorteio...")
        continue

#Vamos fazer a verificação
indice = 0
acertos = 0
while indice < len(sorteio):
    if aposta[indice] in sorteio:
        acertos += 1
    indice += 1

print(f"Vetor sorteio: {sorteio}")
print(f"Vetor aposta: {aposta}")
print(f"Número de acertos: {acertos}")