class NodeTree:

    def __init__(self, key=None):
        self.key = key
        self.node_left = None
        self.node_right = None

    def add(self, key):
        if key is None:
            return

        if self.key:
            if key <= self.key:
                if self.node_left is None:
                    self.node_left = NodeTree(key)
                else:
                    self.node_left.add(key)
            elif key >= self.key:
                if self.node_right is None:
                    self.node_right = NodeTree(key)
                else:
                    self.node_right.add(key)
        else:
            self.key = key

    def search(self, key):
        if key < self.key:
            if self.node_left is None:
                raise ValueError
            return self.node_left.search(key)
        elif key > self.key:
            if self.node_right is None:
                raise ValueError
            return self.node_right.search(key)
        else:
            return self.key

    def delete(self, key):
        if self.key == key:
            if self.node_right and self.node_left:
                parent, next_node = self.node_right.find_min(self)

                if parent.node_left == next_node:
                    parent.node_left = next_node.node_right
                else:
                    parent.node_right = next_node.node_right

                parent.node_left = self.node_left
                parent.node_right = self.node_right

            else:
                if self.node_left:
                    return self.node_left
                else:
                    return self.node_right
        else:
            if self.key == key:
                if self.node_left:
                    self.node_left = self.node_left.delete(key)
            else:
                if self.node_right:
                    self.node_right = self.node_right.delete(key)

    def find_min(self, parent):
        if self.left:
            return self.find_min(self)
        else:
            return parent, self

    def print_tree(self):
        if self.node_left:
            self.node_left.print_tree()

        print(self.key)

        if self.node_right:
            self.node_right.print_tree()

    def __str__(self):
        return 'NodeTree(Key={key}, NodeLeft={node_left}, NodeRight={node_right})'. \
            format(key=self.key,
                   node_left=self.node_left.key,
                   node_right=self.node_right.key)


if __name__ == '__main__':

    binary_tree = NodeTree()

    for i in [27, 14, 35, 31, 10, 19]:
        binary_tree.add(i)

    binary_tree.print_tree()

    binary_tree.delete(31)

    print('''\n''')
    binary_tree.print_tree()