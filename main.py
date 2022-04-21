import time
from questions import *

intro = '''
>>>>
오늘은 뽀귀에게 프로포즈가 진행되는 날입니다.
뽀귀는 지금부터 나타나는 퀴즈를 모두 풀어야만 프로포즈 선물을 받을 수 있습니다.
집중해서 풀어보세요. ㅇㅃㅇ
>>>>

"ans: " 가 나타나면 숫자로 정답을 입력할 수 있습니다.
"ans: "가 나타나기 전부터 답을 입력하지 마세요.
사진을 천천히 살펴보고 신중하게 입력하세요.
'''

ending = '''
편지
만둣국

'''


def wait(sec):
    for _ in range(sec):
        print('**********'*3)
        time.sleep(1)

if __name__ == '__main__':
    print(intro)
    wait(3)
    time.sleep(5)
    q1()
    wait(2)
    q2()
    wait(2)
    cv2.destroyAllWindows()
    q3()
    wait(2)
    cv2.destroyAllWindows()
    q4()
    cv2.destroyAllWindows()
    wait(2)
    q5()
    cv2.destroyAllWindows()
    wait(2)
    q6()
    wait(2)
    cv2.destroyAllWindows()
    q7()
    wait(2)
    cv2.destroyAllWindows()
    q8()
    wait(2)