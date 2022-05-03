from configparser import ConfigParser
from enum import Enum

configuration = ConfigParser()
configuration.read("D:/tools/conf/credentials.ini")
credentials = dict(configuration["CREDENTIALS"])


class MailConfig(Enum):
    email = credentials.get("email")
    password = credentials.get("password")


url = 'https://azerforum.com/latest'
db_config = {}
mail_config = {}
database_folder = "./database_tables"
client_file = f"{database_folder}/client.json"
data_flow_file = f"{database_folder}/data_flow.json"
keyword_file = f"{database_folder}/keyword.json"
media_link_file = f"{database_folder}/media_link.json"
excel_file = '../excel/media_marketing.xlsx'
excel2json_file = './examples/example_excel_content.json'
generated_json_file_path = '../examples/generated_json_data.json'
data_content = {
    "contents": [
        {
            "email": "",
            "keywords": [],
            "time_period": 0
        },
        {
            "email": "",
            "keywords": [],
            "time_period": 0
        },
        {
            "email": "",
            "keywords": [],
            "time_period": 0
        }
    ]
}
