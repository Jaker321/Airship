#---------------------------------------------------------------------------------------------------#
'''
Projeto - Estudo de viabilidade de uso de aeróstatos para transporte de carga. - IC CNPq.
 

Bolsista - Bruno da Silva Almeida - IFSP/SJC  # Orientador - DR. Ney Rafael - ITA.
'''
#---------------------------------------------------------------------------------------------------#
'''
"Não tenha medo de errar, tenha medo de dessistir - Lagum"
'''
#---------------------------------------------------------------------------------------------------#

# Quantidade de análises que o programa deve realizar.
Quant_Analise = 19

# Escolha de salvar ou não salvar os valores analisados no Excel (colocar s (sim) ou n (não)).
Salvar = 's' 

# Escolha de printar ou não printar os resultados das variáveis no terminal da IDE (colocar s (sim) ou n (não)).
Plotar = 'n' 

# Escolha de mostrar as análises em um DOE (Design of Experiments que nos motra uma visão macro dos resultados) (colocar s (sim) ou n (não)).
Plotar_DOE = 'n' 

# Escolha de mostrar as análises em um gráfico de nível (Contour) (colocar s (sim) ou n (não)).
Plotar_graf = 'n'

# Escolha de mostrar uma visão 3D da aeronave (Estrutura) (colocar s (sim) ou n (não)).
Plotar_imag = 'n' 

#####################################################################################################
'''
 O programa foi feito para fazer análises de dirigíveis para o transporte de carga, usando diferen-
tes parâmetros de entrada tendo como objetivo realizar equações de múltiplas áreas disciplinares
relacionadas ao desenvolvimento de um dirigivel, com o foco de entregar aos usuários análises de
importante relevância para o planejamento e pesquisa de dirigíveis.   
'''                                                                                                                
#####################################################################################################

#####################################################################################################

# Aqui são colocados todos os parâmetros de entrada para as análises do programa.                               

#####################################################################################################

#####################################################################################################

# Bibliotecas                                                                                       
import numpy as np                                                                                 
import random 
                                                                                     
## Módulos
                                                                                         
import Funcao_2                                                                                      
import Excel_4                                                                                     
import Grafico_5 
                                                                                    
#####################################################################################################

#####################################################################################################
'''
 Variaveis importantes para o while e analises funcionarem corretamente: (Não mexer)                
                                                                                                 
 A variavel contador está relacionada ao número de voltas em que o while vai se repetir  para   
que a condição total de voltas se complete, portanto, após a primeira volta, no final do programa, 
é somada uma unidade ao contador com o intuito de criação de um "range" para a atuação do whi- 
le. 
''' 
                                                                                           
contador = 0     
                                                                                  
'''                                                                                          
 A variável contador_1 é usada para que o programa possa alterar a linha no Excel onde o dado da 
análise gerada a partir do programa possa ser armazenado.   
'''  
                                 
contador_1 = 0                                                                                     

'''                                                                                                              
 A variavel voltas está relacionada a quantidade de análises em que o programa deve realizar,   
sendo muito prático apenas quando o desejo do usuário é de armazenar todos os resultados no    
Excel, pois se relacionarmos a uma grande quantidade de análises e não armazenarmos, o progra- 
ma vai realizar trabalho repetitivo apenas para uma analise (que não é viavel).                  
 Uso: ao atribuirmos 99 Análises, devemos contar o numero 0, com isso, teremos 100 análises para 
a variável Quant_Analise = 99.   
'''
                                                                
voltas = Quant_Analise                                                                             

'''                                                                                              
 A variável salvar tem o objetivo de controlar o armazenamento do Excel, deixando sobre o contro-
le dos usuários o armazenamento dos dados.                                                
 Uso: Usar na variavel Salvar 'S' ou 's' para armazenar, usar na variavel Salvar 'N' ou 'n' para 
nao armazenar.                                                                                  
'''
                                                                                                                       
if ((Salvar == 'S' or 's') or (Salvar == 'N' or 'n')):                                             
    if (Salvar == 'S' or Salvar == 's'):                                                           
        salvar = 1                                                                                 
    if (Salvar == 'N' or Salvar == 'n'):                                                           
        salvar = 0                                                                                 

