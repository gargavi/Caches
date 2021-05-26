from math import log
import random
import time

class Cache: 
    
    def __init__(self,data,capacity = 1024, block_size = 4, associativity = 1, penalty = 2):
        
        assert int(log(block_size, 2)) == log(block_size, 2)
        assert int(log(len(data), 2)) == log(len(data), 2)
        assert int(log(associativity, 2)) == log(associativity, 2)
        
        self.capacity = capacity 
        self.line_number = None # Fix None - doesn't require adding parameter 
        self.block_size = block_size
        self.associativity = associativity
        self.penalty = penalty
        self.memory = data
        self.offset_size = None # FIX 
        self.index_size = None # FIX 
        self.tag_size =  None # FIX  
        self.cache = {}
        for i in range(100): # FIX 100 to correct value  
            tag_dict = {}
            self.cache[i] = tag_dict
            
    def access(self, memory_index):
        offset_value = memory_index & (2**self.offset_size - 1)  
        index_value = None # FIX ME 
        tag_value = None 
        #print(bin(tag_value), bin(index_value), bin(offset_value))
        
        indexed_data = self.cache[index_value]
        if tag_value in indexed_data.keys():
            return indexed_data[None][None] # FIX ME 
        else:
            time.sleep(self.penalty)
            memory_access_val = None #FIX ME 
            memory_block = self.memory[memory_access_val: memory_access_val + self.block_size] 
            if len(self.cache[index_value].keys()) == self.associativity:
                random_key = random.choice(list(self.cache[index_value].keys()))
                del(self.cache[index_value][random_key])
            self.cache[index_value][tag_value] = None # FIX ME 
            return memory_block[None] # FIX ME 
