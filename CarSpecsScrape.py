from selenium import webdriver
import pandas as pd

# Call the Chrome Webdriver class
browser = webdriver.Chrome()


def ScrapeCarData(url):
    browser.get(url)

    # Pull specific characteristics for vehicle based on XPATH from site
    make = browser.find_elements_by_xpath('//*[@id="content-container"]/cd-specs/section/div[1]/ul/li[2]/a')[0]
    model = browser.find_elements_by_xpath('//*[@id="content-container"]/cd-specs/section/div[1]/ul/li[3]/a')[0]
    price = browser.find_elements_by_xpath('//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[2]/div/p[1]')[0]

    mpg_hwy = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[1]/tr[2]/td[2]')[0]

    mpg_city = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[1]/tr[4]/td[2]')[0]
    fuel_capcty = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[2]/tr[2]/td[2]')[0]
    frnt_brk_rtr_diam = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[4]/tr[7]/td[2]')[0]
    emm_CO2_tonsyr_15kmi = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[5]/tr[2]/td[2]')[0]
    trans = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[6]/tr[2]/td[2]')[0]
    trans_spd = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[6]/tr[4]/td[2]')[0]
    trans_typ = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[6]/tr[5]/td[2]')[0]
    curb_wt = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[9]/tr[2]/td[2]')[0]
    engine_typ = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[11]/tr[3]/td[2]')[0]
    engine_disp = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[11]/tr[4]/td[2]')[0]
    fuel_sys = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[11]/tr[5]/td[2]')[0]
    hp_sae = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[11]/tr[6]/td[2]')[0]
    torque_sae = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[11]/tr[7]/td[2]')[0]
    whl_base = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[18]/tr[2]/td[2]')[0]
    len = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[18]/tr[3]/td[2]')[0]
    wid_wo_mirrors = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[18]/tr[4]/td[2]')[0]
    ht = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[18]/tr[5]/td[2]')[0]
    clearance_min = browser.find_elements_by_xpath(
        '//*[@id="content-container"]/cd-specs/section/div[2]/div[1]/div[4]/table[1]/tbody[18]/tr[8]/td[2]')[0]

    # Create list of car specs
    df_text = [{'Make': make.text, "Model": model.text, "price": price.text, "mpg_hwy": mpg_hwy.text, "mpg_city": mpg_city.text,
                "fuel_capcty": fuel_capcty.text,
                "frnt_brk_rtr_diam": frnt_brk_rtr_diam.text, "emm_CO2_tonsyr_15kmi": emm_CO2_tonsyr_15kmi.text,
                "trans": trans.text, "trans_spd": trans_spd.text, "trans_typ": trans_typ.text, "curb_wt": curb_wt.text,
                "engine_typ": engine_typ.text, "engine_disp": engine_disp.text, "fuel_sys": fuel_sys.text,
                "hp_sae": hp_sae.text, "torque_sae": torque_sae.text, "whl_base": whl_base.text, "len": len.text,
                "wid_wo_mirrors": wid_wo_mirrors.text, "ht": ht.text, "clearance_min": clearance_min.text
                }]

    # Convert list to dataframe
    df = pd.DataFrame(df_text)

    print(df.head(5))

    return df


url_list = ('https://www.caranddriver.com/volkswagen/golf-r/specs#features',
            'https://www.caranddriver.com/mini/cooper-jcw/specs#features',
            'https://www.caranddriver.com/mazda/mx-5-miata/specs#features',
            'https://www.caranddriver.com/ford/focus-rs/specs/2016/ford_focus-rs_ford-focus-rs_2016',
            'https://www.caranddriver.com/audi/a3/specs#features',
            'https://www.caranddriver.com/fiat/500-500c-abarth/specs/2017/fiat_500-500c-abarth_fiat-500c-abarth_2017/specs#features'
            )

# Call Function for specific Car and Driver URL's
df_stack=[]
for item in url_list:
    df = ScrapeCarData(item)
    df = pd.DataFrame(df)
    df_stack.append(df)


df_stack2 = pd.concat(df_stack)

df_stack2.to_csv('C:/Users/matt.wheeler/Documents/ForFun/CarAndDriverScraping/results/CarXSpecs.csv', index=False)