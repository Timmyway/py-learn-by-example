import sys; print(sys.version)

from collections import defaultdict
from dataclasses import dataclass
from collections import namedtuple
from typing import NamedTuple
from types import SimpleNamespace
from collections import deque

# Ex: default dict
heroes = defaultdict(list)
heroes['name'].append('Captain America')
print(f"- {heroes['name']}")

# Ex: dataclass
@dataclass
class StickyNote:
	color: str
	page_number: int
	size: tuple

note = StickyNote('yellow', '96', (7, 10))
print(f'- {note}')

# Ex: Named tuple
colors = namedtuple('color', 'red green blue')(255, 0, 46)
print(f'- Quantity of blue: {colors.blue}')

class Bottle(NamedTuple):
	quantity: float
	brand: str
	material: str

water = Bottle(1.5, "Natur'Eau", 'Plastique')
print(f'- {water}')

# Ex: Simple name space
triangle = SimpleNamespace(shape='Triangle', sides=3)
print(f'- Triangle: {triangle}')


class MaxItemError(Exception):
	def __str__(self):
		return 'Can not add more items'

class Stack:
	def __init__(self, max_size=None, exceptions=namedtuple('exceptions', 'maxitem')(False)):
		super(Stack, self).__init__()
		self.list = deque(maxlen=max_size)
		self.empty = True
		self.max_size = max_size
		self.exceptions = exceptions

	def push(self, elem):
		if len(self.list) == self.max_size:
			print(f'Can not add more than {self.max_size} items')
			if self.exceptions.maxitem:
				raise MaxItemError
		print(f'Add {elem} to stack')
		self.list.append(elem)
		self.empty = False

	def __repr__(self):
		return str(self.list)

	def pop(self):
		try:
			poped_elem = self.list.pop()
			print(f'{poped_elem} was removed from stack')
		except IndexError:
			print('Stack is empty')
			self.empty = True


class Queue(Stack):
	def __init__(self, max_size=None, exceptions=namedtuple('exceptions', 'maxitem')(False)):
		super(Queue, self).__init__()
		Stack.__init__(self, max_size=max_size, exceptions=exceptions)
	
	def pop(self):
		try:
			poped_elem = self.list.popleft()
			print(f'{poped_elem} was removed from stack')
		except IndexError:
			print('Stack is empty')
			self.empty = True

alphabet = Stack(4)

alphabet.push('a')
alphabet.push('b')
alphabet.push('c')
alphabet.push('z')

print(alphabet)

while not alphabet.empty:
	alphabet.pop()