'''                                                                                                 
 A variavel Plotar tem o objetivo de printar os valores analisados para os usuarios.               
 Uso: Usar na variável Plotar 'S' ou 's' para plotar os prints, Usar na variavel Plotar 'N' ou   
'n' para não plotar.                                                                            
'''
                                                                                                
if ((Plotar == 'S' or 's') or (Plotar == 'N' or 'n')):                                             
    if (Plotar == 'S' or Plotar == 's'):                                                           
        plot = 1                                                                                   
    if (Plotar == 'N' or Plotar == 'n'):                                                           
        plot = 0                                                                                   

'''                                                                                                
 A variável Plotar_graf tem o objetivo de plotar diferentes gráficos de volume (Contour), para que
o usuário possa utilizar os resultados para realizar análises de desempenho de diferentes aeronaves. 
 Uso: Usar na variável Plotar 'S' ou 's' para plotar os graficos, Usar na variavel Plotar_graf   
'N' ou 'n' para não plotar.                                                                     
'''
                                                                                                 
if ((Plotar_graf == 'S' or 's') or (Plotar_graf == 'N' or 'n')):                                   
    if (Plotar_graf == 'S' or Plotar_graf == 's'):                                                 
        plot_1 = 1                                                                                 
    if (Plotar_graf == 'N' or Plotar_graf == 'n'):                                                 
        plot_1 = 0                                                                                 

'''                                                                                                   
 A variável Plotar_imag tem o objetivo de plotar como o dirigível ficara com as dimensões adotadas
no código (apenas representação de posicionamento das aletas em relação ao envelope).     
 Uso: Usar na variavel Plotar 'S' ou 's' para plotar a imagem, Usar na variavel Plotar_imag  'N' 
ou 'n' para não plotar.                                                                         
'''
                                                                                         
if ((Plotar_imag == 'S' or 's') or (Plotar_imag == 'N' or 'n')):                                   
    if (Plotar_imag == 'S' or Plotar_imag == 's'):                                                 
        plot_2 = 1                                                                                 
    if (Plotar_imag == 'N' or Plotar_imag == 'n'):                                                 
        plot_2 = 0  
                                                                               
'''                                                                                                
 A variável Plotar_DOE tem o objetivo de plotar todas as variáveis selecionadas de uma só vez,   
dando ao usuário uma visão macro de todo o programa.                                            
'''

if ((Plotar_DOE == 'S' or Plotar_DOE == 's') or (Plotar_DOE == 'N' or Plotar_DOE == 'n')):                                                                             
    if (Plotar_DOE == 'S' or Plotar_DOE == 's'):                                                   
        plot_3 = 1                                                                                 
    if (Plotar_DOE == 'N' or Plotar_DOE == 'n'):                                                   
        plot_3 = 0 
#                                                                                                   #                                                                                
#####################################################################################################

while (contador <= voltas):
    
#####################################################################################################
# Variável importante para o armazenamento funcionar corretamente. (Nao mexer)                      #
    linha_excel = contador_1                                                                       
                                                                                                
    if (contador_1 <= 0):                                                                                                                                                               
        contador_1 = contador_1 + 1  
#                                                                                                   #                                                                
#####################################################################################################

#####################################################################################################
# Entrada de Variaveis                                                                              #
    print (contador,' - Analise')
    
    '''
    Valores atribuídos as variáveis presentes no programa foram todos retirados do livro fundamentals
    of Aircraft and Airship - Volume 2.
    '''
      
# Envelope -----------------------------------------------------------------------------------------#                                 
    
    # Comprimento do envelope (dirigível) - Pés.
    Comprimento = 312.6#np.random.randint (200,400, size = 1) [0] #312.6
    
    # Altura do envelope (dirigível) - Pés.
    Altura = Comprimento/4 #78.2
    
    # Largura do envelope (dirigível) - Pés.
    Largura = Comprimento/4 #78.2
    
    # NL depende da configuração de lóbulos do dirigí­vel e é determinado impiricamente - Adimensional. 
    '''
    Referência: Livro - Fundamentals of Aircraft and Airship Design (Volume 2) - página 66.
    1 lóbulo - NL = 2
    2 lóbulos - NL = 2.25
    3 lóbulos - NL = 2.4
    4 lóbulos - NL = 2.5
    5 lóbulos - NL = 2.54
    '''
    NL = 2 

