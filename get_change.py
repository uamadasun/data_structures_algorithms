# Uses python3
 
def get_change(m):
    num = 0
    if m >= 10:
    	num = m//10
    	m = m%10
    	if m >= 5:
     		num += m//5
     		m = m%5
     		num += m//1
     		m = m%1
    	else:
    		num += m//1
    	return num
    
    if m >=5 and m <10:
    	num = m//5
    	m = m%5
    	if m != 0:
    		num += m//1
    else:
    	num += m//1
 
    return num
 
m = int(input())
print (get_change(m))

