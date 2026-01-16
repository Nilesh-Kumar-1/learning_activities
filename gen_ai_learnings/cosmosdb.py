from azure.cosmos import CosmosClient
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to Cosmos DB
url = os.getenv("COSMOS_DB_ENDPOINT")
key = os.getenv("COSMOS_DB_KEY")
client = CosmosClient(url, credential=key)
print(url, key)

# # Get database and container
# database_name = "EmployeeDB"
# container_name = "Employee"
# database = client.get_database_client(database_name)
# container = database.get_container_client(container_name)

# # Insert 1 item
# employee = {
#     "id": "1",
#     "firstName": "John",
#     "lastName": "Doe",
#     "email": "john.doe@example.com",
#     "phoneNumber": "123-456-7890",
#     "hireDate": "2020-01-15",
#     "salary": 55000,
#     "department": "IT",
#     "isActive": True,
#     "createdAt": "2026-01-15T11:37:00Z"
# }

# container.create_item(body=employee)

# # Insert multiple items (loop)
# for i in range(2, 51):
#     container.create_item(body={
#         "id": str(i),
#         "firstName": f"First{i}",
#         "lastName": f"Last{i}",
#         "email": f"user{i}@example.com",
#         "phoneNumber": f"555-000-{i:04d}",
#         "hireDate": "2021-01-01",
#         "salary": 50000 + i * 100,
#         "department": "Finance" if i % 2 == 0 else "IT",
#         "isActive": True,
#         "createdAt": "2026-01-15T11:37:00Z"
#     })


from azure.cosmos import CosmosClient, PartitionKey
import json

# 🔹 Replace with your actual values
COSMOS_ENDPOINT = os.getenv("COSMOS_DB_ENDPOINT")  # e.g., "https://your-account.documents.azure.com:443/"
COSMOS_KEY = os.getenv("COSMOS_DB_KEY")
DATABASE_NAME = "HotelDB"
CONTAINER_NAME = "Hotels"

# Create client
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)

# Get database & container
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Your hotel document

with open("test.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for hotel in data:
    try:
        container.create_item(body=hotel)
        print(f"Inserted hotel: {hotel['id']} - {hotel['HotelName']}")
        continue
    except:
        print(f"Alreay exists hotel: {hotel['id']} - {hotel['HotelName']}")