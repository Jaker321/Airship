#####################################################################################################
#                                                                                                   # 
# Módulo Excel

'''
 A função Excel tem como objetivo armazenar todos os dados do programa.                          
'''
#                                                                                                   # 
#####################################################################################################

#####################################################################################################
# Aqui são armazenadas todos os dados.                                                              #
#####################################################################################################

#####################################################################################################
# Bibliotecas                                                                                       #
import pandas as pd                                                                                 #
#####################################################################################################

#####################################################################################################
#                                                                                                   #
# Funções                                                                                           #                                        

def planilha (salv_1,
              salv_2,
              salv_3,
              salv_4,
              salv_5,
              salv_6,
              salv_7,
              salv_8,
              Varia_Entrada_DOE,
              Varia_Entrada_Contour):

    Lista_DataFrame = []
    
    for ii in range (len(Varia_Entrada_DOE)):
        Lista_DataFrame.append (Varia_Entrada_DOE [ii])
        
    for jj in range (len(Varia_Entrada_Contour)):
        Lista_DataFrame.append (Varia_Entrada_Contour [jj])
    
    contador_1 = 0
    while (contador_1 <= (len(salv_1)-1)):
        Lista_1_DataFrame = (salv_1 [contador_1])
        Lista_DataFrame.append (Lista_1_DataFrame)
        contador_1 = contador_1 + 1
    
    contador_2 = 0
    while (contador_2 <= (len(salv_2)-1)): 
        Lista_2_DataFrame =  (salv_2 [contador_2])
        Lista_DataFrame.append (Lista_2_DataFrame)
        contador_2 = contador_2 + 1
        
    contador_3 = 0 #
    while (contador_3 <= (len(salv_3)-1)):
        Lista_3_DataFrame =  salv_3 [contador_3]
        Lista_DataFrame.append (Lista_3_DataFrame)
        contador_3 = contador_3 + 1

    contador_4 = 0
    while (contador_4 <= (len(salv_4)-1)):
        Lista_4_DataFrame =  salv_4 [contador_4]
        Lista_DataFrame.append (Lista_4_DataFrame)
        contador_4 = contador_4 + 1

    contador_5 = 0
    while (contador_5 <= (len(salv_5)-1)):
        Lista_5_DataFrame =  salv_5 [contador_5]
        Lista_DataFrame.append (Lista_5_DataFrame)
        contador_5 = contador_5 + 1

    contador_6 = 0 
    while (contador_6 <= (len(salv_6)-1)):
        Lista_6_DataFrame =  salv_6 [contador_6]
        Lista_DataFrame.append (Lista_6_DataFrame)
        contador_6 = contador_6 + 1  
 
    contador_7 = 0
    while (contador_7 <= (len(salv_7)-1)):
        Lista_7_DataFrame =  salv_7 [contador_7]
        Lista_DataFrame.append (Lista_7_DataFrame)
        contador_7 = contador_7 + 1

    contador_8 = 0
    while (contador_8 <= (len(salv_8)-1)):
        Lista_8_DataFrame =  salv_8 [contador_8]
        Lista_DataFrame.append (Lista_8_DataFrame)
        contador_8 = contador_8 + 1

    return (Lista_DataFrame)

