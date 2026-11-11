# IF E ELSE ELIF

# pedra papel e tesoura ....

import random

opcoes_maquina  =  ['pedra','papel','tesoura']


pontos_maquina =  0
pontos_usuario = 0


for n in range(4):
    escolha_usuario = input(f'Escolha {opcoes_maquina} >>')
    escolha_maquina = random.choice(opcoes_maquina)

    if escolha_maquina == escolha_usuario:
        print('EMPATE...')
        print(f'''
            
            ESCOLHA DA MÁQUINA:  {escolha_maquina}
            ESCOLHA DO USUÁRIO:  {escolha_usuario}
          

         ''')
        
    elif escolha_maquina == 'pedra' and escolha_usuario == 'tesoura':
        print('Máquina ganhou')
        pontos_maquina  =  pontos_maquina + 1
        print(f'''
            
            ESCOLHA DA MÁQUINA:  {escolha_maquina}
            ESCOLHA DO USUÁRIO:  {escolha_usuario}
          

         ''')    
    elif escolha_maquina == 'tesoura' and escolha_usuario == 'papel':
        print('Máquina ganhou')
        pontos_maquina  =  pontos_maquina + 1
        print(f'''
            
            ESCOLHA DA MÁQUINA:  {escolha_maquina}
            ESCOLHA DO USUÁRIO:  {escolha_usuario}
          

         ''')    
    elif escolha_maquina == 'papel' and escolha_usuario == 'pedra':
        print('Máquina ganhou')
        pontos_maquina  =  pontos_maquina + 1
        print(f'''
            
            ESCOLHA DA MÁQUINA:  {escolha_maquina}
            ESCOLHA DO USUÁRIO:  {escolha_usuario}
          

         ''')    
    else:
        print('USUÁRIO  VENCEU!!')
        pontos_usuario  = pontos_usuario + 1
        print(f'''
            
            ESCOLHA DA MÁQUINA:  {escolha_maquina}
            ESCOLHA DO USUÁRIO:  {escolha_usuario}
          

         ''')    

print('Usuário: ', pontos_usuario)
print('Máquina: ', pontos_maquina)
    

