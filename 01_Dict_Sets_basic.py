print(" PART 1: DICTIONARIES & SETS ")

# 1. Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# They are ordered, mutable, and do not allow duplicate keys.

student = {
    "name": "Navneet",
    "age": 21,
    "subjects": ["Python", "C++", "Java"],
    "is_adult": True,
    "marks": 95.5
}

print("--- Dictionary Operations ---")
print(f"Full Dictionary: {student}")
print(f"Accessing Name: {student['name']}")

# Modifying and Adding entries
student["name"] = "Navneet Kaur"  # Updating existing key
student["city"] = "India"         # Adding new key-value pair
print(f"Updated Dictionary: {student}\n")


# 2. Sets
# Sets are a collection of unordered, unindexed, and unique elements.
# Duplicate values are automatically removed.

nums = {1, 2, 3, 4, 1, 2, 2} 
print("--- Set Operations ---")
print(f"Initial Set (Duplicates removed): {nums}")

# Adding and Removing elements
nums.add(5)
nums.remove(1)
print(f"Modified Set: {nums}")

# CRITICAL NOTE: Empty Syntax
# {} creates an empty DICTIONARY, not a set.
# Use set() to initialize an empty set.
empty_dict = {}
empty_set = set()

print(f"Type of {{}}: {type(empty_dict)}")
print(f"Type of set(): {type(empty_set)}")
