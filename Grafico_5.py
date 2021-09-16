#####################################################################################################
#                                                                                                   #
# Módulo Gráfico

'''
 O módulo Gráfico tem como objetivo plotar diferentes tipos de gráficos analíticos.                                                                                    ## 
'''
#                                                                                                   #
#####################################################################################################

#####################################################################################################
# Aqui é realizado todos os plots de gráficos do programa                                           #
#####################################################################################################

#####################################################################################################
# Bibliotecas                                                                                       #
import pandas as pd                                                                                
import matplotlib.pyplot as plt                                                                    
import numpy as np                                                                                 
from  mpl_toolkits.mplot3d  import  Axes3D                                                                                                                                      ##
import seaborn as sb                                                                               
#                                                                                                
import Funcao_2
#####################################################################################################

#####################################################################################################
#                                                                                                   #
# Funções

def imagem (Varia_IMA_Junt,
            Varia_CON,
            voltas,
            contador,
            plot_1,
            plot_2,
            plot_3,
            Quant_Analise):

# Variáveis que serão usadas no DOE   
                                                            
    DOE = ['Comprimento (Ft)',
           'Densidade Energetica Bateria (Wh/Kg)',
           'Altitude Cruzeiro (Ft)',
           'Volume (Ft³)',
           'Arquimedes (Lb)',
           'Soma dos Arrastos (Ad)',
           'Arrasto (Lb)',
           'Peso Bateria (Lb)',
           'Carga Util (Lb)']
#                                                                                                   #
#####################################################################################################

    if (contador == voltas):
        if (plot_1 == 1):

# Contour ------------------------------------------------------------------------------------------#

            if (Varia_CON [43] == 1):
                x_DOE_1 = np.linspace ((50),(100), (Quant_Analise)) # Diametro
                y_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimentro
            
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (y_DOE_1,
                                                      x_DOE_1,
                                                      x_DOE_1,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      y_DOE_1/11.8,
                                                      y_DOE_1/15.6,
                                                      y_DOE_1/8.2,
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      Varia_CON [30],
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38], 
                                                      Varia_CON [39],
                                                      Varia_CON [40],
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [0][1]

                    return z
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Volume (ft³)')
                plt.xlabel('Diametro (ft)')
                plt.ylabel('Comprimento (ft)')
            
#---------------------------------------------------------------------------------------------------#

            if (Varia_CON [44] == 1):
                
                x_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
                y_DOE_1 = np.linspace ((50),(100), (Quant_Analise)) # Diametro
            
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (x_DOE_1,
                                                      y_DOE_1,
                                                      y_DOE_1,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      x_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      x_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      x_DOE_1/11.8,
                                                      x_DOE_1/15.6,
                                                      x_DOE_1/8.2,
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      Varia_CON [30],
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38],
                                                      Varia_CON [39],
                                                      Varia_CON [40],
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [0][4]

                    return z
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('AR')
                plt.xlabel('Comprimento (ft)')
                plt.ylabel('Diametro (ft)')
            
#---------------------------------------------------------------------------------------------------#
 
            if (Varia_CON [45] == 1):

                x_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
                y_DOE_1 = np.linspace ((50),(100), (Quant_Analise)) # Diametro
            
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (x_DOE_1,
                                                      y_DOE_1,
                                                      y_DOE_1,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      x_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      x_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13], 
                                                      x_DOE_1/11.8,
                                                      x_DOE_1/15.6,
                                                      x_DOE_1/8.2, 
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      Varia_CON [30],
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38],
                                                      Varia_CON [39],
                                                      Varia_CON [40], 
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [1][13]
 
                    return z
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Arquimedes (lb)')
                plt.xlabel('Comprimento (ft)')
                plt.ylabel('Diametro (ft)')
            
#---------------------------------------------------------------------------------------------------#

            if (Varia_CON [46] == 1):

                x_DOE_1 = np.linspace ((50),(100), (Quant_Analise)) # Diametro
                y_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
            
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (y_DOE_1,
                                                      x_DOE_1,
                                                      x_DOE_1,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      y_DOE_1/7.4, 
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      y_DOE_1/11.8,
                                                      y_DOE_1/15.6,
                                                      y_DOE_1/8.2,
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      Varia_CON [30],
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38],
                                                      Varia_CON [39],
                                                      Varia_CON [40],
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [2][12]

                    return z
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Arrasto Parasita Total (Ad)')
                plt.xlabel('Diametro (ft)')
                plt.ylabel('Comprimento (ft)')
            
