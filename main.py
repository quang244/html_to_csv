from bs4 import BeautifulSoup
import os
import pandas as pd

file_path = r'input\10_Failures_2024-11-15T05-27.html' 
print(file_path)
            
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    dtc_name_list = []
    dtc_code_list = []
    sub_code_list = []
    
    # Phân tích nội dung HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    tables = soup.find_all("table", class_="Function")
    dtc_name = None
    dtc_code = None
    for table in tables:
        for tr in table.find_all("tr"):
            name = tr.find("a", title="click for device documentation")
            code = tr.find("td", width="5%")
            sub_code = tr.find("td", align="center")
            if name and code:
                dtc_name = name.text
                dtc_code = code.text.replace('$', '').strip()
            if sub_code and "$" in sub_code.text:
                print(sub_code.text)  # In ra nội dung của thẻ <td>
                start_index = sub_code.text.find('(')
                end_index = sub_code.text.find(')', start_index)
                sub_code = sub_code.text[start_index + 2:end_index]
                dtc_name_list.append(dtc_name)
                dtc_code_list.append(dtc_code)
                sub_code_list.append(sub_code)
    data = {
    'DTC_Name': dtc_name_list,
    'DTC_Code': dtc_code_list,
    'DTC_Sub_Code': sub_code_list
    }
    df = pd.DataFrame(data)
    df.to_excel(r'output\a.xlsx', index=False)

    print("Device Names:", dtc_name_list,"độ dài : ", len(dtc_name_list))
    print("Device Codes:", dtc_code_list,"độ dài : ", len(dtc_code_list))  
    print("Device Sub Codes:", sub_code_list,"độ dài : ", len(sub_code_list))                    
        
    
    
    
    # # Duyệt qua từng bảng
    # for table in tables:
    #     tabs = table.find_all("table", class_="DTCName")
    #     for tab in tabs:
    #         name = tab.find("a", title="click for device documentation")
    #         if name:
    #             dtc_name_list.append(name.text.strip())  # Lấy tên và loại bỏ khoảng trắng thừa
    #         code = tab.find("td", width="5%")
    #         dtc_code_list.append(code.text.strip())  # Lấy nội dung của mỗi thẻ <td>
    #     tables_DTC_SUB = soup.find_all("table",class_="StatusDTC")
    # # In kết quả
    # print("Device Names:")
    # print(dtc_name_list)
    
    # print("Device Codes:")
    # print(dtc_code_list)



    # tables = soup.find_all("table",class_="DTCName")
    # tables_DTC_SUB = soup.find_all("table",class_="StatusDTC")

    # for table in tables:
    #     links = table.find_all("a",title="click for device documentation")
    #     tds = table.find_all("td")
    #     name = None
    #     dtc_code = None
    #     for link in links:
    #         # print(link.text)
    #         name = link.text
    #         # dtc_name.append(link.text)
    #     for td in tds:
    #         if 'FailureType' in td.text:
    #             dtc_code = 
    #             cleaned_text = td.text.replace('$', '').strip()  # Loại bỏ ký tự $ và khoảng trắng
    #             dtc_code = cleaned_text
    #             # dtc_code.append(cleaned_text)

    #     for table in tables_DTC_SUB:
    #         tds = table.find_all("td")
    #         for td in tds:
    #             if '$' and '(' in td.text:
    #                 start_index = td.text.find('(')
    #                 end_index = td.text.find(')', start_index)
    #                 sub_code = td.text[start_index + 2:end_index]
    #                 dtc_name_list.append(name)
    #                 dtc_code_list.append(dtc_code)
    #                 sub_code_list.append(sub_code)


    # data = {
    # 'DTC_Name': dtc_name_list,
    # 'DTC_Code': dtc_code_list,
    # 'DTC_Sub_Code': sub_code_list
    # }
    # df = pd.DataFrame(data)
    # df.to_excel(r'output\a.xlsx', index=False)
    # print("dtc_name : ",dtc_name_list, "độ dài : ", len(dtc_name_list))
    # print("dtc_code : ",dtc_code_list, "độ dài : ", len(dtc_code_list))
    # print("dtc_sub_code : ",sub_code_list, "độ dài : ", len(sub_code_list))
    # # print("độ dài : ", len(dtc_name))
    # # print( "độ dài : ", len(dtc_code))
    # # print("độ dài : ", len(dtc_sub_code))
    # print("\n")
