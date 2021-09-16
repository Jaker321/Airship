#####################################################################################################
#                                                                                                   #
#Módulo Mestre

'''
 A função mestre tem o objetivo de chamar todas as variáveis de entrada e fazer a distribuição delas,
entre as outras funções que cada uma se adeque para a realização dos cálculos.                                                                                        
'''
#                                                                                                   #
#####################################################################################################

#####################################################################################################
# Aqui são dristribuídas todas as variáveis                                                         #
#####################################################################################################

#####################################################################################################
#                                                                                                   #
import Modulo_3                                                                                  
import ModuloP_6  
#                                                                                                   #                                                                            
#####################################################################################################

#####################################################################################################
# Conversões                                                                                        #

pe_metro = 0.3048                                                                                  
kg_m3__slug_ft3 = 0.001941                                                                         
kg_ms__slug_fts = 0.0208                                                                           
m_s2__ft_s2 = 3.28                                                                                 
ft_s__ft_h = 3600                                                                                  
mn = 6076                                                                                          
#####################################################################################################

#####################################################################################################
#                                                                                                   #
# Funções                                                                                           #

def Mestra (Comprimento,
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
            plot):
                                                                                         
# Função Geometria ---------------------------------------------------------------------------------#             
                                                                                       
    Resultado_1 = Modulo_3.geometria (Comprimento,
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
                                      Largura_gondola)

    (Diametro,
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
     Volume_gondola_S)  = Resultado_1

    salv_1 = (Diametro,
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
             
# Função Escoamento Fluido -------------------------------------------------------------------------#   
                    
    Resultado_2 = Modulo_3.escoamento_fluido (V_fluido,
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
                                              m_s2__ft_s2)

    (Altitude_cruzeiro,
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
     FL_S) = Resultado_2
     
    salv_2 = (Altitude_cruzeiro,
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
    
# Função Arrasto -----------------------------------------------------------------------------------#  

    Resultado_3 = Modulo_3.arrasto (F_corpo_S,
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
                                    NL)

    (CD0_corpo_S,
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
     K_S) = Resultado_3
     
    salv_3 = (CD0_corpo_S,
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
    
# Função Peso --------------------------------------------------------------------------------------#  
                  
    Resultado_4 = Modulo_3.peso (FL_S,
                                 BRland,
                                 Area_ref_S,
                                 V_corpo_max,
                                 Range_cruzeiro,
                                 q_max_S,
                                 ft_s__ft_h,
                                 mn)
    
    (Hora_voo_S,
     W_zero_bateria_S,
     WH1_S,
     W_bruto_decolagem_S,
     CL_potencia_max_S) = Resultado_4

    salv_4 = (Hora_voo_S,
              W_zero_bateria_S,
              WH1_S,
              W_bruto_decolagem_S,
              CL_potencia_max_S)
    
# Função Aerodinâmica ------------------------------------------------------------------------------#   
 
    Resultado_5 = Modulo_3.aerodinamica (Soma_arrasto_S,
                                         K_S,
                                         CL_potencia_max_S,
                                         q_max_S,
                                         Area_ref_S,
                                         FL_S,
                                         W_bruto_decolagem_S)
 
    (Arrasto_S,
     BRto_S) = Resultado_5
    
    salv_5 = (Arrasto_S,
              BRto_S)

# Função Desempenho --------------------------------------------------------------------------------#   

    Resultado_6 = Modulo_3.desempenho (Densidade_ar,
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
                                       mn)
    
    (Cf_envelope_T_S,
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
     W_bateria_T_S) = Resultado_6
                                                                              
    salv_6 = (Cf_envelope_T_S,
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
    
# Função Potência ----------------------------------------------------------------------------------#

    Resultado_7 = Modulo_3.potencia (V_corpo_max,
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
                                     V_vertical_D)   
    
    (Potencia_motor_S_S,
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
     Dp_S) = Resultado_7

    salv_7 = (Potencia_motor_S_S,
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

# Função Peso 2 ------------------------------------------------------------------------------------#    

    Resultado_8 = Modulo_3.peso_2 (q_max_S,
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
                                   Range_taxiamento)
     
    (Pl_S,
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
     Carga_paga_S) = Resultado_8
      
    salv_8 = (Pl_S,
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

#####################################################################################################
## Plotagem dos prints                                                                             ##
##                                                                                                 ##
    if (plot == 1):
        ModuloP_6.plotagem_1 (Volume_S,
                              Area_ref_S,
                              Area_S,
                              Soma_area_molhada_aletas_S,
                              Volume_gondola_S)
        
        ModuloP_6.plotagem_2 (Cf_envelope_S,
                              Cf_aletaV_S,
                              Cf_aletaH_S,
                              q_corpo_S,
                              q_max_S,
                              FL_S)
        
        ModuloP_6.plotagem_3 (CD0_corpo_S,
                              CD0_aletas_S,
                              CD0_gondola_cabos_S,
                              CD0_cabos_S,
                              Soma_especifica,
                              CD0_motor_S,
                              Soma_arrasto_S,
                              K_S)
        
        ModuloP_6.plotagem_4 (WH1_S,
                              W_bruto_decolagem_S,
                              Hora_voo_S)
        
        ModuloP_6.plotagem_5 (Arrasto_S,
                              BRto_S)
        
        ModuloP_6.plotagem_6 (Hora_Tax_S,
                              W_bateria_T_S)
        
        ModuloP_6.plotagem_7 (Potencia_motor_S,
                              Potencia_motor_W_S,
                              Dp_S,
                              W_bateria_S)
        
        ModuloP_6.plotagem_8 (W_vazio_S,
                              Carga_paga_S,
                              BR_decolagem_S)   
#                                                                                                   #
#####################################################################################################
        
    return (Resultado_1,
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
            mn)
##                                                                                                 ##
#####################################################################################################