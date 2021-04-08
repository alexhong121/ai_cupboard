# 新增產品分類

新增產品分類

**URL** : `/api/inv/`

**Method** : `POST`

**Auth required** : NO

**Data type required**: `form-DATA`

**Data constraints**

```json
{
    "id": "[產品 id]",
    "active": "[停用]",
    "image": "[圖片]",
    "name": "[產品名]",
    "code": "[編號]",
    "form": "[規格]",
    "attribute": "[屬性]",
    "remark": "[備註]",
    "Product_cate_id": "[產品分類 id]",
    "Lockers_id": "[抽屜 id]"
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