def menu():
    print()
    print("시스템 메뉴\n 1.주문\n 2.메뉴 추가\n 3.메뉴 삭제\n 4.재고 확인\n 5.재고 추가\n 0. 종료 \n")

def oeder_menu(items,price):
    print("주문 메뉴는 다음과 같습니다.")
    for i in range(len(items)):  #for 문을 통해 케이크의 개수만큼 반복
        print(str(i+1)+".",items[i],price[i],"원")  #'1.케이크 0000원' 출력
        print("0. 주문 종료")  #0번 버튼을 눌렀을때 종료되는 것을 알려주는 출력문



