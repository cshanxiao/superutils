# -*- coding: utf-8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2016-07-18
'''
import time


def print_obj(obj, inner=True, full=False):
    print "\nStart {} {}".format(obj, "=" * 50)
    print "dir info: {}".format(dir(obj))
    
    for attr in dir(obj):
        try:
            if attr.startswith("__") and not full:
                continue
            
            if attr.startswith("_") and not inner:
                continue

            attr_value = getattr(obj, attr)
            if "method" in str(type(attr_value)):
                print "### method {}".format(attr)
            elif "wrapper" in str(type(attr_value)):
                print "=== wrapper {}".format(attr)
            else:
                print "--- attribute {}: {}".format(attr, attr_value)
        except Exception, e:
            print "*** read error {}: {}".format(attr, e)
    print ("End {} {}").format(obj, "=" * 50)

def func_time(func):
    _id = [0]
    def _wrapper(*args,**kwargs):
        start_time = time.time()    
        result = func(*args,**kwargs)
        end_time = time.time()
        _id[0] += 1
        print "{} [{}] [{:.3f} ms] {}".format(
            _id[0],
            time.strftime("%Y-%m-%d %H:%M:%S"), 
            (end_time - start_time) * 1000,
            {"func_name": func.func_name,
             "file_name": func.func_code.co_filename,
             "file_lineno": func.func_code.co_firstlineno
            }
            )
        return result
    return _wrapper

def super_test():
    print_obj(str, full=True)
    print_obj(lambda x: x, inner=True)
    
if __name__ == '__main__':
    super_test()

