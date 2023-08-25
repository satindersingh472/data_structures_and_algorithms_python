class Node:
    # node class with a data or value and link to the next node
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node
    
    # get the value of the node
    def get_value(self):
        return self.value
    # get the next node
    def get_next_node(self):
        return self.next_node
    # set the link to the next node
    def set_next_node(self,next_node):
        self.next_node = next_node

# linked list class
class LinkedList:
    # constructor
    def __init__(self,value=None):
        # head node equal to new Node with  value set to its value
        self.head_node = Node(value)

    # get the head node
    def get_head_node(self):
        return self.head_node
    
    # insert a new node at the beginning
    def insert_beginning(self,new_value):
        # create a new node with new_value
        new_node = Node(new_value)
        # point the new node to the head node
        new_node.set_next_node(self.head_node)
        # update the head node
        self.head_node = new_node

    # this method will return the values of node in a string form
    def stringify_list(self):
        # empty variable to store strings
        string_list = ''
        # will get the current head node
        current_node = self.get_head_node()
        #loop while the current node is there 
        while current_node:
            # until current node is not none
            if current_node.get_value() != None:
                # string_list variable will store the value of a current node and prints a new line
                string_list += str(current_node.get_value()) + "\n"
            # inside the while loop set the current node to the next node to continue the loop until it is not none
            current_node = current_node.get_next_node()
        # after finish it will return the string_list variable to show the stringified values
        return string_list
    
    # remove node method will remove the nodes that matches the value_to_remove
    def remove_node(self,value_to_remove):
        # set the current node equals to the head node so that loop will start from the head node to check if value matches
        current_node = self.get_head_node()
        # if value matches then set the new head node to the next node of a current node which means create the link to another node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        # else when loop does not find the very first node equal to the value_to_remove then it will check other nodes for the value
        else:
            # while the current node is there with some value it will loop or traverse through the linked list
            # because it already went and check the very first node there is no point to check that again
            # so we will start from the second next node
            while current_node:
                # the next node will be next from current node and also it will be node that the while loop will check for
                # next node will always be the next of current so if value does not matches we will use current node to 
                # store the next node value in the else clause
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    # if value of next node matches then we will set the link between current node and next node of the next node
                    # so a -> b -> c (where a is the current node, b is the next node and c is the next node of the next node)
                    # now a -> c will be the remaining linked list
                    current_node.set_next_node(next_node.get_next_node())
                    # after the value matches the current node will be none and it will stop looping
                    # otherwise it will unnecessary check the linked list for value
                    current_node = None
                # if value does not matches then will set the current node to the next node 
                # so that it will use the next node as current and the next node will next of previous next node
                # a -> b -> c -> d ( a is current node, b is next , c is next of next)
                # if a and b does not matches, then b will be current , c is next and d will be next of next
                else:
                    current_node = next_node
    