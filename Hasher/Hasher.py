class Hasher:
    def __init__(self, dump_file, hash_file):
        self._dump_file = dump_file
        self._hash_file = hash_file
        self._hash_list = []
         
    #region Properties
    @property
    def dump_file(self):
        return self._dump_file
    
    @property
    def hash_file(self):
        return self._hash_file
    
    @property
    def hash_list(self):
        return self._hash_list
    #endregion
     
    def hashLister(self):
        with open(self.dump_file, 'r') as dump_file:
            lines = dump_file.readlines()
            
            for line in lines:
                sections = line.split(" ")
                for section in sections[::2]:
                    seeds = section.split(":")
                    if len(seeds) > 1: 
                        self.hash_list.append(seeds[1])

        with open(self.hash_file, 'w') as hash_file:
            hash_file.writelines('\n'.join(list(filter(lambda x: x != '', self.hash_list))))
            