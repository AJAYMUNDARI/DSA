class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

sumParents = 0

def buildTree(root, val, s):
    n = len(s)
    node = root
    for i in range(n-1):
        if s[i] == 'L':
            node = node.left
        else:
            node = node.right
    child = TreeNode(val)
    if s[n-1] == 'L':
        node.left = child
    else:
        node.right = child

def checkMagicParent(node):
    if node is None:
        return 0
    lsum = checkMagicParent(node.left)
    rsum = checkMagicParent(node.right)
    if lsum == 0:
        return node.val + rsum
    if rsum == 0:
        return node.val + lsum
    if (lsum % 2 == 0 and rsum % 2 != 0) or (lsum % 2 != 0 and rsum % 2 == 0):
        global sumParents
        sumParents += node.val
    return node.val + lsum + rsum

n, x = map(int, input().split())
root = TreeNode(x)
for i in range(n-1):
    s = input().split()
    y = int(s[1])
    buildTree(root, y, s[0])

checkMagicParent(root)
print(sumParents)
