# from Qt_class import a

MAX=float('inf')
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


def dijk(arc,spoint,epoint):
    global a
    l=len(arc)
    flag=[False]*l
    dist=[MAX]*l
    dist[spoint]=0
    rout=[[] for i in range(l)]
    while flag.count(False):
        min=MAX
        min_i=l+1

        for i in range(l):
            if not flag[i] and dist[i] < min:
                min = dist[i]
                min_i = i

        if min_i == epoint:
            # print(rout[epoint])
            return rout[epoint]

        flag[min_i]=True

        for i in range(l):
            if dist[min_i]+arc[min_i][i] < dist[i]:
                # print(i)
                dist[i]=dist[min_i]+arc[min_i][i]
                rout[i]=rout[i]+rout[min_i]
                rout[i].append(i)
                # print(rout[i])

        # print(dist)
if __name__ == 'main':
    dijk(arc,11,16)