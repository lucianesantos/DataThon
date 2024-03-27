#import da biblioteecas necessárias para o projeto
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import openpyxl as op
from prophet import Prophet


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

#Leitura do arquivo com informações das universidades - Passos_universitarios.xlsx
caminho_arquivo_UNI = "https://raw.githubusercontent.com/lucianesantos/DataThon/main/Passos_universitarios_V2.xlsx"
df_uni_cursando = pd.read_excel(caminho_arquivo_UNI, sheet_name='CURSANDO_TOTAL', engine='openpyxl')
df_uni_cursando.rename(columns={df_uni_cursando.columns[2] : 'TOTAL'}, inplace=True)
df_uni_cursando= df_uni_cursando.sort_values(by='TOTAL')
df_uni_cursando  = df_uni_cursando.groupby('CURSO')['TOTAL'].sum().reset_index()

df_uni_concluido = pd.read_excel(caminho_arquivo_UNI, sheet_name='FORMADOS_TOTAL', engine='openpyxl')
df_uni_concluido.rename(columns={df_uni_concluido.columns[2] : 'TOTAL'}, inplace=True)
df_uni_concluido= df_uni_concluido.sort_values(by='TOTAL')
df_uni_concluido  = df_uni_concluido.groupby('CURSO')['TOTAL'].sum().reset_index()

#Criei essa lista de cores. Essas são as cores que extraí do site da passos mágicos. Apesar de não ter achado harmônico, são as cores da passos.
cores = [ '#FBBA00' ,'#257CBB', '#F58334','#FFe01F', '#145089'] #'#FF5931' '#FF8427'  '#FFD401' '#FF2E34'

# início do layout da página
tab0, tab1, tab2, tab3 = st.tabs(["Conheça a Passos Mágicos","Resultados Educacionais", "Análises Externas", "Previsões"])

#fim layout da página




#layout da página inteira
#tab0, tab1 = st.tabs(['   ', ' '])

with tab0:
    st.markdown(' ')
    st.markdown('<p style="text-align: justify;font-size:18px;">A Passos Mágicos é uma associação cuja missão é transformar a vida de crianças e jovens de baixa renda com o objetivo de levá-los a ter melhores oportunidades de vida.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">A associação atua no Município de Embu-Guaçu e essa transformação ocorre através de um Programa que incluí educação, nas disciplinas acadêmicas de Português, Matemática, Inglês e no apoio Psicológico e Psicopedagógico.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">Além do apoio educacional em disciplinas específicas, a passos mágicos possui programas como o apadrinhamento de alunos para concessão de bolsas de estudo em colégios particulares, programa de Intercâmbio Internacional e programas de bolsas integrais para graduações de instituições de ensino superior.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">A passos mágicos também promove ações sociais anuais com o objetivo de ajudar os alunos, para que suas vidas sejam inteiramente impactadas, como campanhas de arrecadação para materiais escolares, campanhas de ovos de páscoa, campanha de arrecadação de presente para o dia das crianças e campanha do agasalho para arrecadar roupas de inverno.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">Atualmente a Passos Mágicos possui parceria com instituições educacionais e estabelecimentos comerciais que a ajuda nesse trabalho de transformação social, educacional e de mudança de realidade de vida.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">Além de empresas investidoras e patrocinadoras que a apoiam nesse trabalho.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">A Passos iniciou suas atividades em 1992 apoiando orfanatos com atendimento psicológico, acadêmico e doações e o projeto Passos Mágicos iniciou suas atividades em 2016 com 70 crianças e no ano de 2023 totalizaram 1100 crianças.</p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:18px;">Para conhecer mais as ações e a Passos, acesse o site https://passosmagicos.org.br/quem-somos/.</p>', unsafe_allow_html=True)
with tab1:
    st.write(' ')

