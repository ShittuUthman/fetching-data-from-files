name_of_file = input('Enter file name: ')
characteristic = input('What figures are you after? (total_memory, used_memory, free_memory, cache_memory) ')


class OpenFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile(name_of_file, 'r') as f:
    a = f.readlines()
    total_mem = []
    used_mem = []
    free_mem = []
    cache_mem = []

    if characteristic == 'total_memory':
        for lines in a:
            if lines.endswith('cache', 0, -1):
                b = lines.split(' ')
                try:
                    total_mem.append(float(b[3]))
                except ValueError:
                    pass
        print(total_mem)
    elif characteristic == 'used_memory':
        for lines in a:
            if lines.endswith('cache', 0, -1):
                b = lines.split(' ')
                try:
                    used_mem.append(float(b[12]))
                except ValueError:
                    pass
        print(used_mem)
    elif characteristic == 'free_memory':
        for lines in a:
            if lines.endswith('cache', 0, -1):
                b = lines.split(' ')
                try:
                    free_mem.append(float(b[7]))
                except ValueError:
                    pass
        print(free_mem)
    elif characteristic == 'cache_memory':
        for lines in a:
            if lines.endswith('cache', 0, -1):
                b = lines.split(' ')
                try:
                    cache_mem.append(float(b[-2]))
                except ValueError:
                    pass
        print(cache_mem)
    else:
        print("Invalid input. Only these inputs (total_memory, used_memory, free_memory, cache_memory) are acceptable.")
