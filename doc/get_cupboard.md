# 讀取櫃子資訊

讀取櫃子資訊

**URL** : `/api/locker/cabinet`

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
    "data": [
        {
            "id": 1,
            "name": "[櫃子名]",
            "column": "[列]",
            "row": "[行]"
        }
    ],
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