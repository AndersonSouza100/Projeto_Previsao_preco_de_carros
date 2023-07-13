# Projeto_Previsao_preco_de_carros

Nosso Objetivo:
Desenvolver um projeto de ciência de dados capaz de prever o preço de um carro atráves de suas características. Quando se trata de determinar o preço de um carro , várias informações são relevantes, ex: ano, motor hp, tipo de combustível , etc.

Os dados para realizar esse projeto foram obtidos do site : (https://www.kaggle.com/CooperUnion/cardataset). A IDE usada para desenvolver as linhas de código foi o Jupyter. O projeto em si já é bem autoexplicativo. A seguir , falarei sobre cada arquivo contido neste trabalho:


1 - Projeto_Previsao_preço_de_carros.ipynb : esse é o arquivo principal do projeto, onde nele é realizado todo trabalho de Ciência de Dados. Está dividido em 8 passos:

      1 - Entendimento da área.
      2 - Entendimento do desafio.
      3 - Extração/Obtenção de Dados.
      4 - Ajustes dos dados (Limpeza dos Dados).
      5 - Análise Exploratória e Tratamento de Outliers.
      6 - Modelagem + Algoritmos.
      7 - Interpretação dos Resultados.
      8 - Deploy do Projeto.
Após a etapa 8, foram criados 2 arquivos : 'dados.csv' (que é nossa base de dados completa e tratada) e 'modelo.joblib' (que é o nosso modelo de inteligência artificial salvo em arquivo para facilitar sua leitura na hora do deploy).

2 - Deploy_Previsao_preço_de_carros.ipynb: esse é o arquivo onde gerará uma tela para que o usuário possa colocar as informações do carro e prever o seu preço . Esse arquivo irá ler os dois arquivos gerados no Deploy.

3 - Analise_importancia_features.csv: esse arquivo foi gerado dentro do projeto (arquivo 1) e serviu para analisar o percentual de importância de cada feature no modelo de inteligência artificial. Com essa análise, foi possível descobrir se iríamos manter todas as features ou apagar alguma.  

4 - Análise das colunas.csv: esse arquivo foi gerado dentro do projeto (arquivo 1) e serviu para realizar uma análise direta das colunas. A principio, todas foram consideradas.

5 - nomes_marca.csv: esse arquivo foi gerado dentro do projeto (arquivo 1), em um determinado momento, foi preciso analisar a coluna de marcas para saber se iríamos ficar com todos os nomes.

6 - data.csv: esse é a base de dados sem tratamento e original do projeto. 

7 - pasta .ipynb_checkpoints: é uma pasta que o jupyter cria automáticamente com os backups de save.

8 - Deploy_Previsao_preço_de_carros.py: esse arquivo é a tela final onde o usuário irá colocar as informações do carro para prever o seu preço. Foi gerado pelo arquivo 2 e para que ele funcione , é necessário seguir o passo a passo:

      1 - abra no seu computador o Anaconda Prompt.
      2 - execute o comando: cd C:\Users\AndersonPC\Documents\GitHub\Projeto_Previsao_preco_de_carros Observação: no passo 2 você deve colocar o caminho exato da pasta onde está o seu projeto. No meu caso está desta forma , mas no seu estará diferente.
      3 - execute o comando: streamlit run Deploy_Previsao_preço_de_carros.py
      4 - Abrirá uma aba no seu navegador, basta colocar as informações do carro e clicar no botão 'Prever valor do carro'.
      
