import pickle

# Create a list of dictionaries, where one dictionary has CompID = 1005
data = [
    {"CompID": 1001, "Name": "Company A", "Revenue": 500000},
    {"CompID": 1002, "Name": "Company B", "Revenue": 750000},
    {"CompID": 1003, "Name": "Company C", "Revenue": 900000},
    {"CompID": 1004, "Name": "Company D", "Revenue": 600000},
    {"CompID": 1005, "Name": "Company E", "Revenue": 1200000},  # This dictionary has CompID = 1005
    {"CompID": 1006, "Name": "Company F", "Revenue": 800000},
]

# Write the list of dictionaries to a binary file
with open("companies.dat", "wb") as file:
    pickle.dump(data, file)

print("Binary file 'companies.dat' created successfully.")