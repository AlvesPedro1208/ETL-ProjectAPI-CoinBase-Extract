# Projeto ETL Coinbase

## 📝 Descrição
Este projeto implementa um pipeline ETL (Extract, Transform, Load) que extrai dados de criptomoedas através da API pública da Coinbase, transforma os dados em um formato estruturado e os carrega em um banco de dados PostgreSQL para análise posterior.

## 🚀 Funcionalidades
- Extração de dados em tempo real da API da Coinbase utilizando Kafka acoplado em um Docker
- Coleta de informações sobre preços de criptomoedas
- Transformação, processamento e limpeza dos dados utilizando Spark
- Armazenamento em banco de dados PostgreSQL
- Geração de relatórios analíticos utilizando Streamlit

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.9+
- **APIs**: Requests
- **Mensageria**: Kafka
- **Processamento**: Apache Spark
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker
- **Visualização**: Streamlit

## 📋 Pré-requisitos
Antes de iniciar o projeto, certifique-se de ter instalado os seguintes requisitos:
- Python 3.9 ou superior
- Docker e Docker Compose
- Apache Kafka
- PostgreSQL
- Chave de API da Coinbase (opcional para endpoints autenticados)

## ⚙️ Configuração e Instalação
### 1. Clonar o Repositório
```bash
 git clone https://github.com/seu-usuario/projeto-etl-coinbase.git
 cd projeto-etl-coinbase
```
### 2. Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```
### 4.4. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e defina as credenciais:
```bash
COINBASE_API_KEY=your_api_key_here
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```
### 5. Subir os Containers Docker (Kafka e PostgreSQL)
```bash
docker-compose up -d
```
### 6. Executar o Pipeline ETL
```bash
python main.py
```
## 📊 Análise dos Dados
Para visualizar os dados e gerar relatórios, execute a aplicação Streamlit:
```bash
streamlit run dashboard.py
```
## 📂 Estrutura do Projeto
```bash
projeto-etl-coinbase/
├── data/                # Dados brutos e processados
├── src/
│   ├── extract.py       # Extração dos dados da API da Coinbase
│   ├── transform.py     # Limpeza e processamento dos dados
│   ├── load.py          # Carregamento dos dados para PostgreSQL
│   ├── config.py        # Configuração do projeto
│   ├── dashboard.py     # Visualização dos dados com Streamlit
│   ├── main.py          # Script principal do pipeline ETL
├── requirements.txt     # Dependências do projeto
├── docker-compose.yml   # Configuração dos containers Docker
├── .env                 # Variáveis de ambiente
└── README.md            # Documentação do projeto
```
## 🤝 Contribuição
Contribuições são bem-vindas! Siga estas etapas para contribuir:

1. Faça um fork do repositório
2. Crie um branch com sua feature (git checkout -b minha-feature)
3. Faça commit das mudanças (git commit -m 'Adiciona nova funcionalidade')
4. Envie para o branch principal (git push origin minha-feature)
5. Abra um Pull Request

### 📜 Licença
Este projeto está licenciado sob a MIT License.






