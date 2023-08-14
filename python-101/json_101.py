import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print("dictionary object: {}".format(person_dict))

# Output: ['English', 'French']
print("dictionary languages: {}".format(person_dict['languages']))
