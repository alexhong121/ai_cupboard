# 讀取帳號列表

讀取帳號列表

**URL** : `/api/profiles/registration`

**Method** : `GET`

**Auth required** : NO

**Data type required**: `JSOM`

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
            "password": "加密過後密碼",
            "is_superuser": true,
            "username": "帳戶名",
            "is_staff": true,
            "is_active": true,
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