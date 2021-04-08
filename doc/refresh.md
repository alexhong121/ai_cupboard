# 重新獲取access token

重新獲取access token

**URL** : `/api/profiles/token/refresh/`

**Method** : `POST`

**Auth required** : NO

**Data type required**: `FORM-DATA`

**Data constraints**

```json
{
    "refresh":"[refresh token]"
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
            "access":"[new access token]"
        }
    ],
    "message": null
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