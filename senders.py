from datetime import datetime
import conf


today = datetime.today()
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
query = ""
def senders():
    driver = conf.conf()
    driver.get(
        "https://172.22.4.73:8443/core/orionNavigationLogin.do#/console/orionRunSavedQuery.do?orion.user.security.token=N9rSwVhtfBi6P8Tc&OrionSavedQueryID=510&actionId=queries.run&UIDs=510&newPage=true")

    iframe = driver.find_element_by_name('mfs-container-iframe')
    driver.switch_to.frame(iframe)

    # table_id = driver.find_element_by_id("commonLegendTable_hc_analyticTable")
    # tbody = driver.find_element_by_class_name("commonLegendBody")
    tr_body = driver.find_elements_by_class_name("analyticsHover")
    query = "INSERT INTO sreport(threat_u_name,no_of_events) VALUES ("

    count = 0
    for row_data in tr_body:
        col = row_data.find_elements_by_tag_name("td")
        for i in range(len(col)):
            n_val = col[i].text.replace("'", "")
            if i == 0:
                query += "'"
            query += n_val
            if i == 0:
                query += "',"
        count += 1
        if count % 2 == 0 :
            query += "),("
    tfoot = driver.find_element_by_class_name("commonLegendFooter")
    tr = tfoot.find_element_by_tag_name("tr")
    th = tr.find_elements_by_tag_name("th")
    for i in range(len(th)):
        if i != 1:
            query += "'"
        query += th[i].text
        if i != 1:
            query += "',"
    query += ")"
    print(query)
    return query


