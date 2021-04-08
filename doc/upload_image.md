# 上傳圖片

上傳個人訊息圖片

**URL** : `/api/profiles/image/uid=<uid>`

**Method** : `POST`

**Auth required** : YES

**Data type required**: `Form-Data`

**Data constraints**

```json
{
    "image_url": "上傳圖片檔案"
}

```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "type": "success",
    "data":null,
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