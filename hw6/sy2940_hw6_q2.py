from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(int(num_str[i]))
        while self.data.header.next.data == 0 and len(self.data) > 1:
            self.data.delete_first()

    def __add__(self, other):
        sumNum = Integer("")
        # p1 is the first pointer, p2 is the second pointer.
        p1, p2 = self.data.trailer.prev, other.data.trailer.prev
        carry = 0
        while p1.data is not None and p2.data is not None:
            result = p1.data + p2.data + carry
            carry = result // 10
            sumNum.data.add_first(result % 10)
            p1, p2 = p1.prev, p2.prev
        # if p1 still have data, then point the third pointer p3 to it.
        if p1.data is not None:
            p3 = p1
        else:
            p3 = p2
        while p3.data is not None:
            sumNum.data.add_first((p3.data + carry) % 10)
            carry = (p3.data + carry) // 10
            p3 = p3.prev
        # if we still have carry remaining, add to the first digit.
        if carry != 0:
            sumNum.data.add_first(carry)
        return sumNum

    def __repr__(self):
        strSelf = ""
        # p is the pointer p
        p = self.data.header.next
        # while p has data in it
        while p.data is not None:
            strSelf += str(p.data)
            # move pointer forward
            p = p.next
        return strSelf

    def __mul__(self, other):
        mulNum = Integer("")
        # p1 is the first pointer, p2 is the second pointer.
        # start mul from tail to head.
        p1 = self.data.trailer.prev
        for indexFirstNum in range(len(self.data)):
            p2 = other.data.trailer.prev
            carry = 0
            mulCache = Integer("")
            for indexSecondNum in range(len(other.data)):
                result = p1.data * p2.data + carry
                carry = result // 10
                mulCache.data.add_first(result % 10)
                p2 = p2.prev
            # if still has carry, add to the first digit
            if carry != 0:
                mulCache.data.add_first(carry)
            for indexMulCache in range(indexFirstNum):
                mulCache.data.add_last(0)
            mulNum += mulCache
            p1 = p1.prev
        return mulNum
