total_charge=0
total_order=[]

def menu():
    print()
    print("시스템 메뉴\n 1.주문\n 2.메뉴 추가\n 3.메뉴 삭제\n 4.재고 확인\n 5.재고 추가\n 0. 종료 \n")

def oeder_menu(items,price):
    print("주문 메뉴는 다음과 같습니다.")
    for i in range(len(items)):  #for 문을 통해 케이크의 개수만큼 반복
        print(str(i+1)+".",items[i],price[i],"원")  #'1.케이크 0000원' 출력
        print("0. 주문 종료")  #0번 버튼을 눌렀을때 종료되는 것을 알려주는 출력문

def order(items,price,order_list,check):
    global total_charge
    while True:  #while문을 통해 주문 메뉴의 번호를 sel에 받아 드림
        sel=int(input("주문하실 메뉴는? : "))
        if sel ==0:  #0일때 주문을 종료하기위해서 break를 통해 while문을 탈출
            print("주문을 종료합니다.")
            break
        elif sel >len(items):  #주문 번호가 음료의 번호보다 많을 때는 없느느 번호임으로 잘못 주문했다는 문장을 출력하였다.
            print("잘못 주문하셨습니다.")
        elif sel <= len(items):  #주문 번호가 제대로 입력되었을때, 
            if check[sel-1]==0:  #음료의 재고를 확인하기 위해서 if문을 통해 재고의 개수가 0일때는 재고가 없다는 출력문을 내보냄
                print("재고가 없습니다.")
            else:  #그러지 않을때
                total_charge += price[sel-1]  #총 가격을 구하기 위해 total_charge에 음료 가격을 지정하고
                order_list[sel-1] +=1  #음료 개수를 저장
                check[sel-1] -= 1  #재고를 하나 뺌

def menu_add(order_list,items,price):
    print("현재 메뉴:",items)
    add_item=input("추가하실 메뉴: ")
    if(add_item not in items):   #기존에 존배하는 메뉴인지 검사하기 위해 if문을 사용
        items.append(add_item)   #메뉴 추가 기능을 구현하기 위해 items 리스트에 추가할 메뉴와 가격을 append 함수를 통해 입력
        order_list.append(0)
        price.append(int(input("가격 : ")))
    else:
        print("존재하는 메뉴 입니다.")

def menu_del(order_list,items,price):
    print("현재 메뉴: ", items)
    del_item =input("삭제하실 메뉴: ")
    if(del_item in items):  #기본에 존재하는 메뉴인지 검사하기 위해 if문 사용
        index=items.index(del_item)  #메뉴 삭제 기능을 구현하기 위해 items 리스트에 삭제한 메뉴를 pop 함수를 통해 메뉴와 가격, 주문 개수를 삭제
        print(items.pop(index), "을/를 삭제합니다")
        print.pop(index)
        order_list.pop(index)
    else:
        print("존재하지 않는 메뉴 입니다.")

def check_add(items,check):
    for i in range(len(items)):  #재고 추가 기능을 구현하기 위해 for문을 통해 음료의 개수 만큼 반복
        print(items[i],end="")
        add=int(input("의 추가 개수: "))
        check[i] += add  #추가 개수를 add에 입력하여 check(재고)에 저장

def result(items,order_list):
    print("총 주문하신 케이크는")
    for i in range(len(order_list)):  #총 주문한 케이크를 for문을 통해 주문 개수 만큼 반복
        if order_list[i] !=0:  #주문개수가 0개가 아닐 때, 
            print(items[i],":",order_list[i],"개",end="")  #케이크의 리스트 순서대로 '케이크:0ㅐ'으로 출력되게 하였다.
        order_list[i]=0  #주문 개수가 0개일때는 케이크 개수를 출력하지 않도록 하였다
    print()
    print("총 금액은", total_charge,"원 입니다. \n 감사합니다")    






           

