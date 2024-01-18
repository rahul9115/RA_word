class Combinations:
    def __init__(self):
        self.queue = set()
        self.final = set()

    def combinations(self, a, n, r, i):
        if len(self.queue) == r:
            self.final.add(tuple(sorted(self.queue)))
            return
        for j in range(i, len(a)):
            if a[j] not in self.queue:
                self.queue.add(a[j])
                self.combinations(a, n, r, i + 1)
                self.queue.remove(a[j])

c = Combinations()
r = 2
a = [1, 2, 3]
n = len(a) - 1
c.combinations(a, n, r, 0)
print(list(c.final))
