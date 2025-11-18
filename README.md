📑 Sistema de Controle de Protocolos

Aplicação desenvolvida em Python com Streamlit para registrar, acompanhar e atualizar protocolos de atendimento de forma simples e organizada.
O objetivo do projeto é oferecer uma ferramenta prática para controle de demandas, com foco em:

Registro rápido de solicitações

Acompanhamento da situação de cada protocolo

Busca por código ou nome do solicitante

🌐 Acesse o Projeto Online

👉 Clique aqui para usar o Sistema de Controle de Protocolos
(coloque aqui o link do Streamlit Cloud quando publicar)

Nenhuma instalação ou download é necessário — o sistema roda diretamente no navegador por meio do Streamlit Cloud, bastando ter acesso à internet.

⚙️ Tecnologias Utilizadas
🐍 Python 3

Toda a lógica da aplicação, regras de negócio e manipulação de dados foram desenvolvidas em Python.

💻 Streamlit

Framework utilizado para transformar o script Python em uma aplicação web interativa, com:

Formulário para cadastro de protocolos

Barra lateral para alteração de situação

Tabela dinâmica para exibição dos dados

Campo de busca integrado

📊 Pandas

Biblioteca utilizada para manipular os dados em forma de DataFrame, permitindo:

Armazenar os protocolos em memória (via st.session_state)

Adicionar novos registros

Filtrar resultados na busca por código ou nome

Exibir a tabela de forma organizada

🕒 Módulo datetime

Responsável por registrar automaticamente a data de criação de cada protocolo no formato YYYY-MM-DD.

🎨 CSS Customizado (styles.css)

Arquivo de estilo utilizado para personalizar a aparência padrão do Streamlit, incluindo:

Inputs de texto com borda azul e efeito visual ao focar

Selects com comportamento visual consistente (sem “vermelho padrão”)

Botões com cor personalizada e efeito hover

Título principal em destaque

Essa customização melhora a experiência do usuário (UX), deixando a interface mais limpa, coerente e agradável de usar.

📦 requirements.txt

Arquivo que lista as dependências necessárias para o projeto.
Atualmente, inclui:

streamlit

pandas

🧠 Como o Sistema Funciona

O fluxo principal da aplicação segue estes passos:

O usuário preenche:

Nome do Solicitante

Tipo de Serviço (ex.: Atendimento online, Suporte Técnico, etc.)

Ao clicar em “Salvar Protocolo”:

É gerado automaticamente um código sequencial no formato 2025-0001, 2025-0002, ...

A data atual é registrada usando datetime.now()

A situação inicial do protocolo é definida como “Em andamento”

O novo registro é adicionado ao DataFrame mantido em st.session_state

Todos os protocolos são exibidos em uma tabela, com a coluna Situação colorida de acordo com o status:

Azul para Em andamento

Verde para Concluído

Vermelho para Cancelado

Na sidebar, o usuário pode:

Informar o código de um protocolo

Selecionar uma nova situação

Salvar a alteração, atualizando diretamente o registro na tabela

🔍 Busca de Protocolos

A aplicação também possui uma seção de busca abaixo da tabela principal:

O usuário pode digitar parte do código ou parte do nome do solicitante

O sistema filtra os protocolos existentes usando str.contains

Se houver resultados:

É exibida uma mensagem informando quantos protocolos foram encontrados

Apenas os registros correspondentes são mostrados na tabela filtrada

Caso não haja nenhuma correspondência, o sistema exibe um aviso informando que nenhum protocolo foi encontrado

🧹 Confirmação de Limpeza da Tabela

Para evitar exclusões acidentais, o botão “Limpar Tabela” não apaga os dados imediatamente.

O comportamento é o seguinte:

Ao clicar em “Limpar Tabela”, o sistema ativa um modo de confirmação na sessão.

Uma mensagem de alerta é exibida, perguntando se o usuário realmente deseja apagar todos os protocolos.

São mostrados dois botões:

✅ Sim, apagar tudo → limpa completamente o DataFrame e reseta o estado

❌ Cancelar → sai do modo de confirmação sem excluir nada

Após escolher uma das opções, a página é recarregada usando st.rerun() para atualizar a interface.
