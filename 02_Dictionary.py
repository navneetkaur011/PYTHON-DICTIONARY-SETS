print("---DICTIONARY---")
# Dictionaries are used to store data values in key:value pairs.
#They are unordered, mutable, & don't allow duplicate keys.

#Defining a Dictionary
Data = {
    "Name": "Navneet Kaur", #"key":value
    "Roll no.": 13250059, 
    "Course": "BCA",
    "Cgpa": 9.6,
    "Subjects": {"IT":98, "C++":97, "DSA":95},
    "is_enrolled": True,
}
#Accessing data
print(Data["Name"])
print(Data["Roll no."])
print(Data["Cgpa"])
print(Data["Subjects"])
print(Data["is_enrolled"])

#Accessing data using user input
key_to_find = input("\nEnter key to access(Name/Roll no./Course/Cgpa/Subjects/is_enrolled):")
print(Data.get(key_to_find, "Key not found\n"))

#Essential Methods for Data Processing
print("\n--- Dictionary Methods ---")
# 1. .keys() - Returns all keys
print("Keys: ", list(Data.keys()))
# 2. .values() - Returns all values
print("Values: ", list(Data.values()))
# 3. .items() - Returns all (key, val) pairs as tuples
print("Items (key-value pairs): ", list(Data.items()))
# 4. .get("key") - Returns the value for a specific key
key_input = input("Enter key to search: ")
print("Value found: ", Data.get(key_input, "Key not found"))
# 5. .update(new_dict) - Inserts specified items into the dictionary
new_info = {"skill": "Python", "experience": 1}
Data.update(new_info)
print("Updated Dictionary after .update(): ", Data)

#Nested Dictionaries
print("\n---Nested Dictinary---")
Student = {
    "Name": "Lisa",
    "Subjects": {
        "C language" : 89,
        "DSA": 79,
        "IT": 92
    }
}
print(Student["Subjects"]["DSA"])
