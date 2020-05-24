```python
import pandas as pd
pd.options.display.notebook_repr_html = False
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




          name  English  Math
    0    Alice       12    88
    1      Bob       34    66
    2  Charlie       56    -1
    3    David       78    44
    4      Eve       -1    22
    5     Fred       90    -1




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


