import os

ROOT_PATH = os.path.abspath(os.curdir)
if ROOT_PATH.endswith('\\') == False:
    ROOT_PATH += '\\'

DIR_DATA = 'Base\\'
DIR_MODEL = 'Models\\'
FILE_BASE = 'Animals.csv'  
FILE_NORMAL = 'Animals_Normal.csv'  
FILE_MODEL = 'Animals_Model_{0}.joblib'  

