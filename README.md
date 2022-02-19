# PyPad
Basic padding of multiple columns in Python


## Before padding
Initial input data (generated automatically): `sample_data = test_data(4, 10)`
```python
[['0.', '1.', '2.', '3.'],
 ['fwADRXzZN', 'SND', 'RL', 'okMGFA'],
 ['|', '|', '|', '|'],
 ['GFNwYPKnPC', 'XHf', 'DuUPpf', 'MtgvHVob']]
```
Parsing list and printing: `output_data(sample_data)`
```
0.fwADRXzZN|GFNwYPKnPC
1.SND|XHf
2.RL|DuUPpf
3.okMGFA|MtgvHVob
```

## After padding
Padding original input data: `padded_data = pad(sample_data)`
```python
[['0. ', '1. ', '2. ', '3. '],
 ['fwADRXzZN ', 'SND       ', 'RL        ', 'okMGFA    '],
 ['| ', '| ', '| ', '| '],
 ['GFNwYPKnPC ', 'XHf        ', 'DuUPpf     ', 'MtgvHVob   ']]
```
Parsing padded list and printing: `output_data(padded_data)`
```
0. fwADRXzZN | GFNwYPKnPC 
1. SND       | XHf        
2. RL        | DuUPpf     
3. okMGFA    | MtgvHVob
```
