from city_data import CityData


class HashTable:
    def __init__(self, capacity=8, load_factor_threshold=0.75):
        self.capacity = capacity
        self.load_factor_threshold = load_factor_threshold
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _load_factor(self):
        return self.size / self.capacity

    def insert(self, city: CityData):
        if self._load_factor() >= self.load_factor_threshold:
            self._resize()

        idx = self._hash(city.name)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == city.name:
                bucket[i] = (city.name, city)
                return
        bucket.append((city.name, city))
        self.size += 1

    def search(self, name):
        idx = self._hash(name)
        for k, city in self.buckets[idx]:
            if k == name:
                return city
        return None

    def delete(self, name):
        idx = self._hash(name)
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == name:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for _, city in bucket:
                self.insert(city)

    def bucket_lengths(self):
        return [len(b) for b in self.buckets]
