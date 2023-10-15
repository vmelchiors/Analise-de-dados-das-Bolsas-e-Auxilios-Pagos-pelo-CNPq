import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt


@st.cache_data
def load_data():
    df = pd.read_csv("./Data/Database_filter.csv", sep=",", decimal=".")
    return df


@st.cache_data
def load_colun(data, colun):
    valor = pd.DataFrame(data, columns=[f'{colun}'])
    tabela_frequencia = valor[f'{colun}'].value_counts()
    return tabela_frequencia


@st.cache_data
def load_select_data(ano, modalidade, area):
    df = pd.read_csv("./Data/Database_filter.csv", sep=",", decimal=".")
    datare = df[(df['ano'] == ano) & (df["modalidade"] == modalidade) & (df["area_conhecimento"] == area)]
    return datare


@st.cache_data
def frequency_table(data):
    n = len(data)
    k = 1 + np.log2(n)
    k = int(np.ceil(k))
    amplitude = (data.max() - data.min()) / k
    classes = [data.min() + i * amplitude for i in range(k)]
    classes.append(data.max())
    tabela_frequencia = pd.cut(data, bins=classes, include_lowest=True, right=True)
    frequencia = tabela_frequencia.value_counts().reset_index()
    frequencia.columns = ['Classe', 'Frequência Absoluta']
    frequencia['Limite Inferior'] = frequencia['Classe'].apply(lambda x: x.left)
    frequencia = frequencia.sort_values(by='Limite Inferior')
    frequencia['Frequência Relativa'] = frequencia['Frequência Absoluta'] / n
    frequencia['Frequência Acumulada'] = frequencia['Frequência Absoluta'].cumsum()
    frequencia['Frequência Acumulada Relativa'] = frequencia['Frequência Acumulada'] / n

    xi = (frequencia['Classe'].apply(lambda x: (x.left + x.right) / 2)).values
    xi = xi.astype(float)
    frequencia['Variância'] = xi
    frequencia['Frequência Absoluta'] = frequencia['Frequência Absoluta'].astype(int)
    frequencia['Variância x Frequência Absoluta'] = xi * frequencia['Frequência Absoluta']
    frequencia['Variância^2 x Frequência Absoluta'] = xi ** 2 * frequencia['Frequência Absoluta']

    return frequencia



@st.cache_data
def describe_data(df):
    data = {'Variaveis Nulas': f"{df['valor'].isnull().sum()}",
            'Minimo': f"{df['valor'].min()}",
            'Maximo': f"{df['valor'].max()}",
            'Media': f"{df['valor'].mean()}",
            'Mediana': f"{df['valor'].median()}",
            'Moda': f"{df['valor'].mode()[0]}",
            }
    return data


@st.cache_data
def describe_data_variable(df):
    data = {'Variancia': f"{df['valor'].var()}",
            'Desvio padrão': f"{df['valor'].std()}",
            'Maximo': f"{df['valor'].max()}",
            }
    return data


@st.cache_data
def describe_data_assim(df):
    media = np.mean(df["valor"])
    mediana = np.median(df["valor"])
    desvio_padrao = np.std(df["valor"], ddof=1)
    assimetria_pearson = 3 * (media - mediana) / desvio_padrao
    return {'Coeficiente de assimetria Pearson': f"{assimetria_pearson}"}


@st.cache_data
def describe_data_quarts(df):
    data = {'Quantis 25% ': f"{df['valor'].quantile(0.25)}",
            'Quantis 50% ': f"{df['valor'].quantile(0.50)}",
            'Quantis 75%': f"{df['valor'].quantile(0.75)}",
            }
    return data


@st.cache_data
def describe_data_others(df):
    data = {'Assimetria (Skewness)': f"{df['valor'].skew()}",
            'Curtose (Kurtosis)': f"{df['valor'].kurtosis()}",
            }
    return data


def create_stem_and_leaf(data):
    ramos = [int(x / 10) for x in data]
    folhas = [x % 10 for x in data]
    return ramos, folhas


@st.cache_data
def graf_stem_leaf(df):
    ramos, folhas = create_stem_and_leaf(df["valor"])
    fig, ax = plt.subplots()
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.set_yticks(range(min(ramos), max(ramos) + 1))
    for i in range(min(ramos), max(ramos) + 1):
        folhas_ramo = [folhas[j] for j, ramo in enumerate(ramos) if ramo == i]
        ax.scatter(folhas_ramo, [i] * len(folhas_ramo), label=str(i), marker='o', alpha=0.7)

    ax.set_yticklabels([str(i) for i in range(min(ramos), max(ramos) + 1)])
    ax.set_xlabel("Folhas")
    return fig


@st.cache_data
def stem_and_leaf_plot(data):
    data_sorted = sorted(data)
    ramos = []
    folhas = []

    for item in data_sorted:
        ramo = int(item // 10)
        folha = int(item % 10)
        if ramo not in ramos:
            ramos.append(ramo)
            folhas.append([folha])
        else:
            idx = ramos.index(ramo)
            folhas[idx].append(folha)
    return ramos, folhas


@st.cache_data
def modalidade_graf(modalidade, area):
    df = pd.read_csv("./Data/Database_filter.csv", sep=",", decimal=".")
    datare = df[(df['ano']) & (df["modalidade"] == modalidade) & (df["area_conhecimento"] == area)]
    return datare


@st.cache_data
def plotar_grafico(x, y):
    plt.figure()
    plt.bar(x=x, height=y, color="b")
    plt.xlabel("Subarea")
    plt.ylabel("Valor")
    plt.xticks(rotation=90)
    return plt.show()


@st.cache_data
def cal_rf(ramos1, folhas1):
    for i in range(len(ramos1)):
        np([ramos1[i]] * len(folhas1[i]), sorted(folhas1[i]), linefmt='-', markerfmt='o', basefmt=' ')


@st.cache_data
def create_histogram(data):
    hist, bin_edges = np.histogram(data, bins='auto')
    return hist, bin_edges


@st.cache_data
def plot_grafing_mean(df):
    anos = [2002, 2003, 2004, 2005, 2006, 2007,
            2008, 2009, 2010, 2011, 2012, 2013,
            2014, 2015, 2016, 2017, 2018, 2019,
            2020, 2021, 2022]

    datas = []

    for ano in anos:
        dados_ano = df[df['ano'] == ano]

        if not dados_ano.empty:
            frame_ano = {
                'ano': ano,
                'minimo': dados_ano['valor'].min(),
                'maximo': dados_ano['valor'].max(),
                'media': dados_ano['valor'].mean(),
                'mediana': dados_ano['valor'].median(),
                'moda': dados_ano['valor'].mode().values[0]
            }
            datas.append(frame_ano)

    return datas


@st.cache_data
def graf_lines_min(datas):
    fig, ax = plt.subplots()
    ax.plot(datas["ano"], datas["minimo"])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Minimo')
    return fig


@st.cache_data
def graf_lines_max(datas):
    fig, ax = plt.subplots()
    ax.plot(datas["ano"], datas["maximo"])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Maximo')
    return fig


@st.cache_data
def graf_lines_med(datas):
    fig, ax = plt.subplots()
    ax.plot(datas["ano"], datas["media"])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Media')
    return fig


@st.cache_data
def graf_lines_median(datas):
    fig, ax = plt.subplots()
    ax.plot(datas["ano"], datas["mediana"])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Mediana')
    return fig


@st.cache_data
def graf_lines_moda(datas):
    fig, ax = plt.subplots()
    ax.plot(datas["ano"], datas["moda"])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Moda')
    return fig
