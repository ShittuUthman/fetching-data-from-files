class OpenFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('topCPU.txt.py', 'r') as f:
    a = f.readlines()
    percent_arr = []
    datetime_arr = []

    for lines in a:
        if lines.startswith('%Cpu(s)'):
            b = lines.split(' ')
            # print(b[2])
            try:
                percent = float(b[2]) * 100
                percent_arr.append(round(percent))
            except ValueError:
                pass

        elif len(lines) > 20:
            c = lines
            print('the date is ' + c)
            datetime_arr.append(c.strip())
    print(list(zip(percent_arr, datetime_arr)))








