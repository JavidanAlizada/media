import json
from datetime import datetime

import component.repository as repo
import component.search as search
from component.mail_sender import MailSender
from component.scrapper import Scrapper
from component.settings import media_link_file, excel2json_file, data_flow_file
from component.settings import url


def process():
    links = Scrapper(url).get_links()

    clients = repo.get_excel_content(excel2json_file)['contents']
    media_link = []
    link_content = {}
    data_flows = []
    for link in links:
        content = search.get_content(link)
        link_content['link'] = link
        link_content['content'] = content
        link_content['created_on'] = json.dumps(datetime.now(), default=str)
        data_link_content = link_content.copy()
        media_link.append(data_link_content)
    for client in clients:
        data_flow = {'client': client['email']}
        link_keyword = {}
        data_flow['link_keyword'] = []
        for key in client['keywords']:
            for link_content_item in media_link:
                if key in link_content_item['content'] or key in link_content_item['link']:
                    link_keyword['link'] = link_content_item['link']
                    link_keyword['keyword'] = key
                    data_link_keyword = link_keyword.copy()
                    data_flow['link_keyword'].append(data_link_keyword)
        data_flow['scrapping_period'] = client['time_period']
        data_flow['scrapping_started_on'] = "000"
        data_flow['scrapping_end_on'] = "111"
        data_flows.append(data_flow)
        repo.save_data_flows(data_flow_file, data_flow)

    repo.save_media_links(media_link_file, media_link)
    with open(data_flow_file, encoding='utf8') as json_file:
        json_file_content = json.load(json_file)
        data_flows_content = json_file_content['data_flows']
    payload = search.get_email_payload(data_flows_content)
    mail = MailSender(payload)
    mail.send()


if __name__ == '__main__':
    process()
