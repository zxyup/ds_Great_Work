

MAX= float('inf')

matrix = [
    [0,10,MAX,4,MAX,MAX],
    [10,0,8,2,6,MAX],
    [MAX,8,10,15,1,5],
    [4,2,15,0,6,MAX],
    [MAX,6,1,6,0,12],
    [MAX,MAX,5,MAX,12,0]
    ]

arc=[[0,42,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,25],       #二期运动场
     [42,0,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX],       #信院院楼
     [MAX,MAX,0,35,MAX,45,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,40,40,MAX,44],       #生科院楼
     [MAX,MAX,35,0,62,MAX,MAX,MAX,MAX,MAX,30,MAX,MAX,42,25,MAX,MAX,MAX],       #教学楼群
     [MAX,MAX,MAX,62,0,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,24,60,MAX,32,MAX],      #电院院楼
     [MAX,MAX,45,MAX,MAX,0,35,30,MAX,MAX,25,MAX,MAX,MAX,MAX,MAX,MAX,MAX],       #航院院楼
     [MAX,MAX,MAX,MAX,MAX,35,0,12,26,MAX,MAX,40,MAX,MAX,MAX,MAX,MAX,MAX],       #体育馆
     [MAX,MAX,MAX,MAX,MAX,30,12,0,MAX,MAX,39,MAX,40,MAX,MAX,MAX,MAX,MAX],       #游泳馆
     [MAX,MAX,MAX,MAX,MAX,MAX,26,MAX,0,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX],        #新工科大楼
     [MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,0,MAX,MAX,30,30,MAX,MAX,20,MAX],      #一期运动场
     [MAX,MAX,MAX,30,MAX,25,MAX,39,MAX,MAX,0,MAX,35,MAX,MAX,MAX,MAX,MAX],           #小巨蛋
     [MAX,MAX,MAX,MAX,MAX,MAX,40,MAX,MAX,MAX,MAX,0,MAX,MAX,MAX,MAX,MAX,21],          #三期站台
     [MAX,MAX,MAX,MAX,MAX,MAX,MAX,40,MAX,30,35,MAX,0,40,MAX,MAX,MAX,MAX],         #一期站台
     [MAX,MAX,MAX,42,24,MAX,MAX,MAX,MAX,30,MAX,MAX,40,0,MAX,MAX,28,MAX],         #能源学院
     [MAX,MAX,40,25,60,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,0,MAX,MAX,MAX],           #南大门
     [MAX,MAX,40,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,0,MAX,MAX],          #动物中心
     [MAX,MAX,MAX,MAX,32,MAX,MAX,MAX,MAX,20,MAX,MAX,MAX,28,MAX,MAX,0,MAX],             #东门
     [25,MAX,44,MAX,MAX,MAX,MAX,MAX,MAX,MAX,MAX,21,MAX,MAX,MAX,MAX,MAX,0]]           #二期站台


def dijkstra(matrix, start_node):
    
    #矩阵一维数组的长度，即节点的个数
    matrix_length = len(matrix)

    #访问过的节点数组
    used_node = [False] * matrix_length

    #最短路径距离数组
    distance = [MAX] * matrix_length

    #初始化，将起始节点的最短路径修改成0
    distance[start_node] = 0
    
    #将访问节点中未访问的个数作为循环值，其实也可以用个点长度代替。
    while used_node.count(False):
        min_value = float('inf')
        min_value_index = 999
        
        #在最短路径节点中找到最小值，已经访问过的不在参与循环。
        #得到最小值下标，每循环一次肯定有一个最小值
        for index in range(matrix_length):
            if not used_node[index] and distance[index] < min_value:
                min_value = distance[index]
                min_value_index = index
        
        #将访问节点数组对应的值修改成True，标志其已经访问过了
        used_node[min_value_index] = True

        #更新distance数组。
        #以B点为例：distance[x] 起始点达到B点的距离，
        #distance[min_value_index] + matrix[min_value_index][index] 是起始点经过某点达到B点的距离，比较两个值，取较小的那个。
        for index in range(matrix_length):
            distance[index] = min(distance[index], distance[min_value_index] + matrix[min_value_index][index])

    print(distance)



# start_node = int(input('请输入起始节点:'))
for i in range(len(arc)):
    dijkstra(arc,i)
