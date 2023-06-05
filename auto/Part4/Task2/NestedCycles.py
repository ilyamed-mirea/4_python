from HashDict import HashDict

hash_dict = HashDict()
hash_dict["key1"] = "value1"
hash_dict["key2"] = "value2"
hash_dict["key3"] = "value3"
hash_dict["key4"] = "value4"

for k1, v1 in hash_dict.items():
    for k2, v2 in hash_dict.items():
        print(f"{k1}:{v1} - {k2}:{v2}")