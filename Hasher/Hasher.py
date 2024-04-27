class HasherLogic:
    """Module containing the logic of the hasher"""
    def __init__(self, dump_file, hash_file):
        self._dump_file = dump_file
        self._hash_file = hash_file
        self._hash_list = []

    # region Properties
    @property
    def __dump_file(self):
        return self._dump_file

    @property
    def __hash_file(self):
        return self._hash_file

    @property
    def hash_list(self):
        return self._hash_list

    # endregion
    def hash_lister(self):
        """Function that reads the lines in the dumpfile, and writes the hashes on another file"""
        with open(self.__dump_file, "r", encoding="utf-8") as dump_file:
            lines = dump_file.readlines()

            for line in lines:
                sections = line.split(" ")
                for section in sections[::2]:
                    seeds = section.split(":")
                    if len(seeds) > 1:
                        self.hash_list.append(seeds[1])

        with open(self.__hash_file, "w", encoding="utf-8") as hash_file:
            hash_file.writelines(
                "\n".join(list(filter(lambda x: x != "", self.hash_list)))
            )
