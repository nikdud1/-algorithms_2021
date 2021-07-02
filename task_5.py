class StackPlates:
    def __init__(self,size):
        self.elems = [[]]
        self.size = size
    def is_empty(self):
        return self.elems == []
    def push_in(self,el):
        if len(self.elems[len(self.elems)-1]) < self.size:
            self.elems[len(self.elems)-1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems)-1].append(el)
    def pop_out(self):
        if len(self.elems[len(self.elems)-1]) != 0:
            return self.elems[len(self.elems)-1].pop()
        else:
            return self.elems.pop()
    def get_val(self):
        return self.elems[len(self.elems)-1]
    def stack_size(self):
        s = 0
        for i in self.elems:
            s = s + len(i)
        return s
plates = StackPlates(4)
a = []
print(len(a))
plates.push_in("Plate1")
plates.push_in("Plate2")
plates.push_in("Plate3")
plates.push_in("Plate4")
plates.push_in("Plate5")
print(plates.get_val())
print(plates)


