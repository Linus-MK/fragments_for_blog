# jupyter notebookをmarkdownに変換する

# 残り：
# notebook中のmarkdownに対応する
# htmlによるpandas.DataFrameが来たらエラーを返す
# argparseか関数引数で入出力ファイル名を作る

# 入力ファイルの形式は以下の通り。htmlによるpandas.DataFrameには対応しない。
# ```python
# 入力コード
# ```
#     4字のインデントで
#     出力結果

# ファイルオープン
in_f = open('input.md', 'r')
out_f = open('output.md', 'w')
status = 'none'

for line in in_f:
    line_chomped = line.rstrip()
    if status == 'none' and (line_chomped == '```python' or line_chomped == '```py'):
        # コード開始時には1行空行を入れる
        status = 'code'
        out_f.write('\n')
        
    elif status == 'code' and line_chomped == '```':
        status = 'suspend'
        # コードが終わった状態。
        # 次に（実行結果なしで）別のコードが来るのか、コードの実行結果が来るのか、markdownが来るのかこの時点では不明
        # この時点で、コード終わりの```は出力しない。
    elif status == 'suspend' and (line_chomped == '```python' or line_chomped == '```py'):
        status = 'code'
        # コードが終わって、実行結果なしで、別のコードが来た状態。
        out_f.write('```\n')
        out_f.write('\n')

    elif status == 'suspend' and line_chomped[:4] == '    ':
        status = 'output'
        out_f.write('# --------------------\n')
    elif status == 'output' and line == '\n':
        status = 'none'
        out_f.write('```\n')

    if line == '\n':
        pass
    elif status == 'suspend':
        pass
    elif status == 'output':
        # 最初4文字の空白を削除して出力
        out_f.write(line[4:])
    else:
        out_f.write(line)
