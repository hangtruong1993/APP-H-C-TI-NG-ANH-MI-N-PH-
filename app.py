
import streamlit as st

st.set_page_config(
    page_title="EnglishMate AI",
    page_icon="📚"
)

st.markdown("""
<style>
.card{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 5px 20px rgba(0,0,0,.08);
}
.title{
font-size:42px;
font-weight:800;
color:#2563eb;
}
</style>
""", unsafe_allow_html=True)

TENSES = [
("Present Simple","S + V(s/es)","Thói quen, sự thật","I go to school every day."),
("Present Continuous","S + am/is/are + V-ing","Đang xảy ra","She is reading a book."),
("Present Perfect","S + have/has + V3","Kinh nghiệm, kết quả","I have finished my homework."),
("Present Perfect Continuous","S + have/has been + V-ing","Nhấn mạnh quá trình","I have been studying for 2 hours."),
("Past Simple","S + V2/ed","Đã xảy ra trong quá khứ","I visited Hanoi."),
("Past Continuous","S + was/were + V-ing","Đang xảy ra trong quá khứ","I was watching TV."),
("Past Perfect","S + had + V3","Xảy ra trước quá khứ","She had left before I came."),
("Past Perfect Continuous","S + had been + V-ing","Quá trình trước quá khứ","He had been working."),
("Future Simple","S + will + V","Tương lai","I will help you."),
("Future Continuous","S + will be + V-ing","Đang diễn ra tương lai","I will be studying."),
("Future Perfect","S + will have + V3","Hoàn thành trước tương lai","I will have finished."),
("Future Perfect Continuous","S + will have been + V-ing","Nhấn mạnh thời gian tương lai","I will have been learning English.")
]

VOCAB = {
"A1":[("apple","quả táo"),("school","trường học"),("teacher","giáo viên")],
"A2":[("journey","chuyến đi"),("healthy","khỏe mạnh")],
"B1":[("achievement","thành tựu"),("experience","kinh nghiệm")],
"B2":[("significant","quan trọng")],
"C1":[("comprehensive","toàn diện")]
}

IRREGULAR = [
["go","went","gone","đi"],
["eat","ate","eaten","ăn"],
["write","wrote","written","viết"],
["see","saw","seen","nhìn thấy"],
["take","took","taken","lấy"]
]

QUIZ = [
{"q":"She ___ English every day.","a":["study","studies","studying"],"c":"studies"},
{"q":"I ___ football yesterday.","a":["play","played","playing"],"c":"played"},
{"q":"They have ___ dinner.","a":["eat","ate","eaten"],"c":"eaten"}
]

if "score" not in st.session_state:
    st.session_state.score = 0

st.sidebar.title("EnglishMate AI")

menu = st.sidebar.radio(
    "Chức năng",
    ["Dashboard","Grammar","Vocabulary","Irregular Verb","Test","Writing","Listening","Speaking"]
)

level = st.sidebar.selectbox(
    "Level",
    ["A1","A2","B1","B2","C1"]
)

if menu == "Dashboard":
    st.markdown("""
    <div class="card">
    <div class="title">EnglishMate AI</div>
    <p>Smart English Learning Platform</p>
    Grammar • Vocabulary • Listening • Speaking
    </div>
    """, unsafe_allow_html=True)

    a,b,c = st.columns(3)
    a.metric("Vocabulary","520")
    b.metric("Tests","50")
    c.metric("Score",st.session_state.score)

elif menu == "Grammar":
    st.title("📘 12 English Tenses")
    for t in TENSES:
        with st.expander(t[0]):
            st.write("**Công thức:**",t[1])
            st.write("**Cách dùng:**",t[2])
            st.success(t[3])

elif menu == "Vocabulary":
    st.title("📚 Vocabulary")
    search = st.text_input("Tìm từ")
    for w,m in VOCAB[level]:
        if search.lower() in w.lower():
            st.info(f"{w} - {m}")

elif menu == "Irregular Verb":
    st.title("🔄 Irregular Verbs")
    st.table(IRREGULAR)

elif menu == "Test":
    st.title("📝 English Test")
    score = 0
    answers=[]
    for i,q in enumerate(QUIZ):
        ans=st.radio(q["q"],q["a"],key=i)
        answers.append(ans)
    if st.button("Chấm điểm"):
        for a,q in zip(answers,QUIZ):
            if a==q["c"]:
                score+=1
        st.session_state.score=score
        st.success(f"Kết quả: {score}/{len(QUIZ)}")

elif menu == "Writing":
    st.title("✍ Writing")
    text=st.text_area("Viết đoạn văn")
    if text:
        st.info(f"Số từ: {len(text.split())}")

elif menu == "Listening":
    st.title("🎧 Listening")
    st.write("Anna is a student. She likes reading books.")
    st.radio("What does Anna like?",["Reading books","Football","Cooking"])

elif menu == "Speaking":
    st.title("🎤 Speaking")
    st.write("Record your English speaking")
    audio=st.audio_input("Ghi âm")
    if audio:
        st.audio(audio)
