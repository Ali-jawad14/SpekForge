import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import pypdf  # Make sure to pip install pypdf

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ------------------------------------------------------------------
# 1. PAGE CONFIG & STYLES
# ------------------------------------------------------------------
st.set_page_config(page_title="SpekForge Pro // Enterprise Content Engine", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #fdfdfd; }
    h1 { color: #1E293B; font-weight: 800; }
    .stButton>button { background-color: #4F46E5; color: white; border-radius: 6px; width: 100%; }
    /* Fix sidebar padding to look cleaner */
    [data-testid="stSidebar"] { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ SpekForge Pro")
st.caption("Enterprise AI Migration, Library Auditing, & Content De-Slopping Platform")
st.write("---")

# ------------------------------------------------------------------
# 2. UPGRADED PREMIUM SIDEBAR CONFIGURATION
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚙️ System Control")
    st.write("") # Spacer
    
    # 1. System Status Container (Custom HTML styling)
    st.markdown("### 🔌 System Pipeline Status")
    if GROQ_API_KEY:
        st.markdown(
            """
            <div style="background-color: #DEF7EC; border-left: 5px solid #0E9F6E; padding: 12px; border-radius: 6px; margin-bottom: 15px;">
                <span style="color: #03543F; font-weight: bold;">🔒 Engine Status: Active</span><br>
                <span style="color: #046A38; font-size: 13px;">Groq API connected securely via local environment.</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="background-color: #FDE8E8; border-left: 5px solid #E11D48; padding: 12px; border-radius: 6px; margin-bottom: 15px;">
                <span style="color: #9B1C1C; font-weight: bold;">❌ Engine Status: Disconnected</span><br>
                <span style="color: #C81E1E; font-size: 13px;">Missing GROQ_API_KEY in your local .env file.</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    # 2. Core Model Configurations with interactive tooltips
    st.markdown("### 🧠 LLM Hyperparameters")
    model_option = st.selectbox(
        "Select Optimization Model:",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
        help="Select the specific LLM architecture optimized for either blazing speed or complex contextual reasoning."
    )
    
    st.write("") # Spacer
    
    # 3. Clean, Uniform Pipeline Selection (Symmetrical Dropdown Design)
    st.markdown("### 🎛️ Pipeline Engine")
    workflow_mode = st.selectbox(
        "Select Pipeline Workflow:",
        ["Content Architecture (Forge)", "Content Audit & Migration Strategy"],
        help="Switch between generating instant structured assets or generating a high-level library migration health report."
    )
    
    st.markdown("---")
    
    # 4. Informative Architecture Guide (Fills the blank vertical space beautifully)
    st.markdown("### 📖 Pipeline Guardrails")
    st.info(
        """
        **System Parameters Applied:**
        * **Zero Slop:** Instantly strips passive machine chatter, corporate fluff, and verbose phrasing.
        * **Enablement Ready:** Automatic formatting wrapper to enforce strict hierarchy and high readability.
        * **Auditing Matrices:** Evaluates source duplication or technical obsolescence.
        """
    )
    st.caption("SpekForge Pro v1.2 // Internal Workspace")

# ------------------------------------------------------------------
# 3. ROBUST PROMPT TEMPLATES
# ------------------------------------------------------------------
FORGE_PROMPT = """
You are an expert Content Architect. Take this raw, verbose corporate data and transform it into a highly polished, bite-sized "Spek" (knowledge card) for a sales/CS representative.

Guidelines:
1. ELIMINATE AI SLOP: Strip away corporate fluff, passive transitions, and generic machine chatter.
2. RUTHLESS BREVITY: Make it readable in under 10 seconds during a live call.
3. VISUAL STRUCTURE: Format using crisp Markdown: Use strategic **bolding**, clean bullet points (-), horizontal dividers (---), and blockquotes (>) for warnings/tips.
4. TONE: Actionable, modern human-written copy.

Output ONLY the final markdown block.
"""

# Fixed prompt to make sure it renders beautifully as clean Markdown text
AUDIT_PROMPT = """
You are an AI Content Auditor. Analyze the provided corporate document text for structural efficiency and operational health.
Provide your response strictly in the following clean format:

### 📊 Content Audit Report
---
* **Readability Assessment**: [Provide a 1-sentence verdict on how complex/dense the current text is]
* **Slop & Redundancy Analysis**: [Identify explicit filler phrases, machine jargon, or fluff that needs elimination]
* **Migration Recommendation**: **[KEEP, REWRITE, or RETIRE]**

### 🗺️ Proposed Action Plan
1. [Step 1 to transform this content]
2. [Step 2 to transform this content]
"""

# ------------------------------------------------------------------
# 4. DATA INGESTION ENGINE (File + Text Input)
# ------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Raw Source Ingestion")
    
    # Dual input: File upload OR manual text
    uploaded_file = st.file_uploader("Upload customer source document (PDF or TXT)", type=["pdf", "txt"])
    
    extracted_text = ""
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".txt"):
            extracted_text = uploaded_file.read().decode("utf-8")
        elif uploaded_file.name.endswith(".pdf"):
            pdf_reader = pypdf.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                extracted_text += page.extract_text() or ""
        st.success(f"Successfully extracted {len(extracted_text)} characters from file.")

    raw_input = st.text_area(
        "Or paste raw playbooks/scraped text manually here:",
        value=extracted_text,
        height=250,
        placeholder="Paste copy or use file uploader above..."
    )
    
    context_note = st.text_input("Add specific constraints or jargon requirements (Optional):")
    process_btn = st.button(f"Execute {workflow_mode}")

# ------------------------------------------------------------------
# 5. EXECUTION & OUTPUT ENGINE
# ------------------------------------------------------------------
with col2:
    st.subheader("✨ Streamlined Operational Output")
    
    if process_btn:
        if not GROQ_API_KEY:
            st.error("Please ensure your `.env` contains a valid `GROQ_API_KEY`.")
        elif not raw_input.strip():
            st.warning("Please provide source material via file upload or text box.")
        else:
            with st.spinner("Processing architectural data workflows..."):
                try:
                    client = Groq(api_key=GROQ_API_KEY)
                    
                    # Choose prompt dynamically based on sidebar choice
                    system_instruction = FORGE_PROMPT if workflow_mode == "Content Architecture (Forge)" else AUDIT_PROMPT
                    
                    user_content = raw_input
                    if context_note:
                        user_content += f"\n\nContext Notes: {context_note}"
                        
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": system_instruction},
                            {"role": "user", "content": user_content}
                        ],
                        model=model_option,
                        temperature=0.1 if "Audit" in workflow_mode else 0.3,
                    )
                    
                    output_text = chat_completion.choices[0].message.content
                    st.markdown(output_text)
                    
                    st.write("---")
                    # Feature C: Export Button
                    st.download_button(
                        label="💾 Download Asset as Markdown File",
                        data=output_text,
                        file_name="spekforge_output.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")
    else:
        st.info("Configure settings and trigger pipeline to analyze or structure raw content elements.")