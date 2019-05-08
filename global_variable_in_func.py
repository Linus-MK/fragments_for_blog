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
match = [-2] * V #マッチングのペア

bipartite_matching()
print(match) # dfs関数によって、書き換わっている

# 疑問1 dfs関数の中のmatchはグローバル変数を指しているっぽい。それはどうして? 関数呼び出しを順にたどるならbipartite_matchingの中のmatchじゃないか?
# 疑問2 dfs関数の中のmatchはグローバル変数を指しているっぽい。それはどうして? あとで値の代入が発生しているならローカル変数じゃないか?
