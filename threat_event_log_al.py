import conf
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select


today = datetime.today()
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
query = ""
def ev_log_al():
    driver = conf.driver
    driver.get(
        "https://172.22.4.73:8443/core/orionNavigationLogin.do#/core/orionTab.do?sectionId=orion.report&tabId=EventList&orion.user.security.token=bFJPKoRKcEKpROZQ")
    iframe = driver.find_element_by_name('mfs-container-iframe')
    driver.switch_to.frame(iframe)
    iselect = Select(driver.find_element_by_id('ThreatEventLogTable_filterList'))
    iselect.select_by_value("eventlog.filter.day")
    iselect2 = driver.find_element_by_id('ThreatEventLogTable_advancedFilter').click()
    driver.find_element_by_xpath('//span[text()="allowed"]').click()
    sleep(3)
    tbody = driver.find_element_by_id("ThreatEventLogTable_dataBody")
    tr_body = tbody.find_elements_by_tag_name("tr")
    query = "INSERT INTO threat_event_log_al(event_rec_time,pref_event_time,event_id,event_desc,event_catagory,threat_target,action,threat_type,threat_severity,threat_vector_type,threat_target_ip) VALUES ("
    count = 0
    for row_data in tr_body:
        count += 1
        if count < len(tr_body) - 1:
            col = row_data.find_elements_by_tag_name("td")
            for i in range(len(col)):
                n_val = col[i].text.replace("'", "")
                if (i != 0 and i != len(col) - 1):
                    query += "'"
                    query += n_val
                    query += "'"
                    if i != len(col) - 2:
                        query += ","
            query += ")"
        if count < len(tr_body) - 2:
            query += ",("

    print(query)
    return query
