import streamlit as st


# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="English Master",
    page_icon="🇬🇧",
    layout="wide"
)


# =====================================================
# CSS
# =====================================================

st.markdown(
"""
<style>

body{
    background:#f5f7fb;
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

font-size:20px;
color:#64748b;

}


.badge{

background:#dbeafe;
padding:8px 15px;
border-radius:20px;
color:#1d4ed8;

}


</style>

""",
unsafe_allow_html=True
)



# =====================================================
# DATA
# =====================================================


GRAMMAR = {

"A1":[

{
"name":"Present Simple - Hiện tại đơn",
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




VOCAB = {


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
["see","saw","seen","nhìn thấy"],
["take","took","taken","lấy"],
["make","made","made","làm"],
["give","gave","given","cho"],
["come","came","come","đến"]

]



QUIZ=[

{
"question":
"She ___ English every day",

"options":
[
"study",
"studies",
"studying"
],

"answer":
"studies"

},


{
"question":
"I ___ football yesterday",

"options":
[
"play",
"played",
"playing"
],

"answer":
"played"

},


{
"question":
"They have ___ dinner",

"options":
[
"eat",
"ate",
"eaten"
],

"answer":
"eaten"

}

]



# =====================================================
# SIDEBAR
# =====================================================


st.sidebar.title(
"🇬🇧 English Master"
)



level = st.sidebar.selectbox(

"Trình độ",

[
"A1",
"A2",
"B1",
"B2",
"C1"
]

)



menu = st.sidebar.radio(

"Học tập",

[
"🏠 Dashboard",
"📘 Grammar",
"📚 Vocabulary",
"🔄 Irregular Verb",
"📝 Quiz",
"✍ Writing",
"🎧 Listening",
"🎤 Speaking"

]

)



st.sidebar.divider()


st.sidebar.info(

f"""
Level hiện tại:

**{level}**

Mục tiêu:

English Fluency

"""

)



# =====================================================
# HOME
# =====================================================


if menu=="🏠 Dashboard":


    st.markdown(

"""
<div class="card">

<div class="title">

🇬🇧 English Master

</div>


<p class="subtitle">

Nền tảng học tiếng Anh tương tác
A1 → C1

</p>


<span class="badge">

Learn - Practice - Improve

</span>

</div>

""",

unsafe_allow_html=True

)



    c1,c2,c3,c4=st.columns(4)


    c1.metric(
        "📚 Vocabulary",
        "520"
    )


    c2.metric(
        "📝 Tests",
        "35"
    )


    c3.metric(
        "🔥 Streak",
        "12 ngày"
    )


    c4.metric(
        "⭐ Score",
        "850"
    )



    st.subheader(
        "📈 Today's Progress"
    )


    st.progress(
        0.72
    )


    st.success(
        "Bạn đã hoàn thành 72% mục tiêu hôm nay"
    )



# =====================================================
# GRAMMAR
# =====================================================


elif menu=="📘 Grammar":


    st.title(
        "📘 Grammar"
    )


    for g in GRAMMAR[level]:


        with st.expander(
            g["name"]
        ):


            st.subheader(
                "Công thức"
            )


            st.code(
                g["formula"]
            )


            st.write(
                g["use"]
            )


            st.success(
                "Example: "
                +
                g["example"]
            )



# =====================================================
# VOCABULARY
# =====================================================


elif menu=="📚 Vocabulary":


    st.title(
        "📚 Vocabulary"
    )


    search=st.text_input(
        "🔎 Search vocabulary"
    )


    for word,meaning in VOCAB[level]:


        if search.lower() in word.lower():


            st.markdown(

f"""
<div class="card">

<h2> {word} </h2>

🇻🇳 {meaning}

</div>

""",

unsafe_allow_html=True

)





# =====================================================
# IRREGULAR
# =====================================================


elif menu=="🔄 Irregular Verb":


    st.title(
        "🔄 Irregular Verbs"
    )


    st.dataframe(

        IRREGULAR,

        use_container_width=True

    )



# =====================================================
# QUIZ
# =====================================================


elif menu=="📝 Quiz":


    st.title(
        "📝 Test Grammar"
    )


    score=0


    answers=[]


    for i,q in enumerate(QUIZ):


        ans=st.radio(

            q["question"],

            q["options"],

            key=i

        )


        answers.append(ans)



    if st.button(
        "Submit"
    ):


        for a,q in zip(
            answers,
            QUIZ
        ):


            if a==q["answer"]:

                score+=1



        st.success(

f"""
Kết quả:

{score}/{len(QUIZ)}

"""

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

f"""
Write about:

{topic}

"""

)


    text=st.text_area(

        "Your answer",

        height=250

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
        "🎧 Listening Practice"
    )


    st.audio(

        "audio/lesson01.mp3"

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
        "🎤 Speaking Practice"
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
            "Completed!"
        )

