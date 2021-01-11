import collections
from pprint import pprint
Scientist = collections.namedtuple('Scientist', [
  'name',
  'field',
  'born',
  'nobel'
])
print(Scientist)
scientist = (
  Scientist(name='Bob McSmith', field='math', born=1993, nobel=False),
  Scientist(name='Billy Smilly', field='programming', born=1122, nobel=True)
)
pprint(scientist)


# scientists = [
#   {'name': 'Bob Billhud', 'field': 'programming', 'born': 1999, 'nobel': False},
#   {'name': 'Billy Borge', 'field': 'eating', 'born': 1339, 'nobel': False},
# ]
# print(scientists)