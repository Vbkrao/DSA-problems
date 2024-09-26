class solution:
    def successor(self, root, target):
        #Write your code here...
        successor=None
        while root:
            if root.data>target:
                successor=root
                root=root.left
            else:
                root=root.right
        return successor