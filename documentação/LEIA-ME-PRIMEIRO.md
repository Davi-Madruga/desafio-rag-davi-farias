# Prova prática final — Mini-RAG sobre documentação

## 1. Contexto

Você recebeu uma base documental real e deverá construir um sistema capaz de localizar informações relevantes nela.

O objetivo não é demonstrar domínio avançado de Python nem criar uma interface sofisticada. O objetivo é mostrar que você compreendeu o fluxo estudado e consegue implementar, testar e explicar suas decisões.

Você pode usar ferramentas de inteligência artificial durante todo o trabalho. O uso é permitido e incentivado.

## 2. Prazo e modalidade

- Atividade individual.
- Início: sexta-feira, 28 de agosto de 2026, às 13h.
- Prazo final: domingo, 30 de agosto de 2026, às 13h.
- Fuso adotado: horário de Recife, UTC−3.

A janela oficial é de 48 horas. O horário de compartilhamento da mensagem do professor será o registro de liberação do desafio.

Entregas após as 13h poderão ser registradas como atrasadas. Em caso de falha real no canal de envio, preserve evidências com data e hora.

## 3. O desafio

Construa o núcleo de recuperação de um RAG usando a documentação do projeto HTTPX.

Seu sistema deverá executar este fluxo:

```text
repositório → arquivos Markdown → chunks + metadados → embeddings
             → busca por similaridade → trechos relevantes + fontes
```

O mínimo obrigatório é uma busca que receba uma pergunta e retorne trechos relevantes da documentação com suas fontes. Gerar uma resposta em linguagem natural é uma extensão opcional.

Uma observação conceitual: os documentos serão indexados, não usados para treinar um modelo. Sem a etapa de geração, sua entrega representa o núcleo de recuperação de um RAG.

## 4. Base de dados obrigatória

- Repositório: <https://github.com/encode/httpx>
- Versão da prova: `b5addb64f0161ff6bfe94c124ef76f6a1fba5254`
- Corpus: todos os arquivos `*.md` encontrados recursivamente dentro de `httpx/docs/`

Nesse commit, a busca recursiva deve encontrar 23 arquivos Markdown. Use essa contagem apenas como verificação de que a leitura está apontando para a pasta correta.

Você deverá aprender a clonar ou baixar o repositório. Em um terminal ou célula do Colab, o começo pode ser:

```bash
git clone https://github.com/encode/httpx.git
cd httpx
git checkout b5addb64f0161ff6bfe94c124ef76f6a1fba5254
```

No Colab, comandos de terminal normalmente são executados com `!` no início. Consulte os materiais de apoio antes de simplesmente copiar comandos que você não compreende.

No Colab, a forma equivalente é:

```python
!git clone https://github.com/encode/httpx.git
%cd httpx
!git checkout b5addb64f0161ff6bfe94c124ef76f6a1fba5254
```

Use `%cd`, e não `!cd`, quando quiser manter a mudança de pasta nas células seguintes. Se a pasta já existir após uma execução anterior, não tente cloná-la novamente sem antes entender o estado atual.

## 5. Requisitos obrigatórios

Sua solução deve:

1. Clonar ou baixar a base documental.
2. Encontrar os arquivos Markdown dentro de `docs/`, incluindo subpastas.
3. Ler os documentos e dividi-los em chunks.
4. Preservar metadados que permitam rastrear cada chunk até sua origem.
5. Transformar chunks e perguntas em embeddings compatíveis.
6. Criar algum mecanismo de busca por similaridade.
7. Receber uma pergunta sem exigir alteração do código principal.
8. Retornar entre 3 e 5 resultados ordenados por relevância.
9. Exibir, em cada resultado:

   - o trecho recuperado;
   - o caminho do arquivo de origem;
   - o título ou a seção, quando possível;
   - a posição no ranking;
   - o score de similaridade, quando a tecnologia escolhida o disponibilizar.

