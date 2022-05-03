from settings import excel_file, generated_json_file_path
import pandas as pd
import json


class ExcelHandler:

    def __init__(self, file_name, json_file_name):
        self.file_name = file_name
        self.json_file = json_file_name

    def get_json_from_excel(self):
        data = pd.read_excel(self.file_name, sheet_name=pd.ExcelFile(self.file_name).sheet_names[-1])
        # with open(self.json_file, 'w', encoding='utf-8') as file:
        json_data = json.loads(data.to_json(force_ascii=False))
        with open(self.json_file, "w", encoding='utf8') as outfile:
            json.dump(json_data, outfile, ensure_ascii=False)
        return json_data

    def format_json_data(self):
        data = self.get_json_from_excel()
        contents_data = {"contents": []}
        contents = contents_data['contents']


#
# if __name__ == '__main__':
#     json_file = ExcelHandler(excel_file, generated_json_file_path).get_json_from_excel()
#     a = 5
