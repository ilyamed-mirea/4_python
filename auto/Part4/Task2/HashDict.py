class HashDict:
    def __init__(self, size=10):
        self.size = size
        self.threshold = int(self.size * 0.75)
        self.table = [None] * self.size
        self.count = 0

    def __getitem__(self, key):
        index = hash(key) % self.size
        if self.table[index] is None:
            raise KeyError(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1
        if self.count > self.threshold:
            self._resize()

    def __delitem__(self, key):
        index = hash(key) % self.size
        if self.table[index] is None:
            raise KeyError(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return
        raise KeyError(key)

    def __contains__(self, key):
        index = hash(key) % self.size
        if self.table[index] is None:
            return False
        for k, _ in self.table[index]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self.count

    def _resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        for i in range(self.size):
            if self.table[i] is None:
                continue
            for key, value in self.table[i]:
                index = hash(key) % new_size
                if new_table[index] is None:
                    new_table[index] = []
                new_table[index].append((key, value))
        self.size = new_size
        self.threshold = int(self.size * 0.75)
        self.table = new_table

    def __iter__(self):
        for index in range(self.size):
            if self.table[index] is not None:
                for k, _ in self.table[index]:
                    yield k

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for key in self:
            if key not in other or self[key] != other[key]:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def keys(self):
        return iter(self)

    def values(self):
        for index in range(self.size):
            if self.table[index] is not None:
                for _, v in self.table[index]:
                    yield v

    def items(self):
        for index in range(self.size):
            if self.table[index] is not None:
                for k, v in self.table[index]:
                    yield k, v

    def clear(self):
        self.table = [None] * self.size
        self.count = 0
