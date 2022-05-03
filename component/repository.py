import json


def save_media_links(path, data_list):
    json_file_content = {"media_links": []}
    with open(path, encoding='utf8') as json_file:
        json_file_content = json.load(json_file)
        media_links = json_file_content['media_links']
        media_links.clear()
        for data in data_list:
            media_links.append(data)
    with open(path, "w", encoding='utf8') as json_file:
        json_file_content['media_links'] = media_links
        json.dump(json_file_content, json_file, ensure_ascii=False)


def save_data_flows(path, data: dict):
    json_file_content = {"data_flows": []}
    with open(path, encoding='utf8') as json_file:
        json_file_content = json.load(json_file)
        data_flows = json_file_content['data_flows']
        e = data.copy()
        data_flows.append(e)
    with open(path, "w", encoding='utf8') as json_file:
        json_file_content['data_flows'] = data_flows
        json.dump(json_file_content, json_file, ensure_ascii=False)


def get_excel_content(path):
    with open(path, encoding='utf8') as json_file:
        json_file_content = json.load(json_file)
        media_links = json_file_content
        return media_links
