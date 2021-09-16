#####################################################################################################
#                                                                                                   #
# Modulo 

'''                                                                                               
 O módulo tem como objetivo agrupar todas os cálculos do programa.                                                                   
'''
#                                                                                                   #
#####################################################################################################

#####################################################################################################
# Bibliotecas                                                                                       #
import numpy as np                                                                                  
import ambiance as am                                                                              
#####################################################################################################                                                                     

#####################################################################################################
#                                                                                                   #
# Funções ------------------------------------------------------------------------------------------#                                                                                                
                                                                                                                                                                  
def geometria (Comprimento,
               Altura,
               Largura,
               M_vertical_horizontal,
               Lambda,
               Coef_vertical,
               CordaR_aletaV,
               Espessura_raizV,
               Espessura_pontaV,
               Coef_horizontal,
               Espessura_raizH,
               Espessura_pontaH,
               CordaR_aletaH,
               Comprimento_gondola,
               Altura_gondola,
               Largura_gondola):
    
    '''
    Comprimento - Comprimento do envelope (dirigível) - Pés.
    Altura - Altura do envelope (dirigível) - Pés.
    Largura - Largura do envelope (dirigível) - Pés.
    M_vertical_horizontal - Braço de momento sobre a cauda (Vertical e horizontal) - Adimensional.
    Lambda - Proporção entre a raiz e a ponta da cauda (razão de afunilamento) - Adimensional.
    Coef_vertical - Coeficiente de volume da aleta vertical - Adimensional. 
    Espessura_raizV -  Proporção de espessura da raiz da aleta  - Adimensional.
    Espessura_pontaV - Proporção de espessura da ponta da aleta - Adimensional.
    Coef_horizontal - Coeficiente de volume da aleta horizontal - Adimensional.
    Espessura_raizH - Proporção de espessura da raiz da aleta - Adimensional.
    Espessura_pontaH - Proporção de espessura da ponta da aleta - Adimensional.
    Comprimento_gondola - Comprimento da gôndola - Pés. 
    Altura_gondola - Altura da gôndola - Pés. 
    Largura_gondola - Largura da gôndola - Pés.
    '''
    
# Envelope -----------------------------------------------------------------------------------------#
    
    # Cálculo de diâmentro do envelope - Pés.
    Diametro = np.sqrt (Altura*Largura)
    
    # Cálculo de alongamento (AR) - Adimensional.
    AR_corpo_S = (4*Diametro)/(np.pi*Comprimento)

    # Cálculo de volume do envelope - Pés^3.
    Volume_S = (4*(np.pi*Comprimento*Largura*Altura)/3/8)

    # Cálculo de área em planta do envelope - Pés^2.
    Area_ref_S = Volume_S ** (2/3)

    # Cálculo de área molhada do envelope - Pés^2.
    Area_S = 4*np.pi*np.power((np.power(Comprimento/2,1.6075)*np.power(Largura/2,1.6075)+np.power(Comprimento/2,1.6075)*np.power(Altura/2,1.6075)+np.power(Largura/2,1.6075)*np.power(Altura/2,1.6075))/3,1/1.6075)
    
    # Cálculo de fator de forma do dirigi­vel - Adimensional.
    F_corpo_S = (1+1.5/((Comprimento/Diametro)**1.5)) + (7/(((Comprimento/Diametro))**3))

# Aletas -------------------------------------------------------------------------------------------#
    
    # Cálculo de distância do cg - Pés.
    Cg_S = Comprimento*M_vertical_horizontal

    # Calculo da área em planta da aleta vertical - Pés^2.
    AreaV_S = Coef_vertical*Comprimento*Area_ref_S/Cg_S
    
    # Cálculo da área em planta da aleta horizontal - Pes^2.
    AreaH_S = Coef_horizontal*Comprimento*Area_ref_S/Cg_S

    # Cálculo de área molhada da aleta vertical - Pés^2.
    Area_molhada_aletaV_S = 2*AreaV_S*(1+(Espessura_raizV/(4*(1+Lambda)))*(1+Lambda*(Espessura_raizV/Espessura_pontaV))) 

    # Cálculo de área molhada da aleta horizontal - Pés^2.
    Area_molhada_aletaH_S = 2*AreaH_S*(1+(Espessura_raizH/(4*(1+Lambda)))*(1+Lambda*(Espessura_raizH/Espessura_pontaH)))

    # Soma das áreas molhadas (aletas) - Pés^2.
    Soma_area_molhada_aletas_S = Area_molhada_aletaV_S + Area_molhada_aletaH_S

    # Cálculo de fator de forma das aletas - Adimensional.
    F_aleta_S = 1 + 1.2*(Lambda) + 100 * (Lambda)**4 
    
    # Cálculo de corda média da aleta vertical - Pés.
    CordaM_aletaV = ((2*CordaR_aletaV)/3) * ((1 + Lambda + Lambda**2) / (1 + Lambda))

    # Cálculo de corda média da aleta horizontal - Pés.
    CordaM_aletaH = ((2 * CordaR_aletaH) / 3) * ((1 + Lambda + Lambda**2) / (1 + Lambda))

    # Cálculo de corda da ponta da aleta vertical - Pés.
    CordaP_aletaV = Lambda * CordaR_aletaV

    # Cálculo de corda da ponta da aleta horizontal - Pés.
    CordaP_aletaH = Lambda * CordaR_aletaH

    # Calculo de envergadura da aleta vertical - Pés.
    envergaduraV_S = Area_molhada_aletaV_S / (CordaR_aletaV + CordaP_aletaV)

    # Calculo de envergadura da aleta horizontal - Pés.
    envergaduraH_S = Area_molhada_aletaH_S / (CordaR_aletaH + CordaP_aletaH)

