import streamlit as st
import random

# 제목
st.title("✊✋✌️ 가위 바위 보 게임")

# 사용자 입력
user_choice = st.radio("당신의 선택은?", ("가위", "바위", "보"))

# 컴퓨터 선택
choices = ["가위", "바위", "보"]
computer_choice = random.choice(choices)

# 게임 결과 판단 함수
def get_result(user, computer):
    if user == computer:
        return "비겼습니다! 😐"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "이겼습니다! 🎉"
    else:
        return "졌습니다... 😢"

# 버튼 클릭 시 실행
if st.button("결과 보기"):
    st.write(f"🧑 당신: {user_choice}")
    st.write(f"🤖 컴퓨터: {computer_choice}")
    result = get_result(user_choice, computer_choice)
    st.subheader(result)
