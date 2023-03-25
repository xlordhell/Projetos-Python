#Desenvolvido por LucasHenrique 
#Contato (84) 99813-0162) Whatsapp

print("Seja Bem Vindo ao Quiz")
answer_user = input("Quer começar? (S/N) ")

#verificando se a condição é verdadeira
if answer_user != "S":
    quit()

score = 0


print("começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n)")
answer_1 = input("resposta: ")

#se estiver certo vai mostrar na tela
if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual o nome do protagonista do GTA San andreas ? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n)")
answer_2 = input("resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Quem descobriu o Brasil? \n (A) Pedro Alvares Cabral \n (B) Santos Dumont \n (C) Os Indios \n (D) Os americanos \n)")
answer_3 = input("resposta: ")

if answer_3 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual o nome do atual presidente do brasil? \n (A) Luiz inacio Lula \n (B) Jair Bolsonaro \n (C) Marina Silva \n (D) Haddad \n)")
answer_4 = input("resposta: ")

if answer_4 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Quem foi o primeiro homem a pisar na lua? \n (A) Neil Armstrong \n (B) Luis silva \n (C) Dom pedro 1° \n (D) Carlos pontes \n)")
answer_5 = input("resposta: ")

if answer_5 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")
print(f"Quiz acabou... Pontuação: {score}/5")