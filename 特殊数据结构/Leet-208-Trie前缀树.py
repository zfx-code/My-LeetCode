"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
1. void insert(String word) 向前缀树中插入字符串 word 。
2. boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
3. boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

需要的参数
1. root节点 : root = Trie()
2. child节点: HashMap<charcater, Trie>
3. 结束Flag : Boolean isEnd
3. 对应word : String val

"""


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd    = False

    def insert(self, word: str) -> None:
        node = self 
        for letter in word:
            # map ['a',...,'z'] to [0,...,25]
            ch = ord(letter) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        
        node.isEnd = True

    # 与前缀唯一区别就是"isEnd"是否表示一个单词
    def search(self, word: str) -> bool:
        node = self 
        for letter in word:
            ch = ord(letter) - ord('a')
            if not node.children[ch]:
                return False 
            node = node.children[ch]
        
        return node.isEnd
       
    # 与search唯一区别就是"isEnd"是否表示一个单词
    def startsWith(self, prefix: str) -> bool:
        node = self 
        for letter in prefix:
            ch = ord(letter) - ord('a')
            if not node.children[ch]:
                return False 
            node = node.children[ch]
        
        return True

# Your Trie object will be instantiated and called as such:
# word = "hello"
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Your Trie object will be instantiated and called as such:
# word = "apple"
# obj = Trie()
# obj.insert(word)
# obj.insert("app")
# # print(obj.next["h"].next)
# param_2 = obj.search(word)
# print(param_2)
# prefix = "app"
# param_3 = obj.startsWith(prefix)
# print(f"prefix: {param_3}")

"""
211. 添加与搜索单词 - 数据结构设计
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
 
"""
class WordDictionary:

    def __init__(self):
        self.children = [None] * 26 
        self.isEnd    = False

    def addWord(self, word: str) -> None:
        node = self 
        for letter in word:
            ch = ord(letter) - ord('a') 
            if not node.children[ch]:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        
        node.isEnd = True 
    
    """
    (1) 正常匹配字母
    (2) 特殊处理"."
    """
    # 针对"."通用匹配子部分, 递归匹配
    # node, sub_word是上层"."的下一个位置
    def match(self, node, sub_word: str):
        if len(sub_word) == 0:
            return node.isEnd 
        
        cur = node 
        for i in range(len(sub_word)):
            # "."
            if sub_word[i] == ".":
                for j in range(26):
                    # 该字母不能匹配
                    if not cur.children[j]:
                        continue
                    # 匹配
                    if self.match(cur.children[j], sub_word[i + 1:]):
                        return True 
                # 26个全匹配不上则失败
                return False

            ch = ord(sub_word[i]) - ord('a') 
            if not cur.children[ch]:
                return False
            cur = cur.children[ch]
        
        return cur.isEnd
    
    def search(self, word: str) -> bool:
        node = self 
        return self.match(node, word)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

print(wordDictionary.search("pad")) # 返回 False
print(wordDictionary.search("bad")) # 返回 True
print(wordDictionary.search(".ad")) # 返回 True
print(wordDictionary.search("b..")) # 返回 True
print(wordDictionary.search("a..")) # 返回 False



def letterCombinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []

    hashtable = {
        "2" : "abc"
        , "3" : "def"
        , "4" : "ghi"
        , "5" : "jkl"
        , "6" : "mno"
        , "7" : "pqrs"
        , "8" : "tuv"
        , "9" : "wxyz"
    }

    ans = []

    # 考虑完下标是i(长度是i + 1)的部分
    def dfs(i, cur):
        # print(i, cur)
        nonlocal ans
        # 结束条件, 位数相同, i是当前的结果长度
        if i + 1 == len(digits):
            ans.append(cur)
            return 
        
        # dfs就是要考虑当前-i的全部可能
        n = len(hashtable[digits[i + 1]])
        # 这时的i + 1不会越界, 被i + 1限制住了
        for k in range(n):
            dfs(i + 1, cur + hashtable[digits[i + 1]][k])

    # 对第一位置遍历所有情况 
    for letter in hashtable[digits[0]]:
        dfs(0, letter)

    return ans

digits = "23"

print(letterCombinations(digits))