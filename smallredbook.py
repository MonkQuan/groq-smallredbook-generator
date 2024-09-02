'''
此代码旨在通过LangChain框架与聊天模型进行交互，使用特定的API密钥进行身份验证，并以结构化的格式处理输出。每个部分都是模块化的，允许在提示设计、
模型选择和输出处理方面具有灵活性。
'''
# 导入所需的模块
from langchain_groq import ChatGroq  # 从langchain_groq模块导入聊天模型类
from langchain_core.prompts import ChatPromptTemplate  # 从langchain_core模块导入聊天提示模板类
from langchain_core.output_parsers import PydanticOutputParser  # 从langchain_core模块导入输出解析器类
from smallredbook_model import SmallRedBookModel  # 导入自定义数据模型SmallRedBookModel
from prompt_template import system_template_text, user_template_text  # 导入预定义的系统和用户提示模板文本
import os  # 导入os模块，用于操作系统相关功能（如环境变量）
import json  # 导入JSON模块用于格式化输出

def get_redbook_prompt(subject, groq_api_key):
    # 创建聊天提示模板，使用预定义的系统和用户消息
    subject_prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])

    # 创建聊天模型实例
    model = ChatGroq(
        model="llama3-8b-8192",
        api_key=groq_api_key,
    )

    # 创建输出解析器
    output_parser = PydanticOutputParser(pydantic_object=SmallRedBookModel)

    parser_instructions = output_parser.get_format_instructions()

    # 确保提示模板、模型和输出解析器之间兼容，并将它们链式组合在一起
    chain = subject_prompt | model

    # 调用链式组合，传递所需的输入变量以生成响应
    response = chain.invoke({
        "parser_instructions": parser_instructions,
        "theme": subject
    })

    # 返回格式化后的响应
    return response

# 调用函数并打印结果
# 使用特定主题调用函数，并打印结果
# print(get_redbook_prompt("户外旅行", os.getenv("GROQ_API_KEY")))  # 从环境变量中获取API密钥