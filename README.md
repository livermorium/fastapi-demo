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