import random


class InterInt:
    """a class behave as a generator"""

    def __init__(self):
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a += 1
        return self.a


a = InterInt()
print(next(a))  # 1
print(next(a))  # 2
print(next(a))  # 3


class CustomDict:
    def __init__(self, size=1000):
        # 用list初始化hashtable，并且每个位置都对应一个子list已解决hash冲突问题
        self.hash_list = [list() for _ in range(size)]
        self.size = size

    def __setitem__(self, key, value):
        # 利用Python自带的hash函数，对key哈希并对size取模，得到hashed_key作为list的索引
        hashed_key = hash(key) % self.size

        # hashed_key位置有值就覆盖，否则追加
        for item in self.hash_list[hashed_key]:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.hash_list[hashed_key].append([key, value])

        """
        There are two scenarios in which the loop may end. 
        The first one is when the item is found and break is encountered. 
        The second scenario is that the loop ends without encountering a break statement.
        The for/else's else will be executed in the first scenario.

        This is the basic structure of a for/else loop (so do as while/else loop):
        for item in container:
            if search_something(item):
                # Found it!
                process(item)
                break
        else:
            # Didn't find anything..
            not_found_in_container()
        """

        # 上面用到了 for/else 语句，否则需要用下面的语句实现
        # is_update = False
        # for item in self.hash_list[hashed_key]:
        #     if item[0] == key:
        #         is_update = True
        #         item[1] = value
        #         break
        # if not is_update:
        #     self.hash_list[hashed_key].append([key, value])

    def __getitem__(self, key):
        for item in self.hash_list[hash(key) % self.size]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def __repr__(self):
        # hashtable打印
        result = []
        for sub_list in self.hash_list:
            if not sub_list:
                continue
            for item in sub_list:
                result.append(str(item[0]) + ": " + str(item[1]))
        return "{" + ", ".join(result) + "}"

    def __contains__(self, key):
        # 是否包含key，实现in操作符的功能
        for item in self.hash_list[hash(key) % self.size]:
            if item[0] == key:
                return True
        return False

    # 通过调用 keys() 、values() 、items() 来分别遍历键、值、键值对
    def __iterate_kv(self):
        for sub_list in self.hash_list:
            if not sub_list:
                continue
            for item in sub_list:
                yield item

    def __iter__(self):
        for kv_pair in self.__iterate_kv():
            yield kv_pair[0]

    def keys(self):
        return self.__iter__()

    def values(self):
        for kv_pair in self.__iterate_kv():
            yield kv_pair[1]

    def items(self):
        return self.__iterate_kv()


cdict = CustomDict()

cdict["a"] = 1
cdict["b"] = 2
print(cdict["a"])
print('c' in cdict)  # False
# print(cdict["c"])  # KeyError

print(cdict)
print(list(cdict.keys()))
print(list(cdict.values()))
print(list(cdict.items()))
