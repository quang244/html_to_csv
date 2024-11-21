with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
#     dtc_name_list = []
#     dtc_code_list = []
#     sub_code_list = []
#     soup = BeautifulSoup(content, 'html.parser')
#     tables = soup.find_all("table",class_="Function")
#     for table in tables:
#         tabs = soup.find_all("table",class_="DTCName")
#         for tab in tabs:
#             name = tab.find("a",title="click for device documentation")
#             code = tab.find_all("td", width="5%")
#             print(name.text)
#             print(code.text)