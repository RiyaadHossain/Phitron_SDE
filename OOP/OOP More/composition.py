class Ram:
    def __init__(self, memory):
        self.memory = memory 

class Processor:
    def __init__(self, cores):
        self.cores = cores 

class SSD:
    def __init__(self, storage):
        self.storage = storage 

# Computer has a relation with Composite classes (Ram, Processor, SSd)
class Computer:
    def __init__(self, memory, cores, storage, brand):
        self.brand = brand
        self.memory = Ram(memory) # Composite class
        self.cores = Processor(cores)
        self.storage = SSD(storage)