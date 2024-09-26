class solution:
    def predecessor(self, root, target):
        #Write your code here..
        predecessor = None

        while root:
            if root.data < target:
                predecessor = root
                root = root.right
            else:
                root = root.left
    
        return predecessor