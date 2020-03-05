```python
import pandas as pd
```


```python
pd.__version__
```




    '0.25.3'



## 列名を指定して追加する方法だと末尾（最後、右端）に追加される


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred'],
    'English' : [12, 34, 56, 78, 90, 100],
    'Math'    : [88, 66, 55, 44, 22, 11]    
})

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
      <th>English</th>
      <th>Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>12</td>
      <td>88</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>34</td>
      <td>66</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>56</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>78</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>90</td>
      <td>22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Fred</td>
      <td>100</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['new_column'] = 'value'
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
      <th>English</th>
      <th>Math</th>
      <th>new_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>12</td>
      <td>88</td>
      <td>value</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>34</td>
      <td>66</td>
      <td>value</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>56</td>
      <td>55</td>
      <td>value</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>78</td>
      <td>44</td>
      <td>value</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>90</td>
      <td>22</td>
      <td>value</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Fred</td>
      <td>100</td>
      <td>11</td>
      <td>value</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['new_column_2'] = ['a', 'b', 'c', 'd', 'e', 'f']
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
      <th>English</th>
      <th>Math</th>
      <th>new_column</th>
      <th>new_column_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>12</td>
      <td>88</td>
      <td>value</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>34</td>
      <td>66</td>
      <td>value</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>56</td>
      <td>55</td>
      <td>value</td>
      <td>c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>78</td>
      <td>44</td>
      <td>value</td>
      <td>d</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eve</td>
      <td>90</td>
      <td>22</td>
      <td>value</td>
      <td>e</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Fred</td>
      <td>100</td>
      <td>11</td>
      <td>value</td>
      <td>f</td>
    </tr>
  </tbody>
</table>
</div>



## 先頭（最初、左端）に追加するにはinsertを使う


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred'],
    'English' : [12, 34, 56, 78, 90, 100],
    'Math'    : [88, 66, 55, 44, 22, 11]    
})
```


```python
df.insert(0, 'new_column', 'value')
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
      <th>new_column</th>
      <th>name</th>
      <th>English</th>
      <th>Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>value</td>
      <td>Alice</td>
      <td>12</td>
      <td>88</td>
    </tr>
    <tr>
      <th>1</th>
      <td>value</td>
      <td>Bob</td>
      <td>34</td>
      <td>66</td>
    </tr>
    <tr>
      <th>2</th>
      <td>value</td>
      <td>Charlie</td>
      <td>56</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>value</td>
      <td>David</td>
      <td>78</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>value</td>
      <td>Eve</td>
      <td>90</td>
      <td>22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>value</td>
      <td>Fred</td>
      <td>100</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.insert(0, 'new_column_2', ['a', 'b', 'c', 'd', 'e', 'f'])
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
      <th>new_column_2</th>
      <th>new_column</th>
      <th>name</th>
      <th>English</th>
      <th>Math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>value</td>
      <td>Alice</td>
      <td>12</td>
      <td>88</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>value</td>
      <td>Bob</td>
      <td>34</td>
      <td>66</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>value</td>
      <td>Charlie</td>
      <td>56</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>value</td>
      <td>David</td>
      <td>78</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e</td>
      <td>value</td>
      <td>Eve</td>
      <td>90</td>
      <td>22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>f</td>
      <td>value</td>
      <td>Fred</td>
      <td>100</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.insert(0, 'new_column_error', ['a', 'b', 'c', 'd', 'e'])  # 6行ぶんを書くべきところ、要素数5の配列を入れた
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-bca86ac7c013> in <module>
    ----> 1 df.insert(0, 'new_column_error', ['a', 'b', 'c', 'd', 'e'])  # 6行ぶんを書くべきところ、要素数5の配列を入れた
    

    /usr/local/lib/python3.7/site-packages/pandas/core/frame.py in insert(self, loc, column, value, allow_duplicates)
       3588         """
       3589         self._ensure_valid_index(value)
    -> 3590         value = self._sanitize_column(column, value, broadcast=False)
       3591         self._data.insert(loc, column, value, allow_duplicates=allow_duplicates)
       3592 


    /usr/local/lib/python3.7/site-packages/pandas/core/frame.py in _sanitize_column(self, key, value, broadcast)
       3747 
       3748             # turn me into an ndarray
    -> 3749             value = sanitize_index(value, self.index, copy=False)
       3750             if not isinstance(value, (np.ndarray, Index)):
       3751                 if isinstance(value, list) and len(value) > 0:


    /usr/local/lib/python3.7/site-packages/pandas/core/internals/construction.py in sanitize_index(data, index, copy)
        610 
        611     if len(data) != len(index):
    --> 612         raise ValueError("Length of values does not match length of index")
        613 
        614     if isinstance(data, ABCIndexClass) and not copy:


    ValueError: Length of values does not match length of index



```python

```
