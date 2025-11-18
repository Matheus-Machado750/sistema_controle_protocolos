# 📑 Sistema de Controle de Protocolos

Aplicação web desenvolvida em **Python** com **Streamlit** para registrar, listar e buscar protocolos de atendimento de forma simples e organizada.  
O sistema gera códigos sequenciais automaticamente, permite atualizar a situação dos protocolos e exibe os dados em uma tabela interativa.

---

## 🌐 Acesse o Projeto Online

➡️ **Link do app no Streamlit Cloud:**  
`(adicione aqui o link quando publicar)`

Nenhuma instalação é necessária — o sistema roda diretamente no navegador através do Streamlit Cloud.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3** – Linguagem principal do projeto.  
- **Streamlit** – Framework para criação de interfaces web interativas em Python.  
- **Pandas** – Manipulação dos dados em forma de tabela (DataFrame).  
- **datetime** – Registro automático da data de criação dos protocolos.  
- **CSS customizado (`styles.css`)** – Personalização da interface (inputs, selects, botões e título).  
- **`requirements.txt`** – Lista das dependências do projeto.

---

## 🧠 Funcionalidades

- Registro de novos protocolos com:
  - Código gerado automaticamente (`2025-0001`, `2025-0002`, …)
  - Nome do solicitante  
  - Tipo de serviço  
  - Data de criação  
  - Situação inicial: **“Em andamento”**
- Alteração da situação pela barra lateral:
  - Em andamento
  - Concluído
  - Cancelado
- Tabela interativa com todos os protocolos cadastrados.
- Cores diferentes para cada situação na tabela.
- Campo de busca por:
  - Código do protocolo
  - Nome do solicitante
- Botão de **“Limpar Tabela”** com confirmação antes de apagar todos os registros.

---

## 📜 Sobre a criação do projeto

Este projeto foi criado com fins **educacionais** e **demonstrativos**.  
