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

def nfa(m,w):
	allStates = []
	allStates.append(m[2])
	finalState = m[3]
	for char in w:
		nfaStates = ()
		for state in allStates:
			nfaStates += delta(state,char)
		allStates = nfaStates
	if setIntersection(allStates,finalState):
		return True
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

	NFA = (("x", "y"), ("a", "b"), "x", ("x",), delta)

	w = ["0", "10", "11", "101", "001", "", "011", "100", "1111", "1110", "0101","0000000"]
	for char in w:
		print(char, nfa(NFA,char))
