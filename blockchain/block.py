import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, document_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.document_hash = document_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + self.document_hash
        return hashlib.sha256(data.encode()).hexdigest()