10. Demonstrar pelo menos três perguntas diferentes:

    - uma pergunta cuja resposta esteja claramente na documentação;
    - uma pergunta mais ampla ou ambígua;
    - uma pergunta fora do assunto da base.

11. Incluir instruções para outra pessoa executar o projeto.
12. Funcionar por um caminho gratuito, sem exigir API paga ou computador potente.
13. Tratar de forma básica uma pergunta vazia, um corpus sem documentos e um `top_k` inválido, apresentando uma mensagem compreensível em vez de falhar silenciosamente.

Uma busca somente por palavras-chave pode receber pontuação parcial. Para a pontuação integral de recuperação semântica, use embeddings.

## 6. Liberdade de implementação

O formato mínimo recomendado é um notebook no Google Colab, mas você pode escolher:

- notebook Jupyter ou Colab;
- script de terminal;
- aplicação web simples;
- outra forma que consiga executar e explicar.

Você pode usar bibliotecas para carregar documentos, gerar embeddings, calcular similaridade ou organizar o fluxo. Você deverá, porém, conseguir explicar o papel das etapas principais.

Uma solução pequena e bem compreendida vale mais do que uma arquitetura grande que você não consegue executar ou explicar.

## 7. Caminhos gratuitos sugeridos

### Caminho A — mínimo e recomendado

- Google Colab ou Python local;
- leitura de Markdown com recursos da própria linguagem;
- um modelo público de embeddings executado localmente;
- similaridade calculada em memória;
- saída dos melhores chunks com fontes.

Uma opção adequada para perguntas em português sobre documentos em inglês é `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`. O modelo é público, multilíngue e não exige API key. Você não é obrigado a usá-lo.

Para um corpus deste tamanho, não é obrigatório instalar um banco vetorial. Uma matriz de embeddings e similaridade em memória já pode resolver o problema.

### Caminho B — alternativa lexical

Você pode começar com TF-IDF ou outra busca por palavras para validar o fluxo. Depois, tente substituir ou complementar essa etapa por embeddings. A versão apenas lexical não recebe todos os pontos destinados à recuperação semântica.

### Caminho C — geração opcional

Depois que a busca estiver funcionando, você pode enviar os melhores trechos para um modelo gerador e produzir uma resposta fundamentada.

Essa etapa pode usar:

- um modelo pequeno executado no Colab;
- um serviço que possua nível gratuito no momento da prova;
- Gemini Developer API em um projeto identificado como `Free`, se disponível para sua conta.

Não habilite cobrança apenas para concluir o desafio. Limites e disponibilidade de serviços gratuitos podem variar. A busca de trechos deve continuar funcionando mesmo se a geração falhar.

O Gemini API e o Google AI Studio exigem que o usuário tenha 18 anos ou mais segundo os termos atuais. Se você não cumprir esse requisito ou não quiser criar uma conta, use somente o caminho local sem API; isso não reduz sua pontuação.

Se usar uma API:

- nunca publique a chave no notebook, no GitHub, no vídeo ou no ZIP;
- use Secrets do Colab ou variável de ambiente;
- envie apenas a documentação pública para o serviço;
- documente qual plano gratuito utilizou;
- trate erro de limite ou indisponibilidade.

## 8. Dicas graduais

Leia apenas até o nível necessário. As dicas orientam o caminho, mas não entregam uma implementação pronta.

### Nível 1 — mapa mental

Pense em duas fases:

1. Preparação: descobrir arquivos, ler, dividir, guardar metadados e calcular embeddings.
2. Consulta: calcular o embedding da pergunta, comparar com os chunks e ordenar os resultados.

### Nível 2 — metadados

Não guarde apenas textos soltos. Para cada chunk, mantenha junto pelo menos:

```text
texto | arquivo | título/seção | identificador do chunk
```

Os índices da lista de textos, da matriz de embeddings e da lista de metadados precisam continuar alinhados.

### Nível 3 — chunking

