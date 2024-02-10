import string
import random
print("    .-\"\"-.                                                                                         ")
print("   / .--. \\                                                                                         ")
print("  / /    \\ \\                                                                                       ")
print("  | |    | |        ___                 _              _                    _                        ")
print("  | |.-\"\"-.|       / __|___ _ _ __ _ __| |___ _ _   __| |___   ___ ___ _ _ | |_  __ _ ___          ")
print(" ///`.::::.`\\     | (_ / -_) '_/ _` / _` / _ \\ '_| / _` / -_) (_-</ -_) ' \\| ' \\/ _` (_-<        ")
print("||| ::/  \\:: ;     \\___\\___|_| \\__,_\\__,_\\___/_|   \\__,_\\___| /__/\\___|_||_|_||_\\__,_/__/  ")
print("||; ::\\__/:: ;                                                                                      ")
print(" \\\\  '::::' /                                                                                      ")
print("   `=':-..-'`                                                                                        ")

print("\n------------------------------------------------------------------------------------------+")
tamanho = int(input("Digite o tamanho da senha: "))
print("------------------------------------------------------------------------------------------+")
print('''Escolha os tipos de caracteres que deseja incluir em sua senha: 
[1] Letras
[2] Números
[3] Caracters especiais
[4] Sair''')
print("+------------------------------------------------------------------------------------------+")

caracteres = ""
 
while(True):
    opcoes = int(input("> "))
    if(opcoes == 1):
        caracteres += string.ascii_letters
    elif(opcoes == 2):
        caracteres += string.digits
    elif(opcoes == 3):
        caracteres += string.punctuation
    elif(opcoes == 4):
        break
    else:
        print("Escolha uma opção válida!")
 
senha = []
 
for i in range(tamanho):
    randomchar = random.choice(caracteres)
    senha.append(randomchar)

print("+------------------------------------------------------------------------------------------+")
print("A SENHA GERADA É: " + "".join(senha))
print("+------------------------------------------------------------------------------------------+")
