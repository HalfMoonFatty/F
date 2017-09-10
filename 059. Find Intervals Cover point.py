''' 
1. 给一组区级的二维数组，每一组代表一个接收方，每一个接收方有一组区间。然后给一个整数，要求找出所有区间 ...

例子就是
A想要接收1~4、7~9、12~15
B想要接收2~8、10~12
C想要接收5~6

如果给一个数字8，应该返回A和B
如果给个数字5，应该返回B和C

用二分查找优化吗 还是必须build interval tree, 然后search？？？

'''
class Solution (object):

    def findIndex(self, IntervalList, point):
        points = []
        for i in range(len(IntervalList)):
            for j in range(len(IntervalList[i])):
                points.append([IntervalList[i][j][0]-1, 's', i])
                points.append([IntervalList[i][j][1]+1, 'e', i])
        points.append([point, 'p', -1])
        points.sort()

        result = set()
        for p in points:
            if p[1] == 's':
                result.add(p[2])
            if p[1] == 'e':
                result.remove(p[2])
            if p[1] == 'p':
                break
        return result


s = Solution()
IntervalList = [[[1,4],[7,9],[12,15]],[[2,8],[10,12]],[[5,6]]]
point1 = 8
point2 = 5
print s.findIndex(IntervalList, point1)
print "\n=============\n"
print s.findIndex(IntervalList, point2)
