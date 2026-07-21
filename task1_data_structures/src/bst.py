from city_data import CityData


class BSTNode:
    def __init__(self, city: CityData):
        self.city = city
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, city: CityData):
        self.root = self._insert(self.root, city)
        self.size += 1

    def _insert(self, node, city):
        if node is None:
            return BSTNode(city)
        if city.name < node.city.name:
            node.left = self._insert(node.left, city)
        elif city.name > node.city.name:
            node.right = self._insert(node.right, city)
        else:
            node.city = city
            self.size -= 1
        return node

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

        return node, deleted

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

    def height(self, node="root"):
        if node == "root":
            node = self.root
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