# Aletas -------------------------------------------------------------------------------------------#                                   

    # Braço de momento sobre a cauda (Vertical e horizontal) - Adimensional.
    M_vertical_horizontal = 0.38
    
    # Proporção entre a raiz e a ponta da cauda (razão de afunilamento) - Adimensional.
    Lambda = 0.15
    
# Vertical -------------#

    # Coeficiente de volume da aleta vertical - Adimensional. 
    Coef_vertical = 0.059 
    
    # Tamanho da raiz da aleta vertical - Pés.
    CordaR_aletaV = Comprimento/7.4 #42.29
    
    # Proporção de espessura da raiz da aleta  - Adimensional.
    Espessura_raizV = 0.15 
    
    # Proporção de espessura da ponta da aleta - Adimensional.
    Espessura_pontaV = 0.07

# Horizontal -----------#

    # Coeficiente de volume da aleta horizontal - Adimensional.
    Coef_horizontal = 0.067
    
    # Tamanho da raiz da aleta horizontal - Pés.
    CordaR_aletaH = Comprimento/7.4 #42.29
    
    # Proporção de espessura da raiz da aleta - Adimensional.
    Espessura_raizH = 0.15 
    
    # Proporção de espessura da ponta da aleta - Adimensional.
    Espessura_pontaH = 0.07

# Gondola ------------------------------------------------------------------------------------------#
    
    # Comprimento da gôndola - Pés. 
    Comprimento_gondola = Comprimento / 11.8 # 26.5
    
    # Altura da gôndola - Pés.
    Altura_gondola = Comprimento / 15.6 # 5
    
    # Largura da gôndola - Pés.
    Largura_gondola = Comprimento / 8.2 # 9.5 .
    
# Fluido -------------------------------------------------------------------------------------------# 
    
    # Força de elevação gerada pelo hélio de 98% de pureza - Libra-força / Pés^3.
    FL_fluido = 0.0659 #np.linspace (0.03295,0.0659,voltas)  

# Carga e Peso -------------------------------------------------------------------------------------#
    
    # Fator de peso do dirígivel que é suportado pelo fluido de flutuabilidade (hélio)  - Adimensional.
    BRland = 0.90
    
    # Quantidade de motores usados na aeronave - Adimensional.
    Quantidade_motores = 2
    
    # Indica o peso do material da superfície externa da empenagem (dependendo do valor da pressão dinâmica)
    Fpsq = 1.0
    
    # Fator de seguranca - Adimensional.
    FS = 4 
    
    # Fator de fabricacao do envelope. - Adimensional.
    Fator_fabricacao = 1.2 
    
    # Fator que considera a presença de cabos estruturais externos na parte fixa da empenagem - Adimensional.
    Acessorios_fixacao = 1.26 

    # Fator de carga do septum - Adimensional.
    Carga_septum = 1.5 
    
    # Distância entre o controlador e o motor - Pés.
    Lec = 50
    
    # Quantidade de hélices - Adimensional.
    Numero_helices = 2
    
    # Adimensional.
    Kp = 31.92 
    
    # Quantidade de lâminas por hélice - Adimensional.
    Nbl = 3 

# Potencia -----------------------------------------------------------------------------------------#
    
    # Altitude de cruzeiro - Pés.
    Altitude_cruzeiro = 3000 #np.random.randint (3000,20000, size = 1) [0]
    
    # Velocidade de cruzeiro - Pés / Segundo.
    V_corpo = 64
    V_fluido = V_corpo 
    
    # Velocidadade máxima - Pés / Segundo.
    V_corpo_max = 76 #np.random.randint (70,150, size = 1) [0]
    
    # Range da missão - Milha Náutica.
    Range_cruzeiro = 100 #np.random.randint (50,600, size = 1) [0]
    
    # Tempo de espera da aeronave - Hora.
    Tempo_espera = 0.75

    # Velocidade vertical de subida - Pés / Segundo.
    V_vertical_S = 15 

    # Velocidade vertical de descida - Pés / Segundo.
    V_vertical_D = 15 

    # Velocidade da helice - Pés / Segundo.
    V_helice = 20 
    
    # Eficiência do transporte de energia - Adimensional.
    Eficiencia = 0.75 #np.linspace (0.60,0.75,voltas)#0.75

    #Eficiencia = random.choice (Eficiencia)
    
    # Bateria de Li-ion - Watt x Hora / Quilograma.
    u_bateria = 400 #np.random.randint (100,700, size = 1) [0] 

