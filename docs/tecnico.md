# ⚙️ Documentação Técnica

Esta documentação detalha a estrutura interna e a lógica de dados do projeto.

## 🏗️ Arquitetura do Sistema
O projeto utiliza uma separação simples entre Interface e Lógica de Dados:
* **`main.py`**: Gerencia a interface gráfica (Tkinter), eventos de botões e exibição na Treeview.
* **`dados.py`**: Contém as funções de CRUD que manipulam o arquivo CSV.

## 💾 Persistência de Dados
Os dados são armazenados em um arquivo chamado `dados.csv` na raiz do projeto.
* **Formato**: CSV (Comma Separated Values).
* **Colunas**: Nome, Sexo, Telefone, Email.
* **Encoding**: `utf-8` para suporte a acentos.

## 📋 Fluxo das Funções (CRUD)

1. **Leitura (`ver_dados`)**: 
   - Abre o arquivo em modo de leitura (`r`).
   - Converte cada linha em uma lista e retorna para a interface.

2. **Escrita (`adicionar_dados`)**: 
   - Utiliza o modo `a+` (append) para adicionar novas linhas sem apagar o conteúdo anterior.

3. **Exclusão (`remover_dados`)**: 
   - Lê todo o arquivo para uma lista temporária.
   - Filtra a lista removendo o item pelo telefone.
   - Sobrescreve o arquivo original com a nova lista filtrada.

4. **Atualização (`atualizar_dados`)**: 
   - Funciona de forma similar à exclusão, mas em vez de apenas remover, substitui a linha correspondente pelos novos dados antes de sobrescrever o arquivo.

## 🎨 Cores Utilizadas (Paleta)
* **Azul Escuro (`co3`):** `#38576b` (Cabeçalho)
* **Verde (`co2`):** `#4fa882` (Sucesso/Adicionar)
* **Vermelho (`co6`):** `#ef5350` (Deletar)
* **Fundo (`co0`):** `#f0f3f5`
