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
    
    def print_tree(self):
        if self.node_left:
            self.node_left.print_tree()

        print(self.key)

        if self.node_right:
            self.node_right.print_tree()
                 
    def __str__(self):
        return 'NodeTree(Key={key}, NodeLeft={node_left}, NodeRight={node_right})'.\
                format(key=self.key, 
                       node_left=self.node_left.key, 
                       node_right=self.node_right.key) 


if __name__ == '__main__':

    binary_tree = NodeTree()

    for i in [27, 14, 35, 31, 10, 19]:
        binary_tree.add(i)


    binary_tree.print_tree()
