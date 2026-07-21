from city_data import CityData


class AVLNode:
    def __init__(self, city: CityData):
        self.city = city
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, city: CityData):
        self.root = self._insert(self.root, city)
        self.size += 1

    def _insert(self, node, city):
        if node is None:
            return AVLNode(city)
        if city.name < node.city.name:
            node.left = self._insert(node.left, city)
        elif city.name > node.city.name:
            node.right = self._insert(node.right, city)
        else:
            node.city = city
            self.size -= 1
            return node
        return self._rebalance(node)

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None:
            return None
        if name == node.city.name:
            return node.city
        elif name < node.city.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def delete(self, name):
        self.root, deleted = self._delete(self.root, name)
        if deleted:
            self.size -= 1
        return deleted

    def _delete(self, node, name):
        if node is None:
            return node, False

        if name < node.city.name:
            node.left, deleted = self._delete(node.left, name)
        elif name > node.city.name:
            node.right, deleted = self._delete(node.right, name)
        else:
            deleted = True
            if node.left is None and node.right is None:
                return None, deleted
            if node.left is None:
                return node.right, deleted
            if node.right is None:
                return node.left, deleted
            successor = self._min_node(node.right)
            node.city = successor.city
            node.right, _ = self._delete(node.right, successor.city.name)

        return self._rebalance(node), deleted

    def _min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.city)
            self._inorder(node.right, result)

    def height(self):
        return self._height(self.root) - 1 if self.root else -1
