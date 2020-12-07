def delete_node_at_pos(self, pos):
	if self.head:
		cur_node = self.head
		if pos == 0:
			self.head = cur_node.next
			cur_node = None
			return
		prev_node = None
		count = 0
		while cur_node and count != pos:
			prev_node = cur_node
			cur_node = cur_node.next
			count += 1
		if cur_node.next == None:
			return
		prev_node.next = cur_node.next
		cur_node = None