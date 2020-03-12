class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None
class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        for num in nums:
            node = root
            #从最高位开始到最低位顺序进行构建
            for i in range(31, -1, -1):
                temp = num & (1 << i)
                if temp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
        final=0
        for num in nums:
            node=root
            result=''
            for i in range(31, -1, -1):
                temp = num & (1 << i)
                if(temp==0):
                    if node.zero==None and node.one==None:
                        break
                    #temp=0的情况
                    if(node.one!=None):
                        result=result+'1'
                        node=node.one
                    else:
                        result=result+'0'
                        node=node.zero
                else:
                    #temp=1的情况
                    if node.zero==None and node.one==None:
                        break
                    if(node.zero!=None):
                        result=result+'1'
                        node=node.zero
                    else:
                        result=result+'0'
                        node=node.one        
            x=int(result, 2)
            if x>final:
                final=x
        return final    