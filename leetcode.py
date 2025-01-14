class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2:
            return 0

        height.append(0)
        peak:dict = {}#用来记录峰值
        on_peak:bool = True#用来记录是否在峰值上
        temp_list:list = []#用来记录当前的波峰
        for i in range(len(height) - 1):
            if on_peak:
                temp_list.append(i)
            if height[i] > height[i + 1]:
                on_peak = False
                for j in temp_list:
                    peak[j] = height[i]
                temp_list = []
            else:
                on_peak = True
                temp_list = []

        if len(peak) == 0:
            return 0
        print(peak)
        peak_key:list = list(peak.keys())

        temp = 0#两个都是peak_key的索引
        i = 1
        max_ = [0,0]#[0]是peak_key的索引,[1]是值
        read_calculate:list = []#用来记录可以形成碗的区间
        while temp != len(peak_key) - 1:#这个whie循环是为了找出所有的可以形成碗的区间，小碗会被合并（不过代码逻辑不是这样的）
            if peak[peak_key[i]] >= peak[peak_key[temp]]:#如果当前的peak_key[i]比之前的peak_key[temp]的高度高，就更新max_，同时把这个碗加到read_calculate里面
                read_calculate.append((peak_key[temp],peak_key[i]))
                temp = i
                max_ = [0,0]
            else:
                if peak[peak_key[i]] > max_[1]:
                    max_[0] = i
                    max_[1] = peak[peak_key[i]]

            if i == len(peak_key) - 1 and temp != len(peak_key) - 1:
                read_calculate.append((peak_key[temp],peak_key[max_[0]]))
                if temp == len(peak_key) - 2 and i == len(peak_key) - 1:
                    break
                temp = max_[0]
                i = temp
                max_ = [0,0]
            i += 1
        
        #计算每个碗的面积
        area = 0
        for i in read_calculate:
            if height[i[0]] >= height[i[1]]:
                min_ = height[i[1]]
            else:
                min_ = height[i[0]]
            sum = 0
            for j in range(i[0] + 1,i[1],1):
                a = min_ - height[j]
                if a < 0:
                    continue
                sum += a
            area += sum
            
        return area

if __name__ == "__main__":
    a = Solution()
    print(a.trap([9,6,8,8,5,6,3]))
    # print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    # print(a.trap([4,2,0,3,2,5]))
    pass