# Projeto de detecção de bordas
## Configuração do ambiente

1. Crie o ambiente virtual:

```bash
python -m venv .venv
```

2. Ative o ambiente virtual:

Windows:
```bash
.venv\Scripts\activate
```

Linux:
```bash
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Observação sobre o Jupyter Notebook

Dependendo do ambiente utilizado, ao executar as células que utilizam `ipywidgets`, pode ocorrer ocasionalmente uma falha na renderização dos componentes interativos (botões).

Caso isso aconteça, recarregue a página e execute novamente a célula. Não é necessário reinstalar as dependências ou recriar o ambiente virtual.