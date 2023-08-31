# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)