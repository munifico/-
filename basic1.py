def Buymanual(Money, CurValue, MySto):
    # 정확한 숫자를 입력할 때까지 try -> except 예외구문 적용
    while True:
        try:
            Amount = int(input("주식을 몇 주 구입하시겠습니까? : "))
            # 입력받은 값이 본인이 가진 돈 보다 많은지 확인
            if (Money - Amount * CurValue) >= 0:
                break  # 본인이 가진 돈으로 충분히 살 수 있다면 구매 진행
            else:
                print("본인이 가진 돈 보다 많은 돈을 가질 수 없습니다.")
        except ValueError:  # 예외처리 - 문자를 입력받을 경우
            print("숫자만 입력해주세요")

    print(Amount, "주를 구매하였습니다.")
    Money = Money - Amount * CurValue # 주식 구매한 만큼 현재 돈이 줄어듦
    MySto = MySto + Amount            # 주식 구매한 만큼 현재 주식 보유량 증가
    return [Money, MySto]

def Sellmanual(Money, CurValue, MySto):
    # 정확한 숫자를 입력할 때까지 try -> except 예외구문 적용
    while True:
        try:
            Amount = int(input("주식을 몇 주 판매하시겠습니까? : "))
            # 입력받은 양이 본인이 가진 주식 양보다 많은지 적은지 확인
            if (MySto - Amount) >= 0:
                break  # 본인이 가진 주식의 양보다 같거나 적을 경우 판매 진행
            else:
                print("본인이 가진 주식 보다 많은 주식을 팔 수 없습니다.")
        except ValueError:  # 예외처리 - 문자를 입력받을 경우
            print("숫자만 입력해주세요")

    print(Amount, "주를 판매하였습니다.")
    Money = Money + Amount * CurValue
    MySto = MySto - Amount
    print(Money, "원을 가지고 있습니다.")
    return [Money, MySto]

# 주식 단가 조절을 위한 random 라이브러리 임포트
from random import *

# 주식 거래 프로그램에 필요한 변수들 초기 정의
day=0              # 주식 거래일
mymoney=100000     # 내 잔액
mystock=0          # 내 주식 보유량
stock=5000         # 현재 주식 가격

# 주식 시작 개장 전 프로그램 시작을 알리는 문구
print("----------------------------주식 시장을 개장하겠습니다.----------------------------")
print("초기 주식 가격은",stock ,"원 이고 초기 자본금은", mymoney, "입니다.")

# 주식 거래 무한루프 시작
while True:

    # 시작할 때 1일 추가
    day += 1

    # 주식 거래를 위한 현재 내상태 표시
    print("----------------------", day, "일 째 입니다.----------------------")
    print("당신의 주식 보유량은", mystock, "주 이고, ", mymoney, "원을 보유하고 있습니다.")
    print("오늘 주식 가격은 한 주에", stock, "원 입니다.")
    
    # 주식 거래할지 말지 입력받기 - 제대로 된 값을 입력받을 때까지 무한시공
    while True:
        q = input("주식을 살 지(B), 팔 지(S), 넘어갈 지(P), 끝낼 지(X) 결정하세요 : ")
        if q == 'B' or q == 'b':
            break
        elif q == 'S' or q == 's':
            break
        elif q == 'P' or q == 'p':
            break
        elif q == 'X' or q == 'x':
            break
        else: # 이 외에 입력값을 입력 받은 경우
            print("무엇을 할 지 제대로 입력해 주세요")
            
    # 주식 구매를 원할 경우
    if q == 'B' or q == 'b':
        [mymoney, mystock] = Buymanual(mymoney, stock, mystock) # 주식 매매 함수를 불러온다
    # 주식 판매를 원할 경우
    elif q == 'S' or q == 's':
        [mymoney, mystock] = Sellmanual(mymoney, stock, mystock) # 주식 매매 함수를 불러온다
    # 내일 주식 시장으로 넘어갈 경우
    elif q == 'P' or q == 'p':
        print("오늘은 넘어가겠습니다.")
    # 주식 시장 종료를 원할 경우
    elif q == 'X' or q == 'x':
        print("** 주식 시장을 종료하겠습니다.")
        print("** 최종 수익은", mymoney - 100000)
        break

    # 주식가격 랜덤으로 설정
    stock = stock + randint(-1000,1000)
    stock = stock + randint(-100,100)
    stock = stock + randint(-10,10)

    # 프로그램 종료 조건 확인하기
    if mymoney > 1000000:               # 주식으로 100만원을 벌었을 경우 프로그램 종료
        print("부자가 되었습니다.")
        break
    elif mymoney < 0:                   # 주식으로 전재산을 날릴 경우 프로그램 종료
        print("그지가 되었습니다.")
        break
    elif stock < 0:                     # 주가가 0원 이하가 될 경우 프로그램 종료
        print("주식이 종이가 되었습니다.")
        break