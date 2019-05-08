def dfs(v):
	w = match[v]
	if(w < 0):
		match[v] = v+1
		print(match)
	return True

def bipartite_matching():
	match = [-1] * V
	for v in range(V):
		dfs(v)
		print(match)
	return 

V = 5
match = [-1] * V #マッチングのペア

bipartite_matching()
