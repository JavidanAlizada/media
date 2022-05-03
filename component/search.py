import requests


def get_content(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    text = response.text.split("<div class=\"full-post-article\">")[1]
    text = text[0:text.rindex("<div class=\"post-tags\" itemprop=\"keywords\">")]
    content = ""
    if len(contents := text.split("<p>")) != 0:
        content = __get_content_by_p(contents)
    return content


def search_keyword_in_content(client_data, content):
    pass


def __get_content_by_span(contents):
    data = []
    e = contents.split("</span>")
    c = e[0]
    return c[c.rindex(">"):]
    # for content in contents:
    #     if not content.startswith('<'):
    #         data.append(content)
    # total_content = ""
    # if len(data) > 0:
    #     data[-1] = data[-1].split("</p>")[0]
    #     total_content = " ".join(data)
    # return total_content


def __get_content_by_p(contents):
    data = []
    for content in contents:
        if content.startswith("<span"):
            data.append(__get_content_by_span(content))
        elif (content.startswith('<strong>') or content.startswith('<i>') or content.startswith(
                '<b>')) or not content.startswith('<'):
            data.append(content)
    total_content = ""
    if len(data) > 0:
        data[-1] = data[-1].split("</p>")[0]
        total_content = " ".join(data)
    return total_content


def get_email_payload(data_flows):
    keywords = []
    result = []
    response_obj = []
    models = []
    for data_flow in data_flows:
        model = {"client": data_flow['client']}
        response_obj.append(model)
        for link_keyword in data_flow['link_keyword']:
            obj = {"keyword": "", "link": []}
            if link_keyword['keyword'] not in keywords:
                keywords.append(link_keyword['keyword'])
                obj['keyword'] = link_keyword['keyword']
                obj['link'].append(link_keyword['link'])
                result.append(obj)
            else:
                for res_obj in result:
                    if res_obj['keyword'] == link_keyword['keyword']:
                        res_obj['link'].append(link_keyword['link'])
                        continue
        model['link_keyword'] = result.copy()
        models.append(model)
        result.clear()
    return response_obj
