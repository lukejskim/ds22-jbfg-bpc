from sect15_database.database import common as dbcomm
import pandas as pd

def getBooksDF(books):
    ret_df = pd.DataFrame()

    title = list()
    published_date = list()
    publisher = list()
    pages = list()
    recommendation = list()

    column_name = ['title', 'published_date', 'publisher', 'pages', 'recommendation']
    for book in books:
        title.append(book[0])
        published_date.append(book[1])
        publisher.append(book[2])
        pages.append(book[3])
        recommendation.append(book[4])

    data = {
        'title': title,
        'published_date': published_date,
        'publisher': publisher,
        'pages': pages,
        'recommendation': recommendation
    }

    ret_df = pd.DataFrame(data, columns=column_name)

    return ret_df

def select_all_books(db_name):
    """
    전체 데이터를 조회하는 함수
    Args:
        db_name : Database Name
    Returns :
        is_success : Boolean
        ret_df : DataFrame of books
    """
    ret_df = pd.DataFrame()
    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)
        cur = conn.cursor()

        # 조회용 SQL 실행
        db_sql = "SELECT * FROM book_mgr"
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[1] 전체 데이터 출력하기')
        books = cur.fetchall()

        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success, ret_df



if __name__=="__main__":

    db_name = 'bpcdb'

    is_success, books_df = select_all_books(db_name)
    if is_success:
        print('조회된 데이터는 총 %d 건 입니다.'%len(books_df))
    else :
        print('데이터를 조회하지 못했습니다')

    print(books_df)

