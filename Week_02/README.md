# 学习笔记

## 242#异位词

* 异位词定义: 长度相同，含有的字母及字母个数相同的单词。

最偷懒的方式, 排序:
```
sorted(s) == sorted(t)
```
使用collections的方式
```
import collections
collections.Counter(s) == collections.Counter(t)
```

**Counter** : 一个 Counter 是一个 dict 的子类，用于计数可哈希对象。它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。计数可以是任何整数值，包括0和负数。

```
Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
```

思路很清晰的字典实现:
```python3

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True
```

## 1#两数之和

* List 类型，需要使用typing库
* list的index不是返回-1，而是报ValueError的错误


使用字典，进行空间还时间的话可以将O(N^2)的算法，降低到O(N)
```python
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

```
