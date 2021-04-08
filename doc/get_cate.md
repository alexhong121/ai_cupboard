# 讀取產品分類

讀取產品分類

**URL** : `/api/unit/category/`

**Method** : `GET`

**Auth required** : YES

**Data type required**: NO

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
    "data": {
        "id": "[產品分類 id]",
        "name":"[單位名]",
        "code":"[編號]",
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