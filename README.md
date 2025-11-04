# 🩺 Sistema Clínico
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

> Projeto de integração entre **Python** e **PostgreSQL**, com estrutura modular e operações completas de CRUD.

---

## 📘 Sobre o Projeto

O **Sistema Clínico** foi desenvolvido com o objetivo de demonstrar o uso de **banco de dados SQL** integrado a uma aplicação em **Python**, criando uma base sólida para um sistema de gerenciamento clínico.

Esta é a **primeira etapa do projeto**, que contempla toda a parte de **backend e banco de dados**.
A **segunda etapa** (em desenvolvimento) implementará a **interface gráfica com Tkinter e CustomTkinter**, permitindo que o usuário final interaja com o sistema de forma intuitiva e visual.

---

## 🎯 Objetivos da Primeira Etapa

✅ Modelar e criar um banco de dados relacional no PostgreSQL\
✅ Implementar todas as operações CRUD (Create, Read, Update, Delete)\
✅ Garantir integridade relacional entre as tabelas\
✅ Integrar com Python de forma modular e reutilizável\
✅ Deixar a estrutura pronta para futura interface Tkinter e CustomTkinter

---

## 🧩 Estrutura do Projeto

```
clinic_system/
├── database.py          # Conexão e gerenciamento do banco PostgreSQL
├── patients.py          # CRUD de pacientes
├── doctors.py           # CRUD de médicos
├── consultations.py     # CRUD de consultas
├── treatments.py        # CRUD de tratamentos
└── main.py              # Ponto de execução principal do sistema
```

---

## 🗃️ Modelagem do Banco de Dados

A estrutura foi projetada para representar o relacionamento entre pacientes, médicos, consultas e tratamentos.

```sql
-- Tabela de Pacientes
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    date_of_birth DATE,
    gender CHAR(1),
    phone VARCHAR(20),
    address VARCHAR(255),
    active BOOLEAN DEFAULT TRUE
);

-- Tabela de Médicos
CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    phone VARCHAR(15),
    active BOOLEAN DEFAULT TRUE
);

-- Tabela de Consultas
CREATE TABLE consultations (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    doctor_id INT REFERENCES doctors(id),
    consultation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    observations VARCHAR(255),
    service_type VARCHAR(50),
    active BOOLEAN DEFAULT TRUE
);

-- Tabela de Tratamentos
CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    consultation_id INT REFERENCES consultations(id),
    medications VARCHAR(255),
    treatment_description TEXT
);
```

---

## 🧠 Estrutura Relacional

```
Patients (1) ────< Consultations >──── (1) Doctors
                        │
                        ▼
                    Treatments
```

* Um **paciente** pode ter várias **consultas**
* Um **médico** pode atender várias **consultas**
* Cada **consulta** pode gerar um ou mais **tratamentos**

---

## 🐍 Integração com Python

A conexão com o banco é feita via `psycopg2`, com uso de **context manager** (`with`) para segurança e commits automáticos.

```python
# Exemplo de uso do banco
with get_cursor() as cursor:
    cursor.execute("SELECT * FROM patients WHERE active = TRUE;")
    dados = cursor.fetchall()
```

Cada módulo (`patients.py`, `doctors.py`, etc.) contém as funções CRUD correspondentes, como:

```python
def add_patient():
    nome = input("Nome do paciente: ")
    telefone = input("Telefone: ")
    with get_cursor() as cursor:
        cursor.execute("INSERT INTO patients (full_name, phone) VALUES (%s, %s);", (nome, telefone))
    print("Paciente adicionado com sucesso!")
```

---

## 🧱 Tecnologias Utilizadas

| Tecnologia                        | Descrição                                 |
| --------------------------------- | ----------------------------------------- |
| 🐘 **PostgreSQL**                 | Banco de dados relacional                 |
| 🐍 **Python 3.13**                | Linguagem principal do projeto            |
| ⚙️ **psycopg2**                   | Biblioteca de conexão com PostgreSQL      |
| 🧩 **Arquitetura modular**        | Cada entidade tem seu próprio módulo CRUD |
| 🎨 **CustomTkinter (em desenvolvimento)** | Interface moderna e responsiva    |
| 🎨 **Tkinter** | Biblioteca base da interface |
---

## ⚙️ Execução do Projeto

### 1️⃣ Configure o banco de dados:

* Crie o banco no PostgreSQL (ex: `clinica_bd`)


* Execute o script SQL acima para criar as tabelas
* Atualize as credenciais no `database.py`

### 2️⃣ Instale as dependências:

```
pip install psycopg2-binary customtkinter
```

### 3️⃣ Execute o projeto:

```
python main.py
```

---

## 💡 Segunda Etapa — Interface Tkinter (em desenvolvimento)

A próxima versão do sistema trará:

* **Dashboard em blocos coloridos** (Pacientes, Médicos, Consultas, Tratamentos)
* **Tabelas interativas** com exibição e edição de dados
* **Botões de ação diretos** (Adicionar, Editar, Excluir)
* **Filtros e busca em tempo real**
* **Design moderno e responsivo**

Exemplo visual planejado:

```
[👤 Pacientes]   [🧑‍⚕️ Médicos]
[📋 Consultas]   [💊 Tratamentos]
```

---

## 🧑‍💻 Autor

**Felipe Zeglan**
💼 Desenvolvedor Python | SQL | Automação | Sistemas Desktop\
📧 *felipezeglan@outlook.com*

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e demonstração técnica.
Sinta-se à vontade para clonar, estudar e adaptar.

---
