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

from code import interact
from email.policy import default
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


## 리스트 컴프리헨션
# listcomp 파이썬 리스트의 내용을 선언과 인라인으로 정의

x = [
    word.capitalize() 
    for line in ("hello world?", "or not")
    for word in line.split()
    if not word.startswith("or")
]
# 루프 대신 리스트 컴프리핸션을 사용하면 파이썬 리스트를 빠르고 깔끔하게 정의 가능

{x:x.upper() for x in ['hello','world']}
{x.upper() for x in ['hello','world']}

# 함수형, 함수, 함수화
## map()으로 각 항목에 함수 적용하기
## map() 함수는 형식 map(function, iterable)을 사용한다.
map(lambda x: x + 'bzz!',["I think","I'm good"])
# <map object at 0x1051444f0>

list(map(lambda x: x + 'bzz!',["I think","I'm good"]))

# filter()로 파이썬 리스트 필터링하기
# filter() 함수는 filter(function 또는 None, iterable) 형식을 사용하며 함수에서 반환된 결과에 따라 iterable 항목을 필터링한다. 

# map과 다르게 iteration의 항목을 추출
list(filter(lambda x: x.startswith("I "),["I think","I'm good"]))
# ['I think']

list(map(lambda x: x.startswith("I "),["I think","I'm good"]))
# a[True, False]
list(filter(lambda a: a,(1,2)))

# enumerate()로 인덱스 얻기
i = 0
mylist = [1,2,3]
while i < len(mylist):
    print("Item %d: %s" % (i, mylist[i]))
    i += 1

for i, item in enumerate(mylist):
    print("Item %d: %s" % (i, item))

# sorted()로 파이썬 리스트 정렬하기
## 정렬된 버전의 iterable을 반환한다.
## sorted(iterable, key=None, reverse=False)
sorted([("a",2),("c",1),("d",4)])
# [('a', 2), ('c', 1), ('d', 4)]
sorted([("a",2),("c",1),("d",4)],key=lambda x: x[1])
# [('c', 1), ('a', 2), ('d', 4)]

# any, all 조건을 충족하는 항목 찾기
def all(iterable):
    for x in iterable:
        if not x:
            return False
        
def any(iterable):
    for x in iterable:
        if x:
            return True
    return False

mylist = [0, 1, 3, -1]
if all(map(lambda x: x>0, mylist)): # all(map(lambda x: x>0, mylist)) False
    print("All times are greater than 0")
    
if any(map(lambda x: x>0, mylist)): # any(map(lambda x: x>0, mylist)) True
    print("All times are greater than 0")
    
# list() 와 zip() 결합하기
keys = ["foobar","barzz","ba!"]
map(len,keys) # <map object at 0x105233340>
list(zip(keys, map(len, keys))) # list set
dict(zip(keys, map(len,keys))) # dict 



# 간단한 코드로 항목 찾기 - 효율적인 코드 작성

# 첫번째 상수 찾기

# STEP1 비효율적인 방법 
list(filter(lambda x: x>0,[-1,0,1,2]))[0] # 빈 list 일 경우 IndexError가 발생 할 수도 있다.

## STEP2 효율적인 방법
next(filter(lambda x: x>0, [-1,0,1,2]))

a = range(10)
next(x for x in a if x > 3) # 조건이 충족되지 않으면 StopIteration

# 조건이 충족되지 않을때 기본값 반환하기
next((x for x in a if x>10),"default")

## first()를 사용해 조건에 일치하는 첫번쨰 요소 찾기
def first(iterable, default=None, key=None):
    """
    Return first element of `iterable` that evaluates true, else return None
    (or an optional default value).
    >>> first([0, False, None, [], (), 42])
    42
    >>> first([0, False, None, [], ()]) is None
    True
    >>> first([0, False, None, [], ()], default='ohai')
    'ohai'
    >>> import re
    >>> m = first(re.match(regex, 'abc') for regex in ['b.*', 'a(.*)'])
    >>> m.group(1)
    'bc'
    The optional `key` argument specifies a one-argument predicate function
    like that used for `filter()`.  The `key` argument, if supplied, must be
    in keyword form.  For example:
    >>> first([1, 1, 3, 4, 5], key=lambda x: x % 2 == 0)
    4
    """
    if key is None:
        for el in iterable:
            if el:
                return el
    else:
        for el in iterable:
            if key(el):
                return el

    return default

first([0, False, None, [], (), 42])
# 42
first([-1,0,1,2]) 
# -1

first([-1,0,1,2], key=lambda x: x>0)
# 1

# functools + lambda 
# lambda를 사용하지 않고 first구현  
import operator 

def greater_than_zero(number):
    return number > 0

first([-1,0,1,2], key=greater_than_zero) 

# lambda의 한계, 한 줄 이상의 코드가 필요하므로 key 함수를 전달 할 수 없다.
# key함수에 대해 새 함수를 정의하는 번거로운 패턴으로 바뀐다.

# functools에는 lambda에 대한 유연한 대안인 partial() 메서드가 있다.
# greater_than_zero 처럼 작동하는 새 함수 greater_than을 사용한다.
# 이 버전을 사용하면 숫자를 하드코딩하기 전에 비교할 값을 지정할 수 있다.
# 1. fuctools.partial()을 함수와 최솟값에 전달
# 2. 원하는대로 min 42를 설정한 새로운 함수를 다시 얻는다.
 
from functools import partial
# 두 숫자를 비교
# operator.le(a,b)는 두개의 숫자를 가져와 첫 번째 숫자가 두 번째보다 적거나 같은지 boolean 리턴 후 
# partial()에 반환 
first([-1,0,1,2], key=partial(operator.le,0))

## itertools 활용
# - accumulate  : iterable에서 누적된 아이템의 합계 반환
# - chain       : 모든 항목의 중간 파이썬 리스트를 작성하지 않고 여러 번 반복해서 사용 가능
# - combinations: 주어진 iterable에서 길이 r의 모든 조합을 생성
# - compress    : selectors에서 data에 boolean 마스크를 적용하고 selectors의 해당요소가 True인 data에서 값만 반환
# - count       : 끝없이 많은 시퀀스를 생성
# - cycle       : iterable 값에 대해 반복
# - repeat      : 요소를 n번 반복
# - dropwhile   : predicate가 False가 될 때까지 처음부터 순회 가능한 요소를 필터링
# - groupby     : keyfunc() 함수에서 반환된 결과에 따라 항목을 그룹화하는 이터레이터를 만든다.
# - permutations: 항목의 연속적인 r 길이 순열을 계속 반환
# - product     : 곱집합의 iterables를 반환, 중첩된 for 문을 사용하지 않고 반복할 수 있다.
# - takewhile   : 처음부터 predicate가 False가 될 때까지 순회 가능한 요소를 반환

import itertools
a = [{'foo': 'bar'},{'foo': 'bar','x':42},{'foo': 'baz', 'y':43}]
import operator
list(itertools.groupby(a, operator.itemgetter('foo')))
# [('bar', <itertools._grouper object at 0x10528d940>), ('baz', <itertools._grouper object at 0x10528d790>)]

[(key, list(group)) for key, group in itertools.groupby(a, operator.itemgetter('foo'))] 
# operator를 사용하면 연산자를 사용하지 않아도 된다.


