import  re
#创建数据存储格式
class render_maze():
    def __init__(self, numbers, string):
        self.numbers =numbers
        self.string = string
    def render(self):
        # 输入格式判断
        if not re.match(r'^-?[0-9]\d*\s-?[0-9]\d*$', self.numbers):#若输入的不是整数或者输入格式错误，则报错
            return "Invalid number format. or Incorrect command format​.1"
        flag_1 = re.match(r'^-?[0-9]\d*\,-?[0-9]\d*\s-?[0-9]\d*\,-?[0-9]\d*$', self.string)
        flag_2 = re.match(r'^-?[0-9]\d*\,-?[0-9]\d*\s-?[0-9]\d*\,-?[0-9]\d*(;-?[0-9]\d*\,-?[0-9]\d*\s-?[0-9]\d*\,-?[0-9]\d*)*$',
                          self.string)#多个联通点
        if not flag_1 and not flag_2:
            # 若输入的不是整数或者输入格式错误，则报错
            return "Invalid number format. or Incorrect command format​.2"
        #先判断第一行数字是否超出范围
        numbers = self.numbers.split(" ")
        rows = int(numbers[0])
        columns = int(numbers[1])
        if rows <=0 or columns <=0:
            return "Number out of range"
        # 先判断第二行数字是否超出范围
        #连接迷宫
        self.connect_maze(rows,columns)
    def connect_maze(self,rows,columns):
        connect = self.string.split(";")
        cordinate = []
        for i in range(len(connect)):
            temp = connect[i].split(" ")
             # 将两个坐标点分开来
            temp_one = temp[0].split(",")
            temp_two = temp[1].split(",")
            row1 = int(temp_one [0])
            columns1 = int(temp_one [1])
            row2 = int(temp_two[0])
            columns2 = int(temp_two[1])
            if row1 < 0 or columns1 < 0 or row1 < 0  or columns2 < 0:
                return "Number out of range"
            cordinate.append([row1,columns1,row2,columns2])
        #开始渲染迷宫
        #初始化原始的矩阵信息
        maze = [['[w]']*(2*columns+1) for x in range(2*rows+1)] #创建一个(2*rows+1)*(2*columns+1)的二维数组
        for i in range(2*rows+1):
            for j in range(2*columns+1):
                if i%2==1 and j%2==1:
                    maze[i][j]= '[R]'  #创建原始迷宫所在点,在属于原始节点的位置上填写R
    #根据连接信息填写连接通道
        for i in range(len(cordinate)):
            row1 = cordinate[i][0]#第一个点的行坐标
            columns1 = cordinate[i][1]#第一个点的列坐标
            row2 = cordinate[i][2]#第二个点的行坐标
            columns2 = cordinate[i][3]#第二个点的行坐标
            delta1 = abs(row1 - row2) #行差值
            delta2 = abs(columns1  - columns2) #列差值
            if delta1 + delta2 > 1: #若两个点不相邻,则输出迷宫格式错误
                return "Maze format error"
            Row = (2*row1+1 + 2*row2+1) // 2 #取连通点的坐标，为两相邻两点的中间
            Columns = (2*columns1+1 + 2*columns2+1) // 2 #取连通点的坐标，为两相邻两点的中间
            if Row == 0 or Row == 2*rows or Columns==0 or Columns ==2*columns:#若联通点落在最外围墙壁上
                return "Maze format error"
            maze[Row][Columns] = '[R]'#对应位置的连通区域赋值
    #将二维数组转化为字符串
        final = ""
        for i in range(rows*2 + 1):
            final += " ".join(maze[i])+"\n"
        print(final)
maze =render_maze("3 3","0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1")
maze.render()
