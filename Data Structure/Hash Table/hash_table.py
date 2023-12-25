class HashTable:
    def __init__(self, size):
        # Initialize the HashTable with a given size
        self.size = size
        # Create an array (table) of empty lists to store key-value pairs
        self.table = [[] for _ in range(self.size)]
        # simple way using None value initialize
        # self.table = [None]* size

    def _hash_function(self, key):
        # A simple hash function to determine the index for a given key
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash_function(key)
        # Check if the bucket is empty
        if not self.table[index]:
            self.table[index] = [(key, value)]
        else:
            # Handle collision using separate chaining
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    # If key already exists, update the value and return
                    self.table[index][i] = (key, value)
                    return
            # If key doesn't exist, append a new key-value pair
            self.table[index].append((key, value))

    def get(self, key, default=None):
        # Retrieve the value for a given key from the hash table
        index = self._hash_function(key)
        if self.table[index]:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        # Return the default value if the key is not found
        return default

    def remove(self, key):
        # Remove a key-value pair from the hash table
        index = self._hash_function(key)
        if self.table[index]:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    del self.table[index][i]
                    return
        # Raise an error if the key is not found
        raise KeyError(f"Key '{key}' not found.")

    def keys(self):
        # Get a list of all keys in the hash table
        all_keys = []
        for bucket in self.table:
            if bucket:
                all_keys.extend(key for key, _ in bucket)
        return all_keys

    def values(self):
        # Get a list of all values in the hash table
        all_values = []
        for bucket in self.table:
            if bucket:
                all_values.extend(value for _, value in bucket)
        return all_values

    def items(self):
        # Get a list of all key-value pairs in the hash table
        all_items = []
        for bucket in self.table:
            if bucket:
                all_items.extend(bucket)
        return all_items


if __name__ == "__main__":
    # Example Usage
    hash_table = HashTable(size=5)

    # Inserting key-value pairs
    hash_table.insert('march 1', '23')
    hash_table.insert('march 2', '45')
    hash_table.insert('march 3', '21')
    hash_table.insert('march 4', '13')
    hash_table.insert('march 5', '25')
    hash_table.insert('march 1', '22')
    hash_table.insert('march 6', '32')

    # Retrieving values
    print("Value for 'march 2':", hash_table.get("march 2", default="Not found"))

    # Removing a key
    hash_table.remove('march 4')

    # Displaying keys, values, and items
    print("Keys:", hash_table.keys())
    print("Values:", hash_table.values())
    print("Items:", hash_table.items())
