import config
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils import resample
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

class setModel():
    def __init__(self):        
        self.__root = config.ROOT_PATH     
        
    #por default pega o RandomForest
    def generateModel(self, model="RandomForest"):    
        df = pd.read_csv(config.DIR_DATA + config.FILE_NORMAL, delimiter=';')
       
        attributes = df.drop('outcome_type', axis=1)
        classes = df['outcome_type']
        
        X_train, X_test, y_train, y_test = train_test_split(attributes, classes, test_size=0.20)

        if model.upper() == 'RandomForest'.upper():            
            classifier = RandomForestClassifier()
        elif model.upper() == 'DecisionTree'.upper():            
            classifier = DecisionTreeClassifier()
        elif model.upper() == 'LogisticRegression'.upper():            
            classifier = LogisticRegression()            
        else:
            print('Classificador não encontrado, informe um dos tipos (\'RandomForest\', \'DecisionTree\', \'LogisticRegression\').\n')
            return        
        
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        y_pred_proba = classifier.predict_proba(X_test)
        
        print("################# ", model ," #################")
        print("Predict: \n", y_pred, '\n')
        print("Predict proba: \n", y_pred_proba, '\n')

        ### Acurácia e matriz de contingência
        print("Avaliação do Modelo: ")
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

        fileName = config.DIR_MODEL + config.FILE_MODEL.format(model)
        joblib.dump(classifier, fileName)
        print('Modelo [{0}] gerado com sucesso!'.format(fileName),'\n')
        

setModel().generateModel('RandomForest')
setModel().generateModel('DecisionTree')
setModel().generateModel('LogisticRegression')

