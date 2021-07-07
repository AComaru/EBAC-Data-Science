#!/usr/bin/env python
# coding: utf-8

# ### 01 - Teste de gravidez
# Escreva uma célula com controle de fluxos que tem como premissa a existência das seguintes variáveis:
# 
# - ```sexo``` como ```str``` indicando os valores '**M**' para masculino e '**F**' para feminino  
# - ```beta_hcg``` que indica a quantidade do beta-HCG no sangue em mUI/mL.
# 
# A sua tarefa é escrever um código que imprima como resultado "indivíduo do sexo masculino" quando sexo = 'M', caso sexo = 'F', se o valor de beta-HCG for maior que 5, retorne "Positivo" indicando que a paciente está grávida, e retorne "Negativo" caso contrário.
# 
# Não mexa nos valores da variável ```sexo``` nem em ```beta_hcg```, e escreva um código que funcione para quaisquer valores possíveis de ambos: ```sexo``` = '**M**' ou '**F**' e ```beta_hcg``` assumindo valores inteiros positivos.

# In[32]:


sexo = 'F'
beta_hcg = 5

# seu código vem abaixo desta linha

if sexo == 'M':
    print('Indivíduo do sexo masculino.')
elif sexo == 'F':
    if beta_hcg > 5:
         gravidez = ('positivo')
    elif beta_hcg <= 5:
         gravidez = ('negativo')
    print('Indivíduo do sexo feminino ', end=(','))
    print('testou', gravidez, 'para exame de gravidez.')



# ### 02 - Renomeando variáveis
# 
# Vamos ver adiante que uma forma de renomear variáveis de um conjunto de dados é através de dicionários - o dicionário deve conter como chave o nome original, associando a cada chave um único valor (tipo *str*) que contenha o nome novo.
# 
# A sua tarefa é escrever um dicionário que possa ser utilizado para traduzir as variáveis ```name``` (nome), ```age``` (idade) e ```income``` (renda). Ou seja, esse dicionário deve relacionar as chaves *name, age* e *income* às suas respectivas traduções.

# In[33]:


dic_renomeacao = {'name': 'nome','age':'idade','income':'renda'}
dic_renomeacao


# ### 03 - É divisível?
# A sua tarefa é escrever um código que indique se um número ```N``` é divisível por um número P. Escreva um programa que faça essa verificação para quaisquer combinações de ```N``` e ```M``` e devolva uma mensagem indicativa no output.

# In[35]:


N = 42
M = 7

#Seu código
N / M


# ### 04 - Números primos
# > Um número **N** é primo se e somente se é divisível por 1, -1, por **N** e por -**N**.  
# 
# Escreva um script que verifica se ```N``` é um número primo, verificando se ```N``` é divisível por todos os números de ```1``` a ```N-1```. Você vai precisar usar alguma ferramenta de *loop* que você aprendeu para isto. No final, devolva uma mensagem no output indicando se o número é primo ou não.

# In[23]:


N = 47  #47 é o original


# seu código abaixo

resultado=[]
for numero in (range(1,N)): # Usei N se não 2 não dava resultado. 
    if ((N/numero)-int(N/numero)) == 0:
        resultado.append(N/numero)
        #print(len(resultado), end=' ')  # debug
        #print(resultado)                # debug
if len(resultado)>1:
    print(N," não é numero primo")
elif len(resultado)==1:
    print(N," é numero primo")
elif len(resultado)==0:
    print(N," não é numero primo") # Só para as excessões 1 e 0 não funciona com negativos


# ### 05 - Desafio
# O algorítmo do exercício anterior não é o mais eficiente. O que você pode fazer para deixá-lo mais eficiente? Ou seja, executar menos comparações, portanto consumir menos tempo.
# 1. Será que precisamos correr o loop até o final sempre?
# 2. Será que precisamos mesmo verificar **todos** os números?
# 3. Será que precisamos ir até N-1?
# 
# Essas perguntas levam ao tipo de pensamento voltado a deixar um algoritmo mais eficiente. Veja se você consegue melhorar o seu.

# In[26]:


N = 98        #98

# seu código aqui

resultado=[]
for numero in (range(1,N)): # Usei N se não 2 não dava resultado. 
    #print(numero, end=', ') #
    if ((N/numero)-int(N/numero)) == 0:
        resultado.append(N/numero)
        #print(len(resultado), end=' ')  # debug
        #print(resultado)                # debug
        if len(resultado)>1:
            break
if len(resultado)>1:
    print(N," não é numero primo")
elif len(resultado)==1:
    print(N," é numero primo")
elif len(resultado)==0:
    print(N," não é numero primo") # Só para as excessões 1 e 0 não funciona com negativos    


# ### 06 - Peso ideal 1
# O IMC (índice de massa corpórea) é um indicador de saúde mais bem aceito que o peso. Ele é calculado como:
# 
# $$ IMC = \dfrac{peso}{altura^2}$$
# 
# Segundo a OMS, valores *normais* são entre 18.5 e 24.9.
# 
# Sua tarefa é encontrar o ponto médio dessa faixa.

# In[27]:


