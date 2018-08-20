class Difference:
    def __init__(self, a):
        self.elements = a

    def computeDifference(self):
        largest = max(self.elements)
        smallest = min(self.elements)
        self.maximumDifference = abs(largest - smallest)



_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
