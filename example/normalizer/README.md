

```python
import malaya
```

    /usr/local/lib/python3.6/site-packages/sklearn/cross_validation.py:41: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
      "This module will be removed in 0.20.", DeprecationWarning)



```python
corpus_normalize = ['maka','serious','yeke','masing-masing']
normalizer = malaya.naive_normalizer(corpus_normalize)
normalizer.normalize('masing2')
```




    'masing-masing'




```python

```
