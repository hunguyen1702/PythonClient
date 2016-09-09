from swagger_builder import SwaggerBuilder


if __name__ == '__main__':
    name = 'fbcrawler_client'
    version = '1.2'
    service = 'http://192.168.15.242:1113/'
    SwaggerBuilder.generate_package(name, version, service)
