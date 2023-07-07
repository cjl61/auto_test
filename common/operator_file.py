import yaml
import jsonpath

def operator_yaml(file='../config/desired_caps_android.yaml',mode='r',encoding='utf-8'):
    with open(file=file,mode=mode,encoding=encoding) as f:
        data = yaml.load(f,Loader=yaml.Loader)
    return data

if __name__ == '__main__':
    data = operator_yaml()
    print(data)
    print(type(operator_yaml()))
    uuid = jsonpath.jsonpath(data,'$.uuid')
    print(uuid)