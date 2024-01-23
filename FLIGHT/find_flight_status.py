from selenium import webdriver
from selenium.webdriver.common.by import By


def find_flight_status(url,xpath):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(url)
    driver.maximize_window()
    driver.delete_all_cookies()
    ele = driver.find_elements(By.XPATH,xpath)
    status_flight = list()
    actual = {"Delhi","Goa","Dubai","Bengaluru"}
    present = list()
    for i in ele:
        t = str(i.text)
        tt = t.split("\n")
        for index,value in enumerate(tt):
            if "Delhi" in value or "Goa" in value or "Dubai" in value or "Bengaluru" in value:
                str1 = value.split(" ")[0] + ":" + tt[index+2]
                status_flight.append(str1)
                present.append(value.split(" ")[0])
                #print(value,tt[index+2],sep=":")

    ll = list(actual.difference(present))
    d = "data not available"
    for i in ll:
        status_flight.append(i+": "+d)

    for i in status_flight: print(i)
    driver.quit()




url = "https://www.flightradar24.com/data/airports/pnq"
xpath = '//div[@class="row cnt-schedule-table"]'
find_flight_status(url,xpath)



