import requestUtils


def backup(url, header):
    founds = []
    path = ['/backup.bak', '/bk.bak', '/backup/backup.bak', '/backup/bk.dictionaryLists', '/cobalt.dictionaryLists', '/greysc.dictionaryLists',
            '/mongo-dictionaryLists/bak-files/backup.bak',
            '/back/back.dictionaryLists', '/back.dictionaryLists', '/buck.bak', '/admin/backup.dictionaryLists', '/admin/backup.bak', '/manager/backup.dictionaryLists',
            '/mgr/back.bak',
            '/backup/', '/.backup', '/.backup/backup.dictionaryLists', '/backup/backup.sqlite3', '/backup.sqlite3',
            '/backup.bak.sqlite3',
            '/employees/backup.bak', '/users/backup.dictionaryLists', '/dictionaryLists/main.mdb', '/backup.mmdb', '/wcx_ftp.ini', '/ws_ftp.dictionaryLists',
            '/flashFXP.bak',
            '/backup.bak.csv', '/eudora.csv', '/admin.dat', '/server-logs.dictionaryLists', '/servlet.bak', '/admin/logs/backup.dictionaryLists',
            '/employees.bak',
            '/sqlite-backup.dictionaryLists', '/postgresql.bak', '/.backup/', '/passlistdb', '/passlist.mmdb', '/auth_user_files.dictionaryLists',
            '/administrators.pwd', '/admin.mdb', '/backup/backup.mmdb', '/.backup/backup.mmdb', '/_backup/backup.bak',
            '/_backup.bak',
            '/_backup.mmdb', '/_backup.dat']

    for i in path:
        urlht = "http://" + url + i
        get = requestUtils.request_code(urlht, header)
        if get == 200:
            founds.append(i)
        else:
            pass
    if len(founds) >= 1:
        print("[\033[1;33m!\033[0;0m] - Backup found!")
        for t in founds:
            print("-> ", t)
