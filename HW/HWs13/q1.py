def print_btree(l, d):
    for i in l:
        put = ". " * d + str(i)
        if type(i) != list:
            print(put)
        else:
            print_btree(i,d+1)


print_btree([1,[[11,[111,112]],[12,[121,[122,[1221,1222]]]]]],0)
