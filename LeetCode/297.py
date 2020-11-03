# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tmp_nodes = [root]
        record_str = ""
        while len(tmp_nodes)!=0:
            new_tmp = []
            for node in tmp_nodes:
                if node==None:
                    record_str+="n,"
                else:
                    record_str+=str(node.val)+","
                    new_tmp.append(node.left)
                    new_tmp.append(node.right)
            tmp_nodes = new_tmp
        return record_str


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")[:-1]
        if data[0]=='n':
            return None
        root = TreeNode(int(data[0]))
        tmp_nodes = [root]
        idx = 1
        while len(tmp_nodes)!=0:
            new_tmp = []
            for node in tmp_nodes:
                if data[idx]!='n':
                    node.left = TreeNode(int(data[idx]))
                    new_tmp.append(node.left)
                if data[idx+1]!='n':
                    node.right = TreeNode(int(data[idx+1]))
                    new_tmp.append(node.right)
                idx+=2
            tmp_nodes = new_tmp
        return root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ser = Codec()
    deser = Codec()
    ser_str = ser.serialize(root)
    print(ser_str)
    print(deser.deserialize(ser_str))
    print('yes')