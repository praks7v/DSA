class BinarySearchTree:
    def __init__(self, data):
        """
        Initializes a Binary Search Tree with a given root data.

        Parameters:
        - data: The data for the root of the tree.
        """
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the Binary Search Tree.

        Parameters:
        - data: The data to be inserted into the tree.
        """
        if self.data is None:
            self.data = data
            return
        elif self.data == data:
            return
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        """
        Searches for a value in the Binary Search Tree.

        Parameters:
        - val: The value to be searched in the tree.
        Returns:
        - The value if found, otherwise prints a message indicating it was not found.
        """
        if not self.data:
            print(f"Binary search tree is empty. Cannot search {val}")
            return
        if self.data == val:
            print(f"Value {self.data}. Found in the Binary Search Tree.")
            return self.data

        else:
            if val < self.data:
                if self.left:
                    self.left.search(val)
                else:
                    print(f"Value {val}. Not found in Binary Search Tree.")
            else:
                if self.right:
                    self.right.search(val)
                else:
                    print(f"Value {val}. Not found in Binary Search Tree.")

    def find_min_val(self):
        """
        Finds the minimum value in the Binary Search Tree.

        Returns:
        - The minimum value.
        """
        if not self.data:
            print("Binary Search Tree is empty.")
            return
        if self.left is None:
            return self.data
        return self.left.find_min_val()

    def find_max_val(self):
        """
        Finds the maximum value in the Binary Search Tree.

        Returns:
        - The maximum value.
        """
        if not self.data:
            print("Binary Search Tree is empty.")
            return
        if self.right is None:
            return self.data
        return self.right.find_max_val()

    def delete(self, val):
        """
        Deletes a node with the given value from the Binary Search Tree.

        Parameters:
        - val: The value to be deleted from the tree.
        Returns:
        - The updated tree after deletion.
        """
        if not self.data:
            print(f"Binary Search Tree is empty. Cannot delete {val}")
            return

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                print(f"Value {val} not found in the tree. Cannot delete {val}.")

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                print(f"Value {val} not found in the tree. Cannot delete {val}.")

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max_val()
            self.data = max_val
            self.left = self.left.delete(max_val)

            # min_val = self.right.find_min_val()
            # self.data = min_val
            #
            # self.right = self.right.delete(min_val)

        return self

    def pre_order_traversal(self):
        """
        Performs a pre-order traversal of the Binary Search Tree.
        Prints the nodes in the order: Root, Left, Right.
        """
        if self.data is None:
            print("Binary search tree is empty!")
            return
        print(self.data, end=" ")

        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        """
        Performs an in-order traversal of the Binary Search Tree.
        Prints the nodes in the order: Left, Root, Right.
        """
        if self.data is None:
            print("Binary search tree is empty!")
            return
        if self.left:
            self.left.in_order_traversal()

        print(self.data, end=" ")

        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        """
        Performs a post-order traversal of the Binary Search Tree.
        Prints the nodes in the order: Left, Right, Root.
        """
        if self.data is None:
            print("Binary search tree is empty!")
            return
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()

        print(self.data, end=" ")


# Insertion Operation done
# Search Operation done
# Deletion Operation done

# Traversal Operation done
# In-Order Traversal
# Pre-Order Traversal
# Post-Order Traversal

if __name__ == "__main__":
    # Sample Usage
    bst = BinarySearchTree(40)
    bst.insert(30)
    bst.insert(20)
    bst.insert(10)
    bst.insert(70)
    bst.insert(50)
    bst.insert(60)
    bst.insert(80)

    print("Search operation: ", end=" ")
    bst.search(60)
    print("\nBefore deletion In-order traversal:", end=" ")
    bst.in_order_traversal()
    print()
    bst.delete(10)
    print("\nAfter deletion traversal:", end=" ")

    print("\nIn-order traversal:", end=" ")
    bst.in_order_traversal()
    print("\nPre-order traversal:", end=" ")
    bst.pre_order_traversal()
    print("\nPost-order traversal:", end=" ")
    bst.post_order_traversal()
