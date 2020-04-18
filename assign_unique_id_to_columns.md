```python
import pandas as pd
```


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Bob'],
    'item' : ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'number'    : [3, 2, 4, 3, 2, 1],
})
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>item</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>aaa</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>bbb</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>ccc</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Charlie</td>
      <td>ddd</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alice</td>
      <td>eee</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bob</td>
      <td>fff</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



通販の商品注文なのか、レストランに入って注文してるのか、どういうシチュエーションなんだろう。
まぁ良いや。あんまり考えずに作ったデータセットなので。
で、nameの値に応じて番号を振りたいとしよう。こんなふうに。

（注意：name_idの順序付けには条件が無いものとする。すなわち、出現順やアルファベット順でなくても良いとする。）



```python
df['name_id'] = [0, 1, 2, 2, 0, 1]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>item</th>
      <th>number</th>
      <th>name_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>aaa</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>bbb</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>ccc</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Charlie</td>
      <td>ddd</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alice</td>
      <td>eee</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bob</td>
      <td>fff</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## 方法3


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Bob'],
    'item' : ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'number'    : [3, 2, 4, 3, 2, 1],
})
```


```python
df['name_id'] = df['name'].astype('category').cat.codes
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>item</th>
      <th>number</th>
      <th>name_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>aaa</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>bbb</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>ccc</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Charlie</td>
      <td>ddd</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alice</td>
      <td>eee</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bob</td>
      <td>fff</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['name'].astype('category').cat.codes
```




    0    0
    1    1
    2    2
    3    2
    4    0
    5    1
    dtype: int8



確かにこれでできているけど、何でこれで実現できるのか分からなかった。ので、調べた。


```python
df['name']
```




    0      Alice
    1        Bob
    2    Charlie
    3    Charlie
    4      Alice
    5        Bob
    Name: name, dtype: object




```python
df['name'].astype('category')
```




    0      Alice
    1        Bob
    2    Charlie
    3    Charlie
    4      Alice
    5        Bob
    Name: name, dtype: category
    Categories (3, object): [Alice, Bob, Charlie]



astype()を使ってdtypeを変換した。dtypeがcategoryに変わっている。
dtypeについては以下も参照。


https://linus-mk.hatenablog.com/entry/2019/08/18/150845

categoryとは何か? を調べようとしたけど、
公式ドキュメントとか見ても長い説明が書いてあったので諦めた。

カテゴリ型のseriesはcatを通じて色々な情報を取得できる、らしい（pandasライブラリ活用入門 p.159）

カテゴリにしてそのIDを取得するには、



```python
df['name'].astype('category').cat.categories
```




    Index(['Alice', 'Bob', 'Charlie'], dtype='object')



categoryにすると何が嬉しいのか？

3点メリットがある
・
・

pandasライブラリ活用入門 p.158（pdf的には200）  
https://pbpython.com/pandas_dtypes_cat.html   ：Practical Business Python （あ、名前聞いたことあるわ）    
公式は  https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html  の先頭に3項目列挙されてる


## 方法1


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Bob'],
    'item' : ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'number'    : [3, 2, 4, 3, 2, 1],
})
```


```python
df['name_id'] = df['name'].factorize()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-27-52d75a2b1282> in <module>
    ----> 1 df['name_id'] = df['name'].factorize()
    

    /usr/local/lib/python3.7/site-packages/pandas/core/frame.py in __setitem__(self, key, value)
       2936         else:
       2937             # set column
    -> 2938             self._set_item(key, value)
       2939 
       2940     def _setitem_slice(self, key, value):


    /usr/local/lib/python3.7/site-packages/pandas/core/frame.py in _set_item(self, key, value)
       2998 
       2999         self._ensure_valid_index(value)
    -> 3000         value = self._sanitize_column(key, value)
       3001         NDFrame._set_item(self, key, value)
       3002 


    /usr/local/lib/python3.7/site-packages/pandas/core/frame.py in _sanitize_column(self, key, value, broadcast)
       3634 
       3635             # turn me into an ndarray
    -> 3636             value = sanitize_index(value, self.index, copy=False)
       3637             if not isinstance(value, (np.ndarray, Index)):
       3638                 if isinstance(value, list) and len(value) > 0:


    /usr/local/lib/python3.7/site-packages/pandas/core/internals/construction.py in sanitize_index(data, index, copy)
        609 
        610     if len(data) != len(index):
    --> 611         raise ValueError("Length of values does not match length of index")
        612 
        613     if isinstance(data, ABCIndexClass) and not copy:


    ValueError: Length of values does not match length of index


あれ。何でだろう。


```python
df['name'].factorize()
```




    (array([0, 1, 2, 2, 0, 1]), Index(['Alice', 'Bob', 'Charlie'], dtype='object'))




```python
type(df['name'].factorize())
```




    tuple




```python
df['name'].factorize()[0]
```




    array([0, 1, 2, 2, 0, 1])



というわけで、factorize関数はSeriesではなくtupleを返してくる。

tupleの1番目は「Seriesのどの位置に、どの要素が入っているか」を示す数値のndarrayが返る。
2番めは「使われている要素一覧」を示すIndexが返る。
（公式ドキュメントに書いてあるとおりだが。）
なるほど、Seriesを上記の2つに「分解して」返してくるので、factorizeという関数名なのであろう。

というわけで、今回ほしいのはtupleの1番目なので、factorize()したあとに[0]を指定すればよい。



```python
df['name_id'] = df['name'].factorize()[0]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>item</th>
      <th>number</th>
      <th>name_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>aaa</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>bbb</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>ccc</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Charlie</td>
      <td>ddd</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alice</td>
      <td>eee</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bob</td>
      <td>fff</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## 方法2


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'Charlie', 'Alice', 'Bob'],
    'item' : ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'number'    : [3, 2, 4, 3, 2, 1],
})
```


```python
df['name_id'] = df.groupby(['name']).ngroup()
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>item</th>
      <th>number</th>
      <th>name_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>aaa</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>bbb</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>ccc</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Charlie</td>
      <td>ddd</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alice</td>
      <td>eee</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bob</td>
      <td>fff</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.ngroup.html



```python

```
