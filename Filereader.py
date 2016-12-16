class FileReader:

    def __init__(self, filename):
        self.line_list = []
        with open(filename) as self.fh:
            for line in self.fh:
                self.line_list.append(line.strip())

    def get_Line_List(self):
       return self.line_list