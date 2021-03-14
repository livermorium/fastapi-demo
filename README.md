# fastapi-demo

## 第一步
* 导入 FastAPI。
* 创建一个 app 实例。
* 编写一个路径操作装饰器（如 @app.get("/")）。
* 编写一个路径操作函数（如上面的 def root(): ...）。
* 运行开发服务器（如 uvicorn main:app --reload）。

## 路径参数
* 路径操作是按顺序依次运行的（匹配多个，函数定义顺序决定使用哪个）
* Enum 枚举类型限定输入

* 编辑器支持：错误检查，代码补全等
* 数据 "解析"
* 数据校验
* API 标注和自动生成的文档

## 查询参数

声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数
## 请求体
* The same as when declaring query parameters, when a model attribute has a default value, it is not required. Otherwise, it is required. Use None to make it just optional.
* FastAPI will recognize that the function parameters that match path parameters should be taken from the path, and that function parameters that are declared to be Pydantic models should be taken from the request body.

## Query Parameters and String Validations
* Query(None, min_length=3, max_length=50, regex="^fixedquery$")
* Query(..., min_length=3)
* LIST
  * http://localhost:8000/items/?q=foo&q=bar
  * async def read_items(q: Optional[List[str]] = Query(None)):
* alias: not valid python var
* deprecated
* title
* description
* ...: no default value, required

## Path Parameters and Numeric Validations
* The same way you can declare more validations and metadata for query parameters with Query, you can declare the same type of validations and metadata for path parameters with Path.
* add * in parameter -> parameter with key-value: Order the parameters as you need, tricks
* Number validations: ge, gt, le, lt

## Body - Multiple Parameters
* use the parameter names as keys (field names) in the body: 与只有一个的声明类似，表意差别明显
* instruct FastAPI to treat it as another body key using Body: Body
* But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed