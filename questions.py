import cv2
from playsound import playsound

def img_show(file, dur):
    cv2.imshow(file, cv2.imread(file))
    cv2.waitKey(dur*1000)

def q1():
    q = 'Q1. 뽀귀와 호구가 사귄 날은?'
    a1 = '1) 2012년 12월 5일'
    a2 = '2) 2020년 5월 12일'
    a3 = '3) 2019년 5월 14일'
    a4 = '4) 2019년 5월 12일'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    while ans != '4':
        ans = input('ans: ')
        if ans != '4':
            print('뽀귀? 빵귀..')
        else:
            print('뽀귀야? ㅇ3ㅇ 축하해요~~ ㅇ3ㅇ')
            break

def q2():
    q = 'Q2. 이 사진은 2019년 5월 27일, 난지의 공원에서 찍힌 사진입니다. 사진 속 뽀귀는 어두운 시간까지 무엇을 열심히 보고 있었을까요?'
    a1 = '1) 인스타그램 스토리'
    a2 = '2) 베트남 여행 정보'
    a3 = '3) 시그널'
    a4 = '4) WWW'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    img_show('img/q2_1.JPEG', 5)
    img_show('img/q2_2.JPEG', 5)
    while ans != '3':
        ans = input('ans: ')
        if ans != '3':
            print('뽀귀? 빵귀..')
        else:
            print('시그널 보다가 어두워졌어 ㅇㅅㅇ')
            break
    img_show('img/q2_3.JPEG', 5)
    cv2.destroyAllWindows()

def q3():
    q = 'Q3. 뽀귀가 옴총 좋아하고 있습니다. 샹그리아가 맛있었던 집으로 기억하는데, 어디일까요?'
    a1 = '1) 정자동 호놀룰루'
    a2 = '2) 청담 스케줄'
    a3 = '3) 변귀네 식당'
    a4 = '4) 을지로 파스타'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    img_show('img/q3_1.jpg', 5)
    img_show('img/q3_2.jpg', 5)
    while ans != '3':
        ans = input('ans: ')
        if ans != '3':
            print('뽀귀? 빵귀..')
        else:
            print('우리 백일~~~')
            break
    img_show('img/q3_3.jpg', 5)
    cv2.destroyAllWindows()


def q4():
    q = 'Q4. 뽀귀야아아~~ 뽀귀가 좋아하는 사진 중 하나입니다. 2019년 10월 12일에 우리가 했던 것은?'
    a1 = '1) 도림천 산책 하다가 운동하기'
    a2 = '2) 자전거 타고 도림천 달리다가 핑크뮬리 보기'
    a3 = '3) 탄천 드라이브'
    a4 = '4) 문래동 공원 런닝하다가 배아파서 병원 가기'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    img_show('img/q4_1.JPG', 5)
    while ans != '2':
        ans = input('ans: ')
        if ans != '2':
            print('뽀귀? 빵귀..')
        else:
            print('갑자기 근처에서 핑크뮬리를 만난 날')
            break
    img_show('img/q4_2.JPG', 5)
    cv2.destroyAllWindows()

def q5():
    q = 'Q5. 우리는 사귀는 동안 제주도를 3번 다녀왔습니다. 다음 중 제주도와 관련이 없는 것은?'
    a1 = '1) 씽씽이 타다가 깜귀 되기'
    a2 = '2) 동백나무 정원에서 프사 찍기'
    a3 = '3) 1시간 유람선 타기'
    a4 = '4) 새빌 오름에서 놀다가 갑자기 내가 아프기ㅠ'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    while ans != '3':
        ans = input('ans: ')
        if ans != '3':
            print('뽀귀? 빵귀..')
        else:
            print('유람선은 가평이랑 여수~')
            print('2019년 겨울 카멜리아힐에서 우리의 첫 제주')
            print('2020년 여름 씽씽이 두시간 탔던 날')
            print('2021년 가을 백신 맞고 몸이 안좋았던 여행')
            break
    img_show('img/q5_1.JPG', 5)
    img_show('img/q5_2.jpg', 5)
    img_show('img/q5_3.jpg', 5)
    cv2.destroyAllWindows()

def q6():
    q = 'Q6. 뽀귀? 거의 다 왔어. 조금만 더 힘을 내요.\n이 사진은 내가 좋아하는 영상 중 하나인데요. 뽀귀가 무엇을 하고 있었을까요?'
    a1 = '1) 카트라이더 러시플러스 NPC 사이에서 1등 하기'
    a2 = '2) 터뜨리기 중독귀'
    a3 = '3) 유투브 보기'
    a4 = '4) 틀린그림 찾기'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    img_show('img/q6_1.jpg', 5)
    img_show('img/q6_2.jpg', 5)
    # playsound('img/youtube.mp3')
    while ans != '1':
        ans = input('ans: ')
        if ans != '1':
            print('뽀귀? 빵귀..')
        else:
            print('NPC 없으면 꼴등~~')
            # playsound('img/npc.mp3')
            break
    cv2.destroyAllWindows()

def q7():
    q = 'Q7. 2021년 7월 31일 한 여름날 사진입니다. \n뽀귀가 공부하는 호구를 위해 음식 선택지를 준비했습니다. 남은 메뉴 중 호구가 가장 먼저 선택한 메뉴는?'
    a1 = '1) 광화문 미진이'
    a2 = '2) 고귀리 막국수'
    a3 = '3) 떡만두국'
    a4 = '4) 유부초밥+김치우동'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    img_show('img/q7_1.JPG', 5)
    while ans != '2':
        ans = input('ans: ')
        if ans != '2':
            print('뽀귀? 빵귀..')
        else:
            print('앞으로 호랑이 타고 직접 자주 맛집에 가서 맛있는 걸 먹어요')
            break
    img_show('img/q7_2.JPG', 5)
    cv2.destroyAllWindows()

def q8():
    q = 'Q8. 뽀귀가 깜짝 놀랐습니다. 대체 무슨 일이 있었을까요?'
    a1 = '1) 뽀집에 호구가 자고 있는 줄 알았는데 집에 가버렸다'
    a2 = '2) 가방 속에서 생일 선물로 입생로랑 지갑을 발견했다'
    a3 = '3) 푸라다 호보백'
    a4 = '4) 푸라닭 치킨'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    img_show('img/q8_1.JPG', 5)
    while ans != '3':
        ans = input('ans: ')
        if ans != '3':
            print('뽀귀? 빵귀..')
        else:
            print('뽀귀는 선물 있는 줄도 모르고 새벽까지 술마시고 놀다가 들어갔어..')
            break
    img_show('img/q8_3.jpg', 4)
    img_show('img/q8_2.JPG', 4)
    cv2.destroyAllWindows()

def q9():
    q = 'Q9. 테이블 위의 떡만두국은 이런 날이 오면 내가 꼭 준비해주고 싶던 음식입니다.\n뽀귀를 결혼하고 싶은 귀신이라고 느꼈던 일이라서요.\n그때 만두국을 먹고 갔던 산 이름이 무엇일까요?'
    a1 = '1) 관악산'
    a2 = '2) 인왕산'
    a3 = '3) 안산'
    a4 = '4) 청계산'
    print(q)
    print('{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
    ans = 0
    while ans != '4':
        ans = input('ans: ')
        if ans != '4':
            print('뽀귀? 빵귀..')
        else:
            print('2020년 4월 12일 그날에 감동 받았던 떡만두국이야.')
            img_show('img/q9_2.jpg', 5)
            img_show('img/q9_1.jpg', 5)
            cv2.destroyAllWindows()
            break
    

if __name__ == '__main__':
    pass