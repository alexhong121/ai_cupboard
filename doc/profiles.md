# 讀取個人訊息

讀取個人使用者的訊息

**URL** : `/api/profiles/uid=<id>`

**Method** : `GET`

**Auth required** : yes

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
            "id": 32,
            "image_url": "/media/images/878168.jpg",
            "name": "111",
            "alias": null,
            "email": null,
            "phone": null,
            "remark": "",
            "create_uid": null,
            "write_uid": null,
            "Departments_id": null,
            "AuthUser_id": {
                "id": 70,
                "password": 
                "is_superuser": false,
                "username": "xxa",
                "first_name": "",
                "last_name": "",
                "is_staff": false,
                "is_active": true
            }
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