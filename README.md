
# 🐳 ORCA — Orçamento com IA

ORCA é uma aplicação inteligente para automação de orçamentos utilizando machine learning. Ela integra workflows de MLOps com rastreamento de experimentos via MLflow e deploy utilizando AWS e GitHub Actions.

---

## 📁 Estrutura de Workflows

Para fazer alterações no pipeline:

1. Atualize `config.yaml`
2. Atualize `schema.yaml`
3. Atualize `params.yaml`
4. Atualize a entidade no diretório `entity/`
5. Atualize o configuration manager em `src/config/`
6. Atualize os componentes
7. Atualize o pipeline
8. Atualize `main.py`
9. Atualize `app.py` (interface/execução)

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/ArthurMaciell/ORCA.git
cd ORCA
```

### 2. Crie e ative o ambiente Conda

```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

Acesse no seu navegador:

```
http://localhost:8501
```

---

## 📊 MLflow Tracking

### Interface local

Execute o comando abaixo para abrir o MLflow UI localmente:

```bash
mlflow ui
```

Acesse: http://localhost:5000

### Tracking remoto com DagsHub

Você pode rastrear os experimentos remotamente no [DagsHub](https://dagshub.com/).

#### Inicialização via script:

```python
import dagshub
dagshub.init(repo_owner='ArthurMaciell', repo_name='ORCA', mlflow=True)

import mlflow
with mlflow.start_run():
	mlflow.log_param('parameter_name', 'value')
	mlflow.log_metric('metric_name', 1)
```

#### Configurar variáveis de ambiente:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/ArthurMaciell/ORCA.mlflow
export MLFLOW_TRACKING_USERNAME=ArthurMaciell
export MLFLOW_TRACKING_PASSWORD=SEU_TOKEN_AQUI
```

---

## 🚀 Deploy com AWS + GitHub Actions

### 1. Acesse o console da AWS

### 2. Crie um usuário IAM com permissões:

- `AmazonEC2FullAccess`
- `AmazonEC2ContainerRegistryFullAccess`

### 3. Crie um repositório no ECR

Anote a URI, ex.:

```
897722662134.dkr.ecr.us-east-1.amazonaws.com/orca
```

### 4. Crie uma instância EC2 (Ubuntu)

### 5. Instale o Docker na instância:

```bash
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### 6. Configure EC2 como runner do GitHub:

No GitHub: `Settings > Actions > Runners > New self-hosted runner`  
Siga as instruções para configurar.

### 7. Configure os segredos no GitHub (`Settings > Secrets > Actions`)

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (ex: `us-east-1`)
- `AWS_ECR_LOGIN_URI`
- `ECR_REPOSITORY_NAME`

---

## 📚 Sobre o MLflow

MLflow é uma ferramenta de rastreamento de experimentos de Machine Learning que permite:

- Armazenar métricas e parâmetros
- Versionar modelos
- Reproduzir experimentos
- Fazer deploy de modelos de forma integrada

Documentação oficial: [https://mlflow.org](https://mlflow.org)

---

## 📌 Status do Projeto

✔️ Estrutura de MLOps funcional  
✔️ Treinamento e tracking com MLflow  
✔️ Interface com `app.py` para uso interno  
🚧 Automatização de deploy em andamento

---

## 👨‍💻 Autor

**Arthur Maciel**  
[GitHub](https://github.com/ArthurMaciell) • [LinkedIn](https://www.linkedin.com/in/arthur-maciel6325)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
