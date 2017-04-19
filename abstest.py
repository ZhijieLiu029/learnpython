PI = 3.1415926

# define my abs function
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
# define a empty function
def nop():
    pass
#============================================
