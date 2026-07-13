# Sets are unordered, unindexed, and contain ONLY unique items.

# 1. Dynamic Set Creation via User Input
user_input = input("Enter words separated by space to create a unique set: ")
word_list = user_input.split()
unique_words = set(word_list) 

print("Unique words extracted:", unique_words)

# 2. Mathematical Operations (Crucial for AI feature comparison)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union (All unique):", set1.union(set2))
print("Intersection (Common elements):", set1.intersection(set2))
print("Difference (Elements in set1 not in set2):", set1.difference(set2))

# 3. Memory Performance
# Sets use Hashing, making lookups O(1) time complexity.
# This makes them extremely fast for filtering large datasets in AI pipelines.