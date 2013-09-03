"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3, 1, 3],
            "answer": [1, 3, 1, 3]
        },
        {
            "input": [1, 2, 3, 4, 5],
            "answer": []
        },
        {
            "input": [5, 5, 5, 5, 5],
            "answer": [5, 5, 5, 5, 5]
        },
        {
            "input": [10, 9, 10, 10, 9, 8],
            "answer": [10, 9, 10, 10, 9]
        },
        {
            "input": [2, 2, 3, 2, 2],
            "answer": [2, 2, 2, 2]
        },

        {
            "input": [10, 20, 30, 10],
            "answer": [10, 10]
        },
        {
            "input": [7],
            "answer": []
        },
        {
            "input": [0, 1, 2, 3, 4, 0, 1, 2, 4],
            "answer": [0, 1, 2, 4, 0, 1, 2, 4]
        },
        {
            "input": [99, 98, 99],
            "answer": [99, 99]
        },
        {
            "input": [0, 0, 0, 1, 1, 100],
            "answer": [0, 0, 0, 1, 1]
        }
    ],
    "Extra": [
        {
            "input": [5, 9, 2, 5, 9],
            "answer": [5, 9, 5, 9]
        },
        {
            "input": [5, 4, 3, 2, 1],
            "answer": []
        },
        {
            "input": [7, 7, 7, 7, 7],
            "answer": [7, 7, 7, 7, 7]
        },
        {
            "input": [20, 19, 20, 20, 19, 18],
            "answer": [20, 19, 20, 20, 19]
        },
        {
            "input": [222, 222, 333, 222, 222],
            "answer": [222, 222, 222, 222]
        },

        {
            "input": [100, 200, 300, 100],
            "answer": [100, 100]
        },
        {
            "input": [88],
            "answer": []
        },
        {
            "input": [0, 11, 22, 33, 44, 0, 11, 22, 44],
            "answer": [0, 11, 22, 44, 0, 11, 22, 44]
        },
        {
            "input": [199, 198, 199],
            "answer": [199, 199]
        },
        {
            "input": [0, 0, 0, 1, 1, 101],
            "answer": [0, 0, 0, 1, 1]
        }
    ]
}
