# Sistema de Cadastro de Usuários

Este é um sistema simples de cadastro de usuários, desenvolvido em Python utilizando a biblioteca Tkinter para criação de uma interface gráfica. O programa permite o registro de informações pessoais e exibe esses dados em uma tabela para fácil visualização.

## Funcionalidades

- **Cadastro de Usuários**: Permite o cadastro de informações como Código, Nome Completo, Idade, Gênero, E-mail, Telefone, Endereço, Nome dos Pais, RG, CPF, e Formação Acadêmica.
- **Validação de Campos Obrigatórios**: Os campos "Código" e "Nome Completo" são obrigatórios e o programa exibe um alerta se forem deixados em branco.
- **Exibição de Dados**: Os dados cadastrados são exibidos em uma tabela (`Treeview`) para fácil visualização.
- **Interface Gráfica Intuitiva**: Design responsivo e amigável, com uma paleta de cores suaves para facilitar o uso.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para a criação de interfaces gráficas.
- **Tkinter.ttk**: Fornece widgets com estilo mais moderno, como botões e rótulos.
- **Tkinter.messagebox**: Usado para exibir mensagens de aviso e erro ao usuário.

## Arquitetura

O sistema foi desenvolvido de forma modular para facilitar a manutenção e a expansão futura:

1. **Função `criar_campo`**:
   - Esta função é responsável por criar os campos de entrada (input) com rótulos (labels) e caixas de texto (entries). 
   - Torna o código mais organizado e evita duplicação, criando um padrão para todos os campos de entrada.

2. **Função `adicionarRegistro`**:
   - Valida se os campos obrigatórios foram preenchidos antes de permitir o cadastro.
   - Adiciona os dados do usuário na tabela (`Treeview`).
   - Limpa os campos após o registro para facilitar novos cadastros.

3. **Interface Gráfica**:
   - A interface foi construída utilizando o gerenciador de layout `grid`, que organiza os widgets em linhas e colunas.
   - O programa usa o `Treeview` para exibir os dados cadastrados em formato de tabela.
