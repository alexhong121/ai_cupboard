# 新增部門

新增部門

**URL** : `/api/users/departments`

**Method** : `POST`

**Auth required** : YES

**Data type required**: `form-DATA`

**Data constraints**

```json
{
    "name": "[單位名]",
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