class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def min(a,b):
            if a < b:
                return a
            else:
                return b
        def max(a,b):
            if a > b:
                return a
            else:
                return b 

        content = [intervals[0]]
        for i in range(1,len(intervals)):
            j = -1
            try:
                while True:
                    j += 1
                    if intervals[i][0] < content[j][0]:
                        break
                    elif intervals[i][0] == content[j][0]:
                        if intervals[i][1] > content[j][1]:
                            continue
                        break
            except:
                pass
            content.insert(j,intervals[i])

        end = [content[0]]
        i = 1

        while i < len(content):
            if end[-1][1] >= content[i][0]:
                end.append([min(end[-1][0],content[i][0]),max(end[-1][1],content[i][1])])
                i += 1
                end.pop(-2)
            else:
                end.append(content[i])
                i += 1

        return end



a = Solution()
print(a.merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))