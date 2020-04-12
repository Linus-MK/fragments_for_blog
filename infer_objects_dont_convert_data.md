## infer_objectは文字を数字に変換してはくれないよ、という話

StackOverflowのURL：  https://stackoverflow.com/questions/35003138/python-pandas-inferring-column-datatypes/48269724 のコメント  

関数APIのURL：https://pandas.pydata.org/pandas-docs/version/0.25.3/reference/api/pandas.DataFrame.infer_objects.html  
（今後メジャーアップデートが来るから、バージョン指定したURLにしておくよ）  
https://pandas.pydata.org/pandas-docs/version/0.25.3/reference/api/pandas.Series.infer_objects.html



```python
import pandas as pd
```


```python
pd.__version__
```




    '0.25.3'




```python
df1 = pd.DataFrame(['1', '2', '3'])
df1.dtypes
```




    0    object
    dtype: object




```python
df1.infer_objects().dtypes
```




    0    object
    dtype: object



---


```python
# 公式ドキュメントに載っている例

df2 = pd.DataFrame({"A": ["a", 1, 2, 3]})
df2 = df2.iloc[1:]
df2
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
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.dtypes
```




    A    object
    dtype: object




```python
df2.infer_objects().dtypes
```




    A    int64
    dtype: object



---


```python
# では文字列の代わりに浮動小数点数ではどうだろうか?

df3 = pd.DataFrame({"A": [9.876, 1, 2, 3]})
df3 = df3.iloc[1:]
df3
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
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.dtypes
```




    A    float64
    dtype: object




```python
df3.infer_objects().dtypes
```




    A    float64
    dtype: object




```python
df4 = pd.DataFrame({"A": [1, 2, 3]}, dtype='int8')
df4.dtypes
```




    A    int8
    dtype: object




```python
df4.infer_objects().dtypes
```




    A    int8
    dtype: object




```python
df_temp = pd.DataFrame({"A": [1, 2, 3]})
df_temp.dtypes
```




    A    int64
    dtype: object




```python
df3.infer_objects().dtypes
```




    A    int64
    dtype: object



## じゃあ文字列を数字に変換する方法は?

to_numeric()を使いましょう。
これはDataFrameに対しては使えない。
Seriesに対して使える。


```python
df7 = pd.Series(['1', '2', '3'])
df7.dtypes
```




    dtype('O')




```python
df7.to_numeric()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-16-709a82f0d362> in <module>
    ----> 1 df7.to_numeric()
    

    /usr/local/lib/python3.7/site-packages/pandas/core/generic.py in __getattr__(self, name)
       5177             if self._info_axis._can_hold_identifiers_and_holds_name(name):
       5178                 return self[name]
    -> 5179             return object.__getattribute__(self, name)
       5180 
       5181     def __setattr__(self, name, value):


    AttributeError: 'Series' object has no attribute 'to_numeric'



```python
pd.to_numeric(df7)
```




    0    1
    1    2
    2    3
    dtype: int64




```python

```
