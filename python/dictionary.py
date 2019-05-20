dict = {"Name":"Manoj", "Age":45, "Class":"1st","Type":"Superb"}
print("dict[\"Name\"] = \t",dict["Name"])
print("dict[\"Age\"] = \t",dict["Age"])
print("dict[\'Class\'] = ", dict["Class"])
print("dict[\"Type\"] = \t", dict["Type"] )    

dict["Name"] = "Vikas"
dict["Age"] = 25
dict.update({"Category":"Great"})

del dict["Class"]
print()
for kv in dict: # or dict.keys()
    print(f"Key: {kv} \tValue: {dict[kv]}")
 
print("Using Get: ", dict.get("Name"))
# has_key Not working
#print("Has Key: ", dict.has_key("Name"))

print("\n#dict.items()")
for nvp in dict.items():
    print(nvp)

print("\n#dict.values()")
for cV in dict.values():
    print(cV)    
 