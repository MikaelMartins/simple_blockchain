# ⛓️ Simple Blockchain com Flask

Este é um exemplo básico de uma **blockchain minimalista** implementada em Python com o framework **Flask**, ideal para fins educacionais.

---

## 🚀 Funcionalidades

- Criação de blocos usando SHA-256
- Registro do tempo e hash do bloco anterior
- API REST simples com dois endpoints:
  - `GET /chain`: retorna toda a cadeia de blocos
  - `POST /mine-block`: minera (cria) um novo bloco

---

## 🧰 Tecnologias Usadas

- Python 3
- Flask
- hashlib (nativo do Python)
- time (nativo do Python)

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/MikaelMartins/simple_blockchain.git
cd simple_blockchain/simple_blockchain
```
### 2. Crie um ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install flask
```

---

## ▶️ Como executar

No terminal, rode o script principal:

```bash
python simpleBlockchainFlask.py
```

O servidor Flask será iniciado em:

```cpp
http://127.0.0.1:5000/
```

---

## 📡 Endpoints

`GET /chain`  
Retorna toda a blockchain no formato JSON.

Exemplo de uso:

```bash
curl http://127.0.0.1:5000/chain
```

`POST /mine-block`  
Cria um novo bloco e adiciona à blockchain.

Exemplo de uso:

```bash
curl -X POST http://127.0.0.1:5000/mine-block
```

---

## ⚠️ Aviso
Este projeto é apenas uma simulação educacional de uma blockchain. Ele não deve ser usado em produção nem para aplicações reais com segurança e integridade de dados críticas.

---

## 👨‍💻 Autor
Mikael Martins  
Estudante de Engenharia da Computação  
GitHub: [@MikaelMartins](https://github.com/MikaelMartins)
