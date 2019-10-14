import config
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils import resample
import joblib

class setModel():
    def __init__(self):        
        self.__root = config.ROOT_PATH     

    def setModel(self, kernel='rfc'):
        
        df = pd.read_csv(config.DIR_DATA + config.FILE_NORMAL, delimiter=';')

        attributes = df_balanceado.drop('outcome_type', axis=1)
        classes = df_balanceado['outcome_type']

        X_train, X_test, y_train, y_test = train_test_split(attributes, classes, test_size=0.20)

        nomeModelo = ''
        if kernel == 'rfc':
            classifier = RandomForestClassifier(n_estimators=100)
            nomeModelo = 'RandomForest'
        elif (kernel == 'linear') | (kernel == 'rbf') | (kernel == 'poly'):
            classifier = svm.SVC(kernel = kernel, C=1, probability=True, gamma='auto');
            nomeModelo = kernel
        else:
            print('Informe o tipo do classificador (\'rfc\', \'linear\', \'rbf\' ou \'poly\').\n')
            return

        modelo = classifier.fit(X_train, y_train) 

        y_pred = modelo.predict(X_test)
        y_pred_proba = modelo.predict_proba(X_test)

        print(y_pred, '\n')
        print(y_pred_proba, '\n')

        ### Acurácia e matriz de contingência
        print("Avaliação do Modelo: ")
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

        fileName = config.DIR_MODEL + config.FILE_MODEL.format(nomeModelo)
        joblib.dump(classifier, fileName)
        print('Modelo [{0}] gerado com sucesso!'.format(fileName),'\n')


setModel().setModel(kernel='linear')

