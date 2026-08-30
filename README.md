# Nome do projeto

> Sistema RAG (Retrieval-Augmented Generation) construído com documentação do HTTPX em arquivos Markdown.

## Identificação

- **Nome do aluno:** Davi Farias Madruga
- **Formato da solução:** Aplicação web
- **Link do vídeo:** 
- **Link do Colab, se aplicável:** Não se aplica

## Objetivo

O sistema implementa um **RAG (Retrieval-Augmented Generation)** utilizando a documentação do **HTTPX** em arquivos Markdown.

O fluxo principal consiste em:

1. Ler documentos Markdown.
2. Dividir os documentos em chunks.
3. Transformar os chunks em embeddings.
4. Realizar busca semântica.
5. Enviar os trechos mais relevantes para um modelo **Qwen local**.
6. Gerar uma resposta baseada exclusivamente no contexto recuperado.

## Arquitetura resumida

```text
Documentos Markdown
        ↓
Chunks
        ↓
Embeddings
        ↓
Indexação do índice
        ↓
Embedding da pergunta
        ↓
Busca por similaridade de cosseno
        ↓
Top K chunks
        ↓
Contexto recuperado
        ↓
Qwen local
        ↓
Resposta
```

## Como executar do zero

### 1. Clonar o repositório

```bash
git clone https://github.com/Davi-Madruga/rag-md.git
cd rag-md
```

### 2. Criar e ativar o ambiente virtual
Neste projeto foi utilizado o python 3.12, se tiver algum conflito verifique sua versão
```bash
python --version
```
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```
### 4. Instalar o Ollama
Baixe e instale o Ollama pelo site oficial:
https://ollama.com/
Após a instalação, abra o terminal e verifique se ele está funcionando:
```bash
ollama --version
```
### 5. Baixar o modelo Qwen3 4B
Com o Ollama instalado, execute:
```bash
ollama pull qwen3:4b
```
Esse comando baixa o modelo Qwen3 4B para ser executado localmente.
Para verificar se o modelo foi instalado:
```bash
ollama list
```
O modelo qwen3:4b deve aparecer na lista.

### 6. Gerar a indexação

```bash
python -m src.indexacao
```
### 7. Executar a aplicação

```bash
streamlit run app.py --server.fileWatcherType none
```

## Decisões técnicas

### Chunking

- **Estratégia:** Divisão dos documentos Markdown em chunks de texto.
- **Tamanho aproximado:** 800 caracteres.
- **Overlap:** 100 caracteres.
- **Justificativa:** Dividir documentos grandes em trechos menores permite realizar uma busca semântica mais precisa e fornecer ao modelo apenas as partes relevantes.

### Embeddings e busca

- **Modelo utilizado:** `all-MiniLM-L6-v2`
- **Dimensão dos embeddings:** 384
- **Forma de cálculo da similaridade:** Similaridade por cosseno
- **Valor de `top_k`:** 3

**Justificativa:** três chunks fornecem ao modelo uma quantidade suficiente de contexto relevante sem enviar informação em excesso.

### Metadados e fontes

Durante a divisão dos chunks, são adicionados os seguintes metadados:

- Texto
- Arquivo
- Caminho

Durante a indexação, também são adicionados:

- ID
- Valor do embedding

## Perguntas de teste

### 1. Pergunta com resposta clara

**Pergunta:**

> What are the main types of HTTPX exceptions cited in the documentation, and when is each of them used?

**Resultado esperado:**

O sistema deve recuperar os trechos da documentação relacionados às exceções do HTTPX e explicar os principais tipos e suas situações de uso.

**O resultado foi relevante?**

Sim. A pergunta é diretamente relacionada ao conteúdo da documentação e os chunks recuperados fornecem contexto suficiente para elaborar a resposta.

### 2. Pergunta ampla ou ambígua

**Pergunta:**

> If I want to prevent the application from hanging while waiting for a network response, what timeout behavior does the documentation suggest, and how can it be adjusted?

**Resultado esperado:**

O sistema deve encontrar informações sobre o comportamento de timeout do HTTPX e explicar como configurá-lo ou ajustá-lo.

**O resultado foi relevante?**

Sim, porém a pergunta é mais ampla. Ela envolve conceitos de timeout e configuração, exigindo que o sistema encontre informações relevantes na documentação para construir uma resposta adequada.

### 3. Pergunta fora do escopo

**Pergunta:**

> Porque One Piece é o melhor animanga de toda a história da humanidade??

**Como o sistema reagiu:**

A pergunta não possui relação com a documentação do HTTPX. O sistema deve identificar que o contexto recuperado não é suficiente e informar que não possui informações sobre o assunto, indicando também que o documento aborda HTTPX.

**Como essa reação poderia melhorar:**

O sistema poderia utilizar um limiar mínimo de similaridade antes de considerar os chunks relevantes. Isso ajudaria a identificar perguntas completamente fora do domínio com maior segurança, em vez de depender apenas do `top_k`.

## Limitações conhecidas

- A qualidade das respostas depende da qualidade dos chunks recuperados.
- Um score de similaridade alto não garante necessariamente que o chunk contenha a resposta completa.
- O modelo pode eventualmente não seguir perfeitamente o formato JSON solicitado.
- O sistema depende do modelo Qwen local e do Ollama para a geração das respostas.
- O chunking utilizado é simples e pode dividir informações relacionadas entre chunks diferentes.
- A base atual é focada na documentação do HTTPX.
- Perguntas fora do escopo podem recuperar chunks que possuem alguma semelhança semântica, mesmo que não sejam suficientes para responder à pergunta.

## Uso de ferramentas de IA

- **Ferramentas utilizadas:** ChatGPT.
- **Tarefas em que ajudaram:**
  - Aprendizado dos conceitos de RAG.
  - Definição da arquitetura.
  - Explicação de chunking e embeddings.
  - Desenvolvimento e correção de partes do código.
  - Melhoria da interface.

### Exemplo representativo de prompt ou orientação

```text
Estou aprendendo sobre AI e engenharia de AI. Hoje irei aprender a como criar um RAG.
```

### O que foi testado, modificado ou validado

Durante o desenvolvimento, foram testados e ajustados:

- Funcionamento do pipeline de ingestão.
- Processo de chunking.
- Geração dos embeddings.
- Busca por similaridade.
- Recuperação dos chunks.
- Integração com o Qwen.
- Apresentação dos resultados na aplicação Streamlit.

## Referências e código externo

- **Documentação do HTTPX:** utilizada como base documental do projeto.
- **Sentence Transformers:** utilizada para geração dos embeddings.
- **Transformers:** utilizada no ecossistema dos modelos.
- **Streamlit:** utilizado para construção da aplicação web.
- **Ollama:** utilizado para execução local do modelo Qwen.

## Segurança

Confirme uma opção:

- [x] Minha solução não usa API key.
- [ ] Minha solução usa segredo protegido e nenhuma chave foi publicada.
