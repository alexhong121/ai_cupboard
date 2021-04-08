# 讀取抽屜

讀取抽屜數

**URL** : `/api/locker/`

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
            "location": "[抽屜位置 (座標表示 0,0)]",
            "code": "[編號]",
            "name": "[名子]",
            "lock_time": "[抽屜開啟時間]",
            "status": "[抽屜開啟狀態]",
            "Cabinet_id": "[櫃子 id]",
            "Pro_cate_id": "[產品分類 id]"
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