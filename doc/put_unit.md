# 修改單位

修改單位

**URL** : `/api/unit/<id>`

**Method** : `PUT`

**Auth required** : YES

**Data type required**: `form-Data`

**Data constraints**

```json
{
    "name": "[單位名]"
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