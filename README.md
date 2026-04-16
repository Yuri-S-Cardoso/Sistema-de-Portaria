# Sistema de Portaria

Sistema web desenvolvido em **Django** para controle de **entrada e saída de veículos internos e de terceiros**, com foco em operação de portaria, logística, expedição e recebimento.

A aplicação permite registrar movimentações de veículos, associar informações de motorista, carga, lacre, notas fiscais, malotes, paletes e horários, além de gerar comprovantes, relatórios e exportação para Excel.

---

## Visão geral

O projeto foi construído para atender rotinas operacionais de portaria e controle logístico, centralizando o registro de veículos próprios da operação e de veículos de terceiros em um único sistema.

Pelo fluxo implementado, o sistema oferece:

- login por sessão customizada
- controle de acesso por nível de usuário
- cadastro de veículos, motoristas e usuários
- registro de saída e retorno de veículos internos
- registro de entrada e saída de veículos de terceiros
- emissão de cupom/comprovante para terceiros
- consulta de relatórios por período e placa
- exportação de relatórios em Excel

---

## Finalidade do sistema

A finalidade principal da aplicação é controlar operacionalmente a portaria de uma empresa, especialmente ambientes como:

- centros de distribuição
- operações industriais
- atacados
- pátios logísticos
- docas de expedição e recebimento

### Problemas que o sistema resolve

- registrar movimentação de frota interna
- controlar entrada e saída de terceiros
- armazenar dados de placas, motoristas e empresas
- registrar carga, lacre, NF, malotes e paletes
- manter rastreabilidade de horários
- emitir comprovantes de entrada
- gerar relatórios operacionais
- exportar dados para análise externa

### Público provável

O sistema parece adequado para uso por:

- porteiros
- operadores de expedição
- operadores de recebimento
- supervisores logísticos
- equipe administrativa
- gerentes de operação

---

## Funcionalidades principais

### Autenticação e sessão
- Login com matrícula e senha
- Sessão customizada baseada no model `Porteiro`
- Controle de acesso a páginas protegidas
- Timeout de sessão por inatividade
- Nível de acesso por tipo de usuário

### Cadastro de apoio
- Cadastro de veículos
- Cadastro de motoristas
- Cadastro de usuários operacionais
- Cadastro de empresas de terceiros por CNPJ

### Fluxo de veículos internos
- Registro de saída de veículos internos
- Registro de retorno/entrada de veículos internos
- Controle de placas ainda não retornadas
- Armazenamento temporário da saída até o retorno
- Redirecionamento de fluxo conforme status do veículo

### Fluxo de veículos de terceiros
- Registro de entrada de terceiros
- Registro de saída/liberação de terceiros
- Consulta de empresa por CNPJ
- Verificação de movimentação recente da placa
- Emissão de cupom/comprovante de entrada

### Dados operacionais registrados
Dependendo do fluxo, o sistema registra informações como:

- placa
- motorista
- empresa
- carga
- lacre
- notas fiscais
- malotes
- paletes
- horários
- observações
- dados de descarga e cobrança

### Relatórios
- Relatórios por período
- Filtro por placa
- Relatório de saída de veículos internos
- Relatório de entrada de veículos internos
- Relatório de entrada de terceiros
- Relatório de saída de terceiros

### Exportação
- Exportação de relatórios de Inter para Excel
- Geração de planilha usando `openpyxl`

### Validações dinâmicas
- Verificação de entrada já registrada
- Busca de veículo
- Verificação de CNPJ
- Busca de razão social por CNPJ
- Busca de dados de terceiros via AJAX

---

## Tecnologias utilizadas

### Back-end
- **Python**
- **Django 4.2.1**
- **SQLite**
- **openpyxl**

### Front-end
- **HTML com templates Django**
- **CSS próprio**
- **JavaScript puro**
- **jQuery via CDN**
- **Font Awesome via CDN**

### Recursos do Django
- `django.contrib.sessions`
- `django.contrib.auth`
- `django.contrib.admin`
- `django.contrib.staticfiles`

> Observação: embora o projeto tenha recursos do `auth` instalados, o fluxo principal de autenticação foi implementado de forma customizada.

---

## Arquitetura do projeto

A aplicação segue a arquitetura clássica de um **monólito Django MVT (Model-View-Template)**.

### Características observadas
- views baseadas em função
- renderização no servidor com templates Django
- formulários HTML manuais
- regras de negócio concentradas em `views.py`
- persistência com Django ORM
- interações dinâmicas com JavaScript e jQuery
- ausência de separação forte por camadas

É um sistema de perfil operacional, construído com foco em fluxo direto de cadastro, registro e consulta.

---

## Estrutura do projeto

```bash
Sistema-de-Portaria/
├── manage.py
├── portaria/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── porteiros/
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── middleware.py
│   ├── decorators.py
│   ├── admin.py
│   ├── tests.py
│   ├── migrations/
│   ├── templates/
│   │   └── porteiros/
│   └── static/
│       ├── css/
│       ├── imagens/
│       └── admin/
├── db.sqlite3
└── PORTARIA.bat
