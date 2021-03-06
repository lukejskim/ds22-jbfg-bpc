books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})


many_page     = [ book['제목']  for book in books  if book['쪽수'] > 250 ]
recommends    = [ book['제목']  for book in books  if book['추천유무']  ]
pub_companies = { book['출판사'] for book in books }
all_pages     = sum([book['쪽수'] for book in books])


print(' ### 도서 목록 출력 내용 ### \n', '-'*90)
print(' 1. 쪽수가 250 쪽 넘는 책 리스트 :', many_page)
print(' 2. 내가 추천하는 책 리스트      :', recommends)
print(' 3. 내가 읽은 책 전체 쪽수       :', all_pages)
print(' 4. 내가 읽은 책의 출판사 목록   :', sorted(pub_companies) )




# print(' 1. 쪽수가 250 쪽 넘는 책 리스트 : {}'.format( [ book['제목']  for book in books  if book['쪽수'] > 250 ]))