import networkx as nx
import matplotlib.pyplot as plt
"""
画出二叉树
有缺点：不支持相同值的节点。。
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.val] = (x, y)
    G.add_node(node.val)
    if node.left:
        G.add_edge(node.val, node.left.val)
        l_x, l_y = x - 1 / 2 ** layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.val, node.right.val)
        r_x, r_y = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)


def draw(node):   # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


def build_tree(node_list):
    """层序遍历构建二叉树"""
    from queue import Queue
    root1 = None
    if not node_list:
        return root1
    root1 = TreeNode(node_list[0])
    q = Queue()
    q.put(root1)
    for i in range(1, len(node_list), 2):
        root = q.get()
        node1 = node_list[i]
        node2 = node_list[i+1]
        if node1 is not None:
            root.left = TreeNode(node1)
            q.put(root.left)
        if node2 is not None:
            root.right = TreeNode(node2)
            q.put(root.right)
    return root1




if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(5, right=TreeNode(6)))
    # root = TreeNode(1, left=TreeNode(2))
    # root = TreeNode(1)

    draw(root)

    root_node = [1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6]
    r2 = build_tree(root_node)
    draw(r2)

    r1 = [1, 2, 5, 3, 4, None, 6]
    r1_tree = build_tree(r1)
    draw(r1_tree)
