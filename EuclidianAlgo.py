print("Input two non-negative integers a and b such that a>=b")
a,b= map(int, input().split())
x,y=a,b # Store temporarily

while b>0:
 r=a%b
 a=b
 b=r
print(f"gcd({x},{y})={a}")