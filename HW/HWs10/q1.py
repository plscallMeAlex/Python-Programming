from matplotlib.pyplot import pie, show

def pie_chart(inp):
    new = []
    count = []
    for i in inp:
        if i not in new:
            new.append(i)
    for i in new:
        a = inp.count(i)
        count.append(a )
    pie(count, labels=new)
    show()
    
pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3])