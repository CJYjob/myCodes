# 현재 시간을 불러와 2022.12.02 02:05:35 형태 str으로 가져옴
import datetime
dt_now = datetime.datetime.now()
dt_now_str = dt_now.strftime('%Y.%m.%d %H:%M:%S')

# 디버깅 로그
#   파라미터
#       log : 디버깅 내용 입력
#       filename : 호출 시 __name__으로 파일 이름 전달받음
#   처리
#       현재 시간, 호출 파일, 로그 내용 출력
#   반환
#       없음
def debug(log, filename) :
    print(dt_now_str, filename, log)