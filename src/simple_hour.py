"""
Hour implementation
"""


class Hour:
    """
    Inmutable class.

    Contains an hours and minutes
    HH:MM
    It allows over 24 hours

    Allows mathematical operations between Hour instances
    """

    def __init__(self, hours:int=0, minutes:int=0):
        self.h = hours
        self.m = minutes

        if isinstance(self.h, float):
            self.m += int((self.h % 1) * 60)
            self.h = int(self.h)

        if self.m >= 60 or self.m < 0:
            self.h += int(minutes // 60)
            self.m = abs(minutes % 60)

    @property
    def minutes(self):
        """Alias for m"""
        return self.m

    @property
    def hours(self):
        """Alias for h"""
        return self.h

    def absolute_minutes(self) -> int:
        """Return the total absolute minutes"""
        return self.h * 60 + self.m

    def absolute_hours(self) -> float:
        """Return the total absolute hours with decimals"""
        return self.h + self.m / 60.0

    def compact_string(self):
        """Returns a compact representation of the hour"""
        return f"{self.h}:{self.m}"

    def __eq__(self, target):
        if isinstance(target, Hour):
            return (self.h == target.h and self.m == target.m)
        elif target == 0:
            return self.h == 0 and self.m == 0
        return False

    def __lt__(self, target):
        return self.h < target.h or (self.h == target.h and self.m < target.m)

    def __le__(self, target):
        return self.h < target.h or (self.h == target.h and self.m <= target.m)

    def __add__(self, target):
        if isinstance(target, Hour):
            m = self.m + target.m
            h = self.h + target.h + m // 60
            return Hour(h, m % 60)
        elif target == 0:
            return self
        raise NotImplemented

    def __sub__(self, target):
        return self.__add__(-target)

    def __mul__(self, target):
        if isinstance(target, Hour):
            # What is 3hours * 2 and a half hours? The concept does not work
            return Hour(self.absolute_hours() * target.absolute_hours())
            # raise NotImplemented
        elif isinstance(target, int) or isinstance(target, float):
            return Hour(0, self.absolute_minutes() * target)
        raise NotImplemented

    def __rmul__(self, target):
        return self.__mul__(target)

    def __neg__(self):
        return Hour(-self.h, -self.m)

    def __abs__(self):
        if self.h < 0:
            return Hour((-self.h)-1, 60 - self.m)
        return self

    def __mod__(self, target):
        if isinstance(target, Hour):
            return Hour(0, self.absolute_minutes() % target.absolute_minutes())
        raise NotImplemented

    def __truediv__(self, target):
        if isinstance(target, Hour):
            return self.absolute_minutes() / target.absolute_minutes()
        elif isinstance(target, float) or isinstance(target, int):
            return Hour(0, self.absolute_minutes() / target)
        raise NotImplemented

    def __floordiv__(self, target):
        if isinstance(target, Hour):
            return self.absolute_minutes() // target.absolute_minutes()
        elif isinstance(target, float) or isinstance(target, int):
            return Hour(0, self.absolute_minutes() // target)
        raise NotImplemented

    def __bool__(self):
        return True

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"{self.h:02}:{self.m:02}"

    def __repr__(self):
        return f"{self}"

    def __hash__(self):
        return hash(self.absolute_minutes())
