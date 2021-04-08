# 註冊

新增個人信息

**URL** : `/api/profiles/`

**Method** : `POST`

**Auth required** : YES

**Data type required**: `JSOM`

**Data constraints**

```json
{
    "params": {
        "Profiles_id": {
            "name": "[user`s name]"
        },
        "Answer_ids": [
            {
                "Questions_id": "[question`s id]",
                "answer": "[question answer]"
            }
        ],
        "AuthUser_id": {
            "username": "[account name]",
            "password": "[account password]"
        }
    }
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data": {
        "uid": "[new user`s id]"
    },
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