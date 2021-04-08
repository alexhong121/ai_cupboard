# 忘記密碼提交帳號

忘記密碼時 提交帳號進行註冊題目答案驗證 在修改密碼

**URL** : `/api/profiles/psforget`

**Method** : `POST`

**Auth required** : NO

**Data type required**: `FORM-DATA`

**Data constraints**

```json
{
    "username":"[帳號]"
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data": [
        "uid":"[user`s id]"
    ],
    "message": "account is correct"
}
```

## Error Response

**Condition** : 無法正常讀取.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "type": "error",
    "data":  null,
    "messsage":"[error messsage]"
}
```