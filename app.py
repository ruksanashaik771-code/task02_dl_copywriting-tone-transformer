import streamlit as st

from app.prompts.template import build_prompt
from app.services.groq_service import generate_copy

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Copywriting Studio",
    page_icon="✨",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#eef2ff,#ffffff);
    color:#1f2937; /* Dark gray text for readability */
}

/* Hero Banner */

.hero{
    background: linear-gradient(90deg,#6C63FF,#3B82F6);
    padding:35px;
    border-radius:18px;
    text-align:center;
    margin-bottom:25px;
    color:white;
}

.hero h1{
    color:white;
    margin-bottom:8px;
}

.hero p{
    color:white;
    font-size:18px;
}

/* Cards */

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 18px rgba(0,0,0,0.12);
    margin-bottom:15px;
    color:#111827; /* Dark text inside cards */
}

/* Button */

.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#6C63FF,#4F46E5);
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    padding:12px;
}

.stButton>button:hover{
    color:white;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#F5F7FF;
    color:#1f2937; /* Dark text in sidebar */
}

/* Fix assistant chat message text visibility */
div[data-testid="stChatMessageContent"] {
    color: #111827 !important;   /* Dark text */
    background: #ffffff !important; /* White background */
    border-radius: 12px;
    padding: 12px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🤖 AI Studio")

    st.markdown("---")

    st.subheader("🚀 Features")

    st.write("✅ Marketing Copy Generation")

    st.write("✅ Multiple Platforms")

    st.write("✅ Different Writing Styles")

    st.write("✅ Powered by Groq AI")

    st.markdown("---")

    st.success("Built with ❤️ using\n\nPython + Streamlit + Groq")

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">

<h1>✨ AI Copywriting Studio</h1>

<p>Create engaging marketing content in seconds using Generative AI.</p>

</div>
""", unsafe_allow_html=True)

# ---------------- EXAMPLE ---------------- #

with st.expander("💡 Need an example? Click here"):

    st.markdown("""
### Product Name
**VelvetGlow Lipstick**

### Product Description
A premium matte lipstick enriched with Vitamin E that delivers rich pigmentation,
long-lasting wear, hydration, and a smudge-resistant finish.

### Platform
Instagram

### Tone
Friendly
""")

# ---------------- INPUT ---------------- #

left, right = st.columns([2,1])

with left:

    st.markdown("## 📦 Product Information")

    product_name = st.text_input(
        "Product Name",
        placeholder="Example: VelvetGlow Lipstick"
    )

    product_description = st.text_area(
        "Product Description",
        height=220,
        placeholder="Describe your product here..."
    )

with right:

    st.markdown("## 🎯 Settings")

    platform = st.selectbox(
        "Platform",
        [
            "Instagram",
            "Facebook",
            "LinkedIn",
            "Twitter/X",
            "Email"
        ]
    )

    tone = st.selectbox(
        "Tone",
        [
            "Friendly",
            "Funny",
            "Professional",
            "Luxury",
            "Serious"
        ]
    )

    st.write("")

    generate = st.button("✨ Generate Copy")

# ---------------- OUTPUT ---------------- #

if generate:

    if product_name.strip() == "" or product_description.strip() == "":

        st.warning("⚠ Please fill all the fields.")

    else:

        prompt = build_prompt(
            product_name,
            product_description,
            platform,
            tone
        )

        with st.spinner("🤖 AI is creating your marketing copy..."):

            result = generate_copy(prompt)

        st.success("🎉 Marketing Copy Generated!")

        st.markdown("---")

        st.subheader("🤖 AI Assistant")

        with st.chat_message("assistant"):
            st.write(result)

        st.download_button(
            "📄 Download Copy",
            data=result,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
