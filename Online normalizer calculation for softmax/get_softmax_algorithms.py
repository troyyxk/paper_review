import math

def get_softmax_a1(x):
    V = len(x)
    m = [float("-inf")] * V
    d = [0] * V
    # io, load
    for j in range(V):
        # first j-1 would be 0, as initialized
        d[j] = d[j-1] + math.exp(x[j])
    
    y = [None] * V
    # io, load
    for i in range(V):
        y[i] = math.exp(x[i]) / d[V-1]

    # io, store
    print(f"d = {d}")
    print(f"y = {y}")

def get_softmax_a2(x):
    V = len(x)
    m = [float('-inf')] * V
    # io, load
    for k in range(V):
        m[k] =  max(m[k-1], x[k])
    d = [0] * V
    # io, load
    for j in range(V):
        d[j] = d[j-1] + math.exp(x[j] - m[V-1])
    
    y = [None] * V
    # io, load
    for i in range(V):
        y[i] = math.exp(x[i] - m[V-1]) / d[V-1]

    # io, store
    print(f"d = {d}")
    print(f"y = {y}")

def get_softmax_a3(x):
    V = len(x)
    m = [float('-inf')] * V
    d = [0] * V
    # io, load
    for j in range(V):
        m[j] =  max(m[j-1], x[j])
        d[j] = d[j-1] * math.exp(m[j-1] - m[j]) + math.exp(x[j] - m[j])
    y = [None] * V
    # io, load
    for i in range(V):
        y[i] = math.exp(x[i] - m[V-1]) / d[V-1]

    # io, store
    print(f"d = {d}")
    print(f"y = {y}")
