from platform import node
import sys
sys.setrecursionlimit(10**6)

def post(tree, ans):
    ans.append(tree.idx)
    if tree.left is not None: post(tree.left, ans) 
    if tree.right is not None : post(tree.right, ans) 

def pre(tree, ans):
    if tree.left is not None: pre(tree.left, ans)
    if tree.right is not None: pre(tree.right, ans)
    ans.append(tree.idx)
    
class Tree:
    def __init__(self, nodeinfo):
        # print("Tree : ", nodeinfo)
        self.root = max(nodeinfo, key = lambda x: x[1])
        self.idx = self.root[2]
        
        # datas = sorted(nodeinfo, key=lambda x: x[1])
        
        left_ = [d for d in nodeinfo if d[0] < self.root[0]]
        right_ = [d for d in nodeinfo if d[0] > self.root[0]]
        
        self.left = None if left_ == [] else Tree(left_)
        self.right = None if right_ == [] else Tree(right_)



    
def solution(nodeinfo):
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
        
    tree = Tree(nodeinfo)
    postlist, prelist = [], []
    
    pre(tree, prelist)
    post(tree, postlist)

    return [postlist, prelist]

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))

sys.exit(0)






#############
def preorder(arr, max_idx):
    idx = 0
    ans = []
    def _preorder(idx):
        if idx > max_idx:
            return
        if arr[idx] == 0:
            pass
        else:
            ans.append(arr[idx])
            _preorder(idx*2+1)
            _preorder(idx*2+2)
    _preorder(idx)
    return ans

def postorder(arr, max_idx):
    idx = 0
    ans = []
    def _postorder(idx):
        if idx > max_idx:
            return
        if arr[idx] == 0:
            pass
        else:
            _postorder(idx*2+1)
            _postorder(idx*2+2)
            ans.append(arr[idx])
    _postorder(idx)
    return ans

def _solution(nodeinfo):
    answer = [[]]
    _nodeinfo=[]

    for i, node in enumerate(nodeinfo):
        node.append(i+1)
        _nodeinfo.append(node)
    nodeinfo= sorted(_nodeinfo, key=lambda x:-x[1])
    nodes = [x[2] for x in nodeinfo]
    
    
    ans = [0]*(10**6)
    idx_ans = [0]*(10**6)
    length = len(ans)
    
    cnt = 0
    max_idx = -987654321
    for n in nodeinfo:
        x = n[0]
        v = n[2]
        idx = 0
        while True:
            if ans[idx] == 0:
                ans[idx] = v
                idx_ans[idx] = x
                
                if idx > max_idx:
                    max_idx = idx
                break
            else:
                if idx_ans[idx] < x:
                    idx = 2 * idx + 2
                else:
                    idx = 2 * idx + 1
                # if idx > length:
                #     break

    return preorder(ans[:max_idx+1], max_idx), postorder(ans[:max_idx+1], max_idx)

# 724136895