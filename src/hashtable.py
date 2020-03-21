# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)    

        if self.storage[index]:
            cur_node = self.storage[index]
            found = False
            while cur_node is not None and found is False:
                if cur_node.key == key:
                    cur_node.value = value
                    found = True
                else:
                    cur_node = cur_node.next
            if found == False:
                cur_node = self.storage[index]
                new_node = LinkedPair(key, value)
                new_node.next = cur_node
                self.storage[index] = new_node
        else:
            self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index]:
            prev_node = None
            cur_node = self.storage[index]
            found = False
            while cur_node is not None and found is False:
                if prev_node is None and cur_node.next is None:
                    if cur_node.key == key:
                        self.storage[index] = None
                        found = True
                    else:
                        prev_node = cur_node
                        cur_node = cur_node.next
                else:
                    if cur_node.key == key:
                        if prev_node is None:
                            prev_node = cur_node
                            cur_node = cur_node.next
                            prev_node.next = None
                            self.storage[index] = cur_node
                        elif cur_node.next is None:
                            prev_node.next = None
                        else:
                            prev_node.next = cur_node.next
                            cur_node.next = None
                        found = True
                    else:
                        prev_node = cur_node
                        cur_node = cur_node.next
            if found == False:
                print("Warning: key does not exist.")
        else:
            print("Warning: key does not exist.")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index]:
            cur_node = self.storage[index]
            while cur_node is not None:
                if cur_node.key == key:
                    return cur_node.value
                else:
                    cur_node = cur_node.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = 2 * self.capacity
        self.storage = [None] * self.capacity

        current_pair = None

        for bucket_item in old_storage:
            current_pair = bucket_item
            while current_pair is not None:
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next


        # storage_copy = self.storage
        # current = None
        # self.capacity = self.capacity * 2
        # self.storage = [None] * self.capacity

        # for i in range(0, len(storage_copy)):
        #     current = storage_copy[i]
        #     while current is not None:
        #         self.insert(current.key, current.value)
        #         current = current.next
            

        # new_arr = [None] * self.capacity
        
        # for i in range(0, len(self.storage)):
        #     new_arr[i] = self.storage[i]
        #     print(self.storage[i])

        # self.capacity = self.capacity * 2

        # self.storage = [None] * self.capacity
        # for i in range(0, len(new_arr)):
        #     self.storage[i] = new_arr[i]



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
