class Node:
    def __init__(self, name):
        self.name = name
        self.profit = 0
        self.parent = None
        self.children = []


class Tree:
    def __init__(self):
        self.dic = {}
        self.center = Node("-")
        self.dic["-"] = self.center

    def add(self, name, refer):
        node = Node(name)
        node.parent = self.dic[refer]
        node.parent.children.append(node)
        self.dic[name] = node

    def sell(self, name, amount):
        curr = self.dic[name]
        val = amount*100
        while curr.name != "-":
            if val * 0.1 < 1:
                curr.profit += val
                break
            else:
                curr.profit += val - int(val*0.1)
                val = int(val * 0.1)
                curr = curr.parent

    def print(self, enroll):
        ret = []
        for name in enroll:
            ret.append(self.dic[name].profit)
        return ret


def solution(enroll, referral, seller, amount):
    tree = Tree()
    for idx in range(len(enroll)):
        tree.add(enroll[idx], referral[idx])
    for idx in range(len(seller)):
        tree.sell(seller[idx], amount[idx])
    answer = tree.print(enroll)
    return answer