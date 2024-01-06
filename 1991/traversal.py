from typing import Dict

def preorder(left:Dict[str,str],right:Dict[str,str],root:str)->str:
    if "."!=root:
        return root+preorder(left,right,left[root])+preorder(left,right,right[root])
    else:
        return ""

def inorder(left:Dict[str,str],right:Dict[str,str],root:str)->str:
    if "."!=root:
        return inorder(left,right,left[root])+root+inorder(left,right,right[root])
    else:
        return ""

def postorder(left:Dict[str,str],right:Dict[str,str],root:str)->str:
    if "."!=root:
        return postorder(left,right,left[root])+postorder(left,right,right[root])+root
    else:
        return ""

N=int(input())
left: Dict[str,str] ={}
right: Dict[str,str] ={}
for _ in range(N):
    p,l,r=input().split()
    left[p]=l
    right[p]=r
print(preorder(left,right,"A"))
print(inorder(left,right,"A"))
print(postorder(left,right,"A"))

