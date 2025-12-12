# CRUD de Funcionários em Django + MySQL

Projeto desenvolvido para a Atividade Avaliativa 3 na disciplina de Desenvolvimento de Aplicações do curso de Análise e Desenvolvimento de Sistemas (ADS). O objetivo foi construir um sistema completo de **CRUD (Create, Read, Update e Delete)** utilizando **Python**, **Django**, **MySQL** e **Bootstrap**.

## 🧩 Descrição do Projeto

O sistema implementa o cadastro de funcionários, permitindo:

- Criar novos funcionários  
- Listar todos os funcionários cadastrados  
- Editar informações de um funcionário existente  
- Exibir detalhes de um funcionário  
- Remover registros do banco de dados  

O CRUD foi construído seguindo a arquitetura do Django, utilizando:

- **Models** para definir a estrutura dos dados  
- **Views** para controlar as regras de negócio  
- **URLs** para roteamento entre as páginas  
- **Templates (HTML + Bootstrap)** para a interface do usuário  
- **MySQL** para persistência dos dados  
- **ORM do Django** para comunicação entre a aplicação e o banco  
- **App Django dedicado (“app”), configurado com AppConfig e registrado em INSTALLED_APPS**

## 🗂 Páginas (Templates HTML)

As páginas da aplicação foram desenvolvidas em HTML utilizando Bootstrap para estilização.

O projeto contém:

- `listar_funcionarios.html` – exibe todos os funcionários cadastrados  
- `form_funcionario.html` – formulário para criar e editar funcionários  
- `exibir_funcionario.html` – detalhamento do funcionário  
- `remover_funcionario.html` – página de confirmação de exclusão  

Cada template utiliza Django Template Language para renderizar os dados enviados pelas views.

## 🛠 Tecnologias Utilizadas

- Python  
- Django  
- MySQL (via MySQL Workbench)  
- Bootstrap 5  
- Django ORM  
- mysqlclient
- HTML

## 📁 Estrutura do Projeto

```
/projeto
│── app/                 # Aplicação principal do CRUD
│── templates/           # Arquivos HTML com Bootstrap
│── projeto/             # Configurações (settings, urls, wsgi)
│── manage.py            # Gerenciador do Django
│── requirements.txt     # Dependências (opcional)
│── .gitignore           # Arquivos ignorados pelo Git
```

## 📋 Processo de Desenvolvimento 

1. Instalação do Django e dependências via terminal  
2. Criação do projeto e da aplicação  
3. Configuração das URLs, views, models e templates  
4. Implementação das páginas HTML com Bootstrap  
5. Integração com MySQL Workbench  
6. Testes das operações CRUD  

## 📄 Licença

Uso acadêmico.
