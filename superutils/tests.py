# -*- coding: utf-8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2016-07-21
'''

from superutils import print_obj

def super_test():
    for obj in [int, str, float, list, set, dict]:
        print_obj(obj, full=True)
    print_obj(lambda x: x, inner=True)
    
if __name__ == '__main__':
    super_test()
