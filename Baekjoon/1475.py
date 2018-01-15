# -*- coding: utf-8 -*-
#Exercise 1475
roomNum = raw_input()
'''
    다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
    다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최소값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

    방번호 N 은 1,000,000 보다 작거나 같은 범위.

    >> collection module 의 Counter 함수를 사용해도 풀 수 있지만, Non library 로 해결 가능.
    >> 6,9 가 총 몇번 나오는지 갯수를 카운팅하면 쉽게 해결할 수 있다.
        >> 6,9는 서로 바꿔 사용할 수 있기 때문에 6과 9의 총 갯수가 나머지 수 중 최고 갯수의 값 보다 작은 경우, 큰 경우로 나눠 해결할 수 있다.
        >> 예외처리 항목에 주의할 것.
'''
#get 6,9 count
chkNum = roomNum.count('6') + roomNum.count('9')
max = 0
for i in "01234578":
    if (max < roomNum.count(i)):
        max = roomNum.count(i)
if (chkNum/2 < max):
    print max
else:
    if (chkNum%2 == 1):
        print chkNum/2+1
    else:
        print chkNum/2
