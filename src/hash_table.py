# !/usr/bin/env python3
# encoding: utf-8

"""
    @author: Mohammed Ataaur Rahaman
"""


__author__ = 'Mohammed Ataaur Rahaman'


class HashTable:
    """
    Simple hash Table with hash function as a mod function.
    """

    def __init__(self, buckets):
        self.buckets = buckets
        self.hash_table = [None] * self.buckets

    def mod_func(self, key):
        return key % self.buckets

    def insert(self, key, value):
        idx = self.mod_func(key)
        if self.hash_table[idx] is not None:
            print(f"Collision occured while inserting {(key, value)}")

        self.hash_table[idx] = (key, value)
        print(f"Inserted Data: {(key, value)}")

    def print(self):
        print(f"#" * 20)
        for idx, data in enumerate(self.hash_table):
            print(f"  [{idx}] --> {data}")
        print(f"#" * 20)

class HashTableChain(HashTable):
    """
    Hash Table with Chaining.
    """

    def __init__(self, buckets):
        super().__init__(buckets)

    def insert(self, key, value):
        idx = self.mod_func(key)
        if self.hash_table[idx] is not None:
            self.hash_table[idx].append((key, value))
        else:
            self.hash_table[idx] = [(key, value)]
        print(f"Inserted Data: {(key, value)}")

class HashTableLinearProbe(HashTable):
    """
    Hash Table with linear probing.
    """
    def __init__(self, buckets):
        super().__init__(buckets)

    def insert(self, key, value):
        idx = self.mod_func(key)
        count = 0
        while self.hash_table[idx] is not None:
            idx = (idx + 1) % self.buckets
            count += 1
            if count >= self.buckets:
                print(f"Hash table Full, Counldn't insert: {(key, value)}")
                return

        self.hash_table[idx] = (key, value)
        print(f"Inserted Data with chain: {(key, value)} at {idx}")

if __name__ == '__main__':
    buckets = 10

    ht = HashTableLinearProbe(buckets)
    ht.print()

    ht.insert(13, 'Thirteen')
    ht.insert(15, 'Fifteen')
    ht.insert(33, 'Thirty Three')
    ht.insert(38, 'Thirty Eight')
    ht.insert(28, 'Twenty Eight')
    ht.insert(7, 'Seven')
    ht.insert(78, 'Seventy Eight')
    ht.insert(58, 'Fifty Eight')
    ht.insert(8, 'Eight')
    ht.insert(8, 'Eight')
    ht.insert(8, 'Eight')
    ht.print()