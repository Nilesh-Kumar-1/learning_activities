def isHappy(n: int) -> bool:
        check_loop=set()
        while n not in check_loop:
            check_loop.add(n)
            print(n,n not in check_loop)
            n = square(n)
            if n == 1:
                return True
        return False
def square(val):
        result=0
        while val != 0:
            digit = val%10
            result += digit**2
            val= val//10
        return result
    
print(isHappy(19))