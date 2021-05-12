class VIP_Queue:

    class Node:
        def __init__(self, item, status):
            self.item = item
            self.status = status

    def __init__(self):
        self.vip_count = 0
        self.standard_count = 0
        self.nums = []

    def __len__(self):
        return len(self.nums)

    def enqueue(self, item, status):
        node = self.Node(item, status)
        self.nums.append(node)
        if(status == "VIP"):
            self.vip_count += 1
        else:
            self.standard_count += 1

    def dequeue(self):
        if len(self.nums) == 0:
            raise Exception("VIP_Queue is empty")
        node = self.nums[0]
        if(node.status == "VIP"):
            self.vip_count -= 1
        else:
            self.standard_count -= 1
        self.nums.pop(0)
        return node.item

    def vip_dequeue(self):
        if len(self.nums) == 0:
            raise Exception("VIP_Queue is empty")
        if self.vip_count == 0:
            node = self.nums[0]
            self.nums.pop(0)
            self.standard_count -= 1
            return node.item
        else:
            for i in range(len(self.nums)):
                if self.nums[i].status == "VIP":
                    node = self.nums[i]
                    self.vip_count -= 1
                    self.nums.pop(i)
                    return node.item

    def first(self):
        if len(self.nums) == 0:
            raise Exception("VIP_Queue is empty")
        node = self.nums[0]
        return node.item

    def vip_first(self):
        if len(self.nums) == 0:
            raise Exception("VIP_Queue is empty")
        elif self.vip_count == 0:
            raise Exception("no VIP items in VIP_Queue")
        else:
            for i in range(len(self.nums)):
                if self.nums[i].status == "VIP":
                    node = self.nums[i]
                    return node.item
