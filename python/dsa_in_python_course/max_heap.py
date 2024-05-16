class MaxHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS
  
  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()
    
  def heapify_up(self):
    print("Heapifying up")
    # idx is the last index in the heap list
    idx = self.count
    # while parent idx is greater than 0, loop
    while self.parent_idx(idx) > 0:
      # get the values at the child and parent indices
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      if parent < child:
        print(f"swapping {parent_element} with {element}")
        #put the parent value where the child used to be
        self.heap_list[idx] = parent
        #heapify up the child to where the parent used to be
        self.heap_list[self.parent_idx(idx)] = child
      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))