# Gôndola ------------------------------------------------------------------------------------------#
    
    # Cálculo de volume da gôndola - Pés^3.
    Volume_gondola_S = Comprimento_gondola*Largura_gondola*Altura_gondola

    return (Diametro,
            Volume_S,
            Area_ref_S,
            Area_S,
            AR_corpo_S,
            F_corpo_S,
            Cg_S,
            AreaV_S,
            AreaH_S,
            Area_molhada_aletaV_S,
            Area_molhada_aletaH_S,
            Soma_area_molhada_aletas_S,
            F_aleta_S,
            CordaM_aletaV,
            CordaM_aletaH,
            CordaP_aletaV,
            CordaP_aletaH,
            envergaduraV_S,
            envergaduraH_S,
            Volume_gondola_S)

def escoamento_fluido (V_fluido,
                       Altitude_cruzeiro,
                       Comprimento,
                       V_corpo,
                       CordaM_aletaV,
                       CordaM_aletaH,
                       Volume_S,
                       V_corpo_max,
                       FL_fluido,
                       pe_metro,
                       kg_m3__slug_ft3,
                       kg_ms__slug_fts,
                       m_s2__ft_s2):
    
    '''
    V_fluido -  Velocidade de cruzeiro - Pés / Segundo.
    Altitude_cruzeiro - Altitude de cruzeiro - Pés.
    Comprimento - Comprimento do envelope (dirigível) - Pés.
    V_corpo - Velocidade de cruzeiro - Pés / Segundo.
    CordaM_aletaV - Cálculo de corda média da aleta vertical - Pés.
    CordaM_aletaH - Cálculo de corda média da aleta horizontal - Pés.
    Volume_S - Volume do envelope - unidade ft³.
    V_corpo_max - Velocidadade máxima - Pés / Segundo.
    FL_fluido - Força de elevação gerada pelo hélio de 98% de pureza - Libra-força / Pés^3.
    '''
    
    # Transformando a altitude de cruzeiro de pés para metro - Metro.
    Altitude_cruzeiro = Altitude_cruzeiro * pe_metro
    Atmosfera_cruzeiro = am.Atmosphere(Altitude_cruzeiro)

    # Cálculando a densidade atmosfética para a altitude - Lesma/Pés^3
    Densidade_ar = Atmosfera_cruzeiro.density * kg_m3__slug_ft3
    Densidade_ar = Densidade_ar[0]

    # Cálculando a viscodaide - Lesma/Pés*Segundo.
    Viscosidade_cruzeiro = Atmosfera_cruzeiro.dynamic_viscosity * kg_ms__slug_fts
    Viscosidade_cruzeiro = Viscosidade_cruzeiro[0]

    Atmosfera_terra = am.Atmosphere (0)
    
    # Densidade atmosferica para 0 Pés - Lesma/Pés^3.
    Densidade_terra = (Atmosfera_terra.density*kg_m3__slug_ft3)
    Densidade_terra = Densidade_terra [0]

# Envelope -----------------------------------------------------------------------------------------#
    
    # Cálculo de Reynolds do envelope - Adimensional. 
    Re_envelope_S = (Densidade_ar*V_fluido*Comprimento)/(Viscosidade_cruzeiro)

    # Cálculo de coeficiente de fricção do envelope - Adimensional.
    Cf_envelope_S = 0.455/(np.log10(Re_envelope_S))**2.58

    # Cálculo de pressão dinâmica. - Libra/Pés^2.
    q_corpo_S = Densidade_ar*(V_corpo**2)/2

# Aletas -------------------------------------------------------------------------------------------#
    
    # Cálculo de Reynolds da aleta vertical - Adimensional.
    Re_aletaV_S = (Densidade_ar*V_fluido*CordaM_aletaV)/Viscosidade_cruzeiro

    # Cálculo de Reynolds da aleta horizontal - Adimensional. 
    Re_aletaH_S = (Densidade_ar*V_fluido*CordaM_aletaH)/Viscosidade_cruzeiro

    # Cálculo do coeficiente de fricção da aleta vertical - Adimensional.
    Cf_aletaV_S = 0.455/(np.log10(Re_aletaV_S))**2.58 

    # Cálculo do coeficiente de fricção da aleta horizontal - Adimensional.
    Cf_aletaH_S = 0.455/(np.log10(Re_aletaH_S))**2.58 

