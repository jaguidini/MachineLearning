import config
import joblib

class readModel():
    def __init__(self):        
        self.__root = config.ROOT_PATH
    
    #por default pega o RandomForest
    def readModel(self, model='RandomForest', param=[[15,0,1,0,0,0,0,1]]):
        fileName = config.DIR_MODEL + config.FILE_MODEL.format(model)
        classifier = joblib.load(fileName)
        
        print("Com o modelo (" + model + ") salvo: ")        
        print("Predict") #retorna a classe
        print(classifier.predict(param))
        print("Predict proba") # quantaticamente pode dar a classe
        print(classifier.predict_proba(param))

#modelos 'RandomForest', 'DecisionTree', 'LogisticRegression'
param = [[15,0,1,0,0,0,0,1], [429,0,0,1,0,0,0,1]]
readModel().readModel('RandomForest', param)
readModel().readModel('DecisionTree', param)
readModel().readModel('LogisticRegression', param)