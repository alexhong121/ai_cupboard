
import shutil,os
from datetime import date


def backup_db():
    now=date.today()
    src='./db.sqlite3'
    dst='./ai_cupboard/backup/db-%s.bak' % now
    
    if os.path.exists(src):
        shutil.copy(src,dst)
    else:
        return "資料庫不存在"
    return "備份完成"

def listdir_db():
    print(os.listdir('./backup'))
    return os.listdir('./backup')


    