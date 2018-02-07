def totalavge():
    result = []  #用于存放处理后的结果
    with open('report.txt','r') as f:
        for line in f.readlines():  #逐行读取数据
            l = line.split()   #将每一行字符串转化为列表
            total = 0  #总成绩
            subject = 0  #科目数
            for score in l[1:]: #遍历列表l内的数字
                subject += 1
                total += int(score)
                avge = float(total/subject)
                avg = '%.1f'%avge
            l.append(str(total)) #将该同学的总成绩存进他的成绩列表中
            l.append(str(avg)) #将平均分存进列表
            result.append(l) #将新的个人成绩列表存入结果列表
        result.sort(key=lambda x:x[-2],reverse=True) #按平均分由高到低排序
        return result


def eachavge():
    each_avge = ['0','平均']#用于将每科平均分存进列表
    result = totalavge() #获取结果列表
    for x in range(1,10):
        each_total = 0
        num = 0
        for y in result:
            num += 1
            each_total += int(y[x])
            avge1 = float(each_total/num)
            avge2 = '%.1f'%avge1
        each_avge.append(str(avge2))
    #each_avge.insert(1,'平均')
    result.insert(0,each_avge)
    return each_avge,result

def sort():
    head = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
    each_avge,result = eachavge()#获取result列表数据
    p = 0
    for i in result[1:]:#遍历列表中数据（行）
        p += 1
        i.insert(0,str(p)) #在每行0位子添加序号
        count = 2 #从第二列开始筛查
        for j in i[2:-2]:#遍历每一行的分数
            if int(j) < 60:#判断是否小于60分
                i[count] = '不及格'
                count += 1 #下次从下一列开始筛查
            else:
                count += 1
    result.insert(0,head)
    return result

def newFile():
    result = sort()
    file = open('newcores.txt','w')
    for i in result:
        file.writelines('\n')
        for j in i:
            res = '%s\t\t'%j
            file.writelines(res)

newFile()    
    
                

