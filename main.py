from bs4 import BeautifulSoup
import os
import pandas as pd

directory_path = r'input'
for filename in os.listdir(directory_path):
    if filename.endswith('.html'):
        file_path = os.path.join(directory_path, filename)
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        dtc_name = []
        dtc_code = []
        dtc_sub_code = []
        soup = BeautifulSoup(content, 'html.parser')

        tables = soup.find_all("table",class_="DTCName")
        tables_DTC_SUB = soup.find_all("table",class_="StatusDTC")
        for table in tables_DTC_SUB:
            tds = table.find_all("td")
            for td in tds:
                if '$' in td.text:
                    start_index = td.text.find('(')
                    end_index = td.text.find(')', start_index)
                    value = td.text[start_index + 2:end_index]
                    dtc_sub_code.append(value)
        for table in tables:
            links = table.find_all("a",title="click for device documentation")
            tds = table.find_all("td")
            for link in links:
                # print(link.text)
                dtc_name.append(link.text)
            for td in tds:
                if '$' in td.text:
                    cleaned_text = td.text.replace('$', '').strip()  # Loại bỏ ký tự $ và khoảng trắng
                    dtc_code.append(cleaned_text)
        # data = {
        # 'DTC_Name': dtc_name,
        # 'DTC_Code': dtc_code,
        # 'DTC_Sub_Code': dtc_sub_code
        # }
        # df = pd.DataFrame(data)
        # df.to_csv(f'output\{file_path}.csv', index=False, encoding='utf-8')
        print("dtc_name : ",dtc_name, "độ dài : ", len(dtc_name))
        print("dtc_code : ",dtc_code, "độ dài : ", len(dtc_code))
        print("dtc_sub_code : ",dtc_sub_code, "độ dài : ", len(dtc_sub_code))
    print("\n")



    