# Fluido -------------------------------------------------------------------------------------------#
    
    # Aceleração da gravidade - Pés/Segundo^2.
    g_cruzeiro = Atmosfera_cruzeiro.grav_accel * m_s2__ft_s2
    g_cruzeiro = g_cruzeiro [0]

    # Aceleração da gravidade para 0 Pés - Pés/Segundo^2.
    g_terra = Atmosfera_terra.grav_accel * m_s2__ft_s2
    g_terra = g_terra [0]
    
    # Cálculo de elevação flutuante do fluido de sustentação - Libra.
    FL_S = FL_fluido*Volume_S*(Densidade_ar /Densidade_terra)

# Aerodinâmica -------------------------------------------------------------------------------------#
    
    # Cálculo de pressão dinâmica máxima - Libra/Pés^2.
    q_max_S = (Densidade_terra *V_corpo_max**2)/2

    return (Altitude_cruzeiro,
            Densidade_ar,
            Re_envelope_S, 
            Cf_envelope_S,
            q_corpo_S,
            Re_aletaV_S,
            Re_aletaH_S,
            Cf_aletaV_S,
            Cf_aletaH_S,
            Densidade_terra,
            g_cruzeiro,
            g_terra,
            q_max_S,
            FL_S)

def arrasto (F_corpo_S,
             Cf_envelope_S,
             Area_S,
             Area_ref_S,
             F_aleta_S,
             Volume_S,
             Quantidade_motores,
             Cf_aletaV_S,
             Area_molhada_aletaV_S,
             Cf_aletaH_S,
             Area_molhada_aletaH_S,
             AR_corpo_S,
             NL):
    
    '''
    F_corpo_S - Fator de forma do dirigi­vel - Adimensional.
    Cf_envelope_S - Coeficiente de fricção do envelope - Adimensional.
    Area_S - Área molhada do envelope - Pés^2.
    Area_ref_S - Área em planta do envelope - unidade ft².
    F_aleta_S - Fator de forma das aletas - Adimensional.
    Volume_S - Volume do envelope - Pés^3.
    Quantidade_motores - Quantidade de motores usados na aeronave - Adimensional.
    Cf_aletaV_S - Coeficiente de fricção da aleta vertical - Adimensional.
    Area_molhada_aletaV_S - Área molhada da aleta vertical - Pés^2.
    Cf_aletaH_S - Coeficiente de fricção da aleta horizontal - Adimensional.
    Area_molhada_aletaH_S - Area molhada da aleta horizontal - Pés^2.
    AR_corpo_S - Alongamento (AR) - Adimensional.
    NL - NL depende da configuração de lóbulos do dirigí­vel e é determinado impiricamente - Adimensional.
    '''
    
# Envelope -----------------------------------------------------------------------------------------#
    
    # Cálculo de coeficiente de arrasto de levantamento zero (corpo) - Adimensional.
    CD0_corpo_S = F_corpo_S*Cf_envelope_S*Area_S/Area_ref_S# Sem unidade

# Aletas -------------------------------------------------------------------------------------------#
    
    # Cálculo de coeficiente de arrasto de levantamento zero (aleta vertical) - Adimensional.
    CD0_aletasV_S = (F_aleta_S*Cf_aletaV_S*Area_molhada_aletaV_S)/Area_ref_S

    # Cálculo de coeficiente de arrasto de levantamento zero (aleta horizontal) - Adimensional.
    CD0_aletasH_S = (F_aleta_S*Cf_aletaH_S*Area_molhada_aletaH_S)/Area_ref_S

    # Cálculo de soma dos coeficientes de arrasto de levantamento zero (aletas) - Adimensional.
    CD0_aletas_S = CD0_aletasH_S + CD0_aletasV_S

# Gôndola ------------------------------------------------------------------------------------------#

    # Cálculo de coeficiente de arrasto de levantamento zero (gôndola e cabos) - Adimensional.
    CD0_gondola_cabos_S = (0.108*CD0_corpo_S*Area_ref_S+7.7)/Area_ref_S

    # Cálculo de coeficiente de arrasto de levantamento zero (cabos) - Adimensional.
    CD0_cabos_S = (9.7 * 10 ** -6 * Volume_S + 10.22) / Area_ref_S

