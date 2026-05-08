import datetime
import json
from blockchain.block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.load_chain()

    def create_genesis_block(self):
        return Block(0, "0", datetime.datetime.now(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, document_hash):
        if len(self.chain) == 0:
            self.chain.append(self.create_genesis_block())

        prev_block = self.get_latest_block()

        new_block = Block(
            len(self.chain),
            prev_block.hash,
            datetime.datetime.now(),
            document_hash
        )

        self.chain.append(new_block)
        self.save_chain()

    def display_chain(self):
        for block in self.chain:
            print("\n--- Block ---")
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Document Hash:", block.document_hash)
            print("Hash:", block.hash)

    # ✅ SAVE BLOCKCHAIN
    def save_chain(self, filename="blockchain.json"):
        data = []
        for block in self.chain:
            data.append({
                "index": block.index,
                "previous_hash": block.previous_hash,
                "timestamp": str(block.timestamp),
                "document_hash": block.document_hash,
                "hash": block.hash
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    # ✅ LOAD BLOCKCHAIN
    def load_chain(self, filename="blockchain.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            self.chain = []
            for item in data:
                block = Block(
                    item["index"],
                    item["previous_hash"],
                    item["timestamp"],
                    item["document_hash"]
                )
                block.hash = item["hash"]
                self.chain.append(block)

        except FileNotFoundError:
            self.chain = [self.create_genesis_block()]

    # ✅ VALIDATE BLOCKCHAIN
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True