- Tente não cortar um título de sua explicação.
- Chunks muito pequenos perdem contexto.
- Chunks muito grandes misturam assuntos e podem ser truncados pelo modelo.
- Como ponto inicial de experimento, tente blocos na ordem de 60 a 90 palavras, com pequena sobreposição.
- Palavras e tokens não são a mesma coisa. O modelo multilíngue sugerido aceita no máximo 128 tokens; trechos com código podem atingir esse limite com poucas palavras.
- Registre o valor escolhido e explique por que ele funcionou ou não.

### Nível 4 — embeddings e busca

- Use o mesmo modelo para documentos e perguntas.
- Normalização permite tratar produto escalar como similaridade cosseno em muitas implementações.
- Comece com `top_k = 3` e depois compare com 5.
- Não trate um score como probabilidade sem verificar o significado dado pela biblioteca.

### Nível 5 — geração

Primeiro faça a recuperação funcionar. Somente depois monte um contexto com os melhores chunks e peça ao gerador que:

- responda apenas com base no contexto;
- cite as fontes fornecidas;
- admita quando o contexto não contém a resposta.

## 9. Diagnóstico rápido

| Sintoma | O que verificar |
|---|---|
| Nenhum arquivo encontrado | Pasta atual, padrão recursivo e caminho `httpx/docs/` |
| Menos de 23 arquivos | Subpastas não foram percorridas ou a versão não foi fixada |
| Resultado sempre igual | Embedding da pergunta ou ordenação pode não estar sendo atualizado |
| Perguntas em português funcionam mal | O modelo pode ser monolíngue |
| Trechos terminam abruptamente | Chunk grande demais ou truncamento do modelo |
| Fonte não corresponde ao texto | Metadados e embeddings podem ter perdido o alinhamento |
| Erro de API | Volte ao núcleo local; geração não é obrigatória |
| Colab “esqueceu” variáveis | Execute as células em ordem desde o início |

## 10. Entregáveis

Entregue um repositório GitHub ou um arquivo ZIP contendo:

- notebook ou código-fonte;
- `README.md` preenchido;
- arquivo de dependências ou célula clara de instalação, quando necessário;
- evidências de teste;
- link do vídeo, se o projeto funcionar;
- `DIAGNOSTICO.md`, se não conseguir concluir a execução.

Use os modelos fornecidos neste kit. Você pode adaptá-los, mas não remova as informações essenciais.

Copie `MODELO_README_ENTREGA.md` para sua entrega e renomeie a cópia como `README.md`. Se precisar relatar uma falha, copie `MODELO_DIAGNOSTICO.md` e renomeie a cópia como `DIAGNOSTICO.md`.

### Nome sugerido

- Repositório: `desafio-rag-seu-nome`
- ZIP: `seu_nome_desafio_rag.zip`

Não é necessário incluir uma cópia inteira do repositório HTTPX se seu projeto consegue cloná-lo durante a execução.

O canal de entrega será informado pelo professor. Se enviar um repositório privado, conceda o acesso solicitado antes do prazo.

## 11. Vídeo de apresentação

- Duração recomendada: 4 a 7 minutos.
- Duração máxima: 8 minutos.
- A câmera é opcional; tela e narração são suficientes.
- OBS Studio é a sugestão de gravação, mas qualquer gravador de tela é aceito.
- Edição, câmera, resolução e estética não valem pontos.

Mostre:

1. a estrutura da entrega;
2. o fluxo `documentos → chunks → embeddings → busca → resultados`;
3. a execução de pelo menos duas perguntas;
4. a origem exata de pelo menos um resultado;
5. uma limitação ou resultado ruim;
6. quais ferramentas de IA foram usadas e o que você validou ou modificou.

As três perguntas obrigatórias devem permanecer registradas no notebook ou no README. Para manter o vídeo curto, apenas duas delas precisam aparecer na gravação.

Antes de gravar, esconda chaves, notificações e dados pessoais. Coloque no README um link acessível ao professor, de preferência como vídeo não listado ou arquivo no Drive com permissão de visualização.

## 12. Se o projeto não funcionar

Entregue o que conseguiu produzir e preencha `DIAGNOSTICO.md`.

