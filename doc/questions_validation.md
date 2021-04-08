# 驗證回答問題答案

驗證回答問題答案

**URL** : `/api/profiles/questions/validation`

**Method** : `POST`

**Auth required** : NO

**Data type required**: `FORM-DATA`

**Data constraints**

```json
{
    "Questions_id":"[題目 id]",
    "answer":"[answer]",
    "uid":"[user`s id]"
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data": null,
    "message": "answer is correct"
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