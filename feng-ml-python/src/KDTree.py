import numpy as np

from src.MathUtils import MathUtils


class KDTreeNode(object):
    def __init__(self, point=None, split=None, left=None, right=None):
        self.point = point
        self.split = split
        self.left = left
        self.right = right


class KDTree(object):
    def __init__(self, root=None):
        self.root = root
        pass

    def create_tree(self, data_file):
        if len(data_file) == 0:
            return None
        data_list = np.array(data_file)
        m, n = np.shape(data_list)

        # 方差
        max_var = 0.0

        # 划分区域
        split = 0
        if m == 1:
            root = KDTreeNode(data_file[0], split)
            return root
        for i in range(n):
            array_list = data_list[:, i]
            tmp_var = np.var(array_list).item()
            if max_var < tmp_var:
                max_var = tmp_var
                split = i
        data_file.sort(key=lambda x: x[split])
        index = int(m / 2)
        point = data_file[index]
        root = KDTreeNode(point, split)
        root.left = self.create_tree(data_file[0:index])
        root.right = self.create_tree(data_file[index + 1: m])
        return root

    def tree_traverse(self, root):
        if root is None:
            return
        self.tree_traverse(root.left)
        print(root.point, root.split)
        self.tree_traverse(root.right)
        pass

    def query(self, root, x):
        mathUtils = MathUtils()
        node_list = []
        tmp_root = root
        point = root.point
        nearest = root
        while tmp_root:
            node_list.append(tmp_root)
            split = tmp_root.split
            point = tmp_root.point
            nearest = tmp_root

            if x[split] <= tmp_root.point[split]:
                tmp_root = tmp_root.left
            else:
                tmp_root = tmp_root.right
        min_distance = mathUtils.compute_distance(x, point)
        while node_list:
            back_point = node_list.pop()
            split = back_point.split
            if mathUtils.compute_distance(x, back_point.point) < min_distance:
                min_distance = mathUtils.compute_distance(x, back_point.point)
                nearest = back_point
                if x[split] <= back_point.point[split]:
                    tmp_root = back_point.right
                else:
                    tmp_root = back_point.left
                    pass
                if tmp_root:
                    node_list.append(tmp_root)
                    current_distance = mathUtils.compute_distance(x, tmp_root.point)
                    if min_distance > current_distance:
                        min_distance = current_distance
                        nearest = tmp_root
                pass
            pass

        return nearest.point, min_distance


if __name__ == '__main__':
    array = [[3, 1, 4], [2, 3, 7], [2, 1, 3], [2, 4, 5], [1, 4, 4], [0, 5, 7], [4, 3, 4], [6, 1, 4], [5, 2, 5],
             [4, 0, 6], [7, 1, 4]]
    array = [[7, 2], [5, 4], [9, 6], [2, 3], [4, 7], [8, 1]]
    kd_tree = KDTree()
    kd_tree.root = kd_tree.create_tree(array)
    mathUtils = MathUtils()
    x = [2.0, 4.5]
    print(kd_tree.query(kd_tree.root, x))