Um projeto incompleto não recebe zero automaticamente. Etapas concluídas, compreensão e investigação continuam sendo avaliadas. O diagnóstico não substitui funcionalidades ausentes, mas permite verificar seu raciocínio.

Inclua:

- comportamento esperado;
- etapas que funcionaram;
- erro exato;
- tentativas realizadas e resultados;
- sua hipótese sobre a causa;
- próximo passo concreto;
- logs, saídas ou capturas relevantes.

## 13. Uso de IA e caráter individual

Você pode usar ChatGPT, Codex, Gemini, Claude, outras ferramentas de IA, documentação, fóruns e vídeos para:

- planejar;
- aprender Python;
- gerar ou revisar código;
- interpretar erros;
- criar testes;
- melhorar a documentação.

Não existe vantagem por usar uma ferramenta paga. A atividade continua individual: não compartilhe uma solução final pronta com outros participantes.

No README, declare:

- ferramentas utilizadas;
- para quais tarefas foram usadas;
- um exemplo representativo de prompt ou orientação;
- o que você testou, alterou ou validou;
- códigos e referências externas relevantes.

Não publique o histórico completo de suas conversas nem informações pessoais. Na apresentação, você deverá conseguir explicar as decisões centrais mesmo quando o código foi sugerido por IA.

## 14. Como será avaliado

O total é de 100 pontos:

| Categoria | Pontos |
|---|---:|
| Compreensão do fluxo | 18 |
| Implementação da recuperação | 28 |
| Fontes e rastreabilidade | 14 |
| Reprodutibilidade e qualidade técnica | 14 |
| Testes e reflexão | 10 |
| Comunicação e declaração do uso de IA | 6 |
| Extensões opcionais | até 10 |

Os requisitos obrigatórios somam 90 pontos. As extensões opcionais completam até 10 pontos.

Dos 10 pontos opcionais, até 6 correspondem a geração fundamentada e até 4 a uma melhoria mensurável e justificada.

Podem valer como extensão:

- resposta gerada com base real nos chunks e com fontes;
- avaliação simples da recuperação;
- persistência do índice;
- filtro ou melhoria de metadados;
- deduplicação;
- comparação documentada entre estratégias;
- teste automatizado relevante.

Não geram vantagem por si só:

- interface bonita;
- animações;
- deploy;
- Docker;
- banco vetorial de marca específica;
- múltiplos agentes;
- grande quantidade de arquivos;
- API paga.

Não há uma falha isolada que zere automaticamente toda a prova. Cada item será pontuado conforme evidências observáveis de implementação e compreensão.

Na correção, todos os projetos receberão as mesmas oito perguntas reservadas dentro do escopo. Cada pergunta pode valer 1 dos 8 pontos de relevância quando uma fonte aceita e um trecho realmente relacionado aparecem entre os três primeiros resultados. Uma nona pergunta, fora do escopo, será usada apenas para observar o comportamento e a reflexão do aluno.

### Confirmação individual, se necessária

O professor poderá solicitar uma conversa de 7 a 10 minutos apenas para confirmar evidências de compreensão, funcionamento ou autoria. O mesmo gatilho será aplicado a todos os casos equivalentes: candidatos até três pontos de distância do corte provisório ou entregas com evidência importante ainda inconclusiva.

Essa conversa não cria requisitos novos nem pontos bônus. Poderá ser solicitado apenas que você explique o fluxo ou faça uma alteração pequena no projeto existente, como trocar a pergunta ou mudar `top_k` de 3 para 5. A nota poderá ser corrigida somente nos critérios diretamente confirmados ou contraditos, com justificativa registrada.

## 15. Critério de sucesso

Ao final, outra pessoa deve conseguir executar seu projeto e entender:

- como os documentos viraram chunks;
- como os chunks viraram representações pesquisáveis;
- como uma pergunta encontra trechos relevantes;
- como cada resultado volta ao documento original;
- quais limitações ainda existem.

É isso que será considerado evidência de compreensão e capacidade de implementação.
