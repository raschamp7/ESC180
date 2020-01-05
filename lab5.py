import time

class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
    
class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        
    
    def insert(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.insert_helper(self.root, val)
            
    
    def insert_helper(self, current_node, val):
        if val < current_node.data:
            if current_node.left == None:
                current_node.left = Node(val)
            else:
                return self.insert_helper(current_node.left,val)
        else:
            if current_node.right == None:
                current_node.right = Node(val)
            else:
                return self.insert_helper(current_node.right,val)  
                
    def search(self, val):
        t0 = time.perf_counter() 
        result = self.search_helper(self.root,val)
        tf = time.perf_counter() 
        
        if result:
            #print("Found")
            print("Elapsed time:", tf-t0, "seconds")
            return result
        else:
            #print("Not Found")
            print("Elapsed time:", tf-t0, "seconds")            
            return result   
    
    def search_helper(self, curr_node, val):
        if curr_node == None:
            return False
        elif curr_node.data == val:
            return True
        elif val < curr_node.data:
            return self.search_helper(curr_node.left,val)
        elif val > curr_node.data:
            return self.search_helper(curr_node.right,val)    

def constructBST(file_name):
    webTree = BinarySearchTree()
    myfile = open(file_name, "r")
        
    content = myfile.read()
        
    myfile.close()
        
    content.replace("\n",' ')
        
    content = content.split()
    for i in range(len(content)):
        #if "." in content[i]:
        #   content[i] = content[i][:content[i].index(".")]
        webTree.insert(content[i])
            
    return webTree
            
                 
if (__name__ == "__main__"):
    b = BinarySearchTree()
    b.insert(1)
    b.insert(1)

    
    #tree1 = constructBST("websites.txt")
    #print(tree1.search("helinjituan.com"))
        