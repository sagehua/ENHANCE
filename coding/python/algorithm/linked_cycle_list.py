from linked_list import LNode, LinkedListUnderflow


class LCList(object):
	"""循环单链表 ADT
	[node0] -> [node1] -> [node2] <- tail
	    ^                    |
	    |____________________|
	"""
	def __init__(self):
		self._tail = None

	def is_empty(self):
		return self._tail is None

	def prepend(self, elem):
		p = LNode(elem)
		if self.is_empty():
			self._tail = p
			p.next = p
		else:
			p.next = self._tail.next
			self._tail.next = p

	# def append(self, elem):
	# 	"""直接在尾端插入"""
	# 	p = LNode(elem)
	# 	if self.is_empty():
	# 		self._tail = p
	# 		p.next = p
	# 	else:
	# 		p.next = self._tail.next
	# 		self._tail.next = p
	# 		self._tail = p

	def append(self, elem):
		"""先在首端插入，然后调整 tail"""
		self.prepend(elem)
		self._tail = self._tail.next

	def pop_head(self):
		# 链表为空的情况
		if self.is_empty():
			raise LinkedListUnderflow('in pop_head')
		p = self._tail.next
		if self._tail is p:
			# 链表只有一个节点的情况
			self._tail = None
		else:
			self._tail.next =p.next
		return p.elem

	def pop_tail(self):
		if self.is_empty():
			raise LinkedListUnderflow('in pop_tail')
		p = self._tail
		if self._tail.next is p:
			self._tail = None
		else:
			while True:
				p = p.next
				if p.next is self._tail:
					break
			p.next = self._tail.next
			self._tail = p
		return p.elem

	def __str__(self):
		lst = []
		p = self._tail
		while p:
			p = p.next
			lst.append(p.elem)
			if p is self._tail:
				break
		return str(lst)

	__repr__ = __str__		


if __name__ == '__main__':
	linked_cycle_list = LCList()
	linked_cycle_list.append(1)
	linked_cycle_list.append(2)
	linked_cycle_list.append(3)
	linked_cycle_list.prepend(4)
	linked_cycle_list.prepend(5)
	print(linked_cycle_list)
	linked_cycle_list.pop_head()
	print(linked_cycle_list)
	linked_cycle_list.pop_tail()
	print(linked_cycle_list)
