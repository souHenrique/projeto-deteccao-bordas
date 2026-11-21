# Projeto de detecção de bordas
## Configuração do ambiente

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Observação sobre o Jupyter Notebook

Ao executar as células que utilizam `ipywidgets`, pode ocorrer ocasionalmente uma falha na renderização dos componentes interativos (botões).

Caso isso aconteça, recarregue a página do ambiente (Codespaces/VS Code) e execute novamente a célula. Não é necessário reinstalar as dependências ou recriar o ambiente virtual.