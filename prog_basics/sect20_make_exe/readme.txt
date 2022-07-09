
파이썬 프로그램을 .exe 실행 파일로 만드는 방법 (PyInstaller)
https://www.youtube.com/watch?v=Es1fQqqxIFQ


실행파일 만들기 (PyInstaller)
https://wikidocs.net/21952

PyInstaller 홈페이지
https://pyinstaller.org/en/stable/
-----------------------------------------
1. PyInstaller 설치
2. 실행파일 만들기
3. 콘솔창 출력되지 않도록 하기
4. 실행파일 하나만 생성하기
-----------------------------------------

1. PyInstaller 설치
pip install pyinstaller

PATH = %PATH%;
2. 실행파일 만들기
Python 파일이 있는 폴더로 이동한 다음,
아래 명령어를 입력하면 해당 폴더에 실행파일이 만들어집니다.
pyinstaller filename.py

만들어진 폴더에서 dist로 이동해서, 한 번 더 들어가면
아래 그림과 같이 실행파일을 찾을 수 있습니다.
더블클릭해서 실행을 해보면 아래 그림과 같이 콘솔창이 함께 출력됩니다.

3. 콘솔창 출력되지 않도록 하기
콘솔창이 출력되지 않게 하려면 아래와 같이 명령어에 '-w' 또는 '--windowed'를 추가해줍니다.
pyinstaller -w filename.py

4. 실행파일 하나만 생성하기
실행파일 하나만 생성하기 위해서는 아래와 같이 명령어에 ‘-F’ 또는 ‘–onefile’을 추가합니다.
pyinstaller -w -F filename.py
실행파일 생성이 완료되었습니다.

