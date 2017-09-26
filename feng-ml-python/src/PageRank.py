#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import numpy as np


# def build_index(links):
#     website_list = links.keys()
#     return {website: index for index, website in enumerate(website_list)}
#
#
# def build_transition_matrix(links, index):
#     total_links = 0
#     A = np.zeros((len(index), len(index)))
#     for webpage in links:
#         # dangling page
#         if not links[webpage]:
#             # Assign equal probabilities to transition to all the other pages
#             A[index[webpage]] = np.ones(len(index)) / len(index)
#         else:
#             for dest_webpage in links[webpage]:
#                 total_links += 1
#                 A[index[webpage]][index[dest_webpage]] = 1.0 / len(links[webpage])
#
#     return A
#
#
# def pagerank(A, eps=0.0001, d=0.85):
#     P = np.ones(len(A)) / len(A)
#     while True:
#         new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
#
#         delta = abs((new_P - P).sum())
#         if delta <= eps:
#             return new_P
#         P = new_P

def page_rank(A, eps=0.0001, d=0.85):
    P = np.ones(len(A)) / len(A)
    eeT = np.ones([len(A), len(A)])
    print((1 - d) * eeT / len(A))
    print(d * A)
    G = d * A + (1 - d) * eeT / len(A)
    print("G")
    print(G)
    while True:
        new_P = G.dot(P.T)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P


if __name__ == '__main__':
    # links = {
    #     'webpage-1': set(['webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9', 'webpage-10']),
    #     'webpage-2': set(['webpage-5', 'webpage-6']),
    #     'webpage-3': set(['webpage-10']),
    #     'webpage-4': set(['webpage-9']),
    #     'webpage-5': set(['webpage-2', 'webpage-4']),
    #     'webpage-6': set([]),  # dangling page
    #     'webpage-7': set(['webpage-1', 'webpage-3', 'webpage-4']),
    #     'webpage-8': set(['webpage-1']),
    #     'webpage-9': set(['webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10']),
    #     'webpage-10': set(['webpage-2', 'webpage-3', 'webpage-8', 'webpage-9']),
    # }
    #
    # website_index = build_index(links)
    # # print(website_index)
    #
    # A = build_transition_matrix(links, website_index)
    # # print(A)
    #
    # results = pagerank(A)
    #
    # print("Results:",
    #       results)  # [ 0.151  0.11355952  0.08725  0.10647619  0.07814286  0.07814286 0.0235  0.07105952  0.15605952  0.13480952]
    # print(sum(results))  # 1.0
    # print([item[0] for item in sorted(enumerate(results), key=lambda item: -item[1])])  # [2, 0, 3, 5, 7, 4, 6, 9, 1, 8]

    # M = np.mat([[0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    #             [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    #             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    #             [0, 1, 1, 0, 0, 0, 0, 1, 1, 0]])
    M = np.mat([[0, 1, 1, 1], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]])

    m, n = M.shape
    M_avg = np.zeros([m, n])

    sumRow = np.sum(M, axis=1)
    for i in range(m):
        sum = sumRow[i, 0]
        if sum == 0:
            continue
        for j in range(n):
            M_avg[i, j] = M[i, j] / sum
    print(M_avg)
    print(M_avg.T)
    print(page_rank(M_avg.T))

    # M = np.mat([[0.0375, 0.8875, 0.0375, 0.0375],
    #             [0.4625, 0.0375, 0.0375, 0.4625],
    #             [0.4625, 0.0375, 0.0375, 0.4625],
    #             [0.4625, 0.4625, 0.0375, 0.0375]])
    # p=np.mat([[0.25], [0.25], [0.25], [0.25]])
    # print(M.dot(p))
