class Node:
    """A node full of information from the excel sheet"""
    def __init__(self):
        self.title = None
        self.description = None
        self.contact = None
        self.link = None
        self.image = None
    
    def set_title(self, title):
        self.title = title
        return self
    
    def set_description(self, description):
        self.description = description
        return self
    
    def set_contact(self, contact):
        self.contact = contact
        return self

    def set_link(self, link):
        self.link = link
        return self
    
    def set_image(self, image):
        self.image = image
        return self

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    def get_contact(self):
        return self.contact

    def get_link(self):
        return self.link
    
    def get_image(self):
        return self.image

    def create_node(self, title, description, link, image, contact):
        self.set_title(title).set_description(description).set_link(link).set_image(image).set_contact(contact)
        return self
    
    def display_node(self):
        return [self.get_title(), self.get_description(), self.get_contact(), self.get_link(), self.get_image()]



