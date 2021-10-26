import recipients
import senders
import threat_event_log_al
import threat_event_log_wb
import threat_vector
import connect
from time import sleep

if __name__ == '__main__':
    connect.connect(senders.senders())
    sleep(0.5)
    connect.connect(recipients.recipients())
    sleep(0.5)
    connect.connect(threat_vector.thr_vec())
    sleep(0.5)
    connect.connect(threat_event_log_al.ev_log_al())
    sleep(0.5)
    connect.connect(threat_event_log_wb.ev_log_wb())

#
#
# from selenium import webdriver
# from time import sleep
# from datetime import datetime
#
#
# today = datetime.today()
# dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
# query = ""
# url="http://demo.guru99.com/test/web-table-element.php"
# driver = webdriver.Chrome("D:\\chdrv\\chromedriver.exe")
# driver.get(url)
#
# aa=driver.find_element_by_xpath('//*[@id="leftcontainer"]/table/thead/tr/th[1]').text
# print(aa)
# dd = driver.find_elements_by_xpath('.//*[@id=\"leftcontainer\"]/table/thead/tr/th')
# print(len(dd))
# col = driver.find_elements_by_xpath('.//*[@id="leftcontainer"]/table/tbody/tr/td[1]')
# print(len(col))
