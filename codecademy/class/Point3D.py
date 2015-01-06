class Point3D(object):
    """docstring for  Point3D"""
    def __init__(self, x, y, z):
        super( Point3D, self).__init__()
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print my_point
