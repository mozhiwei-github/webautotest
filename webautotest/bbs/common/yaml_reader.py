from yaml import load, FullLoader

"""yaml文件相关操作"""

class YamlReader:
    @staticmethod
    def read_yaml(yaml_path):
        try:
            dict_data = load(open(yaml_path, 'r', encoding="utf-8"), Loader=FullLoader)
            return dict_data
        except Exception as e:
            raise Exception('读取{0}文件出错，error={1}'.format(yaml_path, e))

if __name__ == '__main__':
    import os
    import pprint
    import logging

    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logging.debug("root_path = %s" % root_path)
    file_path = os.path.join(root_path, "common", "config", "config.yml")
    logging.debug("yaml_path = %s" %file_path)

    reader = YamlReader()
    result = reader.read_yaml(file_path)
    pprint.pprint(result)