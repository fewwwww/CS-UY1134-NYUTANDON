class Vector:
    def __init__(self, d):
        if isinstance(d, list):
            self.coords = d
        else:
            self.coords = [0] * d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __setitem__(self, i, val):
        self.coords[i] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = self[i] - other[i]
        return res

    def __neg__(self):
        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = (-1) * self[i]
        return res

    def __mul__(self, n):
        if isinstance(n, Vector):
            if (len(self) != len(n)):
                raise ValueError("dimensions must agree")
            res = 0
            for i in range(len(self)):
                res += self[i] * n[i]
            return res
        else:
            res = Vector(len(self))
            for i in range(len(self)):
                res[i] = self[i] * n
            return res

    def __rmul__(self, n):
        res = Vector(len(self))
        for i in range(len(self)):
            res[i] = self[i] * n
        return res
