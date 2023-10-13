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
    st.write("Lidy Emanuelle Marinho Santos [22153869]")
    st.write("Liliene Picanço Pereira [22153491]")
    st.write("Vinicius Melchior Liborio Santos [22153668]")
    st.divider()
    st.subheader("INTRODUÇÃO")
    st.subheader("ANALISE EXPLORATÓRIA DOS DADOS")
    base = utils.load_data()
    base = base.dropna()

    with st.container():
        st.subheader("Exploração estatica do Dataframe")
        st.subheader("Tabela de distribuição de frequencia da variavel valor")
        tdf1 = utils.frequency_table(base["valor"])
        st.table(tdf1)

        st.subheader("Estatistica Descritiva")
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

        datas = utils.plot_grafing_mean(base)
        datas = pd.DataFrame(datas)
        st.pyplot(utils.graf_lines_min(datas))
        st.pyplot(utils.graf_lines_max(datas))
        st.pyplot(utils.graf_lines_med(datas))
        st.pyplot(utils.graf_lines_median(datas))
        st.pyplot(utils.graf_lines_moda(datas))

    with st.container():
        st.subheader("Exploração Dinamica do Dataframe")
        st.text("Filtro")
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

        st.subheader("Tabela de distribuição de frequencia da variavel valor")
        tf = utils.frequency_table(df["valor"])
        st.table(tf)

        st.subheader("Estatistica Descritiva")
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
        st.subheader("Grafico de barras")
        st.pyplot(utils.plotar_grafico(df["subarea_conhecimento"], df["valor"]))

        st.subheader("Diagrama de ramo e folhas")
        ramos, folhas = utils.stem_and_leaf_plot(df["valor"])
        fig, ax = plt.subplots()
        for i in range(len(ramos)):
            ax.stem([ramos[i]] * len(folhas[i]), sorted(folhas[i]), linefmt='-', markerfmt='o', basefmt=' ')
        ax.set_xlabel('Ramo')
        ax.set_ylabel('Folha')
        ax.set_title('Gráfico de Ramo e Folha')
        st.pyplot(fig)

        st.subheader("Histograma do dado valor")
        plt.figure()
        plt.hist(df["valor"], bins='auto', alpha=0.7, rwidth=0.85)
        plt.title('Histograma')
        plt.xlabel('Valores')
        plt.ylabel('Frequência')
        st.pyplot()

        st.subheader("Ogiva(de Galton)")
        data_sorted = sorted(df["valor"])
        cumulative_freq = [i for i in range(1, len(data_sorted) + 1)]
        plt.plot(data_sorted, cumulative_freq, marker='o', linestyle='-')
        plt.title('Diagrama de Ogiva (Gráfico de Galton)')
        plt.xlabel('Valores')
        plt.ylabel('Frequência Acumulada')
        st.pyplot()

        st.subheader("Boxplot")
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df["valor"], orient="v", width=0.5, palette="Set2")
        plt.title('Boxplot')
        plt.xlabel('Valores')
        st.pyplot()

    st.subheader("DISCUSSÕES")
    st.subheader("RESULTADOS OBTIDOS")
    st.subheader("DISCUSSÕES")
    st.subheader("CONCLUSÃO")
