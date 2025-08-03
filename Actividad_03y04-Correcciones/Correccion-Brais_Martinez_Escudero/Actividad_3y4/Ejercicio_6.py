def max_value(ls,rs):
    for l in ls:
        if type(l) == list:
            rs = max_value(l,rs)
            continue
        if l > rs:
            rs = l
    return rs

def max_val(ls):
    rs = max_value(ls,0)
    return rs

def main():
    list1 = [4,1,3,11,[1,6,8],[[1,3],[6,15]]]
    list2 = [5,[5,7,9,2],3,[2,6,16],9]
    result1 = max_val(list1)
    result2 = max_val(list2)
    print('list1:%r\nMAX:%s\nlist2:%r\nMAX:%s' %(list1,result1,list2,result2))

main()