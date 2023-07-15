import json

# Specify the path to your credentials JSON file
credentials_file = 'C:/Users/anddh/projects/web_project/webapp/client_secret_642157501724-hamebvpcero1cug5f0gfo5h0kmmjc48i.apps.googleusercontent.com.json'

# Read the contents of the JSON file
with open(credentials_file, 'r') as file:
    credentials_data = json.load(file)

# Print the contents of the file
print(credentials_data)