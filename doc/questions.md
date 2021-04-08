# 讀取註冊問題題目

讀取註冊問題題目 list

**URL** : `/api/profiles/questions`

**Method** : `GET`

**Auth required** : NO

**Data type required**: `FORM`

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
            "id": "[題目 id]",
            "proposition": "[proposition]",
        }
    ],
    "message": null
}
```

## Error Response

**Condition** : 無法正常讀取.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "type": "error",
    "data":  null,
    "messsage":"[error messsage]"
}
```