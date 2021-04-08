# 讀取部門

讀取部門

**URL** : `/api/users/departments`

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
        "id": "[部門 id]",
        "name":"[部門名]",
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