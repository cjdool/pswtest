from collections import deque


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a*b/gcd(a, b))


def isprime (a):
    if a < 2:
        return False
    if a % 2 == 0 and a != 2:
        return False
    i = 3
    while i*i <= a:
        if a % i == 0:
            return False
        i+=2
    return True


def perm_recur(list, r):
    ret = []
    if r > len(list):
        return ret

    if r == 1:
        for item in list:
            ret.append([item])
    elif r>1:
        for i in range(len(list)):
            temp = [i for i in list]
            temp.remove(list[i])
            for p in perm_recur(temp, r-1):
                ret.append([list[i]]+p)

    return ret


def perm_with_duplicate_recur(list, r):
    ret = []

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for item in list:
            for p in perm_recur(list, r-1):
                ret.append([item]+p)

    return ret


def perm_dfs(list, r):
    ret = []
    idx = [i for i in range(len(list))]
    stack = []
    for i in idx:
        stack.append([i])

    while len(stack)!=0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp)==r:
                    element = []
                    for i in temp:
                        element.append(list[i])
                    ret.append(element)
                else:
                    stack.append(temp)

    return ret


def combi_recur(list, r):
    ret = []
    if r > len(list):
        return ret

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for i in range(len(list)-r+1):
            for temp in combi_recur(list[i+1:], r-1):
                ret.append([list[i]]+temp)

    return ret


def combi_with_duplicate_recur(list, r):
    ret = []

    if r == 1:
        for item in list:
            ret.append([item])
    elif r > 1:
        for i in range(len(list)):
            for temp in combi_recur(list[i:], r-1):
                ret.append([list[i]]+temp)

    return ret


def combi_dfs(list, r):
    ret = []
    idx = [i for i in range(len(list))]
    stack = []
    for i in idx[:len(list)-r+1]:
        stack.append([i])

    while len(stack)!=0:
        cur = stack.pop()

        for i in range(cur[-1]+1, len(list)-r+1+len(cur)):
            temp = cur + [i]
            if len(temp) == r:
                element = []
                for i in temp:
                    element.append(list[i])
                ret.append(element)
            else:
                stack.append(temp)

    return ret


def basic_bfs(graph, root):
    visited = [root]
    queue = deque([root])

    while len(queue) != 0:
        cur = queue.popleft()
        for item in graph[cur]:
            if item not in visited:
                visited.append(item)
                queue.append(item)
    return visited


def basic_dfs(graph, root):
    visited = []
    stack = [root]

    while len(stack) != 0:
        cur = stack.pop()
        if cur not in visited:
            visited.append(cur)
            for item in graph[cur]:
                stack.append(item)
    return visited


def recursive_dfs(graph, root, visited=[]):
    visited.append(root)
    for item in graph[root]:
        if not item in visited:
            visited = recursive_dfs(graph, item, visited)
    return visited