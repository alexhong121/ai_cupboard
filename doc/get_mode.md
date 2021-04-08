# 讀取管理抽屜模式

讀取管理抽屜模式

**URL** : `/api/systems/configuration`

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
        "drawer_mod": "[抽屜模式(dra:抽屜,pro_cate:產品分類)]"
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