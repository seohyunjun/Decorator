# function 
_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] =f
    return f

@register
def foo():
    return 'bar'

foo # <function foo at 0x104472d30>
_functions['foo'] # <function foo at 0x104472d30>

# register save function 'foo' 