#import da biblioteecas necessárias para o projeto
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


#Leitura dos arquivos XSL geral, publicados no git
caminho_arquivo_excel = "https://raw.githubusercontent.com/lucianesantos/DataThon/main/PEDE_PASSOS_DATASET_FIAP_V3.xlsx"
df = pd.read_excel(caminho_arquivo_excel, engine='openpyxl')
df.head(2)

#Leitura do arquivo XSL para o grafico do INDE E já ordenei os dados
caminho_arquivo_INDE20 = "https://raw.githubusercontent.com/lucianesantos/DataThon/main/PEDE_PASSOS_DATASET_FIAP_INDE_V1.xlsx"
df_2020 = pd.read_excel(caminho_arquivo_INDE20, engine='openpyxl')
df_2020 = df_2020.sort_values(by='INDE_2020')

df_2021 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2021_INDE', engine='openpyxl')
df_2021 = df_2021.sort_values(by='INDE_2021')

df_2022 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2022_INDE', engine='openpyxl')
df_2022 = df_2022.sort_values(by='INDE_2022')

#Leitura do arquivo XSL para o grafico do IDA E já ordenei os dados
ida_2020 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2020_IDA', engine='openpyxl')
ida_2020 = ida_2020.sort_values(by='IDA_2020')

ida_2021 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2021_IDA', engine='openpyxl')
ida_2021= ida_2021.sort_values(by='IDA_2021')
ida_2021.rename(columns={ida_2021.columns[1] : 'TOTAL'}, inplace=True)

ida_2022 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2022_IDA', engine='openpyxl')
ida_2022= ida_2022.sort_values(by='IDA_2022')
ida_2022.rename(columns={ida_2022.columns[1] : 'TOTAL'}, inplace=True)

#Leitura do arquivo XSL para o grafico do IGE E já ordenei os dados
ige_2020 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2020_IEG', engine='openpyxl')
ige_2020 = ige_2020.sort_values(by='IEG_2020')

ige_2021 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2021_IEG', engine='openpyxl')
ige_2021= ige_2021.sort_values(by='IEG_2021')

ige_2022 = pd.read_excel(caminho_arquivo_INDE20, sheet_name='2022_IEG', engine='openpyxl')
ige_2022= ige_2022.sort_values(by='IEG_2022')


# Títulos da barra lateral
opcao_pagina1 = st.sidebar.title('Análise Educacional')
opcao_pagina2 = st.sidebar.title('Análise Sócio Econômica')
opcao_pagina3 = st.sidebar.title('Análises Externnas')
opcao_pagina4 = st.sidebar.title('AI')

    #título da página 
titulo = "<h1 style='text-align: center;'>Associação Passos Mágicos</h1>"
st.markdown(titulo, unsafe_allow_html=True)




#subtítulos da página

st.markdown('<p style="text-align: center;font-size:23px;">Análise do crescimento da associação, baseado nos metadados do PEDE  (Pesquisa Extensiva de Desenvolvimento Educacional) dos anos de 2020, 2021 e 2022, realizada pelo economista Dario Rodrigues Silva, onde conhecemos e analisamos os resultados da Associação Passos Mágicos.  </p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;font-size:16px;">By Luciane dos Santos Reis & Leonardo Santos Rodrigues & Marcelo Meirelles Junior  </p>', unsafe_allow_html=True)

#Criei essa lista de cores. Essas são as cores que extraí do site da passos mágicos. Apesar de não ter achado harmônico, são as cores da passos.
cores = [ '#FF5931', '#FBBA00' ,'#FFD401',  '#FF2E34','#FF8427','#257CBB', '#145089' ]


#layout da página inteira
tab0, tab1 = st.tabs(['   ', ' '])


with tab0:
    st.write('')



# Gráfico alunos por ano 
    
    #Para esse grafico utilizei a contagem dos alunos de cada ano 
df['INDE_2020'] = pd.to_numeric(df['INDE_2020'], errors='coerce')
df['INDE_2021'] = pd.to_numeric(df['INDE_2021'], errors='coerce')
df['INDE_2022'] = pd.to_numeric(df['INDE_2022'], errors='coerce')

count_2020 = df[df['INDE_2020'].notnull()]
count_2021 = df[df['INDE_2021'].notnull()]
count_2022 = df[df['INDE_2022'].notnull()]

count_2020_1=pd.to_numeric(count_2020.shape[0])
count_2021_1=pd.to_numeric(count_2021.shape[0])
count_2022_1=pd.to_numeric(count_2022.shape[0])

