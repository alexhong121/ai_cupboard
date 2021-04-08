# 修改頁面權限

修改頁面權限

**URL** : `/api/access/ui/uid=<uid>`

**Method** : `PUT`

**Auth required** : YES

**Data type required**: `form-Data`

**Data constraints**

```json
{
    "已修改的欄位": "[數據]"
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data": null,
    "message": "the data is created"
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