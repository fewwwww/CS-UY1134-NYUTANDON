from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        # each char exist at least 1 time, so start with 1.
        occurChar = 1
        for indexChar in range(len(orig_str)-1):
            if orig_str[indexChar] != orig_str[indexChar + 1]:
                self.data.add_last((orig_str[indexChar + 1], occurChar))
                occurChar = 1
            else:
                occurChar += 1
        if len(orig_str) != 0:
            self.data.add_last((orig_str[len(orig_str) - 1], occurChar))

    def __add__(self, other):
        concatStr = CompactString("")
        # p is the pointer.
        p = self.data.header.next
        # while data is not empty
        while p.next.data is not None:
            concatStr.data.add_last(p.data)
            # move pointer forward
            p = p.next
        if p.data[0] == other.data.header.next.data[0]:
            concatStr.data.add_last((p.data[0], p.data[1] +
                                    other.data.header.next.data[1]))
            # let pointer skip one step
            p = other.data.header.next.next
        else:
            concatStr.data.add_last(p.data)
            p = other.data.header.next
        while p.data is not None:
            concatStr.data.add_last(p.data)
            p = p.next
        return concatStr

    def __lt__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return True
        elif p1.data is None and p2.data is None:
            return False
        elif p1.data is not None and p2.data is None:
            return False
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return False
                return p1.data[0] < p2.next.data[0]
            else:
                if p1.next.data is None:
                    return True
                return p1.next.data[0] < p2.data[0]
        return p1.data[0] < p2.data[0]

    def __le__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return True
        elif p1.data is None and p2.data is None:
            return True
        elif p1.data is not None and p2.data is None:
            return False
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return False
                return p1.data[0] < p2.next.data[0]
            else:
                if p1.next.data is None:
                    return True
                return p1.next.data[0] < p2.data[0]
        return p1.data[0] < p2.data[0]

    def __gt__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return False
        elif p1.data is None and p2.data is None:
            return False
        elif p1.data is not None and p2.data is None:
            return True
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return True
                return p1.data[0] > p2.next.data[0]
            else:
                if p1.next.data is None:
                    return False
                return p1.next.data[0] > p2.data[0]
        return p1.data[0] > p2.data[0]

    def __ge__(self, other):
        p1 = self.data.header.next
        p2 = other.data.header.next
        # continue to move pointer when they are not identical
        while p1.data == p2.data and p1.data is not None:
            p1 = p1.next
            p2 = p2.next
        if p1.data is None and p2.data is not None:
            return False
        elif p1.data is None and p2.data is None:
            return True
        elif p1.data is not None and p2.data is None:
            return True
        if p1.data[0] == p2.data[0]:
            if p1.data[1] > p2.data[1]:
                if p2.next.data is None:
                    return True
                return p1.data[0] > p2.next.data[0]
            else:
                if p1.next.data is None:
                    return False
                return p1.next.data[0] > p2.data[0]
        return p1.data[0] > p2.data[0]

    def __repr__(self):
        # p is the pointer
        p = self.data.header.next
        returnedStr = ""
        while p.data is not None:
            returnedStr += p.data[0] * p.data[1]
            # move pointer forward
            p = p.next
        return returnedStr
