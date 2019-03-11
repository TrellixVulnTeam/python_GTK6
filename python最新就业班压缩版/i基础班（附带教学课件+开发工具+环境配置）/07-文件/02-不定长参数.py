def test(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


# 33,44,55,66,77,88这种没有名字的参数 会传给*args
# mm=11,nn=44 这种没名字的参数会传给**kwargs
test(11,22,33,44,55,66,77,88,99,mm=11,nn=44)


A = [11,22,33]
B = {"aa":100, "bb":200}

#当列表/元组在当做实参传递的时候，如果前面有一个*，表示对其进行解包
#意思是：[111,222,333]----->111,222,333
#当字典当做一个实参进行传递的时候，如果前面有两个*，表示对其进行解包
#意思是：{"aa":100,"bb":200}----->aa=100,bb=200
test(11,22,*A,**B)#等价于 test(11,22,11,22,33,aa=100,bb=200)


# 打印
# 11
# 22
# (11, 22, 33)
# {'aa': 100, 'bb': 200}
