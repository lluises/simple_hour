# Hour

Simple python library to do hour and minutes mathematical operations. It consists of a class Hour(HH, MM) that can be operated and compared with other Hour instances.


- **Author**: [LluisE](https://github.com/lluises)
- **Website**: https://kitsune.cat
- **Source**: https://github.com/lluises/hour
- **Licence**: https://www.mozilla.org/en-US/MPL/2.0/


# Installation

This project is available in PyPI: https://pypi.org/project/hour

You can install it in your machine by just doing:

```
pip install hour
```


# Usage


```python
from hour import Hour

a = Hour(12, 30)  # 12h and 30min
b = Hour(8, 25)   # 8h and 25min

c = a + b  # c will be Hour(20, 55)
print(c)   # Prints "20:55"

d = a - b # d will be Hour(4, 5)
print(d)          # Prints "04:05"
print(d.hours)    # Prints "4"
print(d.minutes)  # Prints "5"
print(d.absolute_minutes())  # Prints "245"
print(d.absolute_hours())    # Prints "4.083333333333333"

print(Hour(0, 125))  # 125min gets converted to Hour(2, 5)
print(Hour(1.5, 0))  # 1.5h gets converted to Hour(1, 30)

```

# Notes

You can have over 24 hours. This library does not handle days

```python
from hour import Hour

a = Hour(32, 25)  # 32h and 25min
print(a)          # Prints "32:25"
```

You can always obtain a 24h Hour by using the mod `%` operator:

```python
from hour import Hour

a = Hour(32, 25)
b = a % Hour(24)
print(b)  # Prints "08:25"
```

Negative hours are possible:

```python
from hour import Hour

a = Hour(-2, 10)  # -2h + 10min
b = Hour(3)       # 3h
print(a + b)      # Prints "01:10"

print(-a)         # Prints "01:50"
print(abs(a.absolute_minutes()) == ((-a).absolute_minutes())) # True

```

The operation `bool(Hour(...))` always returns `True` regardless of the hours and minutes.




# LICENSE

This project is licenced under the Mozilla Public License version 2.0. You may obtain a copy of the licence at the [LICENCE file in this repository](./LICENSE), or online at [https://www.mozilla.org/en-US/MPL/2.0/](https://www.mozilla.org/en-US/MPL/2.0/).
