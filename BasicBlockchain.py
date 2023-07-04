import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def mine_block(self, difficulty):

        target = "0" * difficulty 
        t = time.time()
        while self.hash[:difficulty] != target:
            
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(self.nonce)
        print(time.time() - t)

    def print_block(self):
        return f'{self.timestamp} | {self.data} | {self.previous_hash} | {self.hash}'

class Blockchain():
    def __init__(self):
        self.chain = [self.generate_genesis_block()]
        self.difficulty = 5
    
    def generate_genesis_block(self):
        return Block(time.time(), "Genesis Block", 0)
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1,len(self.chain)):
            previous_block = self.chain[i-1]
            current_block = self.chain[i]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
b = Blockchain()

b.add_block(Block(time.time(), "#1", b.get_last_block().hash))
b.add_block(Block(time.time(), "#2", b.get_last_block().hash))
b.add_block(Block(time.time(), "#3", b.get_last_block().hash))

print([bl.print_block() for bl in b.chain])

