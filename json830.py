import json
data2 = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf', 'Running', 'Football', 'Traveling'],
    'is_student': False
}

with open('data2.json', 'w') as json_file:
    json.dump(data2, json_file, indent=4)

print("Data has been written to data2.json")

with open('data2.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print("Successfully able to read data2.json")
print(loaded_data)

loaded_data['age'] = 34
loaded_data['interests'].append('History')

with open('data2.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Data has been re-written to data2.json')