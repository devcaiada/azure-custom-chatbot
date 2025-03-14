# MyChitChat PDF Assistant

MyChitChat PDF Assistant é um sistema interativo de chat desenvolvido para responder perguntas com base no conteúdo de documentos PDF fornecidos. O projeto utiliza conceitos avançados de inteligência artificial, como IA generativa, embeddings e buscas vetoriais, para interpretar e processar informações de arquivos, oferecendo respostas contextuais fundamentadas.

Este projeto é ideal para estudantes, pesquisadores e profissionais que precisam organizar, revisar e correlacionar informações de diversos documentos, como artigos científicos, relatórios ou qualquer material de estudo.

---

## Cenário

Imagine que você é um estudante de Engenharia de Software, prestes a escrever seu Trabalho de Conclusão de Curso (TCC). Para facilitar o processo de revisão e conexão entre ideias de diversos artigos científicos, você decide criar um sistema inteligente capaz de interpretar arquivos PDF, organizar as informações e responder de forma contextual.

---

## Objetivos do Projeto

O sistema tem como principais objetivos:
- ✅ **Carregar arquivos PDF** contendo informações relevantes para estudo ou projeto.
- ✅ **Implementar um sistema de busca vetorial** para indexar e recuperar informações dos PDFs.
- ✅ **Utilizar IA generativa** para criar respostas contextuais baseadas no conteúdo dos documentos carregados.
- ✅ **Desenvolver uma interface interativa de chat**, onde o usuário possa fazer perguntas e obter respostas personalizadas.

---

## Estrutura do Projeto

- **`frontend/`**: Interface do usuário para interação com o sistema.
  - `index.html`: Estrutura da interface de chat.
  - `styles.css`: Estilo visual da interface.
  - `app.ts`: Lógica de interação com o backend, escrita em TypeScript.

- **`backend/`**: Lógica do servidor e processamento de dados.
  - `chat.py`: Aplicação Flask que gerencia requisições, carrega PDFs e processa as respostas.
  - `pdf_processing.py`: Scripts de suporte para extração e indexação de informações de PDFs.

- **Outros Arquivos**:
  - `requirements.txt`: Lista de dependências Python.
  - `.gitignore`: Arquivos e pastas ignorados no repositório.

---

## Tecnologias Utilizadas

### **Frontend**
- HTML, CSS e TypeScript para construção da interface.

### **Backend**
- Python e Flask para gerenciar a lógica de aplicação e interações.
- Bibliotecas Python:
  - **PDFMiner** para extração de texto dos PDFs.
  - **Azure Cognitive Search** para indexação e busca.
  - **OpenAI** para geração de embeddings e respostas inteligentes.

### **Armazenamento** (planejado para o futuro)
- Azure Blob Storage: Para armazenamento e gestão de arquivos carregados.

---

## Como Configurar

### Pré-requisitos

Certifique-se de possuir:
- **Node.js** e **npm** instalados (para o TypeScript).
- **Python** e **pip** instalados (para o Flask).
- Uma conta do Azure configurada, caso deseje utilizar os serviços Azure Cognitive Search ou Blob Storage.

---

## Funcionalidades Futuras 
Planejamos expandir este projeto com as seguintes funcionalidades:

- Suporte a múltiplos formatos de arquivo: Além de PDFs, expandir para DOCX, TXT, entre outros.

- Resumo automático: Gerar resumos de documentos carregados.

- Filtros avançados de busca: Refinar as respostas com base em metadados.

- Persistência de sessões: Salvar logs e interações no Azure Blob Storage.

## Contribuição <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />

Sinta-se à vontade para contribuir com este repositório. Abra uma issue ou envie um pull request com suas sugestões e melhorias.