# Desempenho ---------------------------------------------------------------------------------------#
                      
    # Range de taxiamento - Milha náutica.
    Range_taxiamento = 2
    
    # Velocidade de levantamento - Pés / Segundo.
    V_Taxiamento = 38 
    
    # Soma dos ranges - Milha náutica.
    Range_Max_S = Range_cruzeiro + (Range_taxiamento*2)
    
##                                                                                                 ## 
#####################################################################################################

#####################################################################################################
# Seleção Variável de entrada do DOE                                                                #

    ''' 
 Aqui são colocadas todas as variáveis de entrada que serão atribuídas ao banco de dados para a plo-
tagem dos resultados dos gráficos.                                                           
    '''
    
    Varia_Entrada_DOE = [Range_Max_S,
                         u_bateria,
                         Altitude_cruzeiro,
                         Comprimento,
                         FL_fluido]
                                                                                                                                                    
# Seleção variável de entrada do Contour                                 
                                                                                                 
    Varia_Entrada_Contour = [Largura,
                             FL_fluido,
                             V_corpo_max,
                             Range_cruzeiro,
                             Eficiencia]
#                                                                                                   #
#####################################################################################################

#####################################################################################################
#                                                                                                   #
# Analise ------------------------------------------------------------------------------------------#
    '''                                                                                                
 Após a atribuição de valores nas variáveis, o programa as leva para a função de distribuição e as
encaminha para onde serão usadas para a realização dos cálculos de análises.                  
    '''                                                                                                                        
    
    Resultado_Mestre = Funcao_2.Mestra (Comprimento,
                                        Altura,
                                        Largura,
                                        NL,
                                        M_vertical_horizontal,
                                        Lambda,
                                        Coef_vertical,
                                        CordaR_aletaV,
                                        Espessura_raizV, 
                                        Espessura_pontaV,
                                        Coef_horizontal,
                                        CordaR_aletaH,
                                        Espessura_raizH,
                                        Espessura_pontaH,
                                        Comprimento_gondola,
                                        Altura_gondola,
                                        Largura_gondola,
                                        V_fluido,
                                        V_corpo,
                                        V_corpo_max,
                                        FL_fluido,
                                        Quantidade_motores,
                                        BRland,
                                        Eficiencia,
                                        V_Taxiamento,
                                        Range_cruzeiro,
                                        u_bateria,
                                        Range_taxiamento,
                                        V_vertical_S,
                                        V_vertical_D,
                                        Altitude_cruzeiro,
                                        V_helice,
                                        FS,
                                        Fator_fabricacao,
                                        Acessorios_fixacao,
                                        Carga_septum,
                                        Fpsq,
                                        Lec,
                                        Kp,
                                        Numero_helices,
                                        Nbl,
                                        Tempo_espera,
                                        plot)
 

    (Resultado_1,
     Resultado_2,
     Resultado_3,
     Resultado_4,
     Resultado_5,
     Resultado_6,
     Resultado_7,
     Resultado_8,
     salv_1,
     salv_2,
     salv_3,
     salv_4,
     salv_5,
     salv_6,
     salv_7,
     salv_8,
     pe_metro,
     kg_m3__slug_ft3,
     kg_ms__slug_fts,
     m_s2__ft_s2,
     ft_s__ft_h,
     mn) = Resultado_Mestre
    
#                                                                                                   #   
#####################################################################################################

#####################################################################################################
    ''' 
 Aqui fica as variáveis usadas para a plotagem 3D do dirigível. P.s: Usado apenas realizar análises
de dimensionamento da aeronave e posição das aletas.                                        
    '''
# Seleção de variáveis de entrada do plot_imag                             
                                                                                                
    Varia_Entrada_IMA = [Comprimento,
                         Largura,
                         Altura,
                         CordaR_aletaH,
                         CordaR_aletaV]
                                                                                           
# Seleção de variáveis de saida do plot_imag
                                                                                                 
    Varia_Saida_IMA = [Resultado_1 [6],
                       Resultado_1 [13],
                       Resultado_1 [14],
                       Resultado_1 [17],
                       Resultado_1 [18]]
                                                                                            
