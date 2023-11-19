# PATH_TO_DUMP = "c:\Users\aless\OneDrive\Documenti\Università\Lezioni\Sicurezza\sec-repo\progettino1\"
def getHashes(dump_file, hash_file):
    hash_list = []
    with open(dump_file, 'r') as dump_file:
        lines = dump_file.readlines()
        
        for line in lines:
            sections = line.split(" ")
            for section in sections[::2]:
                seeds = section.split(":")
                if len(seeds) > 1: 
                        hash_list.append(seeds[1])

    with open(hash_file, 'w') as hash_file:
        hash_file.writelines('\n'.join(hash_list))