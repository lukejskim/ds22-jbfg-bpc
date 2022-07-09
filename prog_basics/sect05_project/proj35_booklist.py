from sect05_project import proj31_booklist as booklist

books = booklist.books    # 책 목록 선언

many_page     = [ book['제목']  for book in books  if book['쪽수'] > 250 ]
recommends    = [ book['제목']  for book in books  if book['추천유무']  ]
pub_companies = { book['출판사'] for book in books }
all_pages     = sum([book['쪽수'] for book in books])

print(' ### 도서 목록 출력 내용 ### \n', '-'*90)
print(' 1. 쪽수가 250 쪽 넘는 책 리스트 \t:', many_page)
print(' 2. 내가 추천하는 책 리스트      \t:', recommends)
print(' 3. 내가 읽은 책 전체 쪽수       \t:', all_pages, 'page')
print(' 4. 내가 읽은 책의 출판사 목록    \t:', sorted(pub_companies) )
