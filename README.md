# simple-coin-values
A simple tab that show the values of your coins/altcoins/token. 


## Example
Those are just random values

![example.jpg](https://raw.githubusercontent.com/phastens/simple-coin-values/img/example.jpg)

## Configuration

This script use coinmarketcap website API to get the actual value, percentage over an hour/day/week.

You just need to add the name of coins you want to follow from the [coinmarketcap](https://coinmarketcap.com/) URL to list_curr:
https://coinmarketcap.com/currencies/bitcoin-cash/
```python
list_curr = ['bitcoin', 'bitcoin-cash'] 
```

After you put the amount of coin you have like:
```python
dict_amount = {'bitcoin':3.657,
         'bitcoin-cash':2.9330} 
```

Finally at what price you bought it:
After you put the amount of coin you have like:
```python
dict_buying_prices = {'bitcoin':897.645,
         'bitcoin-cash':400.2810} 
```

## Use it

Launch it under Linux in terminal with the command `python my_coin_values.py` in the directory where you download it.

You can also get the tab to be refresh every minutes by the command `watch -c -n 60 python my_coin_values.py` 
with the number after -n is in second.

Under GNU License
