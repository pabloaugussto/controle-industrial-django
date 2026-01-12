# 🏭 Almoxarifado 2.0 - Sistema de Gestão da Qualidade & 5S

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-3.0-38bdf8)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-orange)

Um sistema web moderno e responsivo desenvolvido para **controle de qualidade industrial**, focado na metodologia **5S** (Seiri, Seiton, Seiso, Seiketsu, Shitsuke). O projeto oferece uma interface fluida para realização de auditorias em chão de fábrica e geração automática de relatórios.

---

## 📸 Screenshots

 **Dashboard Gerencial** 

  <img width="1920" height="969" alt="image" src="https://github.com/user-attachments/assets/a4302b1a-4eb0-4c92-a59a-6d2a0177ef22" />
  Auditoria <img width="1901" height="967" alt="image" src="https://github.com/user-attachments/assets/b810ae81-615a-40e5-b172-675fb4940b63" />|
 *KPIs em tempo real e gráficos de evolução.* | *Interface otimizada para tablets e celulares.* 

 **Histórico & PDF** 

 Relatórios <img width="1918" height="963" alt="image" src="https://github.com/user-attachments/assets/fa06407b-8fdd-412d-8dd5-06f4fed06f4e" />

 *Geração de relatórios oficiais e gestão de histórico.* 

---

## ✨ Funcionalidades Principais

### 📊 Painel de Controle (Dashboard)
- **KPIs em Tempo Real:** Visualização imediata da Média Semanal, Melhor Setor e Pontos de Atenção.
- **Gráficos Interativos:** Evolução diária das notas de qualidade (Chart.js).
- **Ranking:** Classificação automática dos setores baseada na pontuação.

### ✅ Auditoria 5S
- **Checklist Inteligente:** Formulário dividido pelos 5 sensos.
- **UX Otimizada:** Cabeçalhos fixos ("Sticky Headers") para facilitar a navegação em listas longas.
- **Botões Touch-Friendly:** Interface desenhada para operadores usando tablets ou celulares.
- **Evidências:** (Em breve) Suporte para upload de fotos das não-conformidades.

### 📄 Relatórios & Documentação
- **Histórico Completo:** Consulta de todas as auditorias realizadas.
- **Geração de PDF:** Exportação de relatórios oficiais prontos para impressão/arquivamento.
- **Gestão:** Possibilidade de excluir auditorias incorretas com confirmação de segurança.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python + Django (MTV Architecture).
- **Frontend:** HTML5, Tailwind CSS (via CDN para estilização rápida).
- **Visualização de Dados:** Chart.js.
- **Geração de PDF:** xhtml2pdf.
- **Ícones:** Heroicons (SVG).
- **Fonte:** Inter (Google Fonts) para alta legibilidade.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.x instalado.
- Git instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone (https://github.com/pabloaugussto/controle-industrial-django.git)
   cd controle-industrial-django

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

2. Instale as dependências:

Bash

pip install -r requirements.txt

Prepare o Banco de Dados:

Bash

python manage.py migrate | Crie um Superusuário (Admin):

Bash

python manage.py createsuperuser | Inicie o Servidor:

Bash

python manage.py runserver | Acesse: Abra o navegador em http://127.0.0.1:8000

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests. 

📝 Licença
Este projeto está sob a licença MIT.

Desenvolvido por Pablo Augusto.

