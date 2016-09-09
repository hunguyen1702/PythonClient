import ssl

import requests
import json
import urllib
import os
import yaml


class SwaggerBuilder:
    name = None
    version = None
    service = None
    output = os.getcwd()

    def __init__(self):
        pass

    @staticmethod
    def generate_package(name, version, service, output=None):
        SwaggerBuilder.name = name
        SwaggerBuilder.version = version
        SwaggerBuilder.service = service
        if output is not None:
            SwaggerBuilder.output = output
        data = SwaggerBuilder.generate_data()
        SwaggerBuilder.generate_package_folder(data)

    @staticmethod
    def generate_data():
        url = "{}/spec-files/default.yaml".format(SwaggerBuilder.service)
        stream = urllib.urlopen(url).read()
        package_data = {}
        spec = yaml.load(stream)
        package_data["spec"] = spec
        package_data["options"] = {
            "packageName": SwaggerBuilder.name,
            "packageVersion": SwaggerBuilder.version
        }
        return package_data

    @staticmethod
    def generate_package_folder(package_data):
        executed_path = os.getcwd()
        save_path = os.path.join(executed_path, "client.zip")
        url = "http://generator.swagger.io/api/gen/clients/python"
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'}
        r = requests.post(url, data=json.dumps(package_data), headers=headers)
        link = r.json()['link']
        context = ssl._create_unverified_context()
        client_file = urllib.URLopener(context=context)
        client_file.retrieve(link, save_path)
        os.system("cd {}; unzip -o client.zip".format(executed_path))
        os.system("cd {}; rm -rf client.zip".format(executed_path))
        os.system("cd {}; mv python-client {}".format(executed_path, SwaggerBuilder.name))

