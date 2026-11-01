class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name}: {self.number}"

contact_1 = Contact("Riley", "123-456-7890")
print(contact_1)


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

node_1 = Node(contact_1.name, contact_1)
print(node_1.key)
print(node_1.value)
print(node_1.next)

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, number):
        index = self.hash_function(key)
        contact = Contact(key, number)
        
        if self.data[index] is None:
            self.data[index] = Node(key, contact)
            return

        current = self.data[index]
        
        while current:
            if current.key == key:
                current.value.number = number
                return
            if current.next is None:
                break
            current = current.next

        current.next = Node(key, contact)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for index in range(self.size):
            print(f"Index {index}:", end=" ")

            current = self.data[index]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Test your hash table implementation here.  
table = HashTable(10)
table.print_table()
#Add values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()
#Search for a value
contact = table.search("John") 
print("\nSearch result:", contact) 
#Edge Case #1: Hash Collisions
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")
table.print_table()
#Edge Case #2: Duplicate Keys
table.insert("Rebecca", "999-444-9999")   
table.print_table()
#Edge Case #3: Searching for a value not in the table
print(table.search("Chris"))


# Design Memo
# A hash table is the right structure for fast lookups because it allows the program to locate 
# information using a key instead of searching through every entry individually. This is useful for
# a contact management system because each contact can be stored using their name as the key and 
# their Contact object as the value. The HashTable class uses a custom hash_function() method to 
# convert each character in the contact's name into a numerical value using ord(), adds those values
# together, and uses modulus to determine the index where the contact should be stored. This allows
# the program to locate contacts more efficiently when searching for a specific name.
# Collisions were handled using separate chaining, which allows multiple contacts to be stored at 
# the same index through a linked list. The Node class stores the contact's name as the key, the 
# Contact object as the value, and a next pointer that references the next node in the list. The 
# insert() method uses a loop to traverse the linked list and check whether a contact with the same
# name already exists. If it does, the phone number is updated instead of creating a duplicate. 
# Otherwise, a new node is added to the end of the list.
# An engineer might choose a hash table over a list or tree when an application requires frequent 
# lookups using unique keys and does not need to maintain a specific order. Lists are useful for 
# storing ordered information, while trees can maintain an organized structure. However, hash tables
# provide faster average lookups and are useful for applications like contact directories, inventory
# systems, and user account management.
