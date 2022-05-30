# from calendar import c


# strs = ["flower","flow","flight"]
# minlength = 0
# minvalue = 0
# l1 = []
# for i in strs:
#     if len(i) > minlength:
#         minlength = len(i)
#     else:
#         minvalue = i
# strs.remove(minvalue)
# cheack = False
# for index,value in enumerate(minvalue):
#     for string in strs:
#         if value in string:
#             if value == string[index]:
#                 # l1.append(value)
#                 check = True
#         else:
#             check = False
#             break
#     if check:
#         l1.append(value)        
# if l1:
#     print(''.join(l1))
# else:
#     print(''' "" ''')


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minlength = 0
        minvalue = 0
        l1 = []
        for i in strs:
            if len(i) > minlength:
                minlength = len(i)
            else:
                minvalue = i
        strs.remove(minvalue)
        cheack = False
        for index,value in enumerate(minvalue):
            for string in strs:
                if value in string:
                    if value == string[index]:
                        # l1.append(value)
                        check = True
                else:
                    check = False
                    break
            if check:
                l1.append(value)        
        if l1:
            return ''.join(l1)
        else:
            return ''' "" '''
obj = Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))


strs=["flower","flow","flight"]
print(strs[0][0])