# Juntando variáveis de plot 3D da aeronave                           
                                                                                   
    Varia_IMA_Junt = [Varia_Entrada_IMA,Varia_Saida_IMA]
    Varia_IMA_Junt  = np.array (Varia_IMA_Junt )
#                                                                                                   #  
#####################################################################################################

#####################################################################################################
#                                                                                                   #
# Definicao dos graficos ---------------------------------------------------------------------------#

    '''                                                                                               
 Definir quais gráficos de contour devem ser plotados.                                             
 1 = plotar                                                                                       
 0 = nao plotar
    '''                                                                                  
                                                                                                  
    graf_1 = 0 # Diametro X Comprimento = Volume
    graf_2 = 0 # Comprimento X Diametro = AR
    graf_3 = 0 # Comprimento X Diametro = Arquimedes
    graf_4 = 0 # Diametro X Comprimento = Arrasto Parasita
    graf_5 = 0 # Diametro X Comprimento = Arrasto
    graf_6 = 0 # Volume X Altitude = Carga paga
    graf_7 = 0 # Volume X Range = Carga paga
    graf_8 = 0 # Volume X Densidade Energetica = Carga paga
    graf_9 = 0 # Comprimento X Altitude = Arrasto

    
# Contour ------------------------------------------------------------------------------------------#

    Varia_CON = [Comprimento,
                 Altura,
                 Largura,
                 NL,
                 M_vertical_horizontal,
                 Lambda,
                 Coef_vertical,
                 CordaR_aletaV,
                 Espessura_raizV,
                 Espessura_pontaV,
                 Coef_horizontal,
                 CordaR_aletaH,
                 Espessura_raizH,
                 Espessura_pontaH,
                 Comprimento_gondola,
                 Altura_gondola,
                 Largura_gondola,
                 V_fluido,
                 V_corpo,
                 V_corpo_max, 
                 FL_fluido,
                 Quantidade_motores,
                 BRland,
                 Eficiencia,
                 V_Taxiamento,
                 Range_cruzeiro,
                 u_bateria,
                 Range_taxiamento,
                 V_vertical_S,
                 V_vertical_D,
                 Altitude_cruzeiro,
                 V_helice,
                 FS,
                 Fator_fabricacao,
                 Acessorios_fixacao,
                 Carga_septum,
                 Fpsq,
                 Lec,
                 Kp,
                 Numero_helices,
                 Nbl,
                 Tempo_espera,
                 plot,
                 graf_1,
                 graf_2,
                 graf_3,
                 graf_4,
                 graf_5,
                 graf_6,
                 graf_7,
                 graf_8,
                 graf_9]

    Resultado_imagem = Grafico_5.imagem (Varia_IMA_Junt,
                                         Varia_CON,
                                         voltas,
                                         contador,
                                         plot_1,
                                         plot_2,
                                         plot_3,
                                         Quant_Analise)
    
#####################################################################################################
## Importante para o armazenamento funcionar corretamente (Nao mexer)                              ##
##                                                                                                 ##
    Excel_planilha = Excel_4.planilha (salv_1,
                                       salv_2,
                                       salv_3,
                                       salv_4,
                                       salv_5,
                                       salv_6,
                                       salv_7,
                                       salv_8,
                                       Varia_Entrada_DOE,
                                       Varia_Entrada_Contour)
##                                                                                                 ##
    (Lista_DataFrame) = Excel_planilha                                                             ## 
##                                                                                                 ## 
    if (linha_excel == 0):                                                                         ## 
        data = [Lista_DataFrame]                                                                   ##
        Lista_DataFrame = []                                                                       ##
##                                                                                                 ##
    if (linha_excel == 1) :                                                                        ##     
        data_1 = Lista_DataFrame                                                                   ##
        Lista_DataFrame = []                                                                       ##
        data.append (data_1)                                                                       ##  
##                                                                                                 ##    
    Banco_dados = Excel_4.Banco_dados (salvar,data)                                                  ##
##                                                                                                 ##
#####################################################################################################
##                                                                                                 ## 
    contador = contador + 1                                                                         ##  
##                                                                                                 ##
#####################################################################################################
    