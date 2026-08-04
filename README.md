# Sistema de Login em Python

## Sobre o projeto

Este projeto consiste em um sistema simples de cadastro e autenticação
de usuários desenvolvido em Python.

O objetivo do projeto é aplicar os conhecimentos adquiridos durante meus
estudos e aprimorar o sistema gradualmente conforme avanço no aprendizado
da linguagem.

## Funcionalidades atuais

- Cadastro de usuários
- Login de usuários
- Exclusão de usuários
- Listagem de usuários
- Armazenamento dos dados em arquivo JSON

## Estrutura do projeto

- `main.py` - arquivo principal do programa
- `cadastro.py` - responsável pelo cadastro de usuários
- `funcoes.py` - contém funções utilizadas pelo sistema
- `sistema.py` - contém funcionalidades relacionadas ao sistema
- `usuarios.json` - armazenamento dos usuários cadastrados

## Como executar

É necessário ter o Python instalado.

No terminal, dentro da pasta do projeto:

python3 main.py

## Status do projeto

🚧 Projeto em desenvolvimento.

Esta é uma versão inicial criada com foco no aprendizado. Novas
funcionalidades e melhorias de segurança serão implementadas conforme
o desenvolvimento dos meus conhecimentos em Python.

## Próximas melhorias

- [ ] Definir tamanho mínimo para senhas
- [ ] Adicionar regras de validação de senha
- [ ] Melhorar o tratamento de entradas inválidas
- [ ] Implementar armazenamento seguro das senhas
- [ ] Aprimorar a persistência dos dados

## Aviso

Este é um projeto educacional e ainda não implementa os mecanismos de
segurança necessários para utilização como um sistema real de autenticação.

## Atualização

Implementação da função len() para criar uma validação de segurança no cadastro, garantindo que o sistema só aceite senhas com no mínimo 6 caracteres e evitando senhas fracas.