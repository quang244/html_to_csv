from bs4 import BeautifulSoup
import pandas as pd

def valid_code(code):
    code = code.replace('$', '').strip()
    return code

def valid_sub_code(sub_code):
    start_index = sub_code.find('(')
    end_index = sub_code.find(')', start_index)
    sub_code = sub_code[start_index + 2:end_index]
    return sub_code

file_path = r'input\10_Failures_2024-11-15T05-27.html'
print(file_path)

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    function_list = []
    dtc_name_list = []
    dtc_code_list = []
    sub_code_list = []

    soup = BeautifulSoup(content, 'html.parser')

    container_tables = soup.find("table", class_="identification")
    tbody = container_tables.find("tbody")
    rows = tbody.find_all("tr", recursive=False)
    dtc_function = rows[0].find("th", class_="fctname").text.replace("Function: ", "")
    part_2 = rows[1].find_all("tr", recursive=False)
    for i, row in enumerate(part_2):
        function_name = row.find("th", class_="fctname")
        if function_name:
            dtc_function = function_name.text

        tables = row.find_all("table", class_="Function")
        
        for index, table in enumerate(tables):
            print(index)
            if table.find("th").text == "Devices Unknown (Missing database definition)":
                continue
            
            if table.find("td", class_="deviceunknown"):
                for tr in table.find_all("tr"):
                    temp = tr.find("td", class_="deviceunknown")
                    sub_code = tr.find("td", align="center")
                    if temp:
                        name_and_code = temp.find("a")
                        dtc_name = name_and_code.text.split("##")[0].split(":")[0].strip()
                        dtc_code = name_and_code.text.split("##")[1]
                    # if sub_code and "$" in sub_code.text:
                    #     sub_code = valid_sub_code(sub_code.text)
                    #     function_list.append(dtc_function)
                    #     dtc_name_list.append(dtc_name)
                    #     dtc_code_list.append(dtc_code)
                    #     sub_code_list.append(sub_code)                      
                    FailureType = tr.find("td", string="FailureType")
                    if FailureType:
                        sub_code = FailureType.find_next("td")
                        print(sub_code.text)
                    if sub_code and "$" in sub_code.text:
                        sub_code = valid_sub_code(sub_code.text)
                        function_list.append(dtc_function)
                        dtc_name_list.append(dtc_name)
                        dtc_code_list.append(dtc_code)
                        sub_code_list.append(sub_code)
        
            else:
                for tr in table.find_all("tr"):
                    name = tr.find("a", title="click for device documentation")
                    code = tr.find("td", width="5%")
                    sub_code = tr.find("td", align="center")
                    if name and code:
                        dtc_name = name.text
                        dtc_code = valid_code(code.text)
                    if sub_code and "$" in sub_code.text:
                        sub_code = valid_sub_code(sub_code.text)
                        function_list.append(dtc_function)
                        dtc_name_list.append(dtc_name)
                        dtc_code_list.append(dtc_code)
                        sub_code_list.append(sub_code)
    data = {
        'Function_Name': function_list,
        'DTC_Name': dtc_name_list,
        'DTC_Code': dtc_code_list,
        'DTC_Sub_Code': sub_code_list
    }
    df = pd.DataFrame(data)
    df.to_csv(r'output\a.csv', index=False)
    print("Function Names:", function_list, "độ dài : ", len(function_list))
    print("Device Names:", dtc_name_list, "độ dài : ", len(dtc_name_list))
    print("Device Codes:", dtc_code_list, "độ dài : ", len(dtc_code_list))
    print("Device Sub Codes:", sub_code_list, "độ dài : ", len(sub_code_list))
