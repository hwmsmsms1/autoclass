from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


import sys, time
import datetime


from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import QMessageBox, QStackedWidget
from PySide6.QtGui import QPixmap, QIcon

from ui_login import Ui_Dialog as Login_UI
from ui_main import Ui_Dialog as Main_UI


class Main_Window(QMainWindow, Main_UI):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.setupUi(self)

        self.cyber_class_name = None
        self.class_room = None
        self.cyber_class_num = None
        

        self.eclassId = None
        self.eclassPw = None


        self.eclass_id.textChanged.connect(self.set_id)
        self.eclass_pw.textChanged.connect(self.set_pw)
        

        self.class_data.textChanged.connect(self.class_name)
        self.classroom_num.textChanged.connect(self.classroom_number)
        self.class_data2.textChanged.connect(self.class_number)
    

        self.start_btn.clicked.connect(self.start_process)
        self.url2.clicked.connect(self.open_web_site2)


    def open_web_site2(self):
        import webbrowser
        webbrowser.open('https://orinuguri.tistory.com/') 


    def set_id(self, text):
        self.eclassId= text
    
    def set_pw(self, text):
        self.eclassPw= text
    
    def class_name(self, text):
        self.cyber_class_name= text
    
    def classroom_number(self, text):
        self.class_room = text    
    
    def class_number(self, text):
        self.cyber_class_num = text
    
    def show_dialog2(self,title,msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)

    def start_process(self):
        print('프로그램 동작 실행')
        print(self.cyber_class_name,'-')
        
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True) 
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)

        
        driver.get("https://eclass.dongguk.ac.kr/index.jsp")
        time.sleep(3)

        main = driver.window_handles

        for i in main:
            if i != main[0]:
                driver.switch_to.window(i)
                driver.close()
                driver.switch_to.window(main[0])
        
        time.sleep(3)
        driver.maximize_window()

        time.sleep(3)
        driver.switch_to.frame('main')
        
        popup_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/button/span[1]')
        popup_btn.click()

        time.sleep(3)
        start_login_btn = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/ul/li[1]/a')
        start_login_btn.click()

        time.sleep(3)
        username = driver.find_element(By.XPATH,'//*[@id="id"]')
        username.send_keys(self.eclassId)

        password = driver.find_element(By.XPATH,'//*[@id="pw"]')
        password.send_keys(self.eclassPw)

        time.sleep(3)
        login_btn = driver.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/p/a')
        login_btn.click()

        classroom_str1 = '//*[@id="mCSB_1_container"]/ul/li['
        class_room_data = self.class_room
        classroom_str2 = ']/a/span[2]/button'
        classroom_Xpath = classroom_str1 + str(class_room_data) + classroom_str2

        time.sleep(3)
        classroom_btn = driver.find_element(By.XPATH, classroom_Xpath)
        classroom_btn.click()

        time.sleep(3)
        week_td = self.cyber_class_num

        class_str1 = '//*[@id="listBox"]/table/tbody/tr[1]/td['
        class_str2 = ']/div'

        class_str = class_str1 + str(week_td) + class_str2
        class_count = driver.find_elements(By.XPATH, class_str)

        str1 = '//*[@id="listBox"]/table/tbody/tr[1]/td['
        str2 = ']/div['
        str3 = ']/ul[2]/li[2]/a[2]'

        time1 = ']/ul[2]/li[1]'
        
        for n in range(1,len(class_count)+1):
            now = datetime.datetime.now()
            now_time = now.strftime('%H시 %M분 %S초')
            self.show_dialog2(now_time,str(n)+'번째 강의 시작')
            main = driver.window_handles
            driver.switch_to.window(main[0])
            driver.switch_to.frame('main')
            
            class_Xpath = str1 + str(week_td) + str2 + str(n) + str3
            class_btn = driver.find_element(By.XPATH, class_Xpath)
            
            time_Xpath = str1 + str(week_td) + str2 + str(n) + time1
            time_data = driver.find_element(By.XPATH, time_Xpath).text
            time_data = time_data[-4:-2]
            time_data = int(time_data)
            
            second = (time_data * 60) + 500
            
            class_btn.click()
            time.sleep(5)
            
            try:
                driver.switch_to.window(driver.window_handles[-1])
                WebDriverWait(driver, 10).until (EC.alert_is_present())
                
                alert = driver.switch_to.alert
                alert.send_keys(Keys.ENTER)
                alert.accept()
                print('alert O')
           
            except:
                print('alert X')
            
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            driver.switch_to.frame('bodyFrame')
            play_btn = driver.find_element(By.XPATH, '//*[@id="video-player"]/button')
            play_btn.click()
            
            start_time = datetime.datetime.now()
            seconds_to_run = second

            while (datetime.datetime.now() - start_time).seconds < seconds_to_run:
                time.sleep(10)
                main = driver.window_handles
                
                if len(main) < 2:
                    driver.switch_to.window(driver.window_handles[0])
                    driver.switch_to.frame('main')
                    class_btn = driver.find_element(By.XPATH, class_Xpath)
                    class_btn.click()
                    time.sleep(5)
            
                    main = driver.window_handles
                    driver.switch_to.window(main[1])
                    
                    try:
                        WebDriverWait(driver, 10).until (EC.alert_is_present())
                
                        alert = driver.switch_to.alert
                        alert.accept()
                        print('alert O')
                    
                    except TimeoutException:
                        print('alert X')
                    
                    driver.switch_to.window(driver.window_handles[1])
                    driver.switch_to.frame('bodyFrame')
                    play_btn = driver.find_element(By.XPATH, '//*[@id="video-player"]/button')
                    play_btn.click()
                    print('Retry class!')

                    continue
                else:
                    continue
            else:
                print(str(n)+'번째 강의 수강 완료.')

                main = driver.window_handles
        
                driver.switch_to.window(main[1])
                driver.close()
            
                time.sleep(3)        
        print('--------------------')
        
        now = datetime.datetime.now()
        now_time = now.strftime('%H시 %M분 %S초')
        self.show_dialog2(now_time,'모든 강의 수강 완료')
    
    def class_name(self, text):
        self.cyber_class_name= text
    
    def week_name(self, text):
        self.week_number = text    
    
    def class_number(self, text):
        self.cyber_class_num = text
    
    
