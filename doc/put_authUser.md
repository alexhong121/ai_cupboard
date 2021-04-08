# 修改個人訊息

修改個人訊息

**URL** : `api/profiles/authUser/uid=<int:pk>`

**Method** : `PUT`

**Auth required** : YES

**Data type required**: `Form-Data`

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
    "message": "The data is writed"
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