# Partes especi­ficas -------------------------------------------------------------------------------#
    
    # Cálculo de coeficiente de arrasto de levantamento zero (trem de pouso) - Adimensional.
    CD0_trem_pouso_S = (1.76*10**-6*Volume_S+0.92)/Area_ref_S 

    # Cálculo de coeficiente de arrasto de levantamento zero (interferência) - Adimensional.
    CD0_interferencia_S = (4.78*10**-6*Volume_S)/Area_ref_S

    # Cálculo de coeficiente de arrasto de levantamento zero (resfriamento) - Adimensional.
    CD0_resfriamento_S = (Quantidade_motores)*(2*10**-6*Volume_S+4.1)/Area_ref_S

    # Cálculo de coeficiente de arrasto de levantamento zero (estabilizadores) - Adimensional.
    CD0_monte_S = (0.044*CD0_corpo_S*Area_ref_S+0.92)/Area_ref_S 

    # Cálculo de soma dos coeficientes de arrasto de levantamento zero (partes específicas) - Adimensional.
    Soma_especifica =  CD0_trem_pouso_S + CD0_interferencia_S + CD0_resfriamento_S + CD0_monte_S 

# Motor --------------------------------------------------------------------------------------------#
    
    # Cálculo de coeficiente de arrasto de levantamento zero (motor) - Adimensional.
    CD0_motor_S = Quantidade_motores*4.25/Area_ref_S 

    # Cálculo de soma dos coeficientes de arrasto de levantamento zero (todos) - Adimensional.
    Soma_arrasto_S = CD0_corpo_S + CD0_aletas_S + CD0_gondola_cabos_S + CD0_cabos_S + CD0_motor_S + Soma_especifica # Sem unidade

    # Cálculo do fator de arrasto devido ao levantamento - Adimensional.
    K_coef_area_S = -0.0145*(1/AR_corpo_S)**4+0.182*(1/AR_corpo_S)**3-0.514*(1/AR_corpo_S)**2+0.838*(1/AR_corpo_S)-0.053 #1.74 # Sem unidade

    # Cálculo do fator em relação ao plano de superfície do envelope - Adimensional.
    K_S = K_coef_area_S / NL 

    return (CD0_corpo_S,
            CD0_aletasV_S,
            CD0_aletasH_S,
            CD0_aletas_S,
            CD0_gondola_cabos_S,
            CD0_cabos_S,
            CD0_trem_pouso_S,
            CD0_interferencia_S,
            CD0_resfriamento_S,
            CD0_monte_S,
            Soma_especifica,
            CD0_motor_S,
            Soma_arrasto_S,
            K_coef_area_S,
            K_S)         
 
def peso (FL_S, BRland, Area_ref_S, V_corpo_max, Range_cruzeiro, q_max_S, ft_s__ft_h, mn):
    
    '''
     Range da missão - Milha Náutica.
     FL_S - Elevação flutuante do fluido de sustentação - Libra.
     BRland - Fator de peso do dirígivel que é suportado pelo fluido de flutuabilidade (hélio)  - Adimensional.
     Area_ref_S - Área em planta do envelope - Pés^2.
     V_corpo_max - Velocidadade máxima - Pés / Segundo.
     q_max_S - Pressão dinâmica máxima - Libra/Pés^2.
    '''
    
    # Cálculo de hora de voo - Hora.
    Hora_voo_S = Range_cruzeiro/((V_corpo_max * ft_s__ft_h)/ mn)

# Peso ---------------------------------------------------------------------------------------------#
    
    # Cálculo de peso zero bateria - Libra.
    W_zero_bateria_S = FL_S/BRland

    # Cálculo de landing heaviness (Wh1) - Libra. 
    WH1_S = W_zero_bateria_S - FL_S

    # Cálculo de peso bruto decolagem - Libra.
    W_bruto_decolagem_S = W_zero_bateria_S

    # Cálculo do coeficiente de forca aerodinamica - Adimensional.
    CL_potencia_max_S = (WH1_S/q_max_S)/Area_ref_S

    return (Hora_voo_S,
            W_zero_bateria_S,
            WH1_S,
            W_bruto_decolagem_S,
            CL_potencia_max_S)

def aerodinamica (Soma_arrasto_S,
                  K_S,
                  CL_potencia_max_S,
                  q_max_S,
                  Area_ref_S,
                  FL_S,
                  W_bruto_decolagem_S):
    
    '''
    Soma_arrasto_S - Soma dos coeficientes de arrasto de levantamento zero (todos) - Adimensional.
    K_S - Fator em relação ao plano de superfície do envelope - Adimensional. 
    CL_potencia_max_S - Coeficiente de forca aerodinamica - Adimensional.
    q_max_S - Pressão dinâmica máxima - Libra/Pés^2.
    Area_ref_S - Área em planta do envelope - Pés^2.
    FL_S - Elevação flutuante do fluido de sustentação - Libra.
    W_bruto_decolagem_S - Peso bruto decolagem - Libra.
    '''
    
    # Cálculo de arrasto - Libra.
    Arrasto_S = (Soma_arrasto_S + K_S * CL_potencia_max_S**2) * q_max_S * Area_ref_S

    # Cálculo de taxa de empuxo na decolagem - Adimensional. 
    BRto_S = FL_S/W_bruto_decolagem_S

    return (Arrasto_S,
            BRto_S)

