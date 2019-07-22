import queue

class TreeNode:
	"""docstring for TreeNode"""
	def __init__(self,val=None,parent=None,left1=None,right1=None):
		self.val = val
		self.left=left1
		self.right=right1
		self.parent=parent

class BST:
	def __init__(self,root1=None):
		self.root=root1

	def insert(self,x):
		temp=self.root
		if(temp==None):
			self.root=TreeNode()
			self.root.val=x
			return
		t=temp
		while(temp!=None):
			t=temp
			if(x>temp.val):
				temp=temp.right
			else:
				temp=temp.left
		try1=TreeNode(x,t)
		if(t.val<x):
			t.right=try1
		else:
			t.left=try1

	def search(self,x):
		temp=self.root
		if(temp==None):
			return None
		t=temp
		while(temp!=None):
			t=temp
			if(x>temp.val):
				temp=temp.right
			elif(x<temp.val):
				temp=temp.left
			else:
				return temp
		
		return None

	def minimum(self,Node):
		temp=Node
		t=None
		while(temp!=None):
			t=temp
			temp=temp.left
		return t

	def maximum(self,Node):
		temp=Node
		t=None
		while(temp!=None):
			t=temp
			temp=temp.right
		return t

	def preorder_Print(self):
		temp=self.root
		print("Preorder:")
		self.preorder(temp)
		print(" ")

	def inorder_Print(self):
		temp=self.root
		print("Inorder:")
		self.inorder(temp)
		print(" ")

	def postorder_Print(self):
		temp=self.root
		print("Postorder:")
		li=[]
		self.postorder(temp,li)
		print(" ")
		return li

	def inorder(self,Node):
		temp=Node
		if(temp==None):
			return
		self.inorder(temp.left)
		print(temp.val," ",end="")
		self.inorder(temp.right)

	def preorder(self,Node):
		temp=Node
		if(temp==None):
			return
		try1=0
		print(temp.val," ",end="")
		self.preorder(temp.left)
		self.preorder(temp.right)

	def postorder(self,Node,li):
		temp=Node
		if(temp==None):
			return
		self.postorder(temp.left,li)
		self.postorder(temp.right,li)
		print(temp.val," ",end="")
		li.append(temp.val)
	
	def successor(self,val):
		x=self.search(val)
		#print(x.val)
		if(x.right!=None):
			return self.minimum(x.right)
		y=x.parent
		while(y!=None and x!=y.left):
			x=y
			y=y.parent
		return y

	def predecessor(self,val):
		x=self.search(val)
		#print(x.val)
		if(x.left!=None):
			return self.maximum(x.left)
		y=x.parent
		while(y!=None and x!=y.right):
			x=y
			y=y.parent
		return y

	def Level_order(self):
		print("Level Order:")
		L=queue.Queue(maxsize=100)
		L.put(self.root)
		while(not L.empty()):
			temp=L.get()
			print(temp.val)
			if(temp.left!=None):
				L.put(temp.left)
			if(temp.right!=None):
				L.put(temp.right)

	def deleteNode(self,key): 
  		temp=self.search(key)
  		par=temp.parent
  		if(temp.parent==None):
  			return None
  		if(temp.left==None and temp.right==None):
  			
  			if(par.left==temp):
  				par.left=None
  			else:
  				par.right=None

	  	elif(temp.left==None):
  			rig=temp.right
  			if(par.left==temp):
  				par.left=rig
  			else:
  				par.right=rig
  			rig.parent=par

	  	elif(temp.right==None):
  			lef=temp.left
  			if(par.left==temp):
  				par.left=lef
  			else:
  				par.right==lef
  			lef.parent=par

  		else:
  			x=self.successor(key)
  			self.deleteNode(x.val)
  			x.parent = temp.parent
  			if temp.parent is not None:
  				if temp.parent.right == temp:
  					temp.parent.right = x
  				elif temp.parent.left == temp:
  					temp.parent.left = x
  			x.right = temp.right
  			x.left = temp.left


def main():
    tree=BST()
    tree.insert(5)
    tree.insert(6)
    tree.insert(3)
    tree.insert(8)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)
    tree.insert(1)
    tree.Level_order()
    tree.inorder_Print()
    tree.preorder_Print()
    tree.postorder_Print()
    print("Sucessor of 6 :",tree.successor(6).val)
    print("Predecessor of 6 :",tree.predecessor(6).val)
    print("Minimum : ",tree.minimum(tree.root).val)
    print("Maximum : ",tree.maximum(tree.root).val)

if __name__ == '__main__':
    main()