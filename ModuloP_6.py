#####################################################################################################
#                                                                                                   #
# ModuloP

'''
O MóduloP tem como objetivo printar os resultados no terminal.
'''
#                                                                                                   #
#####################################################################################################

#####################################################################################################
#                                                                                                   #
# Funções ------------------------------------------------------------------------------------------#

def plotagem_1 (Volume_S,
                Area_ref_S,
                Area_S,
                Soma_area_molhada_aletas_S,
                Volume_gondola_S):
    
    print ('\n')
    print ('Volume do envelope: {:.4f}'.format(Volume_S))
    print ('Área em planta do envelope: {:.4f}'.format(Area_ref_S))
    print ('Área molhada do envelope: {:.4f}'.format(Area_S))
    print ('Área Molhada das aletas: {:.4f}'.format(Soma_area_molhada_aletas_S))
    print ('Volume da Gôndola: {:.4f}'.format(Volume_gondola_S))
    
def plotagem_2 (Cf_envelope_S,
                Cf_aletaV_S,
                Cf_aletaH_S,
                q_corpo_S,
                q_max_S,
                FL_S):
    
    print ('\n')
    print ('Coeficiente de fricção do envelope: {:.6f}'.format(Cf_envelope_S))
    print ('Coeficiente de fricção da aleta vertical: {:.6f}'.format(Cf_aletaV_S))
    print ('Coeficiente de fricção da aleta horizontal: {:.6f}'.format(Cf_aletaH_S))
    print ('Pressão dinâmica: {:.4f}'.format(q_corpo_S))
    print ('Pressão dinâmica máxima: {:.4f}'.format(q_max_S))
    print ('Elevação flutuante do fluido de sustentação: {:.4f}'.format(FL_S))
    
def plotagem_3 (CD0_corpo_S,
                CD0_aletas_S,
                CD0_gondola_cabos_S,
                CD0_cabos_S,
                Soma_especifica,
                CD0_motor_S,
                Soma_arrasto_S,
                K_S):
    
    print ('\n')
    print ('Soma dos coeficientes de arrasto de levantamento zero: {:.4f}'.format(Soma_arrasto_S))
    
def plotagem_4 (WH1_S,
                W_bruto_decolagem_S,
                Hora_voo_S):
    
    print ('\n')
    print ('Hora de voo {:.4f}'.format(Hora_voo_S))
    print ('Landing heaviness (Wh1): {:.4f}'.format(WH1_S))
    print ('Peso bruto decolagem: {:.4f}'.format(W_bruto_decolagem_S))
    
def plotagem_5 (Arrasto_S,
                BRto_S):
    
    print ('\n')
    print ('Arrasto: {:.4f}'.format(Arrasto_S))
    print ('Taxa de empuxo na decolagem: {:.4f}'.format(BRto_S))
    
def plotagem_6 (Hora_Tax_S,
                W_bateria_T_S):
    
    print ('\n')
    print ('Hora Taxiamento: {:.4f}'.format(Hora_Tax_S))
    print ('Peso de Bateria Para Taxiamento: {:.4f}'.format(W_bateria_T_S))

def plotagem_7 (Potencia_motor_S,
                Potencia_motor_W_S,
                Dp_S,
                W_bateria_S):
    
    print ('\n')
    print ('Potencia Para Cada Motor: {:.4f}'.format(Potencia_motor_S))
    print ('Potencia em Watts: {:.4f}'.format(Potencia_motor_W_S))
    print ('Diamentro da Helice: {:.4f}'.format(Dp_S))
    print ('Peso da Bateria: {:.4f}'.format(W_bateria_S))
    
def plotagem_8 (W_vazio_S,
                Carga_paga_S,
                BR_decolagem_S) :
    
     print ('\n')
     print ('Peso Vazio: {:.4f}'.format(W_vazio_S))
     print ('Carga paga adicional: {:.4f}'.format(Carga_paga_S))
     print ('Razao de flutuabilidade (deve ser maior que 0.8) {:.4f}'.format(BR_decolagem_S))
