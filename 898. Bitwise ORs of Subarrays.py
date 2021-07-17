class Solution:
    def subarrayBitwiseORs(self, a):
        s1=set([a[0]])
        res=set(a)
        for i in range(1,len(a)):
            s2=set()
            for t in s1:
                s2.add(t|a[i]) 
            s2.add(a[i])
            for t in s2: res.add(t)
            s1=s2
        return len(res)
