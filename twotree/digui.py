from tree import TwoTree


def find_node(root,target)->bool:
    if root is None:
        return False
    if root.val == target:
        return True
    if target < root.val:
        return find_node(root.left,target)
    if target > root.val:
        return find_node(root.right,target)


if __name__ == "__main__":
    bst = TwoTree()

    values_is = [8,3,1,6,12,15]

    for val in values_is:
        bst.insert(val)

    result = find_node(bst.root,100)
    print(f"查找结果: {result}")  # 输出: 查找结果: True