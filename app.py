import streamlit as st


# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="EnglishMate AI",
    page_icon="📚",
    layout="centered"
)


# =====================================================
# SESSION SCORE
# =====================================================

if "score" not in st.session_state:
    st.session_state.score = 0

if "total_test" not in st.session_state:
    st.session_state.total_test = 0



# =====================================================
# CSS
# =====================================================

st.markdown(
"""
<style>

.main{
    background:#f8fafc;
}


.card{

background:white;
padding:25px;
border-radius:20px;
box-shadow:0 5px 20px rgba(0,0,0,0.08);
margin-bottom:20px;

}


.title{

font-size:45px;
font-weight:800;
color:#2563eb;

}


.subtitle{

font-size:18px;
color:#64748b;

}


.box{

background:#eff6ff;
padding:15px;
border-radius:15px;

}

</style>

""",
unsafe_allow_html=True
)



# =====================================================
# DATA
# =====================================================


GRAMMAR={

"A1":[

{
"name":"Present Simple",
"formula":"S + V(s/es)",
"use":"Thói quen, sự thật",
"example":"I go to school every day."
},

{
"name":"Present Continuous",
"formula":"S + am/is/are + V-ing",
"use":"Hành động đang xảy ra",
"example":"She is reading a book."
}

],


"A2":[

{
"name":"Present Perfect",
"formula":"S + have/has + V3",
"use":"Kinh nghiệm",
"example":"I have visited Hanoi."
}

],


"B1":[

{
"name":"Past Perfect",
"formula":"S + had + V3",
"use":"Hành động xảy ra trước quá khứ",
"example":"She had left before I came."
}

],


"B2":[

{
"name":"Future Perfect",
"formula":"S + will have + V3",
"use":"Hoàn thành trước tương lai",
"example":"I will have finished."
}

],


"C1":[

{
"name":"Conditional Sentences",
"formula":"Had + S + V3",
"use":"Câu điều kiện nâng cao",
"example":"Had I known, I would have helped."
}

]

}



VOCAB={

"A1":[
("apple","quả táo"),
("book","quyển sách"),
("teacher","giáo viên"),
("school","trường học"),
("friend","bạn bè")
],

"A2":[
("journey","chuyến đi"),
("healthy","khỏe mạnh"),
("environment","môi trường")
],

"B1":[
("achievement","thành tựu"),
("experience","kinh nghiệm"),
("opportunity","cơ hội")
],

"B2":[
("significant","quan trọng"),
("perspective","góc nhìn")
],

"C1":[
("comprehensive","toàn diện"),
("controversial","gây tranh cãi")
]

}



IRREGULAR=[

["go","went","gone","đi"],
["eat","ate","eaten","ăn"],
["write","wrote","written","viết"],
["see","saw","seen","nhìn"],
["take","took","taken","lấy"],
["make","made","made","làm"],
["give","gave","given","cho"],
["come","came","come","đến"]

]



QUIZ={


"A1":[

{
"q":"She ___ a student.",
"a":["am","is","are"],
"answer":"is"
},

{
"q":"I ___ to school every day.",
"a":["go","goes","going"],
"answer":"go"
},

{
"q":"They ___ football now.",
"a":["play","are playing","played"],
"answer":"are playing"
}

],


"A2":[

{
"q":"I have ___ this book.",
"a":["read","reading","reads"],
"answer":"read"
}

],


"B1":[

{
"q":"If I ___ rich, I would travel.",
"a":["am","were","be"],
"answer":"were"
}

],


"B2":[

{
"q":"I ___ finished by tomorrow.",
"a":["will have","have","had"],
"answer":"will have"
}

],


"C1":[

{
"q":"Had I known, I ___ earlier.",
"a":["come","would have come","came"],
"answer":"would have come"
}

]

}



# =====================================================
# SIDEBAR
# =====================================================


st.sidebar.title(
"📚 EnglishMate AI"
)


level=st.sidebar.selectbox(
"Choose Level",
[
"A1",
"A2",
"B1",
"B2",
"C1"
]
)