#---------------------------------------------------------------------------------------------------#

            if (Varia_CON [47] == 1):
                
                x_DOE_1 = np.linspace ((50),(100), (Quant_Analise)) # Diametro
                y_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
            
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (y_DOE_1,
                                                      x_DOE_1,
                                                      x_DOE_1,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      y_DOE_1/11.8,
                                                      y_DOE_1/15.6,
                                                      y_DOE_1/8.2,
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20], 
                                                      Varia_CON [21],
                                                      Varia_CON [22], 
                                                      Varia_CON [23], 
                                                      Varia_CON [24], 
                                                      Varia_CON [25], 
                                                      Varia_CON [26], 
                                                      Varia_CON [27],
                                                      Varia_CON [28], 
                                                      Varia_CON [29], 
                                                      Varia_CON [30],
                                                      Varia_CON [31], 
                                                      Varia_CON [32], 
                                                      Varia_CON [33],
                                                      Varia_CON [34], 
                                                      Varia_CON [35], 
                                                      Varia_CON [36],
                                                      Varia_CON [37], 
                                                      Varia_CON [38], 
                                                      Varia_CON [39],
                                                      Varia_CON [40], 
                                                      Varia_CON [41], 
                                                      Varia_CON [42])
                
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [4][0]

                    return z
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Arrasto (lb)')
                plt.xlabel('Diametro (ft)')
                plt.ylabel('Comprimento (ft)')
            
#---------------------------------------------------------------------------------------------------#

            if (Varia_CON [48] == 1): 
                
                x_DOE_1 = np.linspace ((3000),(20000),(Quant_Analise)) # Altitude de cruzeiro
                y_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
                
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (y_DOE_1,
                                                      y_DOE_1/4,
                                                      y_DOE_1/4,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      y_DOE_1/11.8,
                                                      y_DOE_1/15.6,
                                                      y_DOE_1/8.2,
                                                      Varia_CON [17], 
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      x_DOE_1,
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35], 
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38],
                                                      Varia_CON [39],
                                                      Varia_CON [40], 
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                    
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [7][22]
                    volume = Resultado_1_I [0][1] 
  
                    return z,volume
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
                V = np.zeros ((lenx,leny)) 
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii],V[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1) 
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,V,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Carga Paga (lb)') 
                plt.xlabel('Altitude Cruzeiro (Ft)')
                plt.ylabel('Volume (ft³)')

#############################Contour Peso_Carga#############################
             
            if (Varia_CON [49] == 1):             
                
                x_DOE_1 = np.linspace ((50),(600), (Quant_Analise)) # Range Maximo
                y_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
                
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (y_DOE_1,
                                                      y_DOE_1/4,
                                                      y_DOE_1/4,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      y_DOE_1/11.8,
                                                      y_DOE_1/15.6,
                                                      y_DOE_1/8.2,
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      x_DOE_1,
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      Varia_CON [30],
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38], 
                                                      Varia_CON [39],
                                                      Varia_CON [40],
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                    
                    Resultado_1_I = list (Resultado_1_I)
                
                    carga_paga = Resultado_1_I [7][22]
                    volume = Resultado_1_I [0][1]
  
                    return carga_paga,volume
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
                V = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii],V[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
       
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1) 
                            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,V,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Carga Paga (lb)') 
                plt.xlabel('Range Máximo (mn)')
                plt.ylabel('Volume (ft³)')
                
                plt.show ()
                
#---------------------------------------------------------------------------------------------------#
                
            if (Varia_CON [50] == 1):   
                
                x_DOE_1 = np.linspace ((100),(700), (Quant_Analise)) # Densidade Energetica
                y_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento
                
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (y_DOE_1,
                                                      y_DOE_1/4,
                                                      y_DOE_1/4,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      y_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      y_DOE_1/11.8,
                                                      y_DOE_1/15.6,
                                                      y_DOE_1/8.2, 
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20], 
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      x_DOE_1,
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      Varia_CON [30],
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38],
                                                      Varia_CON [39],
                                                      Varia_CON [40],
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                    
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [7][22]
                    volume = Resultado_1_I [0][1]
                    
                    return z,volume
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
                V = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii],V[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)  
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Carga Paga (lb)') 
                plt.xlabel('Densidade Energetica Bateria (Wh/Kg)')
                plt.ylabel('Volume (ft³)')
                
