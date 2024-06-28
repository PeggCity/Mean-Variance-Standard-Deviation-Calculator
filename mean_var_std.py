import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    M = np.array([
        list[:3],
        list[3:6],
        list[6:]
    ])

    calculations = {
        'mean': [M.mean(axis = 0).tolist(), M.mean(axis = 1).tolist(), M.mean()],
        'variance': [M.var(axis = 0).tolist(), M.var(axis = 1).tolist(), M.var()],
        'standard deviation': [M.std(axis = 0).tolist(), M.std(axis = 1).tolist(), M.std()],
        'max': [M.max(axis = 0).tolist(), M.max(axis = 1).tolist(), M.max()],
        'min':[M.min(axis = 0).tolist(), M.min(axis = 1).tolist(), M.min()],
        'sum':[M.sum(axis = 0).tolist(), M.sum (axis = 1).tolist(), M.sum()]
    }

    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))