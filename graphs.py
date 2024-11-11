import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

xlsx_file_path = './files/Report_ITSrvices_8Meses.xlsx'
df = pd.read_excel(xlsx_file_path)

st.title('Análise Relatório de Serviços de TI')

st.write('## Dados Carregados')
st.dataframe(df)

st.write('## Contagem de tipo')
plt.figure()
colors = ('lime', 'skyblue', 'yellow', 'orange')
df['Tipo'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors)
plt.ylabel('')
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

st.write('## Contagem de urgência')
plt.figure()
colors = ('lime', 'skyblue', 'yellow', 'orange')
df['Urgência'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors)
plt.ylabel('')
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

st.write('## Ocorrências por departamento')
plt.figure()
df['Categoria'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Categorias')
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

"""
# Relatório de Análise de Ocorrências e Desempenho

## 1. Resumo dos Principais Problemas e Padrões Identificados
- **Quantidade Elevada de Ocorrências:** Foram registrados 1.200 chamados, indicando uma demanda contínua por suporte e serviços internos.
- **Predomínio de Dúvidas e Solicitações Rotineiras:** 286 dúvidas e 293 solicitações apontam que grande parte das ocorrências são operacionais e podem ser resolvidas com treinamentos e automação.
- **Problemas Recorrentes:** Falhas de conexão (111), erros de software (108) e problemas de e-mail (96) são os tipos mais comuns. Isso pode indicar falta de estabilidade em sistemas de TI e uma necessidade de revisões técnicas.

## 2. Desempenho por Prioridade e Status
- **Distribuição Equilibrada de Prioridades:** Embora haja equilíbrio entre baixa, média, alta e urgente, o número expressivo de chamados urgentes (291) é um ponto de atenção.
- **Gargalos no Fluxo de Chamados:** Com 908 ocorrências ainda em aberto ou aguardando interação (cliente ou terceiro), é evidente que a gestão de filas precisa ser melhorada para reduzir o tempo de resolução.

## 3. Desempenho por Departamento e Área de Negócio
- **Infraestrutura e Sistemas:** Concentram o maior volume de ocorrências. A recomendação é intensificar o monitoramento preventivo e otimizar processos nesses setores.
- **RH e Gente e Gestão:** Com volumes consideráveis de ocorrências (178 e 183, respectivamente), podem se beneficiar de melhorias nos sistemas ou processos específicos dessas áreas.

## 4. Avaliação dos Analistas e Oportunidades de Otimização
- **Distribuição por Analista Fragmentada:** Cada analista lidou apenas com uma ocorrência, o que pode indicar que não há uma concentração eficiente dos atendimentos.
- **Recomendação:** Criar um sistema de especialização ou escalonamento para permitir que analistas mais experientes assumam maior volume e complexidade, aumentando a eficiência e reduzindo retrabalho.

## 5. Incidentes Críticos e Gerenciamento de Falhas
- **Causas Raiz Identificadas:** Falhas de configuração e conectividade são frequentes e afetam serviços críticos. Isso pode ser mitigado com automação e padronização dos processos de configuração.
- **Impacto no Negócio:** Serviços críticos ficaram indisponíveis por um tempo significativo (precisamos confirmar o downtime). O tempo médio de recuperação (MTTR) deve ser monitorado e otimizado.

## Conclusão e Próximos Passos
A análise mostra que a operação está sobrecarregada com ocorrências rotineiras e alguns incidentes recorrentes, prejudicando a eficiência do time e a experiência do usuário. O sistema mostrou níveis aceitáveis de disponibilidade, mas há oportunidades para otimização em áreas de software e infraestrutura. Além disso, a alta quantidade de analistas lidando com apenas uma ocorrência sugere que uma redistribuição de cargas de trabalho pode melhorar o tempo de resposta e resolução de problemas. 

### Recomendações
1. **Automatizar e Padronizar Processos:** Especialmente para troca de senhas, problemas de e-mail e instalação de software.
2. **Treinamento Proativo:** Capacitar usuários finais e áreas como RH e Financeiro para reduzir o número de dúvidas e requisições simples.
3. **Melhorar o Escalonamento e a Especialização dos Analistas:** Distribuir a carga de trabalho de forma estratégica para aumentar a eficiência.
4. **Implementar SLAs com Terceiros:** Reduzir o tempo de espera e melhorar a gestão dos chamados pendentes.
5. **Monitoramento Contínuo e Automação:** Utilizar ferramentas de observabilidade para antecipar falhas e reduzir o tempo de indisponibilidade.

"""