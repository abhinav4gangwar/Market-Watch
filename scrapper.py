
import pandas as pd
import numpy as np
import zipfile as zf
from selenium import webdriver
import time
import datetime
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
start=datetime.datetime.now()
import pandas as pd
import schedule

def scraping():

    try:
        driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
        driver.minimize_window()
        driver.get("https://www.cnbc.com/quotes/US10Y")
        us_try_yield=driver.find_element(by=By.XPATH, value='//*[@id="quote-page-strip"]/div[3]/div/div[2]/span[1]').text
        # driver.close()


        driver.get("https://in.investing.com/indices/nasdaq-composite-historical-data")
        b=driver.find_element(by=By.XPATH, value='//*[@id="js-main-container"]/section[2]/div/section[2]/section[2]/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        c=driver.find_element(by=By.XPATH, value='//*[@id="js-main-container"]/section[2]/div/section[2]/section[2]/div[1]/div/table/tbody/tr[1]/td[2]/span').text
        d=driver.find_element(by=By.XPATH, value='//*[@id="js-main-container"]/section[2]/div/section[2]/section[2]/div[1]/div/table/tbody/tr[1]/td[7]/span').text




        driver.get("https://www.fbil.org.in/#/home")
        driver.find_element(by=By.XPATH, value='//*[@id="content-A"]/b').click()
        mibor=driver.find_element(by=By.XPATH, value='//*[@id="MIBOR"]/tbody/tr[1]/td[4]/div').text





        driver.get("https://in.investing.com/currencies/usd-inr-historical-data")
        f=driver.find_element(by=By.XPATH, value='//*[@id="js-main-container"]/section[1]/div/section[2]/section[2]/div[1]/div/table/tbody/tr[1]/td[3]/span').text
        g=driver.find_element(by=By.XPATH, value='//*[@id="js-main-container"]/section[1]/div/section[2]/section[2]/div[1]/div/table/tbody/tr[1]/td[2]/span').text
        h=driver.find_element(by=By.XPATH, value='//*[@id="js-main-container"]/section[1]/div/section[2]/section[2]/div[1]/div/table/tbody/tr[1]/td[7]/span').text



        driver.get("https://in.investing.com/commodities/brent-oil")
        brent=driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/section[2]/div/header/div/div[2]/div[1]/div[1]/bdo').text


        driver.get("https://www.wsj.com/market-data/quotes/index/IN/NATIONAL%20STOCK%20EXCHANGE%20OF%20INDIA/NIFTY50/historical-prices")
        m=driver.find_element(by=By.XPATH, value='//*[@id="historical_data_table"]/div/table/tbody/tr[1]/td[2]').text
        n=driver.find_element(by=By.XPATH, value='//*[@id="historical_data_table"]/div/table/tbody/tr[1]/td[5]').text
        z=driver.find_element(by=By.XPATH, value='//*[@id="quote_changePer"]').text
        driver.close()

        driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
        driver.minimize_window()

        driver.get("https://www.wsj.com/market-data/quotes/index/IN/1/historical-prices")
        p=driver.find_element(by=By.XPATH, value='//*[@id="historical_data_table"]/div/table/tbody/tr[1]/td[2]').text
        q=driver.find_element(by=By.XPATH, value='//*[@id="historical_data_table"]/div/table/tbody/tr[1]/td[5]').text
        r=driver.find_element(by=By.XPATH, value='//*[@id="quote_changePer"]').text



        driver.get("https://sgxnifty.org/")
        j=driver.find_element(by=By.XPATH, value='//*[@id="indexes-div"]/div[1]/div[4]/table/tbody/tr/td[3]').text
        k=driver.find_element(by=By.XPATH, value='//*[@id="indexes-div"]/div[1]/div[3]/table/tbody/tr/td[1]').text
        l=driver.find_element(by=By.XPATH, value='//*[@id="indexes-div"]/div[1]/div[3]/table/tbody/tr/td[3]').text




        driver.get("https://www.ccilindia.com/OMHome.aspx")
        gs=driver.find_element(by=By.XPATH, value='//*[@id="grdNDSOMReg"]/tbody/tr[2]/td[10]').text




        driver.get("https://www.ccilindia.com/OMMWSG.aspx")
        sdl_rate=0
        for i in range(1,10):
            t=driver.find_element(by=By.XPATH, value=f'//*[@id="grdMWSG"]/tbody/tr[{i}]/td[2]').text[-4:]
            if t=='2032':
                u=driver.find_element(by=By.XPATH, value=f'//*[@id="grdMWSG"]/tbody/tr[{i}]/td[7]').text
                if ((float(u))>sdl_rate):
                    sdl_rate=float(u)        


        driver.close()
        driver.quit()

    except:
        print ("error occurred")

    else:
        df = pd.read_csv('Market_Update.csv')
        print(df.head)
        df.loc[-1,"Date"] = datetime.datetime.now().strftime('%d-%m-%Y')
        df.loc[-1,"US 10 Year Try Yield"] = us_try_yield
        df.loc[-1,"US Inflation Rate"] = "9.1%"
        df.loc[-1,"NASDAQ"] =f'{b}/{c}({(d)})'
        df.loc[-1,"MIBOR Rate"] = mibor
        df.loc[-1,"USD/INR"] = f'{f}/{g}*({h})' 
        df.loc[-1,"BRENT CRUDE"] = brent
        df.loc[-1,"SGX NIFTY"] = f'{j}/{k}*({l})'
        df.loc[-1,"CNX NIFTY"] = f'{m}/{n}({z})'
        df.loc[-1,"BSE SENSEX"] = f'{p}/{q}({r})'


        df.loc[-1,"6.54% GS 2032"] = gs
        df.loc[-1,"10 Year SDL Rate"] = sdl_rate

        df.loc[-1,"5 Year PSU(AAA)"] = "7.53%"
        df.loc[-1,"10 Year PSU(AAA)"] = "7.73%"


        df.to_csv('Market_Update.csv', index = False)



schedule.every().day.at("11:14:00").do(scraping)
# print("hello")

while True:
    schedule.run_pending()








# print('Market Update')
# print(datetime.datetime.now().strftime('%d-%m-%Y'))
# print('US 10 Year Try Yield : ' , us_try_yield)
# print('US inflation rate     :  9.1% ')
# print(f'NASDAQ               :  {b}/{c}({(d)})')
# print("MIBOR Rate            : " , mibor)
# print(f"USD/INR              : Rs. {f}/{g}*({h}) "  )
# print(f"BRENT CRUDE          : $ {brent}")
# print(f"SGX NIFTY            : {j}/{k}*({l})")
# print(f"CNX NIFTY            : {m}/{n}({z})")
# print(f"BSE SENSEX           : {p}/{q}({r})")
# print(" ")
# print(f"6.54% GS 2032        : {gs}% ")
# print(f"10 year SDL Rate     : {sdl_rate}%")
# print("5 year PSU(AAA)      : 7.53%")
# print("10 year PSU(AAA)     : 7.73% ")
# print(datetime.datetime.now()-start)





