
# coding: utf-8

# In[1]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self,root,val):
        #self.insert_(root,val)
        self.root = root
        print(self.insert)
    def insert_(self,root,val):
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val <= current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = val
                        break;
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = val
                        break;
                else:
                    break
                    print(self.insert_)
    def delete(self,root, target):
        while self.search(root, target) != None:
        # if root doesn't exist, just return it
            if not root:
                return root
            # Find the node in the left subtree	if key value is less than root value
            if root.val > target:
                root.left = self.delete(root.left, target)
            # Find the node in right subtree if key value is greater than root value,
            elif root.val < target:
                root.right = self.delete(root.right, target)
            # Delete the node if root.value == key
            else:
                # 0child or 1child
                if root.left is None:
                    child = root.right
                    root = None
                    return child

                elif root.right is None:
                    child = root.left
                    root = None
                    return child

                elif root.right is None and root.left is None:
                    return None

                    # 我要找右邊最小
                child = self.minRightNode(root.right)

                root.val = child.val

                root.right = self.delete(root.right, child.val)

            self.delete(root, target)

        else:
            return   
        
    def search(self,root,target):
        self.root=root
        if (root == None):
            return None
        if (root.val == target):
            return root
        if target < root.val:
            return self.search(root.left,target)
        else:
            return self.search(root.right,target)
        print(self.search)
        
    def mini(self, root):
        if root.left is None:
            return root
        else:
            return self.mini(root.left)

    def modify(self, root, target, new_val):
        # self.delete(root, target)
        # for i in range(0,target):
        # self.insert(root, new_val)
        # return True
            pass

