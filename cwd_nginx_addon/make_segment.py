#!/usr/bin/env python
# powerline-shell/nginx_addon/update_segment.py
# Author: H.Alper Tuna <halpertuna@gmail.com>
# Date: 02.09.2016

import commands
import os
import sys

sys.path.append('cwd_nginx_addon')
import addon_config

class Server:
    server_name = ''
    root = ''

    def setContent(self, key, value):
        if value == '':
            return

        if value[-1] == ';':
            value = value[:-1]

        if key == 'server_name':
            if value == '_':
                return

            self.server_name = '\'' + value + '\''
            return

        if key == 'root':
            self.root = '\'' + value + '\''
            return

    def isReady(self):
        return self.server_name != '' and self.root != ''

contents = commands.getstatusoutput("cat " + addon_config.NGINX_SITE_CONF_FILES + "  | grep 'server {\|root\|server_name'")[1].split('\n')
source_root_list = []
source_server_list = []
for line in contents:
    if line == 'server {':
        server = Server()
    lineContents = line.strip().split(' ')
    server.setContent(lineContents[0], lineContents[1])

    if server.isReady():
        source_root_list.append(server.root)
        source_server_list.append(server.server_name)


source = 'NGINX_ROOT_LIST = [\n' + ',\n'.join(source_root_list) + '\n]\n'
source += 'NGINX_SERVER_LIST = [\n' + ',\n'.join(source_server_list) + '\n]\n'
source += 'NGINX_SERVER_ICON = u\'' + addon_config.NGINX_SERVER_ICON.encode('utf-8') + '\'\n\n'
source += ''.join(open('cwd_nginx_addon/addon_temp.py').readlines())

OUTPUT_FILE = 'segments/cwd_nginx_addon.py'
open(OUTPUT_FILE, 'w').write(source)

print '"cwd_nginx_addon" segment is updated.'