def desempenho (Densidade_ar,
                V_fluido,
                Comprimento,
                CordaM_aletaV,
                CordaM_aletaH,
                FL_fluido,
                Volume_S,
                AR_corpo_S,
                V_corpo_max,
                F_corpo_S,
                Area_S,
                Area_ref_S,
                F_aleta_S,
                Area_molhada_aletaV_S,
                Area_molhada_aletaH_S,
                NL,
                BRland,
                Eficiencia,
                K_S,
                V_Taxiamento,
                Quantidade_motores,
                Range_taxiamento,
                u_bateria,
                Densidade_terra,
                V_helice,
                Altitude_cruzeiro,
                V_vertical_S,
                V_vertical_D,
                pe_metro,
                kg_m3__slug_ft3,
                kg_ms__slug_fts,
                m_s2__ft_s2,
                ft_s__ft_h,
                mn):
    
   '''
   Densidade_ar - Densidade atmosfética para a altitude - Lesma/Pés^3
   V_fluido - Velocidade de cruzeiro - Pés / Segundo.
   Comprimento - Comprimento do envelope (dirigível) - Pés.  
   CordaM_aletaV - Cálculo de corda média da aleta vertical - Pés. 
   CordaM_aletaH - Cálculo de corda média da aleta horizontal - Pés.
   FL_fluido - Força de elevação gerada pelo hélio de 98% de pureza - Libra-força / Pés^3.
   Volume_S - Volume do envelope - Pés^3.
   V_corpo_max - Velocidadade máxima - Pés / Segundo.
   F_corpo_S - Fator de forma do dirigi­vel - Adimensional.
   Area_S - Área molhada do envelope - Pés^2.
   Area_ref_S - Área em planta do envelope - Pés^2.
   F_aleta_S - Fator de forma das aletas - Adimensional.
   Area_molhada_aletaV_S - Área molhada da aleta vertical - Pés^2.
   Area_molhada_aletaH_S - Área molhada da aleta horizontal - Pés^2.
   BRland - Fator de peso do dirígivel que é suportado pelo fluido de flutuabilidade (hélio) - Adimensional.
   Eficiencia - Eficiência do transporte de energia - Adimensional.
   K_S - Fator em relação ao plano de superfície do envelope - Adimensional.
   V_Taxiamento - Velocidade de levantamento - Pés / Segundo
   Quantidade_motores - Quantidade de motores usados na aeronave - Adimensional.
   u_bateria - Bateria de Li-ion - Watt x Hora / Quilograma.
   '''
    
# Escoamento_fluido (Taxiamento) --------------------------------------------------------------------------------#
   
   Resultado_def_1 = escoamento_fluido (V_fluido,
                                        Altitude_cruzeiro,
                                        Comprimento,
                                        V_Taxiamento,
                                        CordaM_aletaV, 
                                        CordaM_aletaH,
                                        Volume_S,
                                        V_corpo_max,
                                        FL_fluido,
                                        pe_metro,
                                        kg_m3__slug_ft3,
                                        kg_ms__slug_fts,
                                        m_s2__ft_s2)
    
   # Cálculo de coeficiente de fricção do envelope - Adimensional.
   Cf_envelope_T_S = Resultado_def_1 [3]

   # Cálculo do coeficiente de fricção da aleta vertical - Adimensional.
   Cf_aletaV_T_S = Resultado_def_1 [7]

   # Cálculo do coeficiente de fricção da aleta horizontal - Adimensional.
   Cf_aletaH_T_S = Resultado_def_1 [8]
    
   # Cálculo de elevação flutuante do fluido de sustentação - Libra.
   FL_T_S = Resultado_def_1 [13]
    
   # Cálculo de pressão dinâmica máxima - Libra/Pés^2.
   q_max_T_S = Resultado_def_1 [12]
   
# Arrasto (Taxiamento) -----------------------------------------------------------------------------#
   
   Resultado_def_2 = arrasto (F_corpo_S,
                              Cf_envelope_T_S,
                              Area_S,
                              Area_ref_S,
                              F_aleta_S,
                              Volume_S,
                              Quantidade_motores,
                              Cf_aletaV_T_S,
                              Area_molhada_aletaV_S,
                              Cf_aletaH_T_S,
                              Area_molhada_aletaH_S,
                              AR_corpo_S,
                              NL)

   Soma_arrasto_T_S = Resultado_def_2 [12]
   
