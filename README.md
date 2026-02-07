# 🏭 Almoxarifado Industrial 2.0

> Sistema de Gestão de Auditorias 5S e Controle de Qualidade Industrial.

![Status do Projeto](https://img.shields.io/badge/STATUS-FINALIZADO-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)

## 📄 Sobre o Projeto

O **Almoxarifado 2.0** é uma solução web desenvolvida para modernizar e digitalizar o processo de auditoria de qualidade (Metodologia 5S) em ambientes industriais. 

O sistema substitui pranchetas e planilhas manuais por uma aplicação **Mobile-First**, permitindo que auditores realizem inspeções diretamente pelo celular, gerem relatórios automáticos em PDF e acompanhem indicadores de desempenho (KPIs) em tempo real.

## 🚀 Funcionalidades Principais

* **📱 Auditoria Mobile:** Interface otimizada para celulares, facilitando a inspeção no chão de fábrica (App Bar, Cards, Botões Grandes).
* **📊 Dashboard Gerencial:** Visualização gráfica da evolução das notas, média semanal e ranking de setores.
* **📄 Geração de Relatórios:** Criação automática de PDFs detalhados com notas, observações e status de conformidade.
* **⚙️ Gerenciamento Dinâmico:** Painel administrativo para criar, editar e excluir perguntas do checklist sem mexer no código.
* **🔐 Controle de Acesso:** Sistema de login com níveis de permissão (Colaborador vs. Admin/Staff).
* **🗂️ Histórico Completo:** Registro imutável de todas as auditorias realizadas para fins de compliance.

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python, Django Framework.
* **Front-end:** HTML5, CSS3, TailwindCSS (Design Responsivo).
* **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Compatível para Produção).
* **Bibliotecas Chave:**
    * `xhtml2pdf`: Geração de relatórios PDF.
    * `chart.js` (ou similar): Renderização de gráficos.

## 🔧 Como Rodar o Projeto

### Pré-requisitos
* Python 3.x instalado
* Git instalado

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/seu-usuario/almoxarifado-2.0.git](https://github.com/seu-usuario/almoxarifado-2.0.git)
    cd almoxarifado-2.0
    ```

2.  **Crie e ative o ambiente virtual**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser # Crie o admin do sistema
    ```

5.  **Inicie o Servidor**
    ```bash
    python manage.py runserver
    # Para acesso mobile na mesma rede: python manage.py runserver 0.0.0.0:8000
    ```

6.  **Acesse:**
    * Navegador: `http://127.0.0.1:8000`

## 🤝 Contribuição

Este projeto foi desenvolvido como parte do [Trabalho de Conclusão / Estágio] para a empresa [Nome da Empresa/Instituição].

## 👤 Autor

**Pablo Augusto**
* LinkedIn: https://www.linkedin.com/in/pablovelloso/


---
