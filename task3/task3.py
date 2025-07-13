import json
import shutil
import sys
 
tests = sys.argv[1]
report = sys.argv[2]
values = sys.argv[3]

shutil.copy(tests, report)                   #создаем шаблон файла report, в котором будем производить замены

# Чтение данных из файлов values.json, tests.json
with open(values, 'r') as values_file:
    values_data = json.load(values_file)

with open(report, 'r') as report_file:
    report_data = json.load(report_file)

def get_index(values_data):                                 #получаем id из файла values
    index = []
    for values_items in values_data.values():
        for i in range(len(values_items)):
            values_item = values_items[i]
            values_id = values_item['id']
            values_value = values_item['value']
            index.append(values_id)
    return(index)

def get_values(values_data, element):                        #получаем значения values из файла values
    for values_items in values_data.values():
        for i in range(len(values_items)):
            values_item = values_items[i]
            values_id = values_item['id']
            values_value = values_item['value']
            if values_id == element:
                return values_value
            
print(get_index(values_data))                    
print(get_values(values_data, get_index(values_data)[11]))

with open(report) as new_report_file:
    new_report_data = json.load(new_report_file)
    for report_items in new_report_data.values():
        for i in range(len(report_items)):
            report_item = report_items[i]
            report_id = report_item['id']
            report_value = report_item['value']
        for i in range(len(get_index(values_data))):
            if report_item['id'] == get_index(values_data)[i]:
                report_item['value'] = get_values(values_data, get_index(values_data)[i])


        
#my_file = open("report.json", "w+", encoding='utf-8')
#my_file.write(tests_file)
#my_file.close()
