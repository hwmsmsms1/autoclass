# autoclass
* 사이버강의 자동화 프로그램
  -------
  ##### ui_login.py : 로그인 페이지 프론트
  ##### ui_main.py : 로그인 이후 메인페이지 프론트
  ##### make_exe.py : exe 파일로 변환
  ##### app.py : 실행 코드
---------------------------------------
## pyside6 designer 실행
* 경로 : pyside/venv/Scripts/pyside6-designer
* 마우스 우클릭 - reveal in file..
* exe 파일 실행

## 위젯 설정
* Label 끌어오기 (Label : 도화지)
* 마우스 우클릭 - styleSheet 바꾸기
* 배경 하얀색으로 변환 - <span style="color:Yellow ">background-color:white;</span>
* 투명도, RGB값 설정 - <span style="color:Yellow ">background-color:rgba(132,42,52,0.8);</span>
* 글자색 빨간색으로 변환 - <span style="color:Yellow ">color:white;</span>


## 위젯 종류
* Label : 아이디, 비밀번호 등 타이틀
* pushButton : 로그인, 확인 등 눌러서 화면 전환
* line Edit : 아이디 값, 비밀번호 값 등 기입란
* placeholderText(속성편집기) : 값 기입 전 고정 멘트 기입란

## Designer -> Python source
* pyside 폴더 내부에 login.ui로 저장
* 디자이너 상단 폼 클릭
* 파이썬 코드로 보기 클릭
* pyside/venv/lib/site-package/Pyside6 안에 bin 폴더 존재 하는 지 확인 
* bin 폴더 마우스 우클릭 - reveal in file..
* Script/pyside6-uic.exe 마우스 우클릭 - reveal in file..
* pyside6-uic.exe 파일 복붙 -> bin 폴더로 
* 파일이름 uic.exe 로 변경
* <span style="color:RED">uic.exe. 파일 기능 : GUI 를 코드형태로 바꿔줌.</span>


## app.py 기본 구조
* 라이브러리 import
```
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
``````
* Designer 에서 만든 ui_login.py의 클라스 import
``````
from ui_login import Ui_Dialog
``````
* 새로운 클래스 생성
``````
class login_Window(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(login_Window, self).__init__()
        self.setupUi(self)
``````
* 실행
``````
app = QApplication(sys.argv)

window = login_Window()
window.show()

app.exec_()
``````
## 이미지 삽입
* objectName : main_logo
``````
from PySide6.QtGui import QPixmap, QIcon

logo_pixmap = QPixmap('12345.jpg')
logo_pixmap = logo_pixmap.scaled(71,61)
self.main_logo.setPixmap(logo_pixmap)
``````
## 윈도우 타이틀, 아이콘
``````
self.setWindowTitle('AutoClass')
self.setWindowIcon(QIcon('12345.jpg'))

# GUI 화면 크기 고정
elf.setFixedSize(263,475)
``````
## 로그인 버튼 활성화
``````
self.login_btn.clicked.connect()