#listas de dados
anos = ['2020', '2021', '2022']
total_alunos = [count_2020_1, count_2021_1, count_2022_1]
#  DataFrame
total_alunos_df = pd.DataFrame({'Ano': anos, 'Total': total_alunos})


#Gráfico 

with tab0:

    ax = sns.barplot(data=total_alunos_df,  x='Ano', y='Total',  palette=cores, width=0.50, hue=None)

for p in ax.patches:
    ax.annotate(format(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

sns.despine(ax=ax, left=True, right=True, top=True, bottom=False)
ax.get_yaxis().set_visible(False)

plt.suptitle("Alunos por Ano", fontsize=12)
plt.xlabel(' ')
plt.ylabel(' ')
plt.xticks(rotation=45, ha='right')
plt.grid(False)
plt.ylim(0,1000)
st.pyplot(ax.figure)

######



st.markdown("    ")
st.markdown("    ")
st.markdown('<p style="text-align: center;font-size:23px;">Observamos que a Associação Passos Mágicos cresceu ao longo dos anos em número de alunos. ​Ela atingiu o número de 1100 alunos no ano de 2023.  </p>', unsafe_allow_html=True)
st.markdown("---")



# Gráfico PEDE - INDE

titulo1 = "<h2 style='text-align: center;'>INDE - Indice do Desenvolvimento Educacional</h2>"
st.markdown(titulo1, unsafe_allow_html=True)

#Texto introdutório sobre o INDE
st.markdown('<p style="text-align: center;font-size:23px;">A PEDE faz a medição do impacto das ações da Associação Passos Mágicos em seus estudantes, e pôde evidenciar alguns comportamentos como evasão escolar dos estudantes e defasagem no aprendizado. Com a PEDE foi elaborado o INDE (Indice de Desenvolvimento Educacional), uma métrica do Processo avaliativo geral do aluno, dado pela Ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV, notas que compõe avaliações acadêmicas, Psicossociais e Psicopedagógicas dos alunos.​  </p>', unsafe_allow_html=True)


    # para montar o gráfico INDE fiz a seguinte consulta
alunos_2020 = df[df['INDE_2020'].notnull()]
alunos_2021 = df[df['INDE_2021'].notnull()]
alunos_2022 = df[df['INDE_2022'].notnull()]

#Gráfico



# Criando o scatter plot dados 2020
scatter_plot = px.scatter (alunos_2020, x=alunos_2020.index, y=alunos_2020['INDE_2020'], title='Classificação - INDE 2020')
# Exibindo o gráfico no Streamlit


scatter_plot1 = px.scatter (alunos_2021, x=alunos_2021.index, y=alunos_2021['INDE_2021'], title='Classificação - INDE 2021')
# Exibindo o gráfico no Streamlit


scatter_plot2 = px.scatter (alunos_2022, x=alunos_2022.index, y=alunos_2022['INDE_2022'], title='Classificação - INDE 2022')
# Exibindo o gráfico no Streamlit


#col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    st.write("")
    st.plotly_chart(scatter_plot, use_container_width=True)
    st.write("")

with col2:
    st.write("")
    st.plotly_chart(scatter_plot1, use_container_width=True)
    st.write("")

with col3:
    st.write("")
    st.plotly_chart(scatter_plot2, use_container_width=True)
    st.write("")




# Segundo Grafico INDE - SUBPLOTS 
    

col1_1, col2_2, col3_3 = st.columns(3)
col_width = 300
fig_width = 60
fig_height = 30

with col1_1:
 plt.figure(figsize=(20,7))
# Criar o gráfico de barras empilhadas
 fig20, ax = plt.subplots()

barras = ax.bar(df_2020['INDE_2020'], df_2020['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('INDE 2020')
plt.ylim(0,40)
# Exibir o gráfico com streamlit
#st.pyplot(fig20)  


with col2_2:
  # Criar o gráfico de barras empilhadas
    fig21, ax = plt.subplots()

barras = ax.bar(df_2021['INDE_2021'], df_2021['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('INDE 2021')
plt.ylim(0,40)
# Exibir o gráfico
#st.pyplot(fig21)  

with col3_3:
 # Criar o gráfico de barras empilhadas
   # Criar o gráfico de barras empilhadas
  fig22, ax = plt.subplots()

barras = ax.bar(df_2022['INDE_2022'], df_2022['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('INDE 2022')
plt.ylim(0,50) 


#Exibir 
col1_1.pyplot(fig20)
col2_2.pyplot(fig21)
col3_3.pyplot(fig22)

  




#Texto conclusivo sobre o INDE

st.markdown('<p style="text-align: center;font-size:23px;">Além do crescimento em número de alunos, analisamos o INDE de 2020 a 2023 e observamos que o índice dos alunos se mantém em sua maioria notas entre 7 e 9.​ É possível observar um aumento  nas notas entre 6,5 e 8,5  no ano de 2022. .​  </p>', unsafe_allow_html=True)
st.markdown("---")


titulo2 = "<h2 style='text-align: center;'>IDA -  Indice de Desenvolvimento Acadêmico</h2>"
st.markdown(titulo2, unsafe_allow_html=True)
# Gráfico IDA 


st.markdown('<p style="text-align: center;font-size:23px;">O IDA (indicador de desenvolvimento acadêmico) é uma dos índices que compões o INDE e compreende as notas das matérias do PAC (programa de aceleração), sendo elas: Português, Matemática e Inglês. .​  </p>', unsafe_allow_html=True)


# Criando o scatter plot dados 2020
scatter_plot = px.scatter (alunos_2020, x=alunos_2020.index, y=alunos_2020['IDA_2020'], title='Classificação - IDA 2020')
# Exibindo o gráfico no Streamlit


scatter_plot1 = px.scatter (alunos_2021, x=alunos_2021.index, y=alunos_2021['IDA_2021'], title='Classificação - IDA 2021')
# Exibindo o gráfico no Streamlit


scatter_plot2 = px.scatter (alunos_2022, x=alunos_2022.index, y=alunos_2022['IDA_2022'], title='Classificação - IDA 2022')
# Exibindo o gráfico no Streamlit


#col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    st.write("")
    st.plotly_chart(scatter_plot, use_container_width=True)
    st.write("")

with col2:
    st.write("")
    st.plotly_chart(scatter_plot1, use_container_width=True)
    st.write("")

with col3:
    st.write("")
    st.plotly_chart(scatter_plot2, use_container_width=True)
    st.write("")



col1_1, col2_2, col3_3 = st.columns(3)
col_width = 300
fig_width = 60
fig_height = 30

with col1_1:
 # Criar o gráfico de barras empilhadas
    fig_a, ax = plt.subplots()

barras = ax.bar(ida_2020['IDA_2020'], ida_2020['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('IDA 2020')
plt.ylim(0,80)
# Exibir o gráfico 


with col2_2:
  ## Criar o gráfico de barras empilhadas
    fig_b, ax = plt.subplots()

barras = ax.bar(ida_2021['IDA_2021'], ida_2021['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('IDA 2021')
plt.ylim(0,30)

with col3_3:
 fig_c, ax = plt.subplots()

barras = ax.bar(ida_2022['IDA_2022'], ida_2022['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('IDA 2022')
plt.ylim(0,20)


#Exibir 
col1_1.pyplot(fig_a)
col2_2.pyplot(fig_b)
col3_3.pyplot(fig_c)



st.markdown('<p style="text-align: center;font-size:23px;">Ao analisar as notas do IDA de forma isolada, notamos o aumento no índice dos 3 anos, que indica que o desenvolvimento acadêmico dos alunos da Associação..​  </p>', unsafe_allow_html=True)
st.markdown("---")


titulo3 = "<h2 style='text-align: center;'>IEG -  Indice de Engajamento</h2>"
st.markdown(titulo3, unsafe_allow_html=True)

# Gráficos IEG - scatter 

scatter_plot = px.scatter (alunos_2020, x=alunos_2020.index, y=alunos_2020['IEG_2020'], title='Classificação - IEG 2020')
# Exibindo o gráfico no Streamlit


scatter_plot1 = px.scatter (alunos_2021, x=alunos_2021.index, y=alunos_2021['IEG_2021'], title='Classificação - IEG 2021')
# Exibindo o gráfico no Streamlit


scatter_plot2 = px.scatter (alunos_2022, x=alunos_2022.index, y=alunos_2022['IEG_2022_'], title='Classificação - IEG 2022')
# Exibindo o gráfico no Streamlit


#col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    st.write("")
    st.plotly_chart(scatter_plot, use_container_width=True)
    st.write("")

with col2:
    st.write("")
    st.plotly_chart(scatter_plot1, use_container_width=True)
    st.write("")

with col3:
    st.write("")
    st.plotly_chart(scatter_plot2, use_container_width=True)
    st.write("")




# fim dos graficos DO SCATTER IEG

    #INICIO DO IEG BARRAS


col1_1, col2_2, col3_3 = st.columns(3)
col_width = 300
fig_width = 60
fig_height = 30

with col1_1:
 # Criar o gráfico de barras empilhadas
    fig_a, ax = plt.subplots()

barras = ax.bar(ige_2020['IEG_2020'], ige_2020['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('IDA 2020')
plt.ylim(0,100)
# Exibir o gráfico 


with col2_2:
  ## Criar o gráfico de barras empilhadas
    fig_b, ax = plt.subplots()

barras = ax.bar(ige_2021['IEG_2021'], ige_2021['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('IDA 2021')
plt.ylim(0,100)

with col3_3:
 fig_c, ax = plt.subplots()

barras = ax.bar(ige_2022['IEG_2022'], ige_2022['TOTAL'], color=cores)

# Adicionar rótulos e título
plt.xlabel('NOTAS')
plt.ylabel('TOTAL')
plt.title('IDA 2022')
plt.ylim(0,100)


#Exibir 
col1_1.pyplot(fig_a)
col2_2.pyplot(fig_b)
col3_3.pyplot(fig_c)

#FIM DO GRAFICO DE BARRAS DE IEG 


st.markdown('<p style="text-align: center;font-size:23px;">O IEG (índice de engajamento), é o indicador que mede o comprometimento do aluno com estudos com a entrega de lição de casa para até a fase 7 e as ações sociais para alunos até a fase 8. Ao analisar as notas do IEG notamos o aumento, denotando  comprometimento pessoal do aluno para o seu desenvolvimento educacional.  </p>', unsafe_allow_html=True)
st.markdown("---")


titulo4 = "<h2 style='text-align: center;'>Pedra Conceito</h2>"
st.markdown(titulo4, unsafe_allow_html=True)

# DADOS PARA O GRÁFICO
#contagem separada dos alunos por pedra conceito 
contagem_alunos_2020 = pd.DataFrame(alunos_2020['PEDRA_2020'].value_counts())
contagem_alunos_2021 = pd.DataFrame(alunos_2021['PEDRA_2021'].value_counts())
contagem_alunos_2022 = pd.DataFrame(alunos_2022['PEDRA_2022'].value_counts())
#unificando a contagem dos alunos por pedra conceito em um dataframe
contagem_alunos_categoria = pd.merge(pd.merge(contagem_alunos_2020, contagem_alunos_2021, left_index=True, right_index=True, how='inner'),  contagem_alunos_2022, left_index=True, right_index=True, how='inner')
#Renomeando a coluna que estavam sem nome, para melhor uso
contagem_alunos_categoria.rename(columns={contagem_alunos_categoria.columns[0] : '2020'}, inplace=True)
contagem_alunos_categoria.rename(columns={contagem_alunos_categoria.columns[1] : '2021'}, inplace=True)
contagem_alunos_categoria.rename(columns={contagem_alunos_categoria.columns[2] : '2022'}, inplace=True)
#resetando o indice para que a coluna com os anos deixe de ser indice
contagem_alunos_categoria=contagem_alunos_categoria.T
contagem_alunos_categoria.reset_index()
contagem_alunos_categoria=contagem_alunos_categoria.T

# Gráfico Pedra conceito 



# Dados para criação do Dataframe
anos = ['2020', '2021', '2022']
categorias = ['Ametista', 'Ágata', 'Quartzo', 'Topázio']
valores = np.array([contagem_alunos_categoria['2020'], contagem_alunos_categoria['2021'], contagem_alunos_categoria['2022']])


# Normalizar para obter porcentagens
valores_percent = (valores / valores.sum(axis=1, keepdims=True)) * 100

# gráfico
fig, ax = plt.subplots()
# Altura fixa para todas as barras
altura_fixa = 100

# Adicionar barras empilhadas
bottom = np.zeros(len(anos))
for i, categoria in enumerate(categorias):
    barras = ax.bar(anos, valores_percent[:, i], label=categoria, bottom=bottom, color=cores[i] )

    # Atualizar a posição inicial para a próxima categoria
    bottom += valores_percent[:, i]

    # Adicionar rótulos de porcentagem dentro de cada faixa de uma coluna
    for bar in barras:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2,
                f'{height/altura_fixa*100:.1f}%', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

#Retirar as grades e bordas pra ficar mais apresentável
sns.despine(ax=ax, left=True, right=True, top=True, bottom=False)
ax.get_yaxis().set_visible(False)
#Títulos 
plt.xlabel(' ')
plt.ylabel(' ')
plt.title('Proporção - Categoria Pedra Conceito por Ano \n \n')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.grid(False)
#exibindo o gráfico
st.pyplot(ax.figure)


st.markdown('<p style="text-align: center;font-size:23px;">A Classificação do Aluno, baseado no INDE, é dada por: ​  </p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;font-size:23px;">Quartzo​ 2,405 a 5,506​ Ágata​ 5,506 a 6,868​ Ametista​ 6,868 a 8,230​ Topázio​ 8,230 a 9,294​ </p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;font-size:23px;">É possível notar o aumento da categoria Topázio, que representa as notas de 8,2 a 9,2 concluindo que o número de alunos que atingiram as notas altas aumentou ao longo dos anos. ​  </p>', unsafe_allow_html=True)

st.markdown("---")

titulo5 = "<h3 style='text-align: center;'>Pedra Conceito - absoluto </h3>"
st.markdown(titulo5, unsafe_allow_html=True)

# Gráfico Pedra conceito  Pedra Conceito -absoluto

#grafico da pedra conceito absoluto

ax = contagem_alunos_categoria.plot(kind='bar', figsize=(10, 6))

# Exibindo o gráfico
plt.suptitle("Categorias por Ano \n \n", fontsize=12)
plt.xlabel(' ')
plt.ylabel(' ')
plt.xticks(rotation=45, ha='right')
plt.grid(False)
plt.ylim(0,450)

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
st.pyplot(ax.figure)

st.markdown('<p style="text-align: center;font-size:23px;">É possível notar o aumento da categoria Topázio, que representa as notas de 8,2 a 9,2 concluindo que o número de alunos que atingiram as notas altas aumentou ao longo dos anos.  ​  </p>', unsafe_allow_html=True)
st.markdown("---")






titulo6 = "<h2 style='text-align: center;'>IPV (Indicador de Ponto de Virada)</h2>"
st.markdown(titulo6, unsafe_allow_html=True)

alunos_virada_2020 = df[df['PONTO_VIRADA_2020'] == 'Sim']
alunos_virada_2020_Total = alunos_virada_2020.shape[0]
alunos_virada_2021 = df[df['PONTO_VIRADA_2021'] == 'Sim']
alunos_virada_2021_Total = alunos_virada_2021.shape[0]
alunos_virada_2022 = df[df['PONTO_VIRADA_2022'] == 'Sim']
alunos_virada_2022_Total = alunos_virada_2022.shape[0]

#Listas de dados
anos = ['2020', '2021', '2022']
total_alunos_ponto_virada = [alunos_virada_2020_Total, alunos_virada_2021_Total, alunos_virada_2022_Total]
#  DataFrame
total_alunos_ponto_virada_df = pd.DataFrame({'Ano': anos, 'Total': total_alunos_ponto_virada})
total_alunos_ponto_virada_df.rename(columns={total_alunos_ponto_virada_df.columns[1] : 'Total_virada'}, inplace=True)


# Gráfico Ponto de Virada
# Configurando o estilo do Seaborn
sns.set_style("whitegrid")

# Criando a figura
plt.figure(figsize=(10, 6))
# Criando o gráfico de barras usando seaborn
ax = sns.barplot(x="Ano", y="Total", data=total_alunos_df, palette=cores, label="Total de Alunos", width=0.50)
ax = sns.barplot(x="Ano", y="Total_virada", data=total_alunos_ponto_virada_df, color="lightblue", bottom=total_alunos_ponto_virada_df["Total_virada"], label="Ponto de Virada", width=0.50)
# Adicionando anotações aos valores das barras
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')
# Removendo as bordas do gráfico
sns.despine(ax=ax, left=True, right=True, top=True, bottom=False)
ax.get_yaxis().set_visible(False)

# Configurando título e eixos do gráfico - alguns títulos em branco 
plt.title("Total de Alunos & Ponto Virada")
plt.xlabel(" ")
plt.ylabel(" ")
plt.legend([])
plt.xticks(rotation=45, ha='right')
plt.grid(False)
# Exibindo o gráfico no Streamlit
st.pyplot(ax.figure)

st.markdown('<p style="text-align: center;font-size:23px;">O Ponto de virada é um momento do desenvolvimento do aluno em que ele demonstra de forma ativa a consciência do valor de aprender, está integrado com os valores da Associação e demonstra capacidade emocional e acadêmica. ​Ou seja, ele compreendeu que poderá transformar a sua vida através da educação. ​Esse não é um ponto de chegada, é um momento de início de uma mudança radical na vida do aluno, onde ele mesmo acredita na mudança da sua vida..  ​  </p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;font-size:23px;">Analisando o crescimento da Passos, nota-se que mais de 12% dos alunos atingiram o ponto de virada nos últimos 3 anos.  ​  </p>', unsafe_allow_html=True)
st.markdown("---")
