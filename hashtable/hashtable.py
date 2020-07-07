from typing import Generic, TypeVar

T = TypeVar('T')


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key: str, value: T) -> None:
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable(Generic[T]):
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = max(MIN_CAPACITY, capacity)
        self.storage = [None] * self.capacity

    def get_num_slots(self) -> int:
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key: str) -> int:
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    @staticmethod
    def djb2(key: str) -> int:
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        hash_ = 5381
        for x in key:
            hash_ = ((hash_ << 5) + hash_) + ord(x)
        return hash_ & 0xFFFFFFFF

    def hash_index(self, key: str) -> int:
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key: str, value: T) -> None:
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        self.storage[self.hash_index(key)] = value

    def delete(self, key: str) -> T:
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        value = self.storage[index]
        del self.storage[index]
        return value

    def get(self, key: str) -> T:
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        return self.storage[self.hash_index(key)]

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


def main() -> None:
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


if __name__ == "__main__":
    main()
