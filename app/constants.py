# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
SuisenGalleryApi V0.1
@author: marunowork 
"""
## constants
TAGNAME = "黒岩水仙郷"                               ## 検索タグ名
JSON_FILE_NAME = TAGNAME + '/' + TAGNAME + '.json'  ## 取得ファイル名（json）
UPDATE_MAX_YYYY = 9999                              ## 更新日時の最大
UPDATE_MAX_MM = 12                                  ## 更新日時の最大
UPDATE_MAX_DD = 31                                  ## 更新日時の最大
EXPIRE_DAYS = 1                                     ## ファイル使用期限（日数）
LIST_MAXNUM = 10                                    ## 最大取得数
IS_QUIET_MODE = False                               ## サイレントモード
