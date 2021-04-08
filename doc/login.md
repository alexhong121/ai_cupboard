# 登入

使用已註冊帳號 登入系統

**URL** : `/api/profiles/login`

**Method** : `POST`

**Auth required** : NO

**Data type required**: `FROM-DATA`

**Data constraints**

```json
{
    "username": "[account]]",
    "password": "[password in plain text]"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data":[
        "uid":"[account`s id]",
        "access":"[token]",
        "refresh":"[if access expired, refresh accesss ]",
    ],
    "messsage":
}
```

## Error Response

**Condition** : If 'username' and 'password' combination is wrong.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "type": "error",
    "data":  null,
    "messsage":"'username' and 'password' are wrong"
}
```