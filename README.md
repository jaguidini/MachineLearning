# Base de dados utilizada:
  https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-outcomes-and

# Descrição da Base
  São dados da 'Austin Animal Center', uma instituição que cuida de animais abandonados na cidade de Austin, nos EUA.
  Existem duas bases nesse pacote, 'aac_shelter_cat_outcome_eng' e 'aac_shelter_outcomes'. Para o trabalho foi utilizada  'aac_shelter_outcomes', que contém vários tipos de animais - a outra base é apenas para gatos.
  A idéia do trabalho é fazer uma predição sobre a possibilidade de adoção de animais de acordo com suas características.

# Limpeza da base de dados

## Versão V1:
  • Removemos as colunas "animal_id", "monthyear", "name" e "outcome_subtype.
  • Substituímos a coluna "age_upon_outcome" por 'age_days_upon_outcome', convertendo os valores para dias utilizando as colunas  'date_of_birth' e 'datetime'.
  • Substituímos a coluna "sex_upon_outcome" por 'sex', convertendo os valores para 'MALE' e 'FEMALE'
  • Alteramos os valores das células "date_of_birth" e "datetime", trocando o valor de 8 células cujas datas estavam invertidas.
  • Excluímos as linhas referentes à "sex_upon_outcome", 2 linhas com valor NULL, e "outcome_type", 2 linhas com valor VAZIO.

## Versão v2:
  • Removemos na coluna "outcome_type", os registros com tipo igual a perdido (Missing) e morto (Died e Euthanasia). São 6.806 registros, dos 78.243, totalizando menos de 10% dos registros. Além disso, animais nesta situação não podem ser adotados, influenciando negativamente as análises.
  • Removemos as colunas "date_of_birth" e "datetime", pois seus valores já foram utilizados na composição da coluna "age_days_upon_outcome", além do fato que colunas com datas não possuem o processo adequado da função "get_dummies".
  • Removemos 3.121 registros de animais que estavam sem informação de sexo. Neste momento, temos 68.317 registros.
  • Alteramos na coluna "outcome_type", os registros de tipo: "Disposal", "Relocate", "Return to Owner", "Rto-Adopt" e "Transfer", para o tipo "Not Adopted". Alteramos também na mesma coluna os registros do tipo "Adoption" para "Adopted". A intenção é criar duas classes para esta coluna, relacionando os animais adotados (Adopted) e os não adotados (Not Adopted).
  • Alteramos na coluna "animal_type", de "Other" para "Rabbit", onde a descrição na coluna "breed" continha "Rabbit" e "Lionhead".
  • Removemos dos registros da coluna "breed" a descrição "%Mix%".

## Versão v3:
  • Alteramos na coluna "color", todos os registros que continham mais de duas cores para "Mixed".
  • Criamos a coluna "color_new", com os dados copiados da coluna "color".
  • Alteramos na coluna "color_new", todos os registros que continham as descrições: "Brindle", "Cream", "Merle", "Point", "Smoke", "Tabby", "Tick", "Tiger", para "Mixed". Realizamos esta alteração, pois estas descrições significam misturas ou desenhos com cores diferentes nas pelagens dos animais, principalmente dos gatos, onde significam pintas (Point), listras (Tiger), entre outras especificidades destes animais.
  • Alteramos na coluna "color_new", todos os registros do tipo: "Agouti", "Calico", "Liver", "Sable", "Torbie" e "Tortie", para "Mixed". Realizamos esta alteração, pois estes tipos se referem a animais com pelos com mais de uma cor.
  • Desfeita alteração marcada com {A1}.
  • Criamos a coluna "animal_type_new", com os dados copiados da coluna "animal_type".
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "Bantam", "Barred Rock", "Leghorn", "Rhode Island", "Silkie" e "Chicken", de "Bird" para "Chicken". Realizamos esta alteração, pois são todos tipos de galinha.
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "Muscovy", e "Duck", de "Bird" para "Duck". Realizamos esta alteração, pois são todos tipos de pato.
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "Quaker", e "Parakeet", de "Bird" para "Parakeet". Realizamos esta alteração, pois são todos tipos de periquito.
  • Alteramos na coluna "animal_type_new", de "Bird" para o conteúdo da coluna "breed", para os demais passáros, conforme coluna "animal_type" igual a "Bird".
  • Removemos o registro que possuia "Miniature" para o coluna "breed", com a coluna "animal_type" igual a "Livestock", pois não conseguimos identificar de qual animal de trata.
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "Pig", e "Potbelly Pig", de "Livestock" para "Pig". Realizamos esta alteração, pois são todos tipos de porco.
  • Alteramos na coluna "animal_type_new", de "Livestock" para o conteúdo da coluna "breed", para os demais animais em que a coluna "animal_type" é igual a "Livestock".
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "Chinchilla", "Chinchilla-Amer", e "Chinchilla-Stnd", de "Other" para "Chinchilla". Realizamos esta alteração, pois são todos tipos de Chinchilla.
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "", de "Other" para "Rabbit". Realizamos esta alteração, pois são todos tipos de coelho.
  • Alteramos na coluna "animal_type_new", que possuem registros na coluna "breed" do tipo: "Tarantula", de "Other" para "Spider".
  • Alteramos o nome da coluna "outcome_type" para "adoption", alterando os valores "Adopted" para "Yes", e "Not Adopted" para "No".

### A fonte de informação para as próximas três alterações vêm do site: http://hounddogsdrule.com/k9-classroom/coat-colors-and-patterns/
  • Alteramos na coluna "color_new", os registros do tipo: "Black", "Brown" e "Chocolate", para "Dark".
  • Alteramos na coluna "color_new", os registros do tipo: "Buff", "Cream", "Gray", "Silver", "White" e "Yellow", para "Light".
  • Alteramos na coluna "color_new", os registros do tipo: "Apricot", "Fawn", "Gold", "Orange", "Pink", "Red" e "Tan", para "Red".
  • Criamos a coluna "size", onde teremos os registros dos tamanhos dos animais, classificados como: "Small" (Pequeno), "Medium" (Médio) e "Big" (Grande). A fonte de informação para os tamanhos de cachorro vêm deste site: http://petfoodia.com/pet-talk/classification-of-dog-breeds-according-to-body-size-small-and-medium-size-breeds/
  • Criamos a coluna "pure_breed", onde validamos se os animais são puros ou se há misturas de raças. Os gatos com a descrição "Domestic" e animais com a identificação "Mixed", tiveram os seus registros alterados para "No", relatando a mistura de raças. Para o restante alteramos os registros para "Yes", relatando animais puros, sem mistura de raças.

## Versão v4:
  • Removemos as colunas "breed", "breed_new", "animal_type", "color" e "color_qtde_prov".
  • Alteramos o nome da coluna "animal_type_new" para "animal_type".
  • Alteramos o nome da coluna "color_new" para "color".
  • Removemos o upper case dos registros da coluna "sex", alterando de "FEMALE" para "Female", e de "MALE" para "Male".
