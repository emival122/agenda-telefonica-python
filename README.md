# 📞 PhoneBook Pro – Sistema de Gestão de Contatos

![GitHub License](https://img.shields.io/github/license/emival122/agenda-telefonica?style=flat-square&color=4fa882)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python)
![Repo Size](https://img.shields.io/github/repo-size/emival122/agenda-telefonica?style=flat-square)

<p align="center">
  <img src="./assets/screenshot.png" alt="Demonstração do Sistema" width="800px">
</p>

---

## 📌 Sobre o Projeto
O **PhoneBook Pro** é uma aplicação desktop para gerenciamento de contatos telefônicos, desenvolvida com foco em simplicidade, organização e performance.  
O sistema utiliza **separação de camadas (UI e Dados)** e persistência em arquivos CSV, garantindo leveza, portabilidade e fácil manutenção.

---

## ✨ Funcionalidades
- ✅ **CRUD Completo:** cadastrar, visualizar, editar e remover contatos  
- 🔍 **Busca Inteligente:** filtro rápido por número de telefone  
- 💾 **Auto-Save:** dados salvos automaticamente no arquivo `dados.csv`  
- 🎨 **Interface Moderna:** layout em cards com feedback visual  
- 🛡️ **Tratamento de Erros:** validação de campos vazios e arquivos inexistentes  

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10+  
- **Interface Gráfica:** Tkinter  
- **Persistência de Dados:** Módulo `csv` (nativo)  
- **Documentação:** Markdown  

---

## 📂 Estrutura do Projeto
```text
agenda-telefonica/
│
├── assets/
│   └── screenshot.png
├── dados.csv
├── main.py
├── ui.py
├── repository.py
└── README.md
