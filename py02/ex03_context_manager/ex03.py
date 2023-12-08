class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_bottom=0, skip_top=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_bottom#erreur dans le code
        self.skip_bottom = skip_top#erreur dans le code
        self.file_obj =  open(filename, 'r')
        self.data = []
        self.error = 0
        i = 0
        j = 0
        for line in self.file_obj:
            self.data.append(line.split(self.sep))
            self.data[i] = [x.strip() for x in self.data[i]]
            if j == 0:
                self.len = len(self.data[i])
                j = 1
            else:
                if len(self.data[i]) != self.len:
                    self.error = 1
                    return None
            i += 1

    def __enter__(self):
        # ... Your code here ...
        if self.error == 0:
            return self
        else:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # ... Your code here ...
        if self.file_obj:
            self.file_obj.close()
        if isinstance(exc_val, IndexError):
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Traceback: {exc_tb}")
            print(f"Exception message: {exc_val}")
            return None

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        # ... Your code here ...
        return self.data[self.skip_top:len(self.data)-self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        # ... Your code here ...
        if self.header == True:
            return self.data[0]
        else:
            return None

with CsvReader('good.csv', ',', True, 0, 0) as file:
    data = file.getdata()
    header = file.getheader()
    print(data)
    print(header)

with CsvReader('bad.csv') as file:
    if file == None:
        print("File is corrupted")