# Peso (Taxiamento) --------------------------------------------------------------------------------#
   
   Resultado_def_3 = peso (FL_T_S,
                           BRland,
                           Area_ref_S,
                           V_Taxiamento,
                           Range_taxiamento,
                           q_max_T_S,
                           ft_s__ft_h,
                           mn)
   
   # Cálculo de hora de voo - Hora.
   Hora_Tax_S = Resultado_def_3 [0]

   # Cálculo de peso bruto decolagem - Libra.
   W_bruto_T_S = Resultado_def_3 [3]

   # Cálculo do coeficiente de forca aerodinamica - Adimensional.
   CL_potencia_max_T_S = Resultado_def_3 [4]
   
# Aerodinâmica (Taxiamento) ------------------------------------------------------------------------#
   
   Resultado_def_4 = aerodinamica (Soma_arrasto_T_S,
                                   K_S,
                                   CL_potencia_max_T_S,
                                   q_max_T_S,
                                   Area_ref_S,
                                   FL_T_S,
                                   W_bruto_T_S)
   
   # Cálculo de arrasto - Libra.
   Arrasto_T_S = Resultado_def_4 [0]
   
# Bateria (Taxiamento) -----------------------------------------------------------------------------#

   W_bateria_T_S = 0
   Altitude_inicial = 0
   Sem_tempo_espera = 0
   
   Resultado_def_5 = potencia (V_Taxiamento,
                               Arrasto_T_S,
                               Eficiencia,
                               Quantidade_motores,
                               Hora_Tax_S,
                               u_bateria,
                               Sem_tempo_espera,
                               W_bateria_T_S,
                               Densidade_terra,
                               V_helice,
                               Altitude_inicial,
                               V_vertical_S,
                               V_vertical_D)
    
   # Cálculo de potência por motor - HorsePower.
   Potencia_motor_T_S = Resultado_def_5 [8]

   # Cálculo de peso das baterias - Libra.
   W_bateria_T_S = Resultado_def_5 [11]

   return (Cf_envelope_T_S,
           Cf_aletaV_T_S,
           Cf_aletaH_T_S,
           FL_T_S,
           q_max_T_S,
           Soma_arrasto_T_S,
           Hora_Tax_S,
           W_bruto_T_S,
           CL_potencia_max_T_S,
           Arrasto_T_S,
           Potencia_motor_T_S,
           W_bateria_T_S)

def potencia (V_corpo_max,
              Arrasto_S,
              Eficiencia,
              Quantidade_motores,
              Hora_voo_S,
              u_bateria,
              Tempo_espera,
              W_bateria_T_S,
              Densidade_terra,
              V_helice,
              Altitude_cruzeiro,
              V_vertical_S,
              V_vertical_D):
    
    '''
    Tempo_espera - Tempo de espera da aeronave - Hora.
    V_corpo_max - Velocidadade máxima - Pés / Segundo.
    Arrasto_S - Arrasto - Libra.
    Eficiencia - Eficiência do transporte de energia - Adimensional.
    Quantidade_motores - Quantidade de motores usados na aeronave - Adimensional.
    Hora_voo - Hora de voo - Hora.
    Altitude_cruzeiro - Altitude de cruzeiro - Metro.
    u_bateria - Bateria de Li-ion - Watt x Hora / Quilograma.
    V_vertical_S - Velocidade vertical de subida - Pés / Segundo.
    V_vertical_D - Velocidade vertical de descida - Pés / Segundo.
    W_bateria_T_S - Peso das baterias - Libra.
    V_helice - Velocidade da helice - Pés / Segundo.
    '''
    
