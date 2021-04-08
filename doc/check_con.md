# 檢查連線

檢查連線

**URL** : `/api/systems/connection`

**Method** : `GET`

**Auth required** : NO

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
    "data": null,
    "messsage":"message": "Successfully connected"
}
```

## Error Response

**Condition** : If 'username' and 'password' combination is wrong.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "type": "error",
    "data":  null,
    "messsage":"'username' and 'password' are wrong"
}
```