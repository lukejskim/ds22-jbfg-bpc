import logging

# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('기본형 날짜시간 정보 추가')

# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('포맷형 날짜시간 정보 추가')
# 05/20/2022 02:03:03 AM 포맷형 날짜시간 정보 추가

# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y.%m.%d %I:%M:%S %p')
# logging.warning('포맷형 날짜시간 정보 추가')
# 2022.05.20 02:04:15 AM 포맷형 날짜시간 정보 추가

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y.%m.%d %I:%M:%S %a')
logging.warning('포맷형 날짜시간 정보 추가')
# 2022.05.20 02:05:16 Fri 포맷형 날짜시간 정보 추가