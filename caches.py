from math import log
import random

class Cache: 
    
    def __init__(self,data,capacity = 1024, block_size = 4, associativity = 1, penalty = 2):
        self.capacity = capacity 
        self.line_number = None # Fix None - doesn't require adding parameter Answer: capacity/block_size
        self.block_size = block_size
        self.associativity = associativity
        self.penalty = penalty
        self.memory = data
        self.offset_size = None # FIX Answer: log(self.block_size, 2)
        self.index_size = None # FIX Answer: log(self.line_number/self.associativity, 2)
        self.tag_size = None # FIX  Answer: log(len(data), 2) - self.index_size - self.offset_size
        
        self.cache = {}
        for i in 100: # fix 100 to correct value  Answer: self.index_size
            tag_dict = {}
            self.cache[i] = tag_dict
            
    def access(self, memory_index):
        offset_value = memory_index & (2**self.offset_size - 1)  
        index_value = memory_index & None # FIX ME Answer: ((2**self.index_size-1) << offset_size) >> offset_size 
        tag_value = memory_index & None # FIX ME Answer: ((2**self.tag_size-1) << index_size) >> index_size
        
        if None in self.cache.keys():  # FIX Me: Answer: index_value
            time.sleep(self.penalty)
            memory_access_val = None # FIX ME: Answer: tag_value << index_size & index_value << offset_value
            memory_block = self.memory[memory_access_val: memory_access_val + self.block_size]  
            if len(self.cache[index_value].keys()) == self.associativity:
                random_key = random.choice(self.cache[index_value].keys())
                del(self.cache[index_value][random_key])
            self.cache[index_value][tag_value] = memory_block
            return memory_block[100] # FIX ME: Answer offset_value
        else:
            indexed_data = self.cache[index_value]
            if tag_value in indexed_data.keys():
                return indexed_data[tag_value][offset_value]
            else:
                time.sleep(self.penalty)
                memory_block = self.memory[100: 100 + self.block_size] # FIX ME: Answer: tag_value << index_size & index_value << offset_value
                if len(self.cache[index_value].keys()) == self.associativity:
                    random_key = random.choice(self.cache[index_value].keys())
                    del(self.cache[index_value][random_key])
                self.cache[index_value][tag_value] = memory_block
                return memory_block[100] # FIX ME: Answer offset_value
        
  