#subtítulos da página
   
    st.markdown('<p style="text-align: justify;font-size:18px;"> Esta análise foi realizada a partir dos metadados provenientes da PEDE - Pesquisa Extensiva de Desenvolvimento Educacional - referentes aos anos de 2020, 2021 e 2022. A PEDE, conduzida anualmente pelo economista Dario Rodrigues Silva, é reconhecida por apresentar os resultados obtidos através da metodologia da Associação Passos Mágicos. </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;"> É importante ressaltar que os dados referentes ao ano de 2023 não foram considerados nesta análise, uma vez que os resultados desta edição serão disponibilizados a partir de abril de 2024.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;"> O propósito desta análise é fornecer uma visão abrangente do desenvolvimento educacional dos alunos da Associação Passos Mágicos, alcançados pelo Programa de Aceleração, destacando as notas, a fim de evidenciar os benefícios da metodologia adotada pela instituição tanto para os alunos quanto para a sociedade em geral. </p>', unsafe_allow_html=True)    
    

    st.markdown('<p style="text-align: center;font-size:16px;font-weight: bold;">By Luciane dos Santos Reis & Leonardo Santos Rodrigues & Marcelo Meirelles Junior  </p>', unsafe_allow_html=True)
    st.markdown ('')

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

    ax = sns.barplot(data=total_alunos_df,  x='Ano', y='Total',  palette=cores, width=0.50, hue=None)

    for p in ax.patches:
        ax.annotate(format(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

    #sns.despine(ax=ax, left=True, right=True, top=True, bottom=False)
    #ax.get_yaxis().set_visible(False)

    plt.suptitle("Alunos por Ano", fontsize=12)
    plt.xlabel(' ')
    plt.ylabel('Total de alunos por ano ')
    plt.xticks(rotation=45, ha='right')
    plt.grid(False)
    plt.ylim(0,1000)
    st.pyplot(ax.figure)

######

    st.markdown("    ")
    st.markdown("    ")
    st.markdown('<p style="text-align: justify;font-size:23px;">É possível notar que a Associação Passos Mágicos cresceu ao longo dos anos em termos de matrículas de alunos, atingindo em um total de 1100 alunos matriculados no ano de 2023. </p>', unsafe_allow_html=True)
    st.markdown("---")



# Gráfico PEDE - INDE

    titulo1 = "<h2 style='text-align: center;'>INDE - Indice do Desenvolvimento Educacional</h2>"
    st.markdown(titulo1, unsafe_allow_html=True)

#Texto introdutório sobre o INDE
    st.markdown('<p style="text-align: justify;font-size:23px;">O INDE - Indice de Desenvolvimento Educacional - é uma metrica do Processo avaliativo geral do aluno, desenvolvida na PEDE (Pesquisa Extensiva de Desenvolvimento Educacional), dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV, notas que compõe avaliações acadêmicas, psicossociais e psicopedagógicas dos alunos.​ Essa medição apresenta o impacto das ações da Associação Passos Mágicos em seus estudantes, e evidencia alguns comportamentos como evasão escolar dos estudantes e defasagem no aprendizado. </p>', unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    # para montar o gráfico INDE fiz a seguinte consulta
    alunos_2020 = df[df['INDE_2020'].notnull()]
    alunos_2021 = df[df['INDE_2021'].notnull()]
    alunos_2022 = df[df['INDE_2022'].notnull()]

#Gráfico

# Criando o scatter plot dados 2020
   #scatter_plot = px.scatter (alunos_2020, x=alunos_2020.index, y=alunos_2020['INDE_2020'], title='Classificação - INDE 2020')
# Exibindo o gráfico no Streamlit


    #scatter_plot1 = px.scatter (alunos_2021, x=alunos_2021.index, y=alunos_2021['INDE_2021'], title='Classificação - INDE 2021')
# Exibindo o gráfico no Streamlit


    #scatter_plot2 = px.scatter (alunos_2022, x=alunos_2022.index, y=alunos_2022['INDE_2022'], title='Classificação - INDE 2022')
# Exibindo o gráfico no Streamlit


#col1, col2, col3 = st.columns(3)
    #col1, col2, col3 = st.columns([2, 2, 2])
    #with col1:
        #st.write("")
        #st.plotly_chart(scatter_plot, use_container_width=True)
        #st.write("")

    #with col2:
        #st.write("")
        #st.plotly_chart(scatter_plot1, use_container_width=True)
        #st.write("")

    #with col3:
        #st.write("")
       # st.plotly_chart(scatter_plot2, use_container_width=True)
        #st.write("")



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
    st.markdown(" ")
    st.markdown('<p style="text-align: justify;font-size:23px;">Os gráficos nos mostra que o INDE dos alunos se mantém em sua maioria em notas entre 7 e 9 do período analisado, de 2020 a 2022. Observa-se um aumento das notas entre 6,5 e 8,5 no ano de 2022.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:23px;"> Além do crescimento em matrículas, observamos que os alunos possuem notas de desenvolvimento educacional consideravelmente altos ao longo do período analisado. </p>', unsafe_allow_html=True)
    st.markdown("---")


    titulo2 = "<h2 style='text-align: center;'>IDA -  Indice de Desenvolvimento Acadêmico</h2>"
    st.markdown(titulo2, unsafe_allow_html=True)
# Gráfico IDA 


    st.markdown('<p style="text-align: justify;font-size:23px;">O IDA (indicador de desenvolvimento acadêmico) é uma dos índices que compões o cálculo do INDE e compreende as notas das matérias do PAC (programa de aceleração), sendo elas: Português, Matemática e Inglês.  </p>', unsafe_allow_html=True)


# Criando o scatter plot dados 2020
    #scatter_plot = px.scatter (alunos_2020, x=alunos_2020.index, y=alunos_2020['IDA_2020'], title='Classificação - IDA 2020')
# Exibindo o gráfico no Streamlit


    #scatter_plot1 = px.scatter (alunos_2021, x=alunos_2021.index, y=alunos_2021['IDA_2021'], title='Classificação - IDA 2021')
# Exibindo o gráfico no Streamlit


    #scatter_plot2 = px.scatter (alunos_2022, x=alunos_2022.index, y=alunos_2022['IDA_2022'], title='Classificação - IDA 2022')
# Exibindo o gráfico no Streamlit


#col1, col2, col3 = st.columns(3)
    #col1, col2, col3 = st.columns([2, 2, 2])
    #with col1:
        #st.write("")
        #st.plotly_chart(scatter_plot, use_container_width=True)
        #st.write("")

    #with col2:
        #st.write("")
        #st.plotly_chart(scatter_plot1, use_container_width=True)
        #st.write("")

    #with col3:
        #st.write("")
        #st.plotly_chart(scatter_plot2, use_container_width=True)
        #st.write("")



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


    st.markdown(" ")
    st.markdown('<p style="text-align: justify;font-size:23px;">Ao analisar as notas do IDA de forma isolada, notamos o aumento no índice dos 3 anos, que indica que o desenvolvimento acadêmico dos alunos da Associação nas disciplinas do Programa de Aceleração..​  </p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(" ")

    titulo3 = "<h2 style='text-align: center;'>IEG -  Indice de Engajamento</h2>"
    st.markdown(titulo3, unsafe_allow_html=True)

# Gráficos IEG - scatter 

    scatter_plot = px.scatter (alunos_2020, x=alunos_2020.index, y=alunos_2020['IEG_2020'], title='Classificação - IEG 2020')

    scatter_plot1 = px.scatter (alunos_2021, x=alunos_2021.index, y=alunos_2021['IEG_2021'], title='Classificação - IEG 2021')

    scatter_plot2 = px.scatter (alunos_2022, x=alunos_2022.index, y=alunos_2022['IEG_2022_'], title='Classificação - IEG 2022')


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
    plt.title('IEG 2020')
    plt.ylim(0,100)
# Exibir o gráfico 


    with col2_2:
  ## Criar o gráfico de barras empilhadas
        fig_b, ax = plt.subplots()

    barras = ax.bar(ige_2021['IEG_2021'], ige_2021['TOTAL'], color=cores)

# Adicionar rótulos e título
    plt.xlabel('NOTAS')
    plt.ylabel('TOTAL')
    plt.title('IEG 2021')
    plt.ylim(0,100)

    with col3_3:
        fig_c, ax = plt.subplots()

    barras = ax.bar(ige_2022['IEG_2022'], ige_2022['TOTAL'], color=cores)

# Adicionar rótulos e título
    plt.xlabel('NOTAS')
    plt.ylabel('TOTAL')
    plt.title('IEG 2022')   
    plt.ylim(0,100)


#Exibir 
    col1_1.pyplot(fig_a)
    col2_2.pyplot(fig_b)
    col3_3.pyplot(fig_c)

#FIM DO GRAFICO DE BARRAS DE IEG 

    st.markdown(" ")
    st.markdown('<p style="text-align: justify;font-size:23px;">O IEG (índice de engajamento), é o indicador que mede o comprometimento do aluno com estudos, a entrega de lição de casa para alunos até a fase 7 e a participação nas ações sociais para alunos da fase 8. Ao analisar as notas do IEG notamos o aumento, denotando  comprometimento pessoal do aluno para o seu desenvolvimento educacional e participação nos projetos.  </p>', unsafe_allow_html=True)
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


    st.markdown('<p style="text-align: center;font-size:23px;">A Classificação do Aluno, baseado nas notas do INDE, é dada por: ​  </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:23px;">Quartzo​ 2,405 a 5,506​ </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:23px;">Ágata​ 5,506 a 6,868​ </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:23px;">Ametista​ 6,868 a 8,230​ </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:23px;">Topázio​ 8,230 a 9,294​ </p>', unsafe_allow_html=True)

    st.markdown('<p style="text-align: justify;font-size:23px;">É possível notar o aumento da categoria Topázio, que representa as notas de 8,2 a 9,2 concluindo que o número de alunos que atingiram as notas altas aumentou ao longo dos anos. ​  </p>', unsafe_allow_html=True)

    st.markdown("---")

    titulo5 = "<h3 style='text-align: center;'>Pedra Conceito - absoluto </h3>"
    st.markdown(titulo5, unsafe_allow_html=True)

# Gráfico Pedra conceito  Pedra Conceito -absoluto

#grafico da pedra conceito absoluto

    ax = contagem_alunos_categoria.plot(kind='bar', figsize=(10, 6),  color=cores)

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

    st.markdown('<p style="text-align: justify;font-size:23px;">    </p>', unsafe_allow_html=True)
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

    st.markdown('<p style="text-align: justify;font-size:23px;">O Ponto de virada é um momento do desenvolvimento do aluno em que ele demonstra de forma ativa a consciência do valor de aprender, apresenta estar integrado com os valores da Associação e demonstra capacidade emocional e acadêmica, ou seja, ele compreendeu que poderá transformar a sua vida através da educação. </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:23px;"> ​Esse não é um ponto de chegada, é um momento de início de uma mudança radical na vida do aluno, onde ele mesmo acredita na mudança da sua vida. </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:23px;">Analisando o crescimento da Passos, nota-se que mais de 12% dos alunos atingiram o ponto de virada nos últimos 3 anos.  ​  </p>', unsafe_allow_html=True)
    st.markdown("---")




    titulo7 = "<h2 style='text-align: center;'>Alunos Universitários</h2>"
    st.markdown(titulo7, unsafe_allow_html=True)
#grafico universidades 
    plt.figure(figsize=(15, 9))
    ax = sns.barplot(data=df_uni_cursando,  x='CURSO', y='TOTAL',  palette=cores, width=0.80)#, width=0.70)

# Exibindo o gráfico
    plt.suptitle("Alunos Universitários Cursando\n \n", fontsize=12)
    plt.xlabel(' ')
    plt.xticks(rotation=75, ha='right')
    plt.grid(False)
    plt.ylim(0,9)

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    st.pyplot(ax.figure)

    st.markdown('<p style="text-align: justify;font-size:23px;">Atualmente a Passos possui 61 alunos universitários estudando em instituições como FIAP, UNISA, Anhembi Morumbi, Cruzeiro do Sul, ESPM, Estácio de Sá, Fundação Getúlio Vargas, Insper, Mackenzie, Oswaldo Cruz e UNICAMP nos diversos cursos de formação descrito no gráfico. Todos os alunos são bolsista das instituições. Isso nos mostra que o Programa de Aceleração do Projeto Passos Mágicos e todo acompanhamento e ações que visam transformar a vida do aluno, ​os leva para caminhos que sem a Passos Mágicos eles não poderiam andar.  </p>', unsafe_allow_html=True)
    st.markdown("---")

    



    titulo7 = "<h2 style='text-align: center;'>Alunos Universitários Formados</h2>"
    st.markdown(titulo7, unsafe_allow_html=True)
#grafico universidades 
    plt.figure(figsize=(15, 9))
    ax = sns.barplot(data=df_uni_concluido,  x='CURSO', y='TOTAL',  palette=cores, width=0.50) #, hue='INSTITUIÇÃO', width=0.70)

# Exibindo o gráfico
    plt.suptitle("Alunos Universitários Formados\n \n", fontsize=12)
    plt.xlabel(' ')
    plt.xticks(rotation=75, ha='right')
    plt.grid(False)
    plt.ylim(0,9)

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    st.pyplot(ax.figure)

    st.markdown('<p style="text-align: center;font-size:23px;">A Passos já formou ao longo dos anos, 59 alunos nos diversos cursos universitários demonstrados neste gráfico. Todos os alunos foram bolsistas nas universidades. </p>', unsafe_allow_html=True)
    st.markdown("---")

with tab2:
    #st.write(' ') #Análises externas
    st.markdown('<p style="text-align: center;font-size:23px;">A População de Embu-Guaçu</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:12px;">Fontes: https://cidades.ibge.gov.br/brasil/sp/embu-guacu/panorama, https://qedu.org.br/municipio/3515103-embu-guacu  </p>', unsafe_allow_html=True) 
    st.markdown('  ')
    
    
    col2_1, col2_2 = st.columns(2)
    col_width = 300
    fig_width = 60
    fig_height = 30

    with col2_1:
        image_mapa = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/Mapa.png'
        st.image(image_mapa, caption=' ', width=350)
        
    with col2_2:
        image_mapa_legenda = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/Mapa_legenda.png'
        st.image(image_mapa_legenda, caption=' ', width=350)
        
                
    st.markdown('<p style="text-align: justify;font-size:18px;">Segundo o site do IBGE, a população da cidade de Embu-Guaçu era de 66.970 pessoas no ano de 2022 </p>', unsafe_allow_html=True)
    st.markdown('   ')
    st.markdown('   ')    


#URL da imagem
    image_populacao = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/populacao.png'
    st.image(image_populacao, caption=' ', width = 700)
    st.markdown('<p style="text-align: justify;font-size:18px;">A maioria da população no ano de 2022 era de mulheres, de raça branca, compreendendo a faixa etária dos 40 a 44 anos.</p>', unsafe_allow_html=True)
    st.markdown('   ')
    st.markdown('   ')   

# Exibe a imagem
    st.markdown('<p style="text-align: center;font-size:23px;">A Educação em Embu-Guaçu</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:12px;">Fonte: https://www.gov.br/mec/pt-br </p>', unsafe_allow_html=True)
    st.markdown(' ')
 
    image_escola = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/escolas.png'
    st.image(image_escola, caption=' ', width=750)
    st.markdown('<p style="text-align: justify;font-size:18px;">Segundo o Ministério da educação, no ano de 2020, a maioria das escolas do municipio de Embu-Guaçu eram Municipais, seguido das escolas Estaduais e o menor percentual são as Escolas Privadas. </p>', unsafe_allow_html=True)
    
   
    image_escola1 = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/escolas1.png'
    st.image(image_escola1, caption=' ', width=600)
    st.markdown('<p style="text-align: justify;font-size:18px;">No ano de 2020, a maioria dos estudantes estavam nos anos iniciais do ensino fundamental, seguido dos anos finais do ensino fundamental. Observa-se um menor percentual de alunos no Ensino Médio.  </p>', unsafe_allow_html=True)
    

    
    image_ideb = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/IDEB.png'
    st.image(image_ideb, caption=' ', width=600)
    st.markdown('<p style="text-align: center;font-size:12px;">Fonte: https://qedu.org.br/ </p>', unsafe_allow_html=True)
 
    st.markdown('<p style="text-align: justify;font-size:18px;">O IDEB é o Índice de Desenvolvimento da Educação Básica, criado em 2007, pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep), formulado para medir a qualidade do aprendizado nacional e estabelecer metas para a melhoria do ensino.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;">O índice varia numa escala de 0 a 10 e é calculado a cada dois anos para escolas e redes de ensino de todo o Brasil. O IDEB tem como objetivo principal estabelecer metas para a melhoria do ensino. Para cada escola, rede de ensino municipal, estadual e para o país como um todo, são estabelecidas metas de qualidade que devem ser alcançadas em períodos determinados, visando à elevação contínua do nível educacional. </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;">O IDEB serve como um importante instrumento para diagnóstico e planejamento das políticas públicas em educação, apontando não apenas as necessidades de melhorias em termos de infraestrutura e práticas pedagógicas, mas também destacando as escolas e redes de ensino que obtêm bons resultados, servindo de modelo para as demais.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;">Uma "nota boa" no IDEB é relativa, pois depende de superar as metas específicas definidas para cada escola, município ou estado, considerando o contexto e os objetivos educacionais. Assim, uma mesma nota pode ser vista de maneira diferente: como positiva se a meta for superada ou como indicativa de necessidade de melhorias se a meta não for alcançada.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;font-size:12px;">Fonte: http://portal.mec.gov.br/conheca-o-ideb </p>', unsafe_allow_html=True)

    
    st.markdown('<p style="text-align: justify;font-size:18px;">Ao analisarmos as notas do IDEB, disponíveis no site qedu.org.br, dos anos de 2019 e 2021, observamos que as notas estão entre 5 e 6. </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;">Se fosse possível comparar diretamente as notas do IDEB e do IDA, perceberíamos que, enquanto as notas do IDA tendem a ficar entre 6,5 e 8, as maiores notas alcançadas pelo IDEB nos anos de 2019 e 2021 ficaram abaixo de 6,4. </p>', unsafe_allow_html=True)
  


    image_distorção = 'https://raw.githubusercontent.com/lucianesantos/DataThon/main/distorção.png'
    st.image(image_distorção, caption=' ', width=600)
    st.markdown('<p style="text-align: center;font-size:12px;">Fonte: https://qedu.org.br/ </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;">Ao analisarmos as distorções entre idade e série, também disponíveis no site qedu.org.br, observa-se que no ano de 2020, 6,1% dos alunos ingressaram no 1o ano do ensino médio com idade atrasada para a série indicada. Esse percentual aumenta um ponto percentual em 2021 e diminuiu para 5.7% em 2022. Essa distorção é refletida e identificada na Passos, no momento em que o aluno ingressa para o Programa de Aceleração e ao longo dos anos participando essa distorção desaparece. </p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: justify;font-size:18px;">É difícil comparar os resultados da Passos com outra escola de ensino tradicional, porém ao analisarmos seus resultados através da PEDE fazendo correlação com as informações sociais e educacionais disponíveis, compreendemos que os alunos que frequentam a passos permanecem mais na escola, concluem o ensino médio e entram na faculdade sendo esse um impacto real na sociedade. </p>', unsafe_allow_html=True)

with tab3:
    st.write(' ')

    st.markdown('<p style="text-align: justify;font-size:18px;">Efetuamos a previsão do crescimento de alunos da Passos, para os proximos 5 anos. Entendemos que crescer de forma segura e gradativa é importante para ser sustentável e possibilitar diversas tomadas de decisão. Assim será possível que a Passos planeje estrategicamente essa expansão para ter um desenvolvimento equilibrado e aumente o impacto na sociedade.</p>', unsafe_allow_html=True)
    st.markdown(' ')



    url = "https://raw.githubusercontent.com/lucianesantos/DataThon/main/Numero_de_alunos.xlsx"
    df_qtd_alunos = pd.read_excel(url)

    m = Prophet(yearly_seasonality=True)
    m.fit(df_qtd_alunos)
    future_dates = m.make_future_dataframe(periods=6, freq='YS')
    forecast = m.predict(future_dates)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    #fig1 = m.plot(forecast)

    fig, ax = plt.subplots(figsize=(18, 7))  
    m.plot(forecast, ax=ax)
    st.pyplot(fig)