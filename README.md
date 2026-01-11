# 🏭 Controle Industrial & Gestão 5S

Sistema web desenvolvido em **Django** para gestão de processos industriais, focado no controle de estoque e auditorias de qualidade (Programa 5S). O projeto visa eliminar o uso de papel, digitalizar checklists e gerar indicadores de desempenho em tempo real.

## 🚀 Funcionalidades Principais

### 📦 Módulo de Estoque
- **Cadastro de Produtos:** Gestão completa de itens e materiais.
- **Movimentação:** Registro de Entradas e Saídas com rastreabilidade.
- **Histórico:** Log de atividades por usuário e data.
- **Controle de Nível:** Visualização rápida de saldos.

### ✅ Módulo de Qualidade (5S)
- **Checklists Digitais:** Auditorias divididas pelos sensos (Seiri, Seiton, Seiso, Seiketsu, Shitsuke).
- **Evidências:** Upload de fotos para itens "Não Conformes".
- **Cálculo Automático:** Geração de nota final baseada nas respostas.
- **Dashboard de KPIs:** - Gráficos de evolução semanal.
  - Ranking de melhores e piores setores.
  - Indicadores visuais de conformidade.

### 👤 Painel do Usuário
- Perfil com foto, cargo e matrícula.
- Histórico de atividades recentes.
- Acesso restrito via login.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3, Django 4+
- **Frontend:** HTML5, Tailwind CSS (Estilização), Chart.js (Gráficos)
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Testes:** Pytest, Pytest-Django

---

## ⚙️ Como rodar o projeto localmente

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

### 1. Clone o repositório
```bash
git clone [https://github.com/SEU_USUARIO/controle-industrial-django.git](https://github.com/SEU_USUARIO/controle-industrial-django.git)
cd controle-industrial-django

2. Crie e ative o ambiente virtual
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências
Bash

pip install -r requirements.txt
4. Configure o Banco de Dados
Bash

python manage.py migrate
5. Crie um Superusuário (Admin)
Bash

python manage.py createsuperuser
6. Inicie o Servidor
Bash

python manage.py runserver
O sistema estará acessível em: http://127.0.0.1:8000/

