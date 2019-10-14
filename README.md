Base de dados
https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-outcomes-and

São dados da 'Austin Animal Center', uma instituição que cuida de animais abandonados na cidade de Austin, nos EUA.
Existem duas bases nesse pacote, 'aac_shelter_cat_outcome_eng' e 'aac_shelter_outcomes'. Para o trabalho foi utilizada 'aac_shelter_outcomes', que contém vários tipos de animais - a outra base é apenas para gatos.
A idéia do trabalho é fazer uma predição sobre a possibilidade de adoção de animais de acordo com suas características.

A planilha 'Trabalho.xlsx' tem as duas bases, mas, como dito antes, apenas a segunda foi utilizada.
A aba 'Ajustes' tem as colunas e linhas que foram ajustadas, conforme abaixo:

# Colunas removidas
    animal_id
	  monthyear
	  name
	  outcome_subtype
# Colunas substituídas	
    age_upon_outcome:	Substituída por 'age_days_upon_outcome', convertendo os valores para dias utilizando as colunas 'date_of_birth' e       'datetime'
	  sex_upon_outcome:	Substituída por 'sex', convertendo os valores para 'MALE' e 'FEMALE'

# Linhas alteradas
    date_of_birth e datetime:	8 células alteradas, trocando de posição as datas que estavam invertidas

# Linhas excluídas:
    sex_upon_outcome:	2 linhas com valor NULL
	  outcome_type:	2 linhas com valor VAZIO

                  Inícial	Após ajustes
Total de linhas:	78257	  78244
Total de colunas:	12	    8

A aba 'Resultado Final' tem os dados que são exportados para o csv que serve de base para o python, que chamei de 'Animals.csv'.

#######################################################################################################################################

# Python:
    Montei a estrutura do projeto conforme abaixo:
    # 'config.py': tem os parâmetros padrão que são utilizados. Para usar, é só importar dentro do arquivo que quiser (import config)
    # 'analise.py': faz a parte da análise da base. Nessa classe coloquei alguns métodos que usamos nas aulas, mas tem que dar uma     'ajeitada nela.
    # 'setModel.py': nessa classe tem os métodos que vão criar o modelo. Achei mais interessante deixar separado da fase de análise, mas se quiserem juntar tudo, fiquem à vontade.
      # Os parâmetro a serem passados nesse método são:
        kernel=> 'rfc', 'linear', 'rbf' ou 'poly'
        Passando um desses parâmetros o método cria e salva um modelo referente ao kernel desejado.
    # 'readModel.py': aqui é feita a leitura do modelo, passando os parâmetros:
       kernel => 'rfc', 'linear', 'rbf' ou 'poly'
       param => array com os dados a serem analisados pelo modelo. Podem ser vários, tipo:
        [[6.9,0.48,0.2,1.9,0.082,9,23,0.99585,3.39,0.43,9.05], [6.9,0.48,0.2,1.9,0.082,9,23,0.99585,3.39,0.43,9.05]]
  
Para o parâmetro kernel, deixei o valor 'rfc' como padrão (se não passar nada na chamada do método, ele vai usar o 'rfc' como kernel.
A propósito, rfc = Random Forest Classifier...

# Se não quiserem usar essa base, acho que pode ser feita a alteração sem ter que mexer muito no python, então fiquem a vontade para estragar tudo.
# Não terminei tudo, só mesmo a parte da base, então as classes ainda precisam ser ajustadas. Talvez fosse interessante colocar um gráfico lá na classe de análise.





 
		