# Bateria ------------------------------------------------------------------------------------------#
    
    # Subida ---------------------------------------------------------------------------------------#
    
    # Cálculo de potência por motor (Subida) - HorsePower.
    Potencia_motor_S_S = (np.sqrt(V_corpo_max**2+V_vertical_S**2)) *(Arrasto_S/Eficiencia/Quantidade_motores/550)
    
    # Calculo para transformar HorsePower em Watt (Subida) - Watt.
    Potencia_motor_W_S_S = Potencia_motor_S_S * 745.7
    
    # Transformando de Metro para Pés - Pés. 
    Altitude_cruzeiro = Altitude_cruzeiro *3.280

    # Cálculo de carga da bateria (Subida) - Watt X Hora.
    Carga_bateira_S_S = (Potencia_motor_W_S_S*Quantidade_motores) * ((Altitude_cruzeiro/V_vertical_S)/3600) #Transformando de segundos para hora
    
    # Cálculo de massa das baterias (Súbida) - Libra.
    W_bateria_Sub = (Carga_bateira_S_S/(Eficiencia*(u_bateria)))*2.20462 
    
    # Descida --------------------------------------------------------------------------------------#
    
    # Cálculo de potência por motor (Descida) - HorsePower.
    Potencia_motor_D_S = (np.sqrt(V_corpo_max**2+V_vertical_D**2)) *(Arrasto_S/Eficiencia/Quantidade_motores/550)

    # Cálculo para transformar HorsePower em Watt - Watt.
    Potencia_motor_W_D_S = Potencia_motor_D_S * 745.7

    # Cálculo de carga da bateria (Descida) - Watt X Hora.
    Carga_bateira_D_S = (Potencia_motor_W_D_S*Quantidade_motores) * ((Altitude_cruzeiro/V_vertical_D)/3600) 

    # Cálculo de massa das baterias (Descida) - Libra.
    W_bateria_Des = (Carga_bateira_D_S/(Eficiencia*(u_bateria)))*2.20462 

    # Cruzeiro -------------------------------------------------------------------------------------#
  
    # Cálculo de potência por motor - HorsePower.
    Potencia_motor_S = (V_corpo_max)*(Arrasto_S/Eficiencia/Quantidade_motores/550)

    # Cálculo para transformar HorsePower para Watt - Watt.
    Potencia_motor_W_S = Potencia_motor_S * 745.7

    # Cálculo de carga da bateria - Watt X Hora.
    Carga_bateria_S = (Potencia_motor_W_S*Quantidade_motores)*(Hora_voo_S+Tempo_espera) 

    # Cálculo de massa das baterias - Libra.
    W_bateria_S = (Carga_bateria_S/ (Eficiencia*(u_bateria)))*2.20462 + (W_bateria_T_S * 2) + W_bateria_Sub + W_bateria_Des
    
    # Cálculo do coeficiente de potência - Adimensional.
    Cs_S = ((Densidade_terra)*(V_corpo_max)**5/Potencia_motor_S/550/V_helice**2)**0.2
    
    # Cálculo de razão de avanço - Adimensional.
    J_S = 0.156*Cs_S**2+0.241*Cs_S+0.138

    # Cálculo do diâmetro da hélice - Pés.
    Dp_S = V_corpo_max/V_helice/(J_S)

    return (Potencia_motor_S_S,
            Potencia_motor_W_S_S,
            Carga_bateira_S_S,
            W_bateria_Sub,
            Potencia_motor_D_S,
            Potencia_motor_W_D_S,
            Carga_bateira_D_S,
            W_bateria_Des,
            Potencia_motor_S,
            Potencia_motor_W_S,
            Carga_bateria_S,
            W_bateria_S,
            Cs_S,
            J_S,
            Dp_S)

def peso_2 (q_max_S,
            Diametro,
            FS,
            Fator_fabricacao,
            Acessorios_fixacao,
            Area_S,
            Carga_septum,
            Comprimento,
            Comprimento_gondola,
            Largura_gondola,
            Altura_gondola,
            V_corpo_max,
            Fpsq,
            AreaH_S,
            AreaV_S,
            Quantidade_motores,
            Potencia_motor_S,
            Lec,
            Kp,
            Numero_helices,
            Nbl,
            Dp_S,
            WH1_S,
            W_bateria_S,
            W_bruto_decolagem_S,
            FL_S,
            Range_cruzeiro,
            Range_taxiamento):
    
    '''
    q_max_S - Pressão dinâmica máxima - Libra/Pés^2.
    Diametro - Diâmentro do envelope - Pés.
    FS - Fator de seguranca. - unidade adimensional.
    Fator_fabricacao - Fator de seguranca - Adimensional.
    Acessorios_fixacao - Fator que considera a presença de cabos estruturais externos na parte fixa da empenagem - Adimensional.
    Area_S - Área molhada do envelope - Pés^2.
    Carga_septum - Fator de carga do septum - Adimensional.
    Comprimento - Comprimento do envelope (dirigível) - Pés.
    Comprimento_gondola - Comprimento da gôndola - Pés. 
    Largura_gondola - Largura da gôndola - Pés.
    Altura_gondola - Altura da gôndola - Pés. 
    V_corpo_max - Velocidadade máxima - Pés / Segundo.
    Fpsq - Indica o peso do material da superfície externa da empenagem (dependendo do valor da pressão dinâmica) - Adimensional.
    AreaH_S - Área em planta da aleta horizontal - Pes^2.
    AreaV_S - Área em planta da aleta vertical - Pés^2.
    Quantidade_motores - Quantidade de motores usados na aeronave - Adimensional.
    Potencia_motor_S - Potência por motor - HorsePower.
    Lec - Distância entre o controlador e o motor - Pés.
    Kp - Adimensional.
    Numero_helices - Quantidade de hélices - Adimensional.
    Nbl -  Quantidade de lâminas por hélice - Adimensional.
    Dp_S - Diâmetro da hélice - Pés.
    WH1_S - Landing heaviness (Wh1) - Libra.
    W_bateria_S - Massa das baterias - Libra. 
    W_bruto_decolagem_S -  Peso bruto decolagem - Libra.
    '''

