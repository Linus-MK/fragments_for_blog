# jupyter notebookをmarkdownに変換する

# 残り：
# コードと出力を一緒のセットにする
# コードと出力の間に区切り線を入れる
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
        status = 'none'
    elif status == 'none' and line_chomped[:4] == '    ':
        status = 'output'
        out_f.write('```\n')
    elif status == 'output' and line == '\n':
        status = 'none'
        out_f.write('```\n')

    if line == '\n':
        pass
    elif status == 'output':
        # 最初4文字の空白を削除して出力
        out_f.write(line[4:])
    else:
        out_f.write(line)
