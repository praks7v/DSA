class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
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

    def in_order_traversal(self):
        if self.data is None:
            print("Binary search tree is empty!")
            return
        if self.left:
            self.left.in_order_traversal()

        print(self.data, end=" ")

        if self.right:
            self.right.in_order_traversal()

    def search(self, val):
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
        if not self.data:
            print("Binary Search Tree is empty.")
            return
        if self.left is None:
            return self.data
        return self.left.find_min_val()

    def find_max_val(self):
        if not self.data:
            print("Binary Search Tree is empty.")
            return
        if self.right:
            return self.right.find_max_val()
        else:
            print(self.data)

    def delete(self, val):
        if not self.data:
            print(f"Binary Search Tree is empty. Cannot delete {val}")
            return

        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min_val()
            self.data = min_val

            self.right = self.right.delete(min_val)

        return self


# Insertion Operation done
# Search Operation done
# Deletion Operation done

# Traversal Operation done
# In-Order Traversal
# Pre-Order Traversal
# Post-Order Traversal

if __name__ == "__main__":
    bst = BinarySearchTree(40)
    bst.insert(30)
    bst.insert(20)
    bst.insert(10)
    bst.insert(70)
    bst.insert(50)
    bst.insert(60)
    bst.insert(80)
    # bst.insert(60)
    # print("In-order traversal:", end=" ")
    # bst.in_order_traversal()
    # print("\nSearch operation: ", end="")
    # bst.search(60)
    bst.delete(80)
    # bst.min_val()
    # bst.max_val()
    bst.in_order_traversal()
