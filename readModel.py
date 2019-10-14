import config
import joblib

class readModel():
    def __init__(self):        
        self.__root = config.ROOT_PATH     

    #param=[[6.9,0.48,0.2,1.9,0.082,9,23,0.99585,3.39,0.43,9.05]]
    #kernel=valores podem ser => rfc, rbf, poly, linear
    def readModel(self, kernel='rfc', param=[]):
        
        nomeModelo = ''
        if kernel == 'rfc':
            nomeModelo = 'RandomForest'
        elif (kernel == 'linear') | (kernel == 'rbf') | (kernel == 'poly'):
            nomeModelo = kernel
        else:
            print('Informe o tipo do classificador (\'rfc\', \'linear\', \'rbf\' ou \'poly\').\n')
            return

        fileName = config.DIR_MODEL + config.FILE_MODEL.format(nomeModelo)
        modelo = joblib.load(fileName)        

        print("Classificar [6.9,0.48,0.2,1.9,0.082,9,23,0.99585,3.39,0.43,9.05,4] ({0}):".format(nomeModelo))
        print("Resultado: ", modelo.predict(param))
        print("Resultado (proba): ")
        print(modelo.predict_proba(param))


readModel().readModel(kernel='rfc', param=[[6.9,0.48,0.2,1.9,0.082,9,23,0.99585,3.39,0.43,9.05]])