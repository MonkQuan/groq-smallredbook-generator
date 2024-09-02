import streamlit as st
from smallredbook import get_redbook_prompt

st.title("小红书文案生成器")

with st.sidebar:
    groq_api_key = st.text_input("请输入Groq的API Key",type="password")
    st.markdown("[如何获取Groq API Key](https://console.groq.com/keys)")

subject = st.text_input("请输入主题")
submit = st.button("生成文案")

if submit and not groq_api_key:
    st.info("请输入Groq的API Key")
    st.stop()
if submit and not subject:
    st.info("请输入主题")
    st.stop()
if submit:
    with (st.spinner("正在生成文案...")):
       prompt = get_redbook_prompt(subject, groq_api_key)
    st.success("生成文案成功")
    st.divider()
    st.write(prompt.content)