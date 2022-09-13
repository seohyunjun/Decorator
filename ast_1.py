import ast
import ast
from fileinput import lineno
from ipaddress import collapse_addresses
ast.parse # 파이썬 코드를 포함하는 모든 문자열을 분석하고 _ast.Module 객체를 반환
# <function parse at 0x7fb9b5ccbca0> 

ast.parse("x = 42")
# <_ast.Module object at 0x7fb9b5d24070>

ast.dump(ast.parse("x = 42")) # 트리 시각화
# "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], 
# value=Constant(value=42, kind=None), type_comment=None)], 
# type_ignores=[])"

# Module['body'] \
#       Assign['Target', 'Value']
#           Target  \ 
#                   Name['ID','ctx'] \
#                       ID  \
#                               x
#                       ctx \
#                               Store         
#           Value   \ 
#                   Num['n']
#                       n   \
#                               42


compile(ast.parse("x = 42"), '<input>','exec')
# <code object <module> at 0x7fb9b47b5030, file "<input>", line 1>

# 파이썬은 기본으로 제공되는 함수 compile을 통해 exec, eval, single이 가능하다.

eval(compile(ast.parse("x = 42"),'<input>','exec'))

eval(compile(ast.parse("x = 421"),'<input>','exec')) 
## x = 42 동일 실행

x
# 42

# AST 활용
hello_world = ast.Str(s = 'hello world!',lineno=1, col_offset=1)
# str 선언

print_name = ast.Name(id = 'print',ctx=ast.Load(),lineno=1, col_offset=1)
# print 

print_call = ast.Call(func='print_name',ctx=ast.Load(),args=[hello_world], keywords=[],lineno=1, col_offset=1)
# func print

module = ast.Module(body=[ast.Expr(print_call, lineno=1, col_offset=1)],lineno=1, col_offset=1, type_ignores=[])
code = compile(module,'','exec')
eval(code)

# AST 탐색
import ast

class ReplaceBinOp(ast.NodeTransformer):
    """모든 이진 연산자를 더하기 연산자로 교체"""
    def visit_Binop(self,node):
        return ast.BinOp(left=node.left, op=ast.Add(),right=node.right)

tree = ast.parse("x = 1/3")
ast.fix_missing_locations(tree)
eval(compile(tree,'','exec'))

print(ast.dump(tree))
#Module(
    # body=[Assign(targets=
    # [Name(
    # id='x', ctx=Store())], 
    # value=BinOp(left=Constant(value=1, kind=None), 
    # op=Div(), right=Constant(value=3, kind=None)
    #       ), 
    # type_comment=None)], type_ignores=[]
    # )

print(x)
# 0.33333
del tree
tree = ast.parse('x = 1/3')

tree = ReplaceBinOp().visit(tree)
ast.fix_missing_locations(tree)
print(ast.dump(tree))eval(compile(tree,'','exec'))

print(x)

# Module(
    # body=[Assign(targets=[
        # Name(id='x', ctx=Store())], 
        # value=BinOp(left=Constant(value=1, kind=None),
        # op=Div(), right=Constant(value=3, kind=None)), 
        # type_comment=None)], type_ignores=[])

    