import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from Scripts import utils
import plotly.express as px
import seaborn as sns
import stemgraphic

if __name__ == '__main__':
    st.set_page_config(page_title="Analise de dados das Bolsas e Auxílios Pagos pelo CNPq", layout="centered")
    st.header("ANALISE DE DADOS DAS BOLSAS E AUXÍLIOS PAGOS PELO CNPQ")
    st.divider()
    st.header("Equipe Responsavel")
    st.write("Lidy Emanuelle Marinho Santos [22153869]")
    st.write("Liliene Picanço Pereira [22153491]")
    st.write("Vinicius Melchior Liborio Santos [22153668]")
    st.divider()
    st.subheader("1. INTRODUÇÃO")
    st.write("Este relatório foi solicitado pelo Prof.Dr.Hidelbrando Ferreira como parte das atividades avaliativas da "
             "disciplina de Probabilidade e Estatística do curso de Engenharia de Software. A atividade consiste na "
             "produção de um relatório estatístico com base na análise de dados, a escolha dos integrantes da equipe "
             "formada por Lidy Santos, Liliene Picanço e Vinicius Melchior e recuperados do repositório Base dos Dados "
             "com o auxílio da API BigQuery."
             "A base a ser analisada tem como título “Auxílios e bolsas pagas pelo CNPQ”. Considerando-se o caráter da "
             "atividade e o tamanho da base de dados, foram escolhidas quatro variáveis como foco da pesquisa sendo "
             "elas ano, subárea, valor e área. Com tais variáveis serão realizados cálculos para fundamentar e "
             "apresentar elementos básicos da estatística como média, mediana, moda, variância, desvio padrão,"
             "entre outros, além de representação em gráficos que"
             "poderão favorecer e otimizar o processo da análise de dados acompanhados de uma breve discussão acerca "
             "dos resultados obtidos")
    st.divider()
    st.subheader("2. ANALISE EXPLORATÓRIA DOS DADOS")
    st.write("Neste tópico de análise exploratória dos dados, examinaremos os dados de forma a identificar padrões, "
             "tendências, anomalias e relações entre as variáveis, buscando obter uma visão geral dos dados, "
             "verificar sua qualidade e adequação.")
    st.divider()
    base = utils.load_data()

    with st.container():
        st.subheader("2.1 Exploração estatica do Dataframe")
        st.write("A exploração estática dos dados consiste em aplicar técnicas e métodos estatísticos para descrever "
                 "e resumir as características principais de um conjunto de dados. Nesta exploração estática dos "
                 "dados que foi realizada por meio de medidas de tendência central, medidas de dispersão, medidas de "
                 "forma e medidas de posição, busca-se fornecer uma visão geral dos dados da base analisada.")
        st.divider()
        st.subheader("2.1.1 Tabela de distribuição de frequencia da variavel valor")
        st.write("Uma das variáveis escolhidas para a análise dos dados da base Auxílios e bolsas pagas pelo CNPQ foi "
                 "o valor da bolsa, que representa a quantia mensal recebida pelo beneficiário. Para facilitar a "
                 "visualização e interpretação dos dados, foi construída uma tabela de distribuição de frequência, "
                 "que agrupa os valores da bolsa em classes de amplitude igual e mostra quantas observações se "
                 "enquadram em cada classe. A tabela também apresenta as frequências relativas, que indicam a "
                 "proporção de cada classe em relação ao total de dados, e as frequências acumuladas, que mostram o "
                 "número de observações menores ou iguais a um determinado valor da classe. A tabela de distribuição "
                 "de frequência da variável valor da bolsa é mostrada a seguir:")
        tdf1 = utils.frequency_table(base["valor"])
        st.table(tdf1)
        st.divider()
        st.subheader("2.1.2 Estatistica Descritiva")
        st.write("O objetivo deste tópico é fornecer uma descrição simples e objetiva dos dados, que possa servir de "
                 "base para análises e/ou tomada de decisões por meio da estatística descritiva, utilizando medidas "
                 "de tendência central, como média, mediana e moda, para resumir os valores dos dados e indicar sua "
                 "distribuição, utilizou-se também medidas de dispersão, como variância e desvio padrão, "
                 "para quantificar a variabilidade dos dados e mostrar o quanto eles se afastam da média. ")
        ed1 = utils.describe_data(base)
        edv1 = utils.describe_data_variable(base)
        st.divider()

        col11, col12 = st.columns(2)
        col11.subheader("Medidas de tendencia central")
        col11.dataframe(ed1)

        col12.subheader("Medidas de variabilidade")
        col12.dataframe(edv1)

        col11.subheader("Separatrizes")
        edq1 = utils.describe_data_quarts(base)
        col11.dataframe(edq1)

        col12.subheader("Medidas de assimetria")
        eda1 = utils.describe_data_assim(base)
        col12.dataframe(eda1)

        col12.subheader("Outras Medidas")
        edo1 = utils.describe_data_others(base)
        col12.dataframe(edo1)

        st.divider()

        st.subheader("2.1.3 Grafico da Estatistica Descritiva")
        st.write("Nesta seção gráficos é apresentado uma visão geral das variaveis da estatistica descritiva dos "
                 "auxílios e bolsas pagos pelo CNPQ ao longo dos anos.")
        datas = utils.plot_grafing_mean(base)
        datas = pd.DataFrame(datas)
        co1, co2 = st.columns(2)
        co3, co4 = st.columns(2)
        co1.write("A) Variavel minimo ao longo dos anos")
        co1.pyplot(utils.graf_lines_min(datas))
        co2.write("B) Variavel maximo ao longo dos anos")
        co2.pyplot(utils.graf_lines_max(datas))
        co3.write("C) Variavel media ao longo dos anos")
        co3.pyplot(utils.graf_lines_med(datas))
        co4.write("D) Variavel mediana ao longo dos anos")
        co4.pyplot(utils.graf_lines_median(datas))
        st.write("E) Variavel moda ao longo dos anos")
        st.pyplot(utils.graf_lines_moda(datas))

    with st.container():
        st.divider()
        st.subheader("2.2 Exploração Dinamica do Dataframe")
        st.write("A partir do dataframe criado com os dados dos auxílios e bolsas pagos pelo CNPQ, aplicamos filtros "
                 "de ano, modalidade e área para obter subconjuntos de dados de interesse. Por exemplo, "
                 "podemos filtrar os dados para visualizar apenas os auxílios e bolsas pagos no ano de 2020, "
                 "na modalidade de iniciação científica no país e na área de engenharias. Com isso, podemos observar "
                 "as características e tendências desses dados, como a distribuição dos valores, as subáreas mais "
                 "contempladas, a média e o desvio padrão do valor dos auxílios e bolsas, por meio da demonstração  "
                 "de tabelas, gráficos e diagramas.")
        st.divider()
        st.subheader("2.2.1 Filtro")
        colect1, colect2, colect3 = st.columns(3)
        ano = colect1.selectbox("Selecione o ano", [2002, 2003, 2004, 2005, 2006, 2007,
                                                    2008, 2009, 2010, 2011, 2012, 2013,
                                                    2014, 2015, 2016, 2017, 2018, 2019,
                                                    2020, 2021, 2022])
        listz = base["modalidade"]
        modalidade = colect2.selectbox("Selecione a modalidade", listz.unique())
        listy = base["area_conhecimento"]
        area = colect3.selectbox("Selecione a area", listy.unique())
        df = utils.load_select_data(ano, modalidade, area)
        df = df.dropna()
        st.dataframe(df)
        st.divider()

        st.subheader("2.2.2 Tabela de distribuição de frequencia da variavel valor")
        st.write("Uma para analisar a variável valor do data frame,  construiu-se uma tabela de distribuição de "
                 "frequência, que divide os valores da bolsa em intervalos iguais e conta quantos dados pertencem a "
                 "cada intervalo. A tabela também inclui as frequências relativas, que expressam a porcentagem de "
                 "cada intervalo em relação ao total de dados, e as frequências acumuladas, que indicam o número de "
                 "dados menores ou iguais a um certo valor do intervalo. A tabela de distribuição de frequência da "
                 "variável valor da bolsa é exibida abaixo:")

        tf = utils.frequency_table(df["valor"])
        st.table(tf)
        st.divider()

        st.subheader("2.2.3 Estatistica Descritiva")
        st.write("O objetivo deste tópico é fornecer uma descrição simples e objetiva dos dados, que possa servir de "
                 "base para análises e/ou tomada de decisões por meio da estatística descritiva, utilizando medidas "
                 "de tendência central, como média, mediana e moda, para resumir os valores dos dados e indicar sua "
                 "distribuição, utilizou-se também medidas de dispersão, como variância e desvio padrão, "
                 "para quantificar a variabilidade dos dados e mostrar o quanto eles se afastam da média.")
        ed = utils.describe_data(df)
        edv = utils.describe_data_variable(df)
        st.divider()

        col1, col2 = st.columns(2)
        col1.subheader("Medidas de tendencia central")
        col1.dataframe(ed)

        col2.subheader("Medidas de variabilidade")
        col2.dataframe(edv)

        col1.subheader("Separatrizes")
        edq = utils.describe_data_quarts(df)
        col1.dataframe(edq)

        col2.subheader("Medidas de assimetria")
        eda = utils.describe_data_assim(df)
        col2.dataframe(eda)

        col2.subheader("Outras Medidas")
        edo = utils.describe_data_others(df)
        col2.dataframe(edo)
        st.divider()

    with st.container():
        st.subheader("Analise Grafica")
        st.divider()
        st.write("Nesta seção de análise gráfica apresentam-se os resultados de forma objetiva para a  visualização "
                 "das tendências, as relações e as distribuições dos dados, para facilitar a interpretação.")
        st.divider()
        st.subheader("Grafico de barras")
        plt.figure()
        st.pyplot(utils.plotar_grafico(df["subarea_conhecimento"], df["valor"]))

        st.divider()
        st.subheader("Diagrama de ramo e folhas")
        ramos, folhas = utils.stem_and_leaf_plot(df["valor"])
        fig, ax = plt.subplots()
        for i in range(len(ramos)):
            ax.stem([ramos[i]] * len(folhas[i]), sorted(folhas[i]), linefmt='-', markerfmt='o', basefmt=' ')
        ax.set_xlabel('Ramo')
        ax.set_ylabel('Folha')
        ax.set_title('Gráfico de Ramo e Folha')
        st.pyplot(fig)

        st.divider()
        st.subheader("Histograma do dado valor")
        plt.figure()
        plt.hist(df["valor"], bins='auto', alpha=0.7, rwidth=0.85)
        plt.title('Histograma')
        plt.xlabel('Valores')
        plt.ylabel('Frequência')
        st.pyplot()

        st.divider()
        st.subheader(" Grafico Ogiva(de Galton)")
        data_sorted = sorted(df["valor"])
        cumulative_freq = [i for i in range(1, len(data_sorted) + 1)]
        plt.plot(data_sorted, cumulative_freq, marker='o', linestyle='-')
        plt.title('Diagrama de Ogiva (Gráfico de Galton)')
        plt.xlabel('Valores')
        plt.ylabel('Frequência Acumulada')
        st.pyplot()

        st.divider()
        st.subheader("Grafico de Boxplot")
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df["valor"], orient="v", width=0.5, palette="Set2")
        plt.title('Boxplot')
        plt.xlabel('Valores')
        st.pyplot()

    st.divider()
    st.subheader("DISCUSSÕES")
    st.write("Os recursos dos fundos setoriais, criados a partir de 1999, são transferidos ao CNPq para ações "
             "específicas de fomento à pesquisa ou bolsas definidas por seus comitês gestores. Desde 2002, "
             "observa-se um acentuado incremento no aporte de recursos destinados a bolsas e auxílios, porém com uma "
             "queda em suas medidas da estatística descritiva dos auxílios e bolsas pagos pelo CNPQ ao longo dos "
             "anos. Um importante desafio para a ciência nacional é a sua desconcentração em programas de "
             "pós-graduação, ampliando as suas atividades nas várias modalidades como as iniciações científicas "
             "júnior(ICJ). Embora seja esperado uma concentração de atividade científica desde o início da coleta de "
             "dados para a análise, somente a partir de 2018 as ICJ ganharam um número maior de participantes, "
             "onde pode-se associar exclusão de muitos benefícios da ciência. Ampliar a ciência equivale a aumentar a "
             "exposição de jovens a essa atividade, potencializando a nossa capacidade de descobrir e recrutar "
             "talentos.")
    st.divider()
    st.subheader("CONCLUSÃO")
    st.write("A partir do trabalho desenvolvido, conclui-se que a estatística é um instrumento de altíssima "
             "relevância para  o atual cenário de crescimento socioeconômico, pois a partir da aplicação dessa "
             "ferramenta é possível adquirir insights com alto poder de transformação tanto em cenário empresarial "
             "como social. Além disso, por meio dos resultados da análise de dados referentes ao pagamento de "
             "auxílios e bolsas CNPQ destaca-se seu papel de extrema importante no cenário brasileiro, mas os dados "
             "mostrados refletem apenas uma parte da realidade. Levando isso em conta, podemos afirmar que o Brasil "
             "conseguiu avançar em alguns aspectos, como a popularização da ciência, o aumento dos recursos "
             "destinados ao programa de desenvolvimento científico regional, investimentos em R$ milhões de bolsas e "
             "auxílios concedidos, ampliando o apoio à qualificação de pessoal e estabeleceu novas linhas de pesquisa.")
