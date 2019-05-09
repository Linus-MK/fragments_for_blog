def lower_func(v):
	w = match[v]
	if(w < 0):
		match[v] = v+1
		print("lower_func:" , match)
	return True

def higher_func():
	match = [-1] * V
	for v in range(V):
		lower_func(v)
		print("higher_func:", match)
	return 

V = 3
match = [-1] * V

higher_func()
print("global:", match) # dfs関数によって、書き換わっている

# 疑問1 dfs関数の中のmatchはグローバル変数を指しているっぽい。それはどうして? 関数呼び出しを順にたどるならhigher_funcの中のmatchじゃないか?
# 疑問2 dfs関数の中のmatchはグローバル変数を指しているっぽい。それはどうして? あとで値の代入が発生しているならローカル変数じゃないか?
