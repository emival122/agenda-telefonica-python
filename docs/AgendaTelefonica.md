

## Descrição do Código

### Arquivo `main.py`
Responsável pela interface gráfica e interação com o usuário.

Principais funções:
- `mostrar_tabela()` → exibe os contatos na tabela
- `inserir()` → adiciona um novo contato
- `deletar()` → remove um contato selecionado
- `preparar_atualizacao()` → carrega dados para edição
- `confirmar_edicao()` → salva alterações
- `procurar_contato()` → busca contato pelo telefone
- `limpar_campos()` → limpa os campos do formulário

### Arquivo `dados.py`
Responsável pela lógica de dados, contendo funções como:
- `adicionar_dados()`
- `ver_dados()`
- `remover_dados()`
- `atualizar_dados()`

## Como Executar
1. Certifique-se de ter Python instalado
2. Execute o arquivo principal:
```bash
python main.py
