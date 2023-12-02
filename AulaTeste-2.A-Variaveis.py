"""
O conceito de variaveis a grosso modo é basicamente são espaços de alocamento de memoria

int float str bool

"""

print("Abaixo estaremos vendo como podemos atribuir valores as variaveis \n")

nome = "Matheus França" # Atribui a variavel  string "nome" o valor de "Matheus França"
idade = 30 # Atribui a varivel int (inteiro) o valor "30"

print("nome: ",nome,"\n","idade: ",idade)

# essa forma de passar os parametros esta correta
# mas deixa o codigo em certos casos confuso ou ate mesmo poluido

print("\n")

nome1= "Ricardo"
idade1= 22

print("Olá,meu nome é {} \nEu tenho {} Anos".format(nome1, idade1))

# forma Simplificada usando o .format que permite colocar as variaveis de uma
# vez no codigo inves de colocar string "valor" string "valor"

print("\n")

nome2= "Thimethios Pinto"
idade2= 18
sexo ="Masculino"
peso = 56.89

print(f"O jogador {nome2} meteu 45 repetições de movimentos pelvicos em três minutos em uma competiçao \n"
      f"Tendo apenas {idade2} de idade na categoria {sexo} tendo o peseo de {peso}")

# O terceiro exemplo estou usando o metodo F-string aonde ja atribuo o
# valor as variaveis de uma vez sem usar o .format que por sua vez facilita
# a manipulação dos dados para concatenar(juntar) com outros codigos dependo do projeto
# NÃO SIGA MEU EXEMPLO NA TERCEIRA SINTAXE FAZENDO UM CODIGO GRANDE DE MAIS
# NÃO TENHA MEDO DE QUEBRAR O CODIGO quando necessario

print("\n")

pi = 3.14
parte_inteira = int(pi)
print(f"O valor de pi é {pi}\n parte inteira de pi é {parte_inteira}")
print("\n")

PI = 3.14
print(f"Pi antes valia : {PI}\nE seu tipo é {type (PI)}")
PI = int(PI)
print(f"Agora pi vale : {PI}\nE seu tipo é {type(PI)}")
PI = str(PI)
print(f"pi agora é uma String, e seu tipo é {type(PI)}")
