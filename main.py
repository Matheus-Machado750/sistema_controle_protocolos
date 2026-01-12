import streamlit as st
import pandas as pd #P/ trabalhar com tabelas
from datetime import datetime

#---------- CONFIGURAÇÃO DA PÁGINA ----------

st.set_page_config(page_title="Controle de Protocolos", layout="wide")

#---------- APLICAR O CSS ----------

with open("styles.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#---------- INICIALIZAR O DATAFRAME ----------

if "protocolos" not in st.session_state: # "Mémoria" da aplicação
    st.session_state.protocolos = pd.DataFrame(columns=["Código", "Nome", "Serviço", "Data", "Situação"])
if "confirmar_limpeza" not in st.session_state:
    st.session_state.confirmar_limpeza = False

#---------- FUNÇÃO P/ GERAR O PRÓXIMO CÓDIGO AUTOMATICAMENTE ----------

def gerar_codigo():
    ano = "2026"

    if st.session_state.protocolos.empty:
        return f"{ano}-0001"

    ultimo_codigo = st.session_state.protocolos["Código"].iloc[-1] #Pega a coluna "Código" e .iloc[-1] pega a última linha dessa coluna

    #Se o último código NÃO for de 2026, reinicia a contagem
    if not ultimo_codigo.startswith(ano):
        return f"{ano}-0001"

    numero = int(ultimo_codigo.split("-")[1]) + 1  #Divide a str no "-", pega a 2º parte [1], converte p/ int e soma 1
    return f"{ano}-{numero:04d}"

#---------- SIDEBAR - ALTERAR SITUAÇÃO ----------

st.sidebar.header("Alterar Situação")
codigo_alterar = st.sidebar.text_input("Código do Protocolo:")
nova_situacao = st.sidebar.selectbox("Nova Situação:", ["Em andamento", "Concluído", "Cancelado"])

if st.sidebar.button("Salvar Alteração"): #No clique, vira True
    idx = st.session_state.protocolos[st.session_state.protocolos["Código"] == codigo_alterar].index #Filtra o DataFrame (tabela) e seleciona a linha onde a coluna "Código" é igual ao "codigo_alterar"

    if len(idx) > 0: #Para verificar se achou um protocolo compatível
        st.session_state.protocolos.at[idx[0], "Situação"] = nova_situacao #Altera o valor no DataFrame
        st.sidebar.success("Situação alterada com sucesso!")
    else:
        st.sidebar.error("Protocolo não encontrado.")

#---------- TÍTULO PRINCIPAL ----------

st.title("Sistema de Controle de Protocolos")

#---------- FORMULÁRIO PRINCIPAL ----------

with st.form("form_protocolo", clear_on_submit=True): #No envio os campos zeram
    nome = st.text_input("Nome do Solicitante:")
    servico = st.selectbox(
        "Serviço:",
        ["", "Atendimento online", "Suporte Técnico", "Financeiro", "Atualização de Cadastro","Emissão de documento", "Outro"]
    )
    col1, col2 = st.columns([1, 1]) #P/ colocar os botões lado a lado
    salvar = col1.form_submit_button("Salvar Protocolo")
    limpar = col2.form_submit_button("Limpar Tabela")

#---------- AÇÕES DO FORMULÁRIO ----------

if salvar:
    if nome.strip() == "" or servico == "": #P/ não ficar nenhum campo em branco
        st.warning("Preencha todos os campos antes de salvar.") 

    else:
        codigo = gerar_codigo()
        data = datetime.now().strftime("%Y-%m-%d")

        novo = pd.DataFrame( #Cria um DataFrame de uma linha com os dados novos
            [[codigo, nome, servico, data, "Em andamento"]],
            columns=["Código", "Nome", "Serviço", "Data", "Situação"]
        )

        st.session_state.protocolos = pd.concat([st.session_state.protocolos, novo], ignore_index=True) #Concatena o DataFrame antigo com o novo e uma linha e forma 1 só
        st.success(f"✅ Protocolo {codigo} salvo com sucesso!")

#---------- BOTÃO DE LIMPEZA ----------

if limpar:
    st.session_state.confirmar_limpeza = True

#---------- CONFIRMAÇÃO DE LIMPEZA ----------

if st.session_state.confirmar_limpeza:

    st.warning("⚠️ Tem certeza que deseja apagar TODOS os protocolos? Essa ação não pode ser desfeita.")

    c1, c2 = st.columns([1, 1]) #P/ dividir os botões em 2 colunas

    if c1.button("✅ Sim, apagar tudo"):
        st.session_state.protocolos = pd.DataFrame(columns=["Código", "Nome", "Serviço", "Data", "Situação"]) #Zerando o DataFrame
        st.session_state.confirmar_limpeza = False
        st.success("Todos os protocolos foram apagados com sucesso.")
        st.rerun()
        
    if c2.button("❌ Cancelar"):
        st.session_state.confirmar_limpeza = False #P/ sair do modo de confimação
        st.rerun()

#---------- EXIBIÇÃO DA TABELA ----------

st.subheader("📄 Protocolos Registrados")

if not st.session_state.protocolos.empty: #Só mostra a tabela se houver pelo menos 1 protocolo registrado
    df = st.session_state.protocolos.copy()

    def colorir_situacao(val):
        cores = {
            "Em andamento": "background-color: #e8f2fc; color: #2b94d2;",
            "Concluído": "background-color: #d4efdf; color: #196f3d;",
            "Cancelado": "background-color: #f5b7b1; color: #7b241c;"
        }
        return cores.get(val, "") #Caso o valor esteja no dict, retorna a cor

    st.dataframe(
        df.style.map(colorir_situacao, subset=["Situação"]), #Aplica a função acima apenas nas células de "Situação"
        use_container_width=True,
        hide_index=True
    )

# ---------- SEÇÃO DE BUSCA ----------

    st.divider() #Linha horizontal que separa a tabela da seção de busca
    st.subheader("🔍 Buscar Protocolo")
    termo_busca = st.text_input("Digite o número do protocolo ou nome:")

    if termo_busca.strip(): 
        resultados = df[ #Busca linhas onde a coluna de código ou nome contém o texto inserido
            df["Código"].str.contains(termo_busca, case=False, na=False) |
            df["Nome"].str.contains(termo_busca, case=False, na=False)
        ]

        if not resultados.empty: #Caso o filtro encontre pelo menos 1 linha
            st.success(f"{len(resultados)} resultado(s) encontrado(s):")

            st.dataframe( #Mostra só os resultados filtrados, já com cor
                resultados.style.map(colorir_situacao, subset=["Situação"]),
                use_container_width=True,
                hide_index=True
            )
        else:
            st.warning("Nenhum protocolo encontrado com esse termo.")
else:
    st.info("Nenhum protocolo registrado ainda.")