menu=st.sidebar.radio(
"Learning",

[
"🏠 Dashboard",
"📘 Grammar",
"📚 Vocabulary",
"🔄 Irregular Verb",
"📝 Test",
"✍ Writing",
"🎧 Listening",
"🎤 Speaking"
]

)



# =====================================================
# DASHBOARD
# =====================================================


if menu=="🏠 Dashboard":


    st.markdown(
"""
<div class="card">

<div class="title">
EnglishMate AI
</div>

<p class="subtitle">
Smart English Learning Platform
</p>

Grammar • Vocabulary • Listening • Speaking

</div>
""",
unsafe_allow_html=True
)



    c1,c2,c3=st.columns(3)


    c1.metric(
        "Vocabulary",
        "520"
    )

    c2.metric(
        "Tests",
        st.session_state.total_test
    )

    c3.metric(
        "Score",
        st.session_state.score
    )


    st.subheader(
        "Learning Progress"
    )


    st.progress(
        0.75
    )


    st.success(
        "Keep learning every day!"
    )



# =====================================================
# GRAMMAR
# =====================================================


elif menu=="📘 Grammar":


    st.title(
        "📘 Grammar"
    )


    for item in GRAMMAR[level]:

        with st.expander(item["name"]):

            st.code(
                item["formula"]
            )

            st.write(
                item["use"]
            )

            st.success(
                item["example"]
            )



# =====================================================
# VOCAB
# =====================================================


elif menu=="📚 Vocabulary":


    st.title(
        "📚 Vocabulary"
    )


    search=st.text_input(
        "Search word"
    )


    for word,meaning in VOCAB[level]:


        if search.lower() in word.lower():

            st.info(
                f"{word} : {meaning}"
            )



# =====================================================
# IRREGULAR
# =====================================================


elif menu=="🔄 Irregular Verb":


    st.title(
        "🔄 Irregular Verb"
    )


    st.table(
        IRREGULAR
    )



# =====================================================
# TEST
# =====================================================


elif menu=="📝 Test":


    st.title(
        "📝 Placement Test"
    )


    questions=QUIZ[level]


    score=0


    answers=[]


    for i,q in enumerate(questions):

        ans=st.radio(
            q["q"],
            q["a"],
            key=i
        )

        answers.append(ans)



    if st.button(
        "Submit Test"
    ):


        for ans,q in zip(
            answers,
            questions
        ):

            if ans==q["answer"]:
                score+=1



        st.session_state.score=score

        st.session_state.total_test+=1



        percent=int(
            score/len(questions)*100
        )


        st.success(
            f"Result: {score}/{len(questions)} ({percent}%)"
        )


        if percent>=80:

            st.balloons()

            st.info(
                "Excellent!"
            )

        elif percent>=50:

            st.warning(
                "Good job. Keep practicing!"
            )

        else:

            st.error(
                "Need more practice!"
            )



# =====================================================
# WRITING
# =====================================================


elif menu=="✍ Writing":


    st.title(
        "✍ Writing Practice"
    )


    topic=st.selectbox(
        "Topic",
        [
        "Introduce yourself",
        "My hobby",
        "Technology",
        "Future career"
        ]
    )


    st.info(
        topic
    )


    text=st.text_area(
        "Write your essay",
        height=200
    )


    if text:

        st.metric(
            "Word count",
            len(text.split())
        )



# =====================================================
# LISTENING
# =====================================================


elif menu=="🎧 Listening":


    st.title(
        "🎧 Listening"
    )


    st.write(
"""
Anna is a student.

She likes reading books.

Question:

What does Anna like?
"""
)


    st.radio(
        "Answer",
        [
        "Reading books",
        "Football",
        "Cooking"
        ]
    )



# =====================================================
# SPEAKING
# =====================================================


elif menu=="🎤 Speaking":


    st.title(
        "🎤 Speaking"
    )


    st.info(
"""
Topic:

Introduce yourself.

Speak for 1 minute.
"""
)


    audio=st.audio_input(
        "Record your voice"
    )


    if audio:

        st.audio(
            audio
        )

        st.success(
            "Recording completed!"
        )
