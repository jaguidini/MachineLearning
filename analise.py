import config
import numpy as np
import pandas as pd
from scipy import stats

class Analise():
    def __init__(self):        
        self.__root = config.ROOT_PATH        

    ### Função para correlação usando Método de Pearson
    def pearsonr_ci(self, x,y,alpha=0.05):
       r, p = stats.pearsonr(x, y)
       r_z = np.arctanh(r)
       se = 1 / np.sqrt(x.size - 3)
       z = stats.norm.ppf(1 - alpha / 2)
       lo_z, hi_z = r_z - z * se, r_z + z * se
       lo, hi = np.tanh((lo_z, hi_z))
 
       return r, p, lo, hi

    def valida_forca_correlacao(self, r, lo, hi):        

        neutro = (lo + ((hi - lo) / 2))
        parte = (neutro - lo) / 3

        menor = lo  
        menor2 = menor + parte
        menor1 = menor2 + parte 

        neutro =  menor1 + parte

        maior1 = neutro + parte  
        maior2 =  maior1 + parte
        maior = hi

        if(r >= menor) & (r < menor2):      
            return "RELAÇÃO FORTE NEGATIVA"
        elif(r >= menor2) & (r < neutro):  
            return "RELAÇÃO FRACA NEGATIVA"
        elif(r <= maior) & (r >= maior2):   
            return "RELAÇÃO FORTE POSITIVA"
        elif(r < maior2) & (r >= neutro):   
            return "RELAÇÃO FRACA POSITIVA"

    def checa_correlacao(self, r, p, lo, hi):
        if (r > lo) & (r < hi) :
            forca = self.valida_forca_correlacao(r, lo, hi)
            return r, lo, hi, forca

        return 0, 0, 0, 0

    def MostraRelacao(self, df):
        c1 = 0
        for i, j in df.iteritems():
            c2 = 0
            for i2, j2 in df.iteritems():
                r, p, lo, hi = self.pearsonr_ci(df[i], df[i2])
                val_r, val_lo, val_hi, forca = self.checa_correlacao(r, p, lo, hi)
                if(val_r > 0) & (i != i2):
                    print(i,"/",i2," => ", val_r, val_lo, val_hi, forca)
                c2 += 1
            c1 += 1

    def Normalizar(self):
        df = pd.read_csv(config.DIR_DATA + config.FILE_BASE, sep=";")
        
        #Colunas date_of_birth e datetime precisam ser revistas
        df_normal = pd.concat([df.get(['age_days_upon_outcome']),
                              pd.get_dummies(df.animal_type, prefix='animal_type_'),
                              #pd.get_dummies(df.breed, prefix='breed_'),
                              #pd.get_dummies(df.color, prefix='color_'),
                              pd.get_dummies(df.sex, prefix='sex_'),
                              df.get(['outcome_type']),
                              ],
                     axis=1)
            
        #print(df_normal)
        #Salva arquivo
        df_normal.to_csv(config.DIR_DATA + config.FILE_NORMAL, sep=';', index = None, header=True)
        print('Arquivo {0} criado com sucesso!'.format(config.DIR_DATA + config.FILE_NORMAL))
        
        return df_normal;
        
#BEGIN
#Pega o dataframe normalizado
df = Analise().Normalizar()
#Mostra a relação
#Analise().MostraRelacao(df)
        
