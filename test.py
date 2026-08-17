#!/usr/bin/python3

from src.hour import Hour


def test():
    a = Hour(12, 30)
    b = Hour(8, 25)

    assert a.hours == 12, f"a.hours should be 12, not {a.hours}"
    assert a.minutes == 30, f"a.hours should be 30, not {a.minutes}"

    c = a + b
    assert str(c) == "20:55", 'a'

    d = a - b # d will be Hour(4, 5)
    assert d.absolute_minutes() == 245, f"d.absolute_minutes() should be 245 not {d.absolute_minutes()}"
    assert d.absolute_hours() == 4.083333333333333, f"d.absolute_hours() should be 4.083333333333333 not {d.absolute_hours()}"

    assert Hour(0, 125) == Hour(2, 5), f"Hour(0, 125) should be the same as Hour(2, 5)"
    assert Hour(1.5) == Hour(1, 30), f"Hour(1.5) should be the same as Hour(1, 30)"

    assert Hour(2) < Hour(3)
    assert Hour(2, 10) < Hour(2, 20)
    assert Hour(2, 20) <= Hour(2, 20)

    assert Hour(32, 25).absolute_minutes() == 32*60+25

    assert Hour(32, 25) % Hour(24) == Hour(8, 25), f"Hour(32, 25) % Hour(24) must give 8:25"

    assert str(Hour(-2, 10)) == "-2:10"
    assert str(Hour(-2, -10)) == "-3:50"
    assert Hour(2, 10) == --Hour(2, 10)

    e = Hour(64, 32)
    assert (e % Hour(24)) + (e // Hour(24)) * Hour(24)

    assert bool(a)

    assert abs(-Hour(2, 10)) == Hour(2, 10)

    return True

def main():
    ok = test()
    if ok:
        print("All tests passed")
    else:
        print("Some tests failed")

if __name__ == '__main__':
    main()