def Banco_dados (salvar,data):
    
    if (salvar == 1): 
     
        dados = pd.DataFrame (data ,  columns = ['Range Maximo (Mn)',
                                                 'Densidade Energetica Bateria (Wh/Kg)',
                                                 'Altitude Cruzeiro (Ft)',
                                                 'Comprimento (Ft)',
                                                 'Forca elevacao helio (lb/ft³)',
                                                 
                                                 'Largura (ft)','Força flutuante (lb/ft³)',
                                                 'Velocidade maxima de cruzeiro (ft/s)',
                                                 'Range de cruzeiro (Mn)',
                                                 'Eficiencia',
                                                 
                                                 'Diametro do Envelope (Ft)',
                                                 'Volume (Ft³)',
                                                 'Area em Planta (Ft²)',
                                                 'Area Molhada (Ft)',
                                                 'AR do Corpo (Ad)',
                                                 'Fator do Corpo (Ad)',
                                                 'Centro de Gravidade (Ft)',
                                                 'Area em Planta da Aleta Vertical (Ft²)',
                                                 'Area em Planta da Aleta Horizontal (Ft²)',
                                                 'Area Molhada da Aleta Vertical (Ft²)', 
                                                 'Area Molhada da Aleta Horizontal (Ft²)',
                                                 'Soma Area molhada das aletas (Ft²)',
                                                 'Fator das Aletas (Ad)',
                                                 'Corda Media Aleta Vertical (Ft)',
                                                 'Corda Media Aleta Horizontal (Ft)', 
                                                 'Corda Ponta da Aleta Vertical (Ft)',
                                                 'Corda Ponta da Aleta Horizontal (Ft)', 
                                                 'Envergadura Aleta Vertical (Ft)',
                                                 'Envergadura Aleta Horizontal (Ft)',
                                                 'Volume da Gondola (Ft³)',
                                                 
                                                 'Altitude de Cruzeiro (M)',
                                                 'Densidade Ar',
                                                 'Reynolds do Envelope (Ad)',
                                                 'Coef. de Friccao do Envelope (Ad)',
                                                 'Q_Corpo (Lb/Ft²)',
                                                 'Reynolds da Aleta Vertical (Ad)',
                                                 'Reynolds da Aleta Horizontal (Ad)',
                                                 'Coef. de Friccao da Aleta Vertical (Ad)',
                                                 'Coef. de Friccao da Aleta Horizontal (Ad)',
                                                 'Densidade Terra (Slug/Ft³)',
                                                 'Gravidade de Cruzeiro (Ft²)',
                                                 'Gravidade da Terra (Ft/S²)',
                                                 'Q_Max (Lb/Ft²)',
                                                 'Arquimedes (Lb)',
                                                 
                                                 'Coef. Arrasto Corpo (Ad)',
                                                 'Coef. Arrasto Aleta Vertical (Ad)', 
                                                 'Coef. Arrasto Aleta Horizontal (Ad)',
                                                 'Coef. Arrasto Aletas (Ad)',
                                                 'Coef. Arrasto Gondola (Ad)', 
                                                 'Coef. Arrasto Cabos (Ad)',
                                                 'Coef. Arrasto Trem de Pouso (Ad)',
                                                 'Coef. Arrasto Interferencia (Ad)',
                                                 'Coef. Arrasto Resfriamento (Ad)',
                                                 'Coef Arrasto Monte (Ad)',
                                                 'Soma Especifica (Ad)',
                                                 'Coef. Arrasto Motor (Ad)',
                                                 'Soma dos Arrastos (Ad)',
                                                 'K_Coef_Area_S (Ad)',
                                                 'K_S (Ad)',
                                                 
                                                 'Hora de Voo (H)',
                                                 'Peso Sem Bateria (Lb)',
                                                 'WH1 (Lb)',
                                                 'Peso Bruto Decolagem (Lb)',
                                                 'Coef. Forca Aerodinamica (Ad)',
                                                 
                                                 'Arrasto (Lb)',
                                                 'BRto (Ad)', 
                                                 
                                                 'Coef. Friccao Envelope Taxiamento (Ad)',
                                                 'Coef. Friccao Aleta Vertical Taxiamento (Ad)', 
                                                 'Coef. Friccao Aleta Horizontal Taxiamento (Ad)',
                                                 'Arquimedes Taxiamento (Lb)', 
                                                 'Q_Max_T_S (Lb/Ft²)',
                                                 'Soma Arrasto Taxiamento (Ad)',
                                                 'Hora de Taxiamento (H)',
                                                 'Peso Bruto Taxiamento (Lb)', 
                                                 'Coef. Forca Aerodinamica Taxiamento (Ad)',
                                                 'Arrasto Taxiamento (Lb)',
                                                 'Potencia Motor Taxiamento (Hp)', 
                                                 'Peso Bateria Taxiamento (Lb)',
                                                 
                                                 'Potencia Motor Subida (Hp)',
                                                 'Potencia Watts Subida (W)', 
                                                 'Carga Bateria Subida (Wh)',
                                                 'Peso Bateria Subida (Lb)',
                                                 'Potencia Motor Descida (Hp)', 
                                                 'Potencia Watts Descida (W)',
                                                 'Carga Bateria Descida (Wh)',
                                                 'Peso Bateria Descida (Lb)', 
                                                 'Potencia Motor (Hp)',
                                                 'Potencia Motor Watts (W)',
                                                 'Carga Bateria (Wh)',
                                                 'Peso Bateria (Lb)',
                                                 'Cs (Ad)',
                                                 'J_S (Ad)',
                                                 'Diametro Helice (Ft)',
                                                 
                                                 'Pl (Lb/In²)',
                                                 'Carga_tecido_casco (Lb/In)',
                                                 'Densidade_fab_casco (Oz/Yd²)',
                                                 'Peso Envelope (Lb)',
                                                 'Densidade_fab_septum (Oz/Yd²)',
                                                 'Peso Septum (Lb)',
                                                 'Peso Gondola (Lb)',
                                                 'W_ssf_S (Lb)',
                                                 'W_CS_S (Lb)',
                                                 'Peso Aletas (Lb)',
                                                 'Peso Atuadores (Lb)',
                                                 'Peso Motores (Lb)',
                                                 'Peso suporte Motor (Lb)',
                                                 'Peso Controle Motor (Lb)',
                                                 'Peso de Partida (Lb)',
                                                 'W_soma_motores_ace_S (Lb)',
                                                 'Peso Helice (Lb)',
                                                 'Peso Sistema Trem de Pouso (Lb)',
                                                 'W_vazio (Lb)',
                                                 'Peso Estrutura (Lb)',
                                                 'Peso Motor (Lb)',
                                                 'BR_decolagem (ad)',
                                                 'Carga Util (Lb)'])
        
        dados.to_excel ('Resultados.xls')
##                                                                                                 ##
#####################################################################################################