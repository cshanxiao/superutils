# -*- coding: utf-8 -*-
u'''
@summary:
@author: cshanxiao
@date: 2016-07-18
'''
import time


def print_obj(obj, inner=True, full=False, detail=False):
    print "\n{} Start {} {}".format("=" * 16, obj, "=" * 16)
        
    attributes = []
    methods = []
    wrappers = []
    unkonws = []
    for attr in dir(obj):
        try:
            if attr.startswith("__") and not full:
                continue
            
            if attr.startswith("_") and not inner:
                continue

            attr_value = getattr(obj, attr)
            if "method" in str(type(attr_value)):
                methods.append([attr, attr_value.__doc__])
            elif "wrapper" in str(type(attr_value)):
                wrappers.append([attr, attr_value.__doc__])
            else:
                attributes.append((attr, attr_value))
                
        except Exception, e:
            unkonws.append((attr, e))
    
    attributes.sort()
    methods.sort()
    wrappers.sort()
    unkonws.sort()
    
    for attr, attr_value in attributes:
        print "--- attribute {}: {}".format(attr, attr_value)
    
    for attr, doc in methods:
        if detail:
            print "### method {}: {}".format(attr, doc)
        else:
            print "### method {}".format(attr)
    
    for attr, doc in wrappers:
        if detail:
            print "=== wrapper {}: {}".format(attr, doc)
        else:
            print "=== wrapper {}".format(attr)
    
    for attr, e in unkonws:
        print "*** unkonw {}: {}".format(attr, e)
    
    print "\n{} dir {}".format("*" * 20, "*" * 20)
    attrs = dir(obj)
    for index, attr in enumerate(attrs, 1):
        if index == len(attrs):
            print "{}\n".format(attr),
            break
        print "{},".format(attr),
        if index % 4 == 0:
            print "\n",
            
    print "\n{} End {} {}".format("=" * 16, obj, "=" * 16)

def func_time(func):
    _id = [0]
    def _wrapper(*args, **kwargs):
        start_time = time.time()    
        result = func(*args, **kwargs)
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



