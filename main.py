import streamlit as st
from smallredbook import get_redbook_prompt

# 设置 Streamlit 应用的标题
st.title("小红书文案生成器")

# 在侧边栏中创建输入 Groq API 密钥的部分
with st.sidebar:
    # 使用密码输入类型隐藏 API 密钥输入
    groq_api_key = st.text_input("请输入Groq的API Key", type="password")
    # 添加获取 Groq API 密钥的链接
    st.markdown("[如何获取Groq API Key](https://console.groq.com/keys)")

# 创建输入主题的文本框
subject = st.text_input("请输入主题")

# 创建一个提交按钮
submit = st.button("生成文案")

# 检查是否点击了提交按钮且未提供 API 密钥
if submit and not groq_api_key:
    # 显示提示信息并停止执行
    st.info("请输入Groq的API Key")
    st.stop()

# 检查是否点击了提交按钮且未输入主题
if submit and not subject:
    # 显示提示信息并停止执行
    st.info("请输入主题")
    st.stop()

# 检查是否点击了提交按钮
if submit:
    # 在生成提示的时候显示一个 spinner
    with st.spinner("正在生成文案..."):
        # 调用 get_redbook_prompt 函数生成提示
        prompt = get_redbook_prompt(subject, groq_api_key)
    # 显示成功信息
    st.success("生成文案成功")
    # 添加一个分隔线
    st.divider()
    # 显示生成的提示
    st.write(prompt.content)