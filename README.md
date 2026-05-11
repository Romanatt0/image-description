# POC - Agente de IA para Descrição de Imagens

POC de um agente que descreve imagens usando **LLaVA via Ollama**, com orquestração em **LangChain** e interface web em **Streamlit**.

## Requisitos

- Python 3.10+
- Ollama instalado e rodando
- Modelo LLaVA baixado no Ollama

## Como rodar

1. Instale dependências Python:

```bash
pip install -r requirements.txt
```

2. Garanta que um modelo vision está disponível no Ollama:

```bash
ollama pull moondream
```

Opcional (mais pesado):

```bash
ollama pull llava:7b
```

3. Inicie o app Streamlit:

```bash
streamlit run app.py
```

4. No navegador:
   - Faça upload de uma imagem
   - (Opcional) ajuste o prompt
   - Clique em **Gerar descrição**

## Estrutura

- `agent.py`: agente LangChain que envia imagem + prompt para o modelo LLaVA no Ollama.
- `app.py`: front-end Streamlit para upload e visualização da descrição.
- `requirements.txt`: dependências do projeto.

## Observações

- O modelo padrão no app é `moondream` (mais leve para máquinas com pouca RAM).
- Para reduzir consumo de memória, mantenha `num_ctx` baixo (ex.: 256 ou 512).
- Se sua máquina tiver mais memória, use `llava:7b` para descrições geralmente mais ricas.
- Se ocorrer erro de conexão, confira se o serviço do Ollama está ativo.
