# 현재 시간을 불러와 2022.12.02 02:05:35 형태 str으로 가져옴
import datetime
dt_now = datetime.datetime.now()
dt_now_str = dt_now.strftime('%Y.%m.%d %H:%M:%S')

'''
디버깅 로그
    파라미터
        log : 디버깅 내용 입력
        filename : 호출 시 __name__으로 파일 이름 전달받음
    처리
        현재 시간, 호출 파일, 로그 내용 출력
        용법 : if debug_flag in range(low, high+1) : debug(f'log', __name__)
            중요한 log에 넓은 범위(최소 low, 최대 high)를 할당하고,
            low를 높여가며, 덜중요한 로그를 제거해서 출력 제어
            Ex) # debug_log = 0 : 미출력, 1 : 함수 실행 로그 출력, 2 : 함수 내부 로그 출력
    반환
        없음
'''
def debug(log, filename) :
    print(dt_now_str, filename, log)