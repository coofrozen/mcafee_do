from selenium import webdriver
from datetime import datetime
import conf

today = datetime.today()
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
query = ""
def thr_vec():
    driver = conf.driver
    driver.get(
        "https://172.22.4.73:8443/core/orionNavigationLogin.do#/console/orionRunSavedQuery.do?orion.user.security.token=bFJPKoRKcEKpROZQ&OrionSavedQueryID=&actionId=queries.run&UIDs=294&newPage=true")
    iframe = driver.find_element_by_name('mfs-container-iframe')
    driver.switch_to.frame(iframe)

    # table_id = driver.find_element_by_id("commonLegendTable_hc_analyticTable")
    # tbody = driver.find_element_by_class_name("commonLegendBody")
    tr_body = driver.find_elements_by_class_name("analyticsHover")
    query = "INSERT INTO threat_vector(atk_vec_typ,no_of_end_pt,perc) VALUES ("

    count = 0
    for row_data in tr_body:
        col = row_data.find_elements_by_tag_name("td")
        for i in range(2,len(col)):
            n_val = col[i].text.replace("'", "")
            query += "'"
            query += n_val
            query += "'"
            if i != 4:
                query += ","

        count += 1
        if count % 2 == 0 :
            query += "),("

    tfoot = driver.find_element_by_class_name("commonLegendFooter")
    tr = tfoot.find_element_by_tag_name("tr")
    th = tr.find_elements_by_tag_name("th")
    for i in range(len(th)):
        query += "'"
        query += th[i].text
        query += "'"
        if i != 2:
            query += ","
    query += ")"
    print("done")
    print(query)
    return query



