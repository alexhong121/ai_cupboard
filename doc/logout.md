# 登出

登出系統

**URL** : `/api/profiles/logout`

**Method** : `GET`

**Auth required** : NO

**Data type required**: 

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
    "data": null,
    "message": "logout of the account"
}
```

## Error Response

**Condition** : 無法正常登出時

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "type": "error",
    "data":  null,
    "messsage":"[except error]"
}
```