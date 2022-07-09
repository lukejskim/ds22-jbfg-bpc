import logging

# logging.warning('%s before you %s', 'Look', 'leap!')
# levelname(심각도), message(이벤트설명)

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)

level=logging.DEBUG
logging.basicConfig(format='%(levelname)s:%(message)s', level=level)

logging.debug('   [1단계] 디버깅 메시지')
logging.info('    [2단계] 정보성 메시지')
logging.warning(' [3단계] 경고성 메시지')
logging.error('   [4단계] 에러성 메시지')
logging.critical('[5단계] 심각한 메시지')





# logging.debug   ('\t[1단계] 디버깅 메시지')
# logging.info    ('\t[2단계] 정보성 메시지')
# logging.warning ('\t[3단계] 경고성 메시지')
# logging.error   ('\t[4단계] 에러성 메시지')
# logging.critical('\t[5단계] 심각한 메시지')
