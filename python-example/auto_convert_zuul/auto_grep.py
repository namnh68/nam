import os
import yaml
import sys

INPUT_FILE = '/home/stack/infra-openstack/openstack-zuul-jobs/' \
             'zuul.d/zuul-legacy-jobs.yaml'
HEADER_FILE = '/home/stack/infra-openstack/openstack-zuul-jobs'
CURRENT_PATH = os.getcwd()


class IndentDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


def read_yaml(name_file):
    with open(name_file, 'r') as f:
        content_list = yaml.safe_load(f)
    return content_list


def auto_grep(key_word):
    content_list = read_yaml(INPUT_FILE)
    content_after = []
    for i in content_list:
        name = i.get('job').get('name')
        if key_word in name:
            content_after.append(i)
    path_output = CURRENT_PATH + '/projects/' + key_word + '.yaml'
    with open(path_output, 'w') as f:
        stream = yaml.dump(content_after, Dumper=IndentDumper,
                           default_flow_style=False)
        f.write(stream.replace('\n- ', '\n\n- '))


def main():
    keywords = sys.argv[1:]
    for keyword in keywords:
        auto_grep(keyword)


if __name__ == '__main__':
    main()
