# 修改個人訊息

修改個人訊息

**URL** : `/api/profiles/uid=<id>`

**Method** : `PUT`

**Auth required** : YES

**Data type required**: `form-DATA`

**Data constraints**

```json
{
    "已修改的欄位":"數據"
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data": null,
    "message": "The user is writed"
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