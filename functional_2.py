# 제너레이터
## Generator : 이터레이션처럼 작동하는 객체, StopIteration이 발생할 때까지 next() 메서드의 각 호출에 값을 생성하고 반환한다.

# 제너레이터를 만들려면 yield 문이 포함된 일반 파이썬 함수를 작성한다. 파이썬은 yield의 사용을 감지하고 함수에 태그를 붙인다. 인터프리터는 스택참조를 저장하고 next() 함수가 다시 호출될 때 함수의 실행을 다시 시작하도록 하는데 사용한다.

# 함수가 실행되면 실행 체인이 스택을 생성하며 함수 호출은 서로 스택으로 쌓인다. 함수가 반환되면 스택에서 제거되고 함수가 반환하는 값은 호출함수에 전달된다.
# 제너레이터는 함수가 실제로 반환되지 않고 대신 출력된다.
# 함수의 상태를 스택 참조로 저장하여 제너레이터의 다음 반복이 필요할 때 저장한 지점에서 제너레이터의 실행을 다시 시작한다.
 
# <제너레이터_1 : 세 번 반복으로 제너레이터 만들기>
def mygenerator():
    yield 1
    yield 2 
    yield 'a'
    
mygenerator
# <function mygenerator at 0x105257820>

g = mygenerator()

next(g)
# 1

next(g)
# 2 

next(g)
# 'a'

next(g)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# 제너레이터를 사용하지 않고 데이터를 반복할 때 전체 파이썬 리스트를 먼저 작성하면 메모리를 낭비한다.


# yield로 값 반환 및 전달
## yield 문은 함수 호출과 동일한 방식으로 값을 반환할 수 있다. yield 문으로 하면 send() 메서드를 호출하여 값을 제너레이터에 전달할 수 있다. send()를 사용하는 예로, 문자열 파이썬 리스트를 가져와서 동일한 문자열로 구성된 파이썬 리스트를 반환하는 shorten()이라는 함수를 작성한다.

def shorten(string_list):
    length = len(string_list[0]) # 10
    for s in string_list:
        length = yield s[:length]
        
        
mystring_list = ['loremipsum','dolorsit','ametfoobar']
shortstringlist = shorten(mystring_list)

result=[]
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(list(filter(lambda letter: letter in 'aeiou',s)))
        # 이전 실행 결과에 있는 모음 개수를 기준으로 
        # 이어지는 문자열 처리
        s = shortstringlist.send(number_of_vowels)
        result.append(s)        
except StopIteration:
    pass
print(result)

# yield 와 send()를 사용하면 couroutine처럼 작동할 수 있다.

(x.upper() for x in ['hello','world'])
# <generator object <genexpr> at 0x105251c10>

gen = (x.upper() for x in ['hello','world'])

list(gen)
# ['HELLO', 'WORLD']
# gen은 yield 문을 사용한 것처럼 제너레이터이다.
# 이 경우 yield가 되어있다.

# 제너레이터 검사하기
# 함수가 제너레이터로 고려할 수 있는지 확인하려면 inspect.isgeneratorfunction()를 사용한다.
import inspect
def mygenerator():
    yield 1

inspect.isgeneratorfunction(mygenerator)
# True

inspect.isgenerator(sum)
# False

# inspect 패키지는 제너레이터의 현재 상태를 보여주는 inspect.getgeneratorstate() 함수가 있다.

gen = mygenerator()
gen
# <generator object mygenerator at 0x105368820>
 
inspect.getgeneratorstate(gen)
#'GEN_CREATED' : 처음 실행을 기다리는 상태

next(gen)
# 1 

inspect.getgeneratorstate(gen)
# 'GEN_SUSPENDED' : 다음 호출로 다시 시작되기를 기다림

next(gen)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

inspect.getgeneratorstate(gen)
# 'GEN_CLOSED' : 실행 완료

## 제너레이터를 디버깅하는데 유용하다
