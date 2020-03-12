# X and Y are sets. Returns the set X intersect Y. Assumes that the elements
# are ’simple enough to be compared naively’. The output is ordered to match
# the order in X.
def setIntersection(x, y):
    result = []
    for z in x:
        if z in y:
            result.append(z)
    return tuple(result)
# X is a set. Returns the power set P(X). The output set itself is not sorted
# in any particular way, but each element of the output set is sorted to match
# the order in X.
def setPower(x):
    if len(x) == 0:
        return ((),)
    else:
        withoutFirst = setPower(x[1:])
        withFirst = [(x[0],) + y for y in withoutFirst]
        return tuple(withFirst) + withoutFirst

def dfa(m,w):
    allStates = m[2]
    for char in w:
        dfaStates = ()
        for state in allStates:
            dfaStates += delta(state, char)
        allStates = dfaStates
    allStates = setPower(state)
    finalStates = m[3]
    if setIntersection(allStates, finalStates):
        return True
    return False

def nfa(m,w):
    allStates = []
    allStates.append(m[2])
    for char in w:
        nfaStates = ()
        for state in allStates:
            nfaStates += delta(state, char)
        allStates = nfaStates
    if setIntersection(states, m[3]):
        return True
    return False

def dfaFromNFA(nfa):
    allStates = setPower(nfa[0])
    sigma = nfa[1]
    finalStates = ()
    start = (nfa[2],)
    for i in allStates:
        if setIntersection(i, nfa[3]):
            finalStates += (i,)
    deltaPrime = nfa[4]
    return (allStates, sigma, start,finalStates, deltaPrime)

if __name__ == "__main__":
    def delta(q,a):
        if (q,a) == ("x", "a"):
            return ("x", "y")
        elif (q,a) == ("x", "b"):
            return ("y",)
        elif (q,a) == ("y", "a"):
            return ()
        elif (q,a) == ("y", "b"):
            return ("x",)

    accepts = ["", "a", "aaaa", "aabba"]
    nfa = (("x", "y"), ("a", "b"), "x", ("x",), delta)
    DFA = dfaFromNFA(nfa)
    for i in accepts:
        print(i, nfa(DFA, i))
