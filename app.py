import streamlit as st
import pandas as pd

st.set_page_config(page_title="학생 이수시간 조회", layout="centered")
st.title("📘 학생 이수시간 조회 시스템")

st.write("이름과 생년월일을 입력하면 해당 학생의 정보를 확인할 수 있습니다.")

# 엑셀 파일 읽기 (GitHub에 같이 올린 파일)
df = pd.read_excel("time.xlsx")  # students.xlsx 이름 그대로 사용

st.subheader("🔍 학생 정보 입력")
name = st.text_input("이름")
birth = st.text_input("생년월일 (YYYYMMDD)")

if st.button("조회하기"):
    if name.strip() == "" or birth.strip() == "":
        st.warning("이름과 생년월일을 모두 입력해주세요.")
    else:
        result = df[
            (df["이름"].astype(str).str.strip() == name.strip()) &
            (df["생년월일"].astype(str).str.contains(birth.replace("-", "").strip()))
        ]

        if len(result) == 0:
            st.error("❌ 일치하는 학생이 없습니다.")
        else:
            st.success("✅ 조회 성공!")
            st.dataframe(result, use_container_width=True)
