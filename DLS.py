def DLS(node, goal_state, limit):
    if node.state == goal_state:
        return node

    if limit == 0:
        return None

    for child_node in node.expand():
        result = DLS(child_node, goal_state, limit - 1)
        if result is not None:
            return result

    return None

class Node:
    def __init__(self, state, children=[]):
        self.state = state
        self.children = children

    def expand(self):
        return self.children

goal_state = "goal"

tree = Node("root", [
    Node("child1", [
        Node("grandchild1"),
        Node("grandchild2")
    ]),
    Node("child2", [
        Node("grandchild3"),
        Node("grandchild4",[Node(goal_state)])
    ])
])

depth_limit = 2
result = None

while result is None and depth_limit < 4:
    result = DLS(tree, goal_state, depth_limit)
    depth_limit += 1

if result is None:
    print("Goal state not found.")
else:
    print("Goal state found at node with state:", result.state)
