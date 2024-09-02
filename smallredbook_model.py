'''
此代码定义了一个名为 SmallRedBookModel 的数据模型类，用于描述小红书的内容结构，其中包括5个主题和正文内容。
使用了Pydantic库的 BaseModel 和 Field 来定义和验证字段类型及其属性。
'''
# 导入所需的模块
from pydantic import BaseModel, Field  # 从langchain_core.pydantic_v1模块导入BaseModel和Field类，用于数据模型定义
from typing import List  # 从typing模块导入List，用于定义字段的类型

# 定义一个数据模型类，用于描述小红书的结构
class SmallRedBookModel(BaseModel):
    # 定义一个名为titles的字段，用于存储小红书的5个主题
    titles: List[str] = Field(
        description="小红书的5个主题",  # 字段的描述，解释这个字段表示的内容
        example=[  # 提供一个示例值，用于在生成文档时显示示例值
            "标题1", "标题2", "标题3", "标题4", "标题5"
        ]
        #min_items=5,  # 最小数量限制，表示列表最少包含5个元素
        #max_items=5,  # 最大数量限制，表示列表最多包含5个元素
    )
    # 定义一个名为content的字段，用于存储小红书的正文
    content: str = Field(
        description="小红书的正文内容", # 字段的描述，解释这个字段表示的内容
        example="正文内容"# 提供一个示例值，用于在生成文档时显示示例值
    )
