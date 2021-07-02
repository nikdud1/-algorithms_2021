class Queue:
    def __init__(self):
        self.elems = []
    def is_empty(self):
        return self.elems == []
    def to_queue(self, item):
        self.elems.insert(0,item)
    def from_queue(self):
        return self.elems.pop()
    def __size__(self):
        return len(self.elems)
class Tasks:
    def __init__(self):
        self.basic_queue = Queue()
        self.add_queue = Queue()
        self.done_list = []
    def solving(self):
        task = self.basic_queue.from_queue()
        self.done_list = task
    def to_revision(self):
        task = self.basic_queue.from_queue()
        self.add_queue.to_queue(task)
    def from_revision(self):
        task = self.add_queue.from_queue()
        self.basic_queue.to_queue(task)
    def current_task(self):
        return self.basic_queue[len(self.basic_queue)-1]
    def list_task(self):
        return self.basic_queue.elems
    def done_list(self):
        return self.done_list
task = Tasks()
task.basic_queue.to_queue("task 1")
print(task.list_task())
task.solving()
print(task.done_list)


