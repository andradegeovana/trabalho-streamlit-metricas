import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

xlsx_file_path = './files/Report_ITSrvices_8Meses.xlsx'
df = pd.read_excel(xlsx_file_path)

st.title('Análise Relatório de Serviços de TI')

st.write('## Dados Carregados')
st.dataframe(df)

st.write('## Evolução das ocorrências por mês')
df['Ano_Mes'] = df['Aberto em'].astype(str).str.slice(0, 7)
ocorrencias_por_mes = df['Ano_Mes'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.plot(ocorrencias_por_mes.index, ocorrencias_por_mes.values, color='skyblue', marker='o')

for i, v in enumerate(ocorrencias_por_mes.values):
    plt.text(i, v + 5, str(v), color='skyblue', ha='center', fontsize=10)

plt.xlabel('Data', fontsize=12)
plt.ylabel('Ocorrências', fontsize=12)
plt.ylim(0, max(ocorrencias_por_mes.values) + 20)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
st.pyplot(plt)

st.write('## Divisão por tipo de ocorrência')
plt.figure()
colors = ('lime', 'skyblue', 'yellow', 'orange')
df['Tipo'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors)
plt.ylabel('')
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

st.write('## Divisão por nível de urgência')
plt.figure()
colors = ('lime', 'skyblue', 'yellow', 'orange')
df['Urgência'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors)
plt.ylabel('')
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

st.write('## Ocorrências por categorias')
plt.figure()
df['Categoria'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Categorias')
plt.ylabel('Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

st.write('## Ocorrências por assunto')
plt.figure(figsize=(9.4, 6.8))
df['Assunto'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Assunto')
plt.ylabel('Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

st.write('## Ocorrências por área de negócio')
plt.figure()
df['Área de Negócio'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Área de negócio')
plt.ylabel('Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)