# Envelope -----------------------------------------------------------------------------------------#
    
    # Cálculo de pressao interna do envelope - Libra / in^2.
    Pl_S = (1.2 * q_max_S + 0.0635 * Diametro)/144

    # Cálculo de carga do tecido - Libra/in.
    Carga_tecido_casco_S = FS*12*Pl_S*Diametro/2

    # Cálculo de densidade do tecido do casco - oz/yd^2.
    Densidade_fab_casco_S = 0.0453 * Carga_tecido_casco_S + 1.962

    # Cálculo de peso do envelope - Libra.
    W_envelope_S = (Densidade_fab_casco_S) * (Fator_fabricacao) * (Acessorios_fixacao) * (Area_S) /16/9

    # Cálculo de densidade de fabricação do septum - oz/yd^2.
    Densidade_fab_septum_S = 0.0453 * (Carga_septum) * (Carga_tecido_casco_S) +1.962

    # Cálculo de peso do septum - Libra.
    W_septum_S = (Densidade_fab_septum_S)*(0.2)*np.pi*Diametro*(Comprimento)/4/16/9

# Gôndola ------------------------------------------------------------------------------------------#
    
    # Cálculo de peso da gôndola - Libra.
    W_gondola_S = 353*((Comprimento_gondola/10)**(0.857)*(Largura_gondola+Altura_gondola)/10*(V_corpo_max/10)**(0.338))**(1.1)

# Aletas -------------------------------------------------------------------------------------------#
    
    # Cálculo de peso dos estabilizaores - Libra.
    W_ssf_S = Fpsq*(AreaH_S+AreaV_S)*(Acessorios_fixacao)*(0.80) 

    # Cálculo de peso CS - Libra.
    W_CS_S = Fpsq * (AreaH_S+AreaV_S) * (0.20) * (1)

    # Cálculo de peso das aletas - Libra.
    W_aletas_S = W_CS_S + W_ssf_S

    # Cálculo de peso dos atuadores - Libra.
    W_atuadores_S = (1.15)*(AreaH_S+AreaV_S)*(0.79)*(0.2)

# Motor --------------------------------------------------------------------------------------------#
    
    # Cálculo de peso do motores - Libra.
    W_motores_S = Quantidade_motores*4.848*(Potencia_motor_S)**0.7956

    # Cálculo de peso do suporte dos motores - Libra.
    W_suporte_motor_S = 0.57*(Quantidade_motores)*(W_motores_S/2)

    # Cálculo de peso do controle do motor - Libra.
    W_controle_motor_S = (60.27) *((Lec)*(Quantidade_motores)/100)**(0.724)

    # Cálculo de peso do motor ocasionado na partida - Libra.
    W_partida_S = (50.38) * (Quantidade_motores*W_motores_S/1000)**0.459

    # Cálculo de peso do motor (geral) - Libra.
    W_soma_motores_ace_S = W_suporte_motor_S+W_controle_motor_S+W_partida_S

    # Cálculo de peso das hélices - Libra.
    W_helice_S =  Kp*Numero_helices*(Nbl)**0.391 *(Dp_S*Potencia_motor_S/1000)**0.782 

    # Cálculo de peso do sistema de trem de pouso - Libra.
    W_sistema_trem_pouso_S = (31.2) * (WH1_S/1000) ** 0.84

    # Cálculo de estimativa de peso - Libra.
    W_vazio_S = W_envelope_S + W_septum_S + W_gondola_S + W_aletas_S + W_atuadores_S + W_motores_S + W_soma_motores_ace_S + W_helice_S + W_sistema_trem_pouso_S + W_bateria_S

    # Soma de pesos - Libra.
    W_estrutura = W_envelope_S + W_septum_S + W_gondola_S + W_aletas_S + W_atuadores_S + W_sistema_trem_pouso_S
    W_motor = W_motores_S + W_soma_motores_ace_S + W_helice_S
    
    '''
     Cálculo de verificação (se realmente o dirigivel consegue voar, é esperado um valor maior que 0.8)  
    '''
    BR_decolagem_S = FL_S/(W_bruto_decolagem_S + W_bateria_S)

    # Cálculo de carga paga - Libra. 
    Carga_paga_S = (W_bruto_decolagem_S) - W_vazio_S

    return (Pl_S,
            Carga_tecido_casco_S,
            Densidade_fab_casco_S,
            W_envelope_S,
            Densidade_fab_septum_S,
            W_septum_S,
            W_gondola_S,
            W_ssf_S,
            W_CS_S,
            W_aletas_S,
            W_atuadores_S,
            W_motores_S,
            W_suporte_motor_S,
            W_controle_motor_S,
            W_partida_S,
            W_soma_motores_ace_S,
            W_helice_S,
            W_sistema_trem_pouso_S,
            W_vazio_S,
            W_estrutura,
            W_motor,
            BR_decolagem_S,
            Carga_paga_S)
##                                                                                                 ##
#####################################################################################################
