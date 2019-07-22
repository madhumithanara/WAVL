import time
import random
from wavl import WAVL
from bst import BST
from avl import AVL_Tree
from rb_tree import RedBlackTree

wavl_tree=WAVL()
avl_tree=AVL_Tree()
bst=BST()
rbt=RedBlackTree()
root=None


def insert(n):
    list=random.sample(range(1,n+1),n)
    start=time.time()
    for i in list:
        avl_tree.insert(root,i)
    print("Total Time for AVL is :",time.time()-start)

    start=time.time()
    for i in list:
        wavl_tree.insert(i)
    # wavl_tree.inorder()
    print("Total Time for WAVL is :",time.time()-start)
    

    start=time.time()
    for i in list:
        rbt.add(i)
    print("Total Time for RBT is :",time.time()-start)

def remove(n):
    start=time.time()
    for i in range(n,1,-1):
        avl_tree.delete(root,i)
    print("Total Time for AVL is :",time.time()-start)
    
    start=time.time()
    for i in range(n,1,-1):
        wavl_tree.remove(i)
    print("Total Time for WAVL is :",time.time()-start)
    

    start=time.time()
    for i in range(n,1,-1):
        rbt.remove(i)
    print("Total Time for RBT is :",time.time()-start)

def search(n):
    start=time.time()
    for i in range(n,1,-1):
        avl_tree.search(root,i)
    print("Total Time for AVL is :",time.time()-start)
    
    start=time.time()
    for i in range(n,1,-1):
        wavl_tree.search(i)
    print("Total Time for WAVL is :",time.time()-start)
    

    start=time.time()
    for i in range(n,1,-1):
        rbt.search(i)
    print("Total Time for RBT is :",time.time()-start)

def main():
    rand_int=random.randint(10000,100000)
    insert(rand_int)
    print()
    print()
    remove(rand_int)
    print()
    print()
    search(rand_int)
if __name__=='__main__':
    main()