```python
import pandas as pd
```


```python
df = pd.DataFrame({
    'name'    : ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred'],
    'English' : [12, 34, 56, 78, -1, 90],
    'Math'    : [88, 66, -1, 44, 22, -1]    
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
      <td>-1</td>
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
      <td>-1</td>
      <td>22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Fred</td>
      <td>90</td>
      <td>-1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[4, 'English'] = 99999
```


```python
df.loc[4]
```




    name         Eve
    English    99999
    Math          22
    Name: 4, dtype: object




```python
df['English']
```




    0       12
    1       34
    2       56
    3       78
    4    99999
    5       90
    Name: English, dtype: int64




```python
df.loc[3, 'Math']
```




    44


