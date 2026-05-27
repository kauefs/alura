# ReColocAI – FrameWork de Orquestração

## Visão Geral

Sistema multi-agente para desenvolvimento de carreira, ajudando a descobrir vagas de emprego, identificar lacunas de habilidades, encontrar cursos direcionados e praticar habilidades de entrevista através de pipeline orquestrado de agentes especializados.

## Arquitetura

```
┌─────────────────────────────────────────────────┐
│                  Usuário                        │
└────────────────────┬────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│              MAESTRO (Orquestrador)             │
│  - Interface primária com o usuário             │
│  - Coordena agentes especializados              │
│  - Consolida resultados e apresenta ao usuário  │
└──┬──────────────┬──────────────┬────────────────┘
   │              │              │
   ▼              ▼              ▼
┌─────────┐  ┌──────────┐  ┌──────────────┐
│ SCOUT   │  │ CURATOR  │  │ COACH        │
│ (Busca  │  │ (Busca   │  │ (Simulador   │
│ de      │  │ de       │  │ de           │
│Empregos)│  │ Cursos)  │  │ Entrevistas) │
└─────────┘  └──────────┘  └──────────────┘
```

## Estrutura de Diretórios

```
recoloca-ia/
├── README.md                          # Este arquivo
├── data/
│   ├── personality-quiz.md            # Respostas do quiz do usuário (modelo)
│   ├── user-profile.md                # Perfil consolidado (modelo)
│   ├── job-search-results.md          # Resultados de busca de vagas
│   ├── course-recommendations.md      # Recomendações de cursos
│   └── interview-session.md           # Rastreamento de estado da entrevista do Coach
├── personas/
│   ├── maestro.md                     # Definição do orquestrador Maestro
│   ├── scout.md                       # Definição do agente de busca de vagas Scout
│   ├── curator.md                     # Definição do agente de busca de cursos Curator
│   └── coach.md                       # Definição do agente de simulação de entrevista Coach
└── skills/
    ├── dispatch.md                    # Protocolo de despacho e handoff de agentes
    ├── firecrawl.md                   # Uso do CLI Firecrawl para busca e raspagem
    ├── job-search.md                  # Skill do Scout: fluxo de busca de vagas
    ├── course-analysis.md             # Skill do Curator: fluxo de busca de cursos
    └── interview-sim.md              # Skill do Coach: fluxo de simulação de entrevista
```

## Como Usar

### Pré-requisitos

1. **Zed**        – editor assistido por IA usado para executar agentes
2. **OpenRouter** – configurado como provedor de LLM no Zed
3. **FireCrawl**  – instalado & configurado para busca & raspagem web

### Configuração

1. Certificar-se de que o FireCrawl está instalado e o CLI está disponível no PATH
2. Configurar chave API do FireCrawl no ambiente
3. Abrir o projeto no Zed
4. Carregar persona do Maestro (`personas/maestro.md`) como agente primário

### Executando o Agente

1. Iniciar o Zed com o projeto ReColocAI aberto
2. Inicializar o agente Maestro a partir de `personas/maestro.md`
3. Maestro cumprimenta o usuário e inicia o quiz de personalidade
4. Após o quiz, escolher no menu:
   - **A** – Buscar vagas de emprego (despacha Scout)
   - **B** – Encontrar cursos para preencher lacunas de habilidades (despacha Curator)
   - **C** – Praticar com entrevista simulada (despacha Coach 6 vezes)
   - **D** – Refazer o quiz (sobrescreve dados do quiz e reseta resultados)

## Agentes

### Maestro (Orquestrador)

Interface primária que gerencia o fluxo de conversa, mantém arquivos de estado e despacha sub-agentes via `spawn_agent`, mas nunca realizando buscas de emprego ou cursos diretamente, sempre delegando ao Scout ou ao Curator.

**Localização**: `personas/maestro.md`

**Responsabilidades**:

- Cumprimentar o usuário e executar o quiz de personalidade
- Gerar e manter `data/user-profile.md`
- Apresentar o menu após cada operação
- Construir envelopes de despacho para sub-agentes
- Analisar envelopes de resposta e exibir resultados
- Lidar com refazer quiz (opção D do menu)
- Manter `data/interview-session.md` durante os despachos do Coach

### Scout (Agente de Busca de Empregos)

Busca vagas de emprego usando o FireCrawl em Indeed, Catho, LinkedIn, GlassDoor e InfoJobs, realizando correspondência de habilidades contra o perfil do usuário, retornando até 5 vagas com análise de correspondência.

**Localização**: `personas/scout.md`
**Skill**: `skills/job-search.md`

**Fluxo de Trabalho**:

1. Ler perfil do usuário do contexto do despacho
2. Executar `firecrawl search "vagas [area] [localização]" --json`
3. Fazer scrape de até 5 URLs de vagas para detalhes completos
4. Comparar habilidades necessárias com as habilidades atuais do usuário
5. Retornar resultados em formato de lista numerada com dados de correspondência de habilidades

### Curator (Agente de Busca de Cursos)

Busca na Alura cursos que abordem lacunas de habilidades identificadas pelo Scout, retornando lista curada e ordenada de recomendações de cursos com metadados (duração, nível).

**Localização**: `personas/curator.md`
**Skill**: `skills/course-analysis.md`

**Fluxo de Trabalho**:

1. Validar que resultados de busca de vagas existem
2. Extrair habilidades faltantes dos resultados de busca de vagas
3. Executar `firecrawl search "alura [habilidade]" --json` para cada habilidade faltante
4. Fazer scrape das URLs dos cursos para extrair duração e nível
5. Ordenar cursos por nível de dificuldade
6. Retornar recomendações ordenadas com ordem de estudo sugerida

### Coach (Agente de Simulação de Entrevista)

Conduz entrevista simulada estruturada de 5 perguntas, gera perguntas específicas por função, avalia cada resposta, fornece feedback e entrega pontuação final.

**Localização**: `personas/coach.md`
**Skill**: `skills/interview-sim.md`

**Fluxo de Trabalho**:

1. Receber contexto da vaga e perfil do usuário do despacho
2. Despacho 1: gerar Pergunta 1 (sem histórico anterior)
3. Despacho 2: avaliar R1, gerar Pergunta 2
4. Despacho 3: avaliar R2, gerar Pergunta 3
5. Despacho 4: avaliar R3, gerar Pergunta 4
6. Despacho 5: avaliar R4, gerar Pergunta 5
7. Despacho 6: avaliar R5, calcular pontuação final e áreas de melhoria

## Início Rápido

1. Abrir o projeto no Zed
2. Carregar `personas/maestro.md` como agente ativo
3. Siguir o quiz de personalidade guiado pelo Maestro
4. Selecionar a opção A do menu para buscar vagas de emprego
5. Selecionar a opção B do menu para encontrar cursos para suas lacunas de habilidades
6. Selecionar a opção C do menu para praticar com uma entrevista simulada

## Diretrizes do Modelo MoE

Este sistema usa arquitetura Mixture-of-Experts (MoE) com regras de formatação rigorosas:

- Nenhuma instrução ambígua. Cada etapa deve especificar exatamente o que fazer, qual ferramenta usar e qual formato de saída produzir.
- Nenhuma tabela markdown em qualquer saída. Usar listas numeradas com pares chave-valor para todos os dados estruturados.
- Todos os caminhos de arquivo devem ser relativos à raiz do projeto com prefixo explícito `data/`.
- Se uma ferramenta falhar, relatar a falha explicitamente. Nunca continuar silenciosamente em caso de erro.
- Nunca inventar dados. Se uma busca ou raspagem do firecrawl falhar, relatar o erro exato e parar.
