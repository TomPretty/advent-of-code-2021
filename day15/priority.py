import itertools
from heapq import heappop, heappush

REMOVED = "<removed-task>"  # placeholder for a removed task


class PriorityQueue:
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.counter = itertools.count()  # unique sequence count

    def add_task(self, task, priority=0):
        "Add a new task or update the priority of an existing task"
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        "Mark an existing task as REMOVED.  Raise KeyError if not found."
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task(self):
        "Remove and return the lowest priority task. Raise KeyError if empty."
        while self.pq:
            _, _, task = heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError("pop from an empty priority queue")

    def empty(self):
        return len(self.pq) == 0
