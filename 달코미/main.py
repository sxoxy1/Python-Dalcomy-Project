import cake
print("*안녕하세요. 달코미 입니다.*")
order_list=[]
items = []
price=[]
check=[]

c=open("paris_baguette.txt","r")

for line in c.readlines():   #for문을 통해 txt파일을 한줄씩 읽어드림(readlines)
    line=line.strip()   #strip을 동해 첫 부분과 끝 부분의 공백과 ',' 문자를 제거
    parts=line.strip()
    parts=line.split(",")
    order_list.append(0)
    items.append(parts[0])  #첫번째 문자(케이크)를 items 리스트에 입력
    #가격과 재고는 숫자이므로 int를 통해 실수로 반환
    price.append(int(parts[1]))  #두번째 문자(가격)를 price 리스트에 입력
    check.append(int(parts[2]))  #세번째 문자(재고)를 check 리스트에 입력
    
c.close()