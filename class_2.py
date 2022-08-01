# print 함수를 래핑해 세션에서 호출된 횟수 확인
# 함수를 class로 래핑
class CountCalls(object):
    def __init__(self,f):
        self.f = f
        self.called = 0
        
    def __call__(self, *args, **kwargs):
        print('*args',args)
        print('*kwargs',kwargs)
        self.called += 1
        return self.f(*args, **kwargs)
@CountCalls
def print_hello():
    print('hello')
    

print_hello.called # 0
print_hello() # hello
print_hello.called # 1
print_hello() # hello
print_hello.called # 2
