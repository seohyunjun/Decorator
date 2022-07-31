# 데코레터 사용 법

def identify(f):
    return f


# ---- Ex
@identify
def foo():
    return 'bar'

# ---- same 
foo = identify(foo)
foo # <function foo at 0x104472af0>
foo() #'bar'
