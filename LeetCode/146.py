class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__capacity = capacity
        self.__dict = {}
        self.__record = []


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.__dict:
            return -1
        else:
            self.__record.remove(key)
            self.__record.append(key)
            return self.__dict[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.__dict:
            self.__record.remove(key)
            self.__record.append(key)
        else:
            if len(self.__dict) == self.__capacity:
                self.__dict.pop(self.__record[0])
                self.__record.pop(0)
            self.__record.append(key)
        self.__dict[key] = value


if __name__ == '__main__':
    so = LRUCache(2)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)