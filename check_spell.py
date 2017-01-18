# Author: Nguyen Hoai Nam

import commands
import os
import sys


def filter_spell(path_file, extensions):
    for ext in extensions:
        command = 'find %s -name "*.%s"| xargs cat | aspell --list | sort -u' % (path_file, ext)
        typos = commands.getstatusoutput(command)[1]
        typos_list = typos.split('\n')
        typos_list += typos_list
    return typos_list


def check_spell_again(list_word, current_folder):
    os.chdir(current_folder)
    list_word_finally = []
    for word in list_word:
        # print word
        command = 'grep -ron "%s" | grep -v "Binary" | wc -l' % word
        count = commands.getstatusoutput(command)[1]
        if len(count) >= 1:
            if int(count) >= 5:
                pass
            else:
                list_word_finally.append(word)
        elif len(count) == 0:
            pass
    return list_word_finally


def main():
    if len(sys.argv) == 1:
        path_file = os.getcwd()
        extension = ['py']
    elif len(sys.argv) == 2:
        path_file = sys.argv[1]
        extension = ['py']
    else:
        path_file = sys.argv[1]
        extension = sys.argv[2:]
    list_spell = filter_spell(path_file, extension)
    out_put = check_spell_again(list_spell, path_file)
    print out_put


if __name__ == '__main__':
    main()











