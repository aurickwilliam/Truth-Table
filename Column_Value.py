class List:
    value = None
    var_col = []

    def append_value(self):
        self.var_col.append(self.value)

    def display_value(self):
        for x in range(len(self.var_col)):
            print(x)
