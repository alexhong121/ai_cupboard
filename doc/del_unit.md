# 刪除單位

刪除單位

**URL** : `/api/unit/<id>`

**Method** : `DELETE`

**Auth required** : YES

**Data type required**: no

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
    "data": null,
    "message": "the data is successfully deleted"
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