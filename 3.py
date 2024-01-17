numbers={1:'One',2:'Two',3:'Three',4:'Four'}
num={i:j for i,j in numbers.items() if i%2==0}
print(num)