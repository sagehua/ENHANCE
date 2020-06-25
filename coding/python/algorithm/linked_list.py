class LNode(object):
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_

class LinkedListUnderflow(ValueError):
	pass


class LList(object):
	"""单链表 ADT
	head -> [node0] -> [node1] -> [node2]
	"""
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head is None

	def prepend(self, elem):
		self._head = LNode(elem, self._head)

	def pop_head(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_head")
		e = self._head.elem
		self._head = self._head.next
		return e

	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			return
		p = self._head
		while p.next:
			p = p.next
		p.next = LNode(elem)

	def pop_tail(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_tail")
		p = self._head
		if p.next is None:
			e = p.elem
			self._head = None
			return e
		while p.next.next:
			p = p.next
		e = p.next.elem
		p.next = None
		return e

	def find(self, elem):
		p = self._head
		while p:
			if p.elem == elem:
				return p.elem
			p = p.next

	def __str__(self):
		lst = []
		p = self._head
		while p:
			lst.append(p.elem)
			p = p.next
		return str(lst)

	__repr__ = __str__


if __name__ == '__main__':
	linked_list = LList()
	linked_list.prepend(3)
	linked_list.prepend(4)
	linked_list.prepend(5)
	print(linked_list)
	linked_list.pop_head()
	print(linked_list)
	linked_list.append(2)
	linked_list.append(1)
	print(linked_list)
	linked_list.pop_tail()
	print(linked_list)
	print(linked_list.find(3))
