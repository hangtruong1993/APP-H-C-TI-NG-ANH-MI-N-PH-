
import streamlit as st

st.set_page_config(
    page_title="EnglishMate AI",
    page_icon="📚"
)

st.title("EnglishMate AI")

st.write("Smart English Learning Platform")

st.sidebar.title("EnglishMate AI")

menu = st.sidebar.radio(
    "Chức năng",
    [
        "Dashboard",
        "Grammar - 12 Tenses",
        "Vocabulary",
        "Irregular Verb",
        "Test",
        "Writing",
        "Listening",
        "Speaking"
    ]
)

TENSES = [
("Present Simple","S + V(s/es)","I go to school every day."),
("Present Continuous","S + am/is/are + V-ing","She is reading."),
("Present Perfect","S + have/has + V3","I have finished."),
("Present Perfect Continuous","S + have/has been + V-ing","I have been studying."),
("Past Simple","S + V2/ed","I visited Hanoi."),
("Past Continuous","S + was/were + V-ing","I was studying."),
("Past Perfect","S + had + V3","She had left."),
("Past Perfect Continuous","S + had been + V-ing","He had been working."),
("Future Simple","S + will + V","I will go."),
("Future Continuous","S + will be + V-ing","I will be studying."),
("Future Perfect","S + will have + V3","I will have finished."),
("Future Perfect Continuous","S + will have been + V-ing","I will have been learning.")
]

QUIZ = {
"A1":[
("She ___ a student.",["is","are","am","be"],"is"),
("I ___ to school every day.",["go","goes","going","gone"],"go")
],
"A2":[
("I have ___ English for 3 years.",["learn","learned","learning","learns"],"learned")
],
"B1":[
("If I ___ you, I would study harder.",["am","were","be","was"],"were")
],
"B2":[
("By next year I ___ my course.",["finish","finished","will have finished","finishing"],"will have finished"),
],
"C1":[
("Had I known, I ___ earlier.",["come","came","would have come","coming"],"would have come")
]
}

if menu == "Dashboard":
    st.success("Learn - Practice - Improve")

elif menu == "Grammar - 12 Tenses":
    st.header("📘 12 English Tenses")
    for name, formula, ex in TENSES:
        with st.expander(name):
            st.code(formula)
            st.write(ex)

elif menu == "Vocabulary":
    st.header("📚 Vocabulary")
    st.write("A1 - C1 Vocabulary system")

elif menu == "Irregular Verb":
    st.header("🔄 Irregular Verbs")
    st.table([
        ["go","went","gone"],
        ["eat","ate","eaten"],
        ["write","wrote","written"]
    ])

elif menu == "Test":
    st.header("📝 English Test")
    level = st.selectbox("Level", list(QUIZ.keys()))
    answers = []

    for i,q in enumerate(QUIZ[level]):
        ans = st.radio(
            q[0],
            ["A. "+x for x in q[1]],
            key=i
        )
        answers.append(ans)

    if st.button("Nộp bài"):
        score = 0
        for ans,q in zip(answers, QUIZ[level]):
            if ans == "A. "+q[2]:
                score += 1
        st.success(f"Kết quả: {score}/{len(QUIZ[level])}")

elif menu == "Writing":
    st.header("✍ Writing")
    text = st.text_area("Write your essay")
    if text:
        st.info(f"Words: {len(text.split())}")

elif menu == "Listening":
    st.header("🎧 Listening")
    st.write("Anna is a student. She likes reading books.")

elif menu == "Speaking":
    st.header("🎤 Speaking")
    audio = st.audio_input("Record your voice")
    if audio:
        st.audio(audio)
