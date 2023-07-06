import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Node import Node
import write



def read():
    """Reads all the data from the excel sheet inputted, and stores the information 
    in lists. Returns those lists as a list of lists."""
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("LinkTree").get_worksheet(1)

    # Extract and print all of the values
    list_of_hashes = sheet.get_all_records()
    return list_of_hashes

def create_nodes(node_lst):
    """Creates a list of nodes"""
    nodes = []
    for dict in node_lst:
        g = Node()
        g.create_node(dict["Title"], dict["Description"], dict["Link"], dict["Image"], dict["Contact"])
        nodes.append(g)

    return nodes

def main():
    node_lst = read()
    nodes = create_nodes(node_lst)
    write.update(nodes)

if __name__ == "__main__":
    main()
