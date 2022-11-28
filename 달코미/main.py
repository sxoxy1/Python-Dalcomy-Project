import cake
print("*안녕하세요. 달코미 입니다.*")
order_list=[]
items = []
price=[]
check=[]

with open("paris_baguette.txt","r", encoding='euc-kr') as c:
    print(c.readline())


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

select=1

while True:  #while문을 통해 시스템 메뉴의 번호를 선택하였을때 그에 따른 함수 호출문들로 구성
    cake.menu()
    select = int(input("메뉴를 선택하세요 : "))
    if select ==1:  #1.주문을 하였을때 메뉴를 보여준 뒤 주문을 하고 주문 결과를 보여준다
        cake.order_menu(items,price)
        cake.order(items,price,order_list,check)
        cake.result(items,order_list)
    elif select ==0:  #0.종료를 하였을때 파일 입출력을 통해 쓰기 모드로 txt를 불러와 txt를 원래 txt대로
        print("종료합니다.")
        c=open("paris_baguette.txt","w")
        for i in range(len(items)):
            c.write(items[i]+",")
            c.write(str(price[i])+"\n")
        c.close()
        break
    elif select ==2:
        cake.menu_add(order_list,items,price)
    elif select ==3:
        cake.menu_del(order_list,items,price)
    elif select ==4:
        cake.check(items,check)
    elif select ==5:
        cake.check_add(items,check)
