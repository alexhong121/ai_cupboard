# 入庫

入庫

**URL** : `/api/inv/stock/enter/`

**Method** : `POST`

**Auth required** : NO

**Data type required**: `form-DATA`

**Data constraints**

```json
{
    "initial_value":"[初始值]",
    "in_value":"[入庫數量]",
    "Product_id":"[鏟品id]",
    "remark":"[備註]",
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