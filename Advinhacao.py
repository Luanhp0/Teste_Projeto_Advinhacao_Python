import random

print("Seja muito bem vindo ao Guess Number do Luan")
choise_number = input("Digite o numero testo do desafio: ")

if choise_number.isdigit():
    choise_number = int (choise_number)
else:
    print("Erro: valor informado nao e numerico. Favor execute novamente e informe um numero")
    quit()

random_number = random.randint(0, choise_number) 

n_choices = 0

while True:
    answer_user = input("Advinhe o numero")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado nao e numerico. Favor informe um numero")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou")
        break
    elif answer_user > random_number:
        print("Chutou alto, o numero randomico e menor que isso...")
    else:
        print("Chutou baixo, o numero randomico e meior que isso...") 

print("Numero de tentativas: " + str(n_choices))        