#---------------------------------------------------------------------------------------------------#

            if (Varia_CON [51] == 1):
                
                x_DOE_1 = np.linspace ((200),(400), (Quant_Analise)) # Comprimento 
                y_DOE_1 = np.linspace ((3000),(20000), (Quant_Analise)) # Altitude
            
                def Func_Mestra (x_DOE_1,y_DOE_1):
                    Resultado_1_I =  Funcao_2.Mestra (x_DOE_1,
                                                      x_DOE_1/4,
                                                      x_DOE_1/4,
                                                      Varia_CON [3],
                                                      Varia_CON [4],
                                                      Varia_CON [5],
                                                      Varia_CON [6],
                                                      x_DOE_1/7.4,
                                                      Varia_CON [8],
                                                      Varia_CON [9],
                                                      Varia_CON [10],
                                                      x_DOE_1/7.4,
                                                      Varia_CON [12], 
                                                      Varia_CON [13],
                                                      x_DOE_1/11.8,
                                                      x_DOE_1/15.6,
                                                      x_DOE_1/8.2,
                                                      Varia_CON [17],
                                                      Varia_CON [18],
                                                      Varia_CON [19],
                                                      Varia_CON [20],
                                                      Varia_CON [21],
                                                      Varia_CON [22],
                                                      Varia_CON [23],
                                                      Varia_CON [24], 
                                                      Varia_CON [25],
                                                      Varia_CON [26],
                                                      Varia_CON [27],
                                                      Varia_CON [28],
                                                      Varia_CON [29],
                                                      y_DOE_1,
                                                      Varia_CON [31],
                                                      Varia_CON [32],
                                                      Varia_CON [33],
                                                      Varia_CON [34],
                                                      Varia_CON [35],
                                                      Varia_CON [36],
                                                      Varia_CON [37],
                                                      Varia_CON [38],
                                                      Varia_CON [39],
                                                      Varia_CON [40],
                                                      Varia_CON [41],
                                                      Varia_CON [42])
                
                    Resultado_1_I = list (Resultado_1_I)
                
                    z = Resultado_1_I [4][0]

                    return z
            
                lenx = len(x_DOE_1)
                leny = len(y_DOE_1)
            
                Z = np.zeros ((lenx,leny))
            
                for ii in range (lenx):
                    for jj in range (leny):
                        Z[jj,ii] = Func_Mestra(x_DOE_1[ii],y_DOE_1[jj])
                    
                X, Y = np.meshgrid (x_DOE_1,y_DOE_1)
            
                fig_1, ax = plt.subplots()
                CS = ax.contour (X,Y,Z,20)
                ax.clabel(CS, inline=True, fontsize=10)
                ax.set_title ('Arrasto (lb)')
                plt.xlabel('Comprimento (ft)')
                plt.ylabel('Altitude (ft)')
            
           
# Plot 3D ------------------------------------------------------------------------------------------#
# Não Finalizado !           
        if (plot_2 == 1):
            
            Cg_S = Varia_IMA_Junt [[1],[0]] 
            CordaM_aletaV = Varia_IMA_Junt [[1],[1]]
            CordaM_aletaH = Varia_IMA_Junt [[1],[2]]
            envergaduraV_S = Varia_IMA_Junt [[1],[3]]
            envergaduraH_S = Varia_IMA_Junt [[1],[4]]

    
            #Deforma o corpo as duas funcoes a baixo
            theta = np.arange (0,2*np.pi, 0.01)
            phi = np.arange (0, np.pi, 0.01)
    
            theta, phi = np.meshgrid (theta * 2, phi)
    
            a = Varia_IMA_Junt [[0],[0]]/2
            b = Varia_IMA_Junt [[0],[1]]/2
            c = Varia_IMA_Junt [[0],[2]]/2
    
            # Dirigível
    
            x = a * np.sin (phi) * np.cos (theta)
            y = b * np.sin (phi) * np.sin (theta)
            z = c * np.cos (phi)
    
            # Aletas
    
            fig_2 = plt.figure ()
    
            ax = Axes3D(fig_2)
    
            x_aH, y_aH = np.meshgrid([-Cg_S [0] - CordaM_aletaH [0], 0], [-envergaduraH_S [0]/2,envergaduraH_S [0]/2])
    
            z_aH = np.zeros((2, 2))
    
            x_aV, z_aV = np.meshgrid((-Cg_S [0] - CordaM_aletaV [0], 0), (-envergaduraV_S[0]/2,envergaduraV_S[0]/2))
            y_aV = x_aV*0
    
            ax.plot_surface (x,y,z)
            ax.plot_surface (x_aH,y_aH,z_aH)
            # Plot top half of inclined plane.
            ax.plot_surface(x_aV, y_aV, z_aV)
            # Plot bottom half of inclined plane.
    
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            Xmax = a
            Xmin = -a
            Ymax = b
            Ymin = -b
            Zmax = c
            Zmin = -c
            max_range = np.array([Xmax-Xmin, Ymax-Ymin, Zmax-Zmin]).max()
            Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(Xmax+Xmin)
            Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Ymax+Ymin)
            Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Zmax+Zmin)

            # Comment or uncomment following both lines to test the fake bounding box:
            for xb, yb, zb in zip(Xb, Yb, Zb):
                ax.plot([xb], [yb], [zb], 'w')
    
            plt.show ()    

# Plot Doe -----------------------------------------------------------------------------------------#
    
        if (plot_3 == 1):
            
            # Create a pandas dataframe with all the information
            df = pd.read_excel('Resultados.xls',usecols=DOE)

            # Plot the correlation matrix
            #sb.set(font_scale = 0.5)
            fig = sb.pairplot(df,corner=True)
            
            plt.tight_layout()
            plt.show()

            fig.savefig('doe.pdf')
            