"""Lists are great, but Dictionaries are better."""
person3 = {
    # Rows (each key/value pair) are separated by a comma
    "Name": "Ford Prefect",
    "Gender": "Male",
    "Occupation": "Researcher",
    "Home Planet": "Betelguese Seven"
}
# Unlike lists, insertion order may not be maintained: they are unordered
# print(person3)
"""print(person3["Home Planet"])
print(person3['Gender'])
print(person3["Occupation"])
print(person3["Name"])

# Adding a new key/value pair
person3["Age"] = 33
print(person3)"""

# Perform a frequency count using
found = {}
found['i'] = 0
found['e'] = 0
found['o'] = 0
found['a'] = 0
found['u'] = 0
print(found)
found['e'] += 1
for k in sorted(found):
    print(f"{k} was found {found[k]} time(s)")