class login_Window(QMainWindow, Login_UI):
    def __init__(self):
        super(login_Window,self).__init__()
        
        self.setupUi(self)        
        self.userId = None
        self.userPw = None
        self.userKey = None

        logo_pixmap = QPixmap('12345.jpg')
        logo_pixmap = logo_pixmap.scaled(71,61)
        self.main_logo.setPixmap(logo_pixmap)
        
        self.setWindowTitle('AutoClass')

        self.setWindowIcon(QIcon('12345.jpg'))
        self.setFixedSize(263,475)

        self.login_btn.clicked.connect(self.login_btn_clicked)
        
        self.account_id.textChanged.connect(self.change_id)
        self.account_pw.textChanged.connect(self.change_pw)
                
        self.key_btn.clicked.connect(self.key_btn_clicked)

        self.account_key.textChanged.connect(self.change_key)

        self.url1.clicked.connect(self.open_web_site)


    def login_btn_clicked(self):
        print("로그인 버튼이 클릭되었습니다.")
        print(self.userId, self.userPw, self.userKey)
        # 입력한 계정 정보를 서버에 전송 서버 전송
        
        # 서버의 역할을 대신할 텍스트 파일 기반의 데이터베이스 제조

        User_Data = [["user","1234",'qwe123']]
        
        # DB 조회 기능
        LOGIN_SUCCESS = False
        
        for user in User_Data:
            user_id, user_pw, user_key = user
            print(user_id, user_pw, '가 현재 유저입니다.')
            
            if self.userId == user_id and self.userPw == user_pw and self.userKey==user_key:
                print('로그인 성공')
                LOGIN_SUCCESS = True
                main_widget.setCurrentIndex(1) # 메인 화면으로 이동
                main_widget.setFixedSize(330,610)
        
        if LOGIN_SUCCESS:
            print('화면을 전환합니다.')

        else:
            print('에러 발생')
            self.show_dialog('로그인 실패',"로그인 실패 - 일치하는 계정 정보가 없습니다.")
        # 로그인 성공 - 화면 전환
        # 로그인 실패 - 에러 메세지를 출력해줘야함

    def key_btn_clicked(self):
        print("인증키 버튼이 클릭되었습니다.")

    def open_web_site(self):
        import webbrowser
        webbrowser.open('https://eclass.dongguk.ac.kr/index.jsp') 
    
    def show_dialog(self,title,msg):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)

        msgBox.exec()

    def change_id(self, text):
        self.userId = text
    
    def change_pw(self, text):
        self.userPw = text

    def change_key(self, text):
        self.userKey = text

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_widget = QStackedWidget()

    login_ui = login_Window()
    main_ui = Main_Window()
    main_widget.addWidget(login_ui) # 0 idx
    main_widget.addWidget(main_ui) # 1 idx
    
    # 화면 전환 방법
    # main_widget.setCurrentIndex() # 로그인 성공시 현재 0 idx -> 메인 화면
    
    main_widget.show()

    app.exec()
