# 智能櫃api Doc

提供給手機app api

## 開放api
--------------------------------
不需要驗證 即可使用

* [登入](doc/login.md) : `POST /api/profiles/login`
* [登出](doc/logout.md) : `GET /api/profiles/logout`
* [註冊](doc/registration.md) : `POST /api/profiles/registration`
* [讀取題目](doc/questions.md) : `GET /api/profiles/questions`
* [驗證回答問題的答案](doc/questions_validation.md) : `POST /api/profiles/questions/validation`
* [忘記密碼提交驗證帳號](doc/psforget.md) : `POST /api/profiles/psforget`
* [refrush access token](doc/refresh.md) : `POST /api/profiles/token/refresh/`

## 封閉api
--------------------------------
需要取得驗證 token 方能進行訪問

### 個人訊息
--------------------------------
* [讀取個人訊息](doc/get_profiles.md) : `GET /api/profiles/uid=<id>`
* [修改個人訊息](doc/put_profiles.md) : `PUT /api/profiles/uid=<id>`
* [讀取帳號列表](doc/authUser.md) : `GET /api/profiles/authUser`
* [上傳圖片](doc/upload_image.md) : `POST /api/profiles/image/uid=<id>`
* [修改帳號](doc/put_authUser.md) : `POST /api/profiles/logout`

### 基本單位
--------------------------------
* [新增單位](doc/post_unit.md) : `POST /api/unit/`
* [修改單位](doc/put_unit.md) : `PUT /api/unit/<id>`
* [刪除單位](doc/del_unit.md) : `DELETE /api/unit/<id>`
* [讀取單位](doc/get_unit.md) : `GET /api/unit/`
* [讀取產品分類](doc/get_cate.md) : `GET /api/unit/category/`
* [新增產品分類](doc/post_cate.md) : `POST /api/unit/category/`
* [修改產品分類](doc/put_cate.md) : `PUT /api/unit/category/<id>`
* [刪除產品分類](doc/del_cate.md) : `DELETE /api/unit/category/<id>`

### 部門
--------------------------------
* [新增部門](doc/post_department.md) : `POST /api/users/departments`
* [刪除部門](doc/del_department.md) : `DELETE /api/users/departments/<id>`
* [修改部門](doc/put_department.md) : `PUT /api/users/departments/<id>`
* [讀取部門](doc/get_department.md) : `GET /api/users/departments`
  
### 權限
--------------------------------
* [讀取頁面權限](doc/get_UI.md) : `GET /api/access/ui/uid=<uid>`
* [修改頁面權限](doc/put_UI.md) : `PUT /api/access/ui/uid=<uid>`
  
### 庫存
--------------------------------
* [讀取產品](doc/get_product.md) : `GET /api/inv/`
* [新增產品](doc/post_product.md) : `POST /api/inv/`
* [修改產品](doc/put_product.md) : `PUT /api/inv/`
* [入庫](doc/in_inv.md) : `POST /api/inv/stock/enter`
* [出庫](doc/out_inv.md) : `POST /api/inv/stock/out/`
* [讀取當前產品庫存量](doc/get_currect.md) : `GET /api/inv/stock/product/<id>`
  
### 櫃子
--------------------------------
* [讀取櫃子資訊](doc/get_cupboard.md) : `GET /api/locker/cabinet`
* [讀取抽屜](doc/get_locker.md) : `GET /api/locker/`

### 系統
--------------------------------
* [讀取管理抽屜模式](doc/get_mode.md) : `GET /api/systems/configuration`
* [檢查連線](doc/check_con.md) : `GET /api/systems/connection`
