# 讀取頁面權限

讀取頁面權限

**URL** : `/api/access/ui/uid=<uid>`

**Method** : `GET`

**Auth required** : YES

**Data type required**: NO

**Data constraints**

```json
{
    
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data": [
        {
            "id": 1,
            "name": "[頁面名]",
            "perm_read": "[讀取]",
            "perm_unlink": "[刪除]",
            "perm_write": "[修改]",
            "perm_create": "[新增]",
            "Profiles_id": "[個人訊息 id]",
            "Functions_id": "[主功能 id]"
        }
    ],
    "message": null
}
```

## Error Response

**Condition** : 無法正常註冊程序.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "type": "error",
    "data":  null,
    "messsage":"[error messsage]"
}
```