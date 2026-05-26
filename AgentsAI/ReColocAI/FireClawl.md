# Skill FireCrawl

## Propósito

Esta skill fornece capacidades de busca e raspagem web para o sistema ReColocAI, usando CLI do Firecrawl para descobrir empregos dos principais portais de emprego e encontrar cursos na Alura.

## Fontes Agregadas

O Firecrawl agrega conteúdo destas plataformas:
- Indeed
- Catho
- LinkedIn
- Glassdoor
- Infojobs

## Ferramentas

- **Zed**: `terminal`
- **CLI**: `firecrawl`

## Comandos

### Busca Web

Busca conteúdo nas fontes agregadas:

```
firecrawl search "[consulta]" --json
```

**Parâmetros**:
- `[consulta]` – string de consulta de busca

**Retorna**: Array JSON onde cada resultado contém:
- `url`         – URL da página
- `title`       – título da página
- `description` – breve trecho ou descrição

### Raspagem de Página

Faça scrape de uma única URL e extraia seu conteúdo como markdown:

```
firecrawl scrape <url> --format markdown
```

**Parâmetros**:
- `<url>` – URL completa para fazer scrape

**Retorna**: Conteúdo da página formatado em markdown

**Fallback**: Se `firecrawl scrape` falhar ou expirar, use o `title` e `description` do resultado de busca como dados de fallback.

## Descoberta de Empregos

Busque vagas de emprego:

```
firecrawl search "vagas [area] [localização]" --json
```

**Parâmetros**:
- `[area]`        – área  alvo  do usuário (ex: Frontend, Backend, Ciência de Dados)
- `[localização]` – localização do usuário (ex: São Paulo, Remoto)

**Exemplo**:
```
firecrawl search "vagas Frontend São Paulo" --json
```

## Busca de Cursos

Busque na Alura cursos correspondentes a uma habilidade:

```
firecrawl search "alura [habilidade]" --json
```

**Parâmetros**:
- `[habilidade]` – nome da habilidade (ex: React, Python, Docker)

**Exemplo**:
```
firecrawl search "alura Docker" --json
```

## Tratamento de Erros

- **Código de saída diferente de zero**: se qualquer comando firecrawl retornar código de saída diferente de zero, relatar a mensagem de erro exata. Não continuar silenciosamente.
- **Timeout**: se um comando expirar, relate-o como erro de timeout. Não tente novamente mais de uma vez.
- **Resultados vazios**: se uma busca não retornar resultados, relatar que nenhum resultado foi encontrado. Não fabricar dados.
- **Falha de scrape**: se `firecrawl scrape` falhar para URL específica, usar dados de fallback do resultado de busca e notar a URL com falha no campo de erros. Continuar processando URLs restantes.
- **Campos ausentes**: se o conteúdo raspado carecer de campos esperados (ex: duração, nível para cursos), marque-os como `não especificado` em vez de inventar valores.

## Regras Gerais

- Nunca inventar ou adivinhar dados. Se o firecrawl falhar, relatar o erro e parar.
- Sempre passar `--json` para `firecrawl search` para saída estruturada.
- Sempre passar `--format markdown` para `firecrawl scrape` para análise consistente.
- Processar URLs sequencialmente para evitar limitação de taxa.
