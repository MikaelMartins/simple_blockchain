from flask import Flask, jsonify
import hashlib
import time


# Blockchain
blockchain = []

# Instancia Flask
app = Flask(__name__)

def create_block(previous_hash):
    block = {
        "index": len(blockchain),
        "timestamp": time.time(),
        "hash": '',
        "previous_hash": previous_hash
    }

    block['hash'] = hashlib.sha256(str(block).encode()).hexdigest()
    blockchain.append(block)

    return block


# Bloco Gênesis
create_block('0')


@app.route('/chain', methods=['GET'])
def get_blockchain():
    return jsonify(blockchain), 200

@app.route('/mine-block', methods=['POST'])
def mine_block():
    return create_block(blockchain[-1]['hash']), 201


if __name__ == "__main__":
    app.run(debug=True)