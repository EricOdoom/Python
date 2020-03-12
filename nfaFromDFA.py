# X and Y are sets. Returns the set X intersect Y. Assumes that the elements
# are ’simple enough to be compared naively’. The output is ordered to match
# the order in X. INTERSECTION OF 2 SETS
def setIntersection(x, y):
	result = []
	for z in x:
		if z in y:
			result.append(z)
	return tuple(result)
# X is a set. Returns the power set P(X). The output set itself is not sorted
# in any particular way, but each element of the output set is sorted to match
# the order in X. POWER SET
def setPower(x):
	if len(x) == 0:
		return ((),)
	else:
		withoutFirst = setPower(x[1:])
		withFirst = [(x[0],) + y for y in withoutFirst]
		return tuple(withFirst) + withoutFirst


def dfaFromNFA(nfa):
	dfaStates = setPower(nfa[0])
	Sigma = nfa[1]
	startState = (nfa[2],)
	finalStates = ()
	for state in dfaStates:
		if setIntersection(state,nfa[3]):
			finalStates = finalStates + (state,)
	deltaFunc = nfa[4]
	P = (dfaStates, Sigma, startState, finalStates, deltaFunc)
	return P

def dfa(m,w):
	allStates = m[2]
	for char in w:
		dfaStates = ()
		for state in allStates:
			dfaStates +=  delta(state,char)
		allStates = dfaStates
	allStates = setPower(allStates)
	if setIntersection(allStates,m[3]):
		return True
	else:
		return False


if __name__ == "__main__":
	def delta(q, a):
		if (q, a) == ("x", "0"):
			return ("x","y")
		elif (q, a) == ("x", "1"):
			return ("y",)
		elif (q, a) == ("y", "0"):
			return ()
		elif (q, a) == ("y", "1"):
			return ("x",)

	newNFA = (("x", "y"), ("a", "b"), "x", ("x",), delta)
	newDFA = dfaFromNFA(newNFA)
	w = ["0", "10", "11", "101", "001", "", "011", "100", "1111", "1110", "0101","0000000"]
	for char in w:
		print(char,dfa(newDFA,char))
