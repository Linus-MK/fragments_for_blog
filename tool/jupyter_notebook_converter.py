# jupyter notebookをmarkdownに変換する

# 残り：
# notebook中のmarkdownに対応する
# htmlによるpandas.DataFrameが来たらエラーを返す
# 出力がエラーメッセージの場合にうまく行かないので直せたら直す。

# 仕様：
# markdown中の空行は削除している
# markdown中にコードブロック```code``` や4字インデントが来た場合の動作は保証外

# 入力ファイルの形式は以下の通り。htmlによるpandas.DataFrameには対応しない。
# ```python
# 入力コード
# ```
#     4字のインデントで
#     出力結果
# markdown部分はの開始終了を示すサインは無いです。
# コードブロック周囲に改行が無いとレイアウトが崩れるので、markdownの開始終了で1行改行することにしときます。

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="input file name. (markdown)")
parser.add_argument("output_file", help="output file name. if it exist already, the file is overritten.")
args = parser.parse_args()

# ファイルオープン
in_f = open(args.input_file, 'r')
out_f = open(args.output_file, 'w')
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
        # この時点では、コード終わりの```を出力しない。次に実行結果が来たら一緒のコードブロックに入れたいから。
    elif status == 'suspend' and (line_chomped == '```python' or line_chomped == '```py'):
        status = 'code'
        # コードが終わって、実行結果なしで、別のコードが来た状態。
        out_f.write('```\n')
        out_f.write('\n')

    elif status == 'suspend' and line_chomped[:4] == '    ':
        status = 'output'
        # コードが終わって、実行結果が来た状態。
        # コードと実行結果との区切りを出力する。
        out_f.write('\n')
        out_f.write('# --------------------\n')
        out_f.write('\n')
    elif status == 'output' and line == '\n':
        status = 'none'
        out_f.write('```\n')

    elif status == 'suspend' and line_chomped != '':
        status = 'markdown'
        out_f.write('```\n')
        out_f.write('\n')  # コードブロックとmarkdown境界の改行

    elif status == 'markdown' and line_chomped == '':
        status = 'none'
        # markdown中の改行でもnoneに戻っちゃうけど、実害はないはず……


    if line == '\n':
        pass
    elif status == 'suspend':
        pass
    elif status == 'output':
        # 最初4文字の空白を削除して出力
        out_f.write(line[4:])
    else:
        out_f.write(line)

# suspend状態のままファイルが終わると、コードブロックを閉じていないので、最後に閉じる

if status == 'suspend':
    out_f.write('```\n')
