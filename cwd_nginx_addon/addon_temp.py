import os

def add_cwd_nginx_addon_segment(powerline):
    cwd = powerline.cwd or os.getenv('PWD')

    if cwd[0] == '~':
        long_cwd = os.environ['HOME'] + cwd[1:]
    else:
        long_cwd = cwd

    for i in range(len(NGINX_ROOT_LIST)):
        server_root = NGINX_ROOT_LIST[i]
        server_root_len = len(server_root)
        if long_cwd[:server_root_len] == server_root:
            powerline.cwd = (NGINX_SERVER_ICON + ' ' + NGINX_SERVER_LIST[i] + long_cwd[server_root_len:]).encode('utf-8')
            return
    return
