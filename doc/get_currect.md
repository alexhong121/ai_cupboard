# 讀取當前產品庫存量

讀取當前產品庫存量

**URL** : `/api/inv/stock/product/<id>`

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
        "initial_value": "[初始數量]",
        "out_value": "[出庫總數]",
        "in_value": "[入庫總數]",
        "current_value": "[當前庫存數量]"
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