imc_ideal = (18.5 + 24.9)/2
imc_ideal


# ### 07 - Peso ideal 2
# Recebendo um valor de altura, encontre o peso '*ideal*' dessa pessoa, que fornece o IMC encontrado acima

# In[83]:


altura = 1.70

# Seu código
peso_ideal = imc_ideal*(altura**2)
str(peso_ideal)[0:5]


# ### 08 - Peso ideal 3
# Dada uma lista contendo as alturas de pacientes, crie uma nova lista que contenha o peso '*ideal*' (que fornece o IMC calculado em **Peso ideal 1**) desses pacientes.

# In[81]:


lista_alturas = [1.95, 2.05, 1.70, 1.65]

lista_peso_ideal = []

# seu código
peso_0 = (str(imc_ideal*(lista_alturas [0])**2)[0:5])
peso_1 = (str(imc_ideal*(lista_alturas [1])**2)[0:5])
peso_2 = (str(imc_ideal*(lista_alturas [2])**2)[0:5])
peso_3 = (str(imc_ideal*(lista_alturas [3])**2)[0:5])
lista_peso_ideal.append(peso_0)
lista_peso_ideal.append(peso_1)
lista_peso_ideal.append(peso_2)
lista_peso_ideal.append(peso_3)

lista_peso_ideal


# ### 09 - Peso ideal 4
# Dada uma lista de tuplas - cada elemento da lista é uma tupla contendo altura e peso de um paciente - crie uma nova lista com o IMC desses pacientes.

# In[99]:


altura_peso = [(1.80, 90), (1.65, 75), (1.91, 70)]

imc = []

# seu código

#    peso/ altura**2

paciente_0 = (altura_peso[0])
paciente_1 = (altura_peso[1])
paciente_2 = (altura_peso[2])

imc_0 = (paciente_0[1]/(paciente_0[0]**2))
imc_1 = (paciente_1[1]/(paciente_1[0]**2))
imc_2 = (paciente_2[1]/(paciente_2[0]**2))

imc.append(str(imc_0)[0:5])
imc.append(str(imc_1)[0:5])
imc.append(str(imc_2)[0:5])

imc


# ### 10 - Peso ideal 5
# Dada uma lista de **listas** - cada elemento da lista é uma **lista** contendo altura e peso de um paciente, adicione mais um elemento à lista de cada paciente contendo o IMC do paciente. Verifique também se é 'baixo', 'normal' ou 'alto' segundo os padrões da OMS em que normal é entre 18.5 e 24.9.
# 
# Reflexão: por que no problema anterior temos que criar uma nova lista, e não podemos adicionar os dados de cada indivíduo à tupla?

# In[139]:


altura_peso = [[1.80, 90], [1.65, 75], [1.91, 70]]

# seu código

paciente_0 = (altura_peso[0])
paciente_1 = (altura_peso[1])
paciente_2 = (altura_peso[2])

altura_paciente_0 = paciente_0[0]
altura_paciente_1 = paciente_1[0]
altura_paciente_2 = paciente_2[0]
peso_paciente_0   = paciente_0[1]
peso_paciente_1   = paciente_1[1]
peso_paciente_2   = paciente_2[1]
imc_paciente_0    = (paciente_0[1]/(paciente_0[0]**2))
imc_paciente_1    = (paciente_1[1]/(paciente_1[0]**2))
imc_paciente_2    = (paciente_2[1]/(paciente_2[0]**2))

if imc_paciente_0 > 24.9:
    oms_paciente_0 = ('alto')
elif imc_paciente_0 < 18.5:
    oms_paciente_0 = ('baixo')
else:
    oms_paciente_0 = ('normal')
                        
if imc_paciente_1 > 24.9:
    oms_paciente_1 = ('alto')
elif imc_paciente_1 < 18.5:
    oms_paciente_1 = ('baixo')
else:
    oms_paciente_1 = ('normal')

if imc_paciente_2 > 24.9:
    oms_paciente_2 = ('alto')
elif imc_paciente_2 < 18.5:
    oms_paciente_2 = ('baixo')
else:
    oms_paciente_2 = ('normal')


paciente_0 =[]
paciente_1 =[]
paciente_2 =[]

paciente_0.append(altura_paciente_0)
paciente_0.append(peso_paciente_0)
paciente_0.append(imc_paciente_0)
paciente_0.append(oms_paciente_0)

paciente_1.append(altura_paciente_1)
paciente_1.append(peso_paciente_1)
paciente_1.append(imc_paciente_1)
paciente_1.append(oms_paciente_1)

paciente_2.append(altura_paciente_2)
paciente_2.append(peso_paciente_2)
paciente_2.append(imc_paciente_2)
paciente_2.append(oms_paciente_2)

altura_peso=[]
altura_peso.append(paciente_0)
altura_peso.append(paciente_1)
altura_peso.append(paciente_2)

# Referencia
#[[1.8, 90, 27.777777777777775, 'alto'],
# [1.65, 75, 27.548209366391188, 'alto'],
# [1.91, 70, 19.188070502453332, 'normal']]


altura_peso

