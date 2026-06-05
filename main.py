import streamlit as st
import base64
import os
import urllib.parse

# =========================================================================
# 1. PAGE CONFIGURATION (Must be the absolute first Streamlit command)
# =========================================================================
st.set_page_config(
    page_title="EMBER Project - Resource Portal",
    page_icon="🏥",
    layout="wide"
)


# HELPER FUNCTION: Safely reads and converts local logos to base64 images
def get_image_base64(image_name):
    base, ext = os.path.splitext(image_name)
    possible_names = [image_name, f"{base}{ext.lower()}", f"{base}{ext.upper()}"]

    possible_paths = []
    for name in possible_names:
        possible_paths.extend([
            os.path.join("Static", name),
            os.path.join("static", name),
            name
        ])

    for path in possible_paths:
        if os.path.exists(path):
            with open(path, "rb") as img_file:
                encoded = base64.b64encode(img_file.read()).decode()
                mime_type = "image/jpeg" if path.lower().endswith(('.jpg', '.jpeg')) else "image/png"
                return f"data:{mime_type};base64,{encoded}"
    return f"https://via.placeholder.com/150x80?text={urllib.parse.quote(image_name.split('.')[0])}"


# =========================================================================
# 2. INJECT FONTS & GLOBAL GRAPHICS RULES
# =========================================================================

st.html("""
    <!-- Import Whimsical Fantasy & Friendly Display Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Emilys+Candy&family=Fredoka:wght@400;500;600;700&family=Quicksand:wght@500;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded" rel="stylesheet">
    

    <style>
    .tab-header-card {
        padding: 18px;
        border-radius: 14px;
        margin-bottom: 24px;
    }
    
    .tab-header-card h2 {
        margin: 0 0 8px 0;
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
    }
    
    .tab-header-card p {
        margin: 0;
        color: #475569;
        font-size: 15px;
    }    
    
    /* Global Canvas Styling */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Quicksand', sans-serif !important;
        background-color: #F8FAFC; 
    }

    /* PHOTOGRAPHIC HERO BANNER CONFIGURATION */
    .ember-banner {
        width: 100%;
        border-radius: 24px;
        text-align: center;
        border: 2px solid #E2E8F0;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.05);
        margin-bottom: 35px;
        position: relative;
        overflow: hidden;
    }
    .banner-title {
        font-family: 'Emilys Candy', cursive !important;
        font-size: 56px !important;
        letter-spacing: 1px;
    }
    .banner-subtitle {
        font-family: 'Fredoka', sans-serif !important;
        font-weight: 500;
        letter-spacing: 0.5px;
    }

    /* EXPANDER SUMMARY HOVER POP EFFECT */
    div[data-testid="stExpander"] {
        background: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 20px !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    div[data-testid="stExpander"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px rgba(79, 70, 229, 0.1) !important;
        border-color: #A5B4FC !important;
    }
    div[data-testid="stExpander"] summary p {
        font-family: 'Fredoka', sans-serif !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        color: #1E293B !important;
    }

    .expander-header { 
        font-family: 'Fredoka', sans-serif !important;
        font-size: 22px !important; 
        color: #EC4899; 
        font-weight: 600 !important; 
        margin-bottom: 20px; 
    }

    /* DYNAMIC PORTAL RESOURCE CARD STYLING */
    .custom-card {
        background-color: #FFFFFF;
        border: 2px solid #F1F5F9;
        border-radius: 16px;
        padding: 22px;
        height: 420px; /* Increased slightly to handle larger logos smoothly */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 15px;
    }
    .custom-card:hover {
        transform: scale(1.02);
        box-shadow: 0 20px 30px rgba(79, 70, 229, 0.12);
        border-color: #C7D2FE;
    }
    .card-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }
    .card-title {
        font-family: 'Fredoka', sans-serif !important;
        font-size: 19px !important;
        font-weight: 600 !important;
        color: #0F172A;
        margin-top: 14px;
        margin-bottom: 6px;
        line-height: 1.3;
    }
    .card-meta {
        font-size: 13px;
        color: #6366F1;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .card-body {
        font-size: 14px;
        color: #475569;
        line-height: 1.5;
    }

    /* UPDATED: Larger layout limits & strict flush-left forces */
    .img-container {
        height: 140px; 
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: left !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100%;
    }
    img.logo {
        max-height: 140px !important; /* Scaled up from 110px */
        max-width: 90% !important;
        width: auto !important;
        object-fit: contain !important;
        object-position: left center !important; /* Force content mapping to start on the absolute left */
        margin-left: 0 !important; 
        margin-right: auto !important;
        display: block !important;
    }

    /* CUSTOM PURPLE TABS MATRIX */
    div[data-testid="stTabs"] {
        border-bottom: 2px solid #E2E8F0 !important;
        margin-bottom: 35px !important;
        gap: 10px !important;
    }
    div[data-testid="stTabs"] button {
        background-color: transparent !important;
        border: none !important;
        padding: 10px 20px !important;
        transition: transform 0.2s ease, color 0.2s ease, font-weight 0.2s ease !important;
    }
    div[data-testid="stTabs"] button p {
        font-family: 'Fredoka', sans-serif !important;
        font-size: 19px !important;
        color: #64748B !important; 
        font-weight: 400 !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stTabs"] button:hover {
        transform: translateY(-2px) scale(1.03); 
    }
    div[data-testid="stTabs"] button:hover p {
        color: #6366F1 !important; 
        font-weight: 600 !important; 
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #F3E8FF !important; 
        border-radius: 10px 10px 0 0 !important;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] p {
        color: #4C1D95 !important; 
        font-weight: 700 !important; 
    }
    div[data-testid="stTabs"] [data-baseweb="tab-highlight-bar"] {
        background-color: #4C1D95 !important;
    }
       /* =====================================================
   CUSTOM LINK BUTTON STYLING
   ===================================================== */

    div.stLinkButton > a {
        background: #4C1D95 !important;
    
        color: white !important;
    
        font-weight: 600 !important;
    
        font-size: 15px !important;
    
        border-radius: 10px !important;
    
        padding: 0.75rem 1rem !important;
    
        text-decoration: none !important;
    
        transition: all 0.25s ease !important;
    }
    
    div.stLinkButton > a:hover {
        background: #5B21B6 !important;
        color: #FFFFFF !important;
    
        font-weight: 700 !important;
        letter-spacing: 0.3px;
    
        transform: translateY(-3px) scale(1.03);
    
        box-shadow: 0 10px 24px rgba(76, 29, 149, 0.30);
    
        transition: all 0.25s ease;
    }
    </style>
""")

# =========================================================================
# 3. DISPLAY HERO BANNER
# =========================================================================
hero_image_url = "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?q=80&w=2070&auto=format&fit=crop"

banner_html = f"""
<div class="ember-banner" style="
    background: linear-gradient(rgba(76, 29, 149, 0.45), rgba(79, 70, 229, 0.55)), url('{hero_image_url}');
    background-size: cover;
    background-position: center 30%;
    padding: 80px 20px;
    color: #FFFFFF;
">
    <h1 class="banner-title" style="color: #FFFFFF; text-shadow: 2px 4px 10px rgba(0,0,0,0.4); margin: 0 0 8px 0 !important;">
        EMBER Project Resource Portal
    </h1>
    <p class="banner-subtitle" style="color: #F1F5F9; text-shadow: 1px 2px 6px rgba(0,0,0,0.4); font-size: 22px; margin: 0 !important;">
        Empowering Motherhood through Behavioral health, Education & Recovery
    </p>
</div>
"""
st.markdown(banner_html, unsafe_allow_html=True)

#st.caption("Data Source Verbatim: EMBER Convening 2026 Resource List.docx")
st.markdown("---")

# =========================================================================
# 5. TAB MATRIX LOGIC WITH REFRESHED ICON BLUEPRINTS
# =========================================================================
tab1, tab2, tab3 = st.tabs([
    "🧭 Clinical Networks",
    "🌱 Recovery Programs",
    "🤝 Community Support"
])

# -------------------------------------------------------------------------
# TAB 1: CLINICAL CONSULTATIONS & QUALITY NETWORKS
# -------------------------------------------------------------------------
with tab1:
    st.markdown("""
    <div class="tab-header-card"
         style="background:#EEF2FF;border-left:6px solid #4F46E5;">
    <h2> Clinical Networks</h2>
    <p>
    Provider consultation services, quality collaboratives,
    perinatal expertise, and statewide clinical resources.
    </p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander(" Statewide Provider & Perinatal Consultation Networks", expanded=False):
        t1_col1, t1_col2 = st.columns(2)

        with t1_col1:
            mhap_img = get_image_base64("Missouri Maternal Health Access Project.jpg")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mhap_img}"></div>
                        <div class="card-title">Missouri’s Maternal Health Access Project (MHAP)</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Provider Mental Health Consultation</div>
                        <div class="card-body">Provides free, expert provider-to-provider perinatal psychiatric consultations, resource matching, and clinical mental health training systems for healthcare groups.</div>
                        </div>
                    </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://mochildwellbeing.org/mhap/", use_container_width=True)

        with t1_col2:
            kcc_img = get_image_base64("Kansas Connecting Community.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{kcc_img}"></div>
                        <div class="card-title">Kansas Connecting Community (KCC)</div>
                        <div class="card-meta">✨ Service Area: Kansas | Focus: Maternal & Child Mental Health</div>
                        <div class="card-body">Statewide clinical consultation line supporting front-line practitioners with real-time psychiatric assessments, screening integration workflows, and maternal health mapping.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.kansasmch.org/kcc-home.aspx", use_container_width=True)

    with st.expander(" Perinatal Quality Collaboratives & Health Associations", expanded=False):
        t1_col3, t1_col4 = st.columns(2)

        with t1_col3:
            mopqc_img = get_image_base64("Missouri Perinatal Quality Collaborative.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mopqc_img}"></div>
                        <div class="card-title">Missouri Perinatal Quality Collaborative (MoPQC)</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Quality Initiatives & Education</div>
                        <div class="card-body">A comprehensive platform running evidence-based safety bundles across Missouri hospitals to optimize response to maternal safety emergencies.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://mopqc.org/", use_container_width=True)

        with t1_col4:
            kpqc_img = get_image_base64("Kansas Perinatal Quality Collaborative.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{kpqc_img}"></div>
                        <div class="card-title">Kansas Perinatal Quality Collaborative (KPQC)</div>
                        <div class="card-meta">✨ Service Area: Kansas | Focus: Quality Initiatives & Education</div>
                        <div class="card-body">Coordinates collaborative hospital quality networks across Kansas, specializing in maternal care metrics and clinical safety toolkits.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.kansasmch.org", use_container_width=True)

        t1_col5, _ = st.columns([1, 1])
        with t1_col5:
            mha_img = get_image_base64("Missouri Hospital Association (MHA).png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mha_img}"></div>
                        <div class="card-title">Missouri Hospital Association (MHA)</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Quality Care & Patient Safety</div>
                        <div class="card-body">Statewide hospital data network initiating collaborative pathways to track health statistics, improve clinical safety markers, and expand safety-net coordination.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource",
                            "https://www.mohospitals.org/how-we-help-hospitals/quality-care-and-patient-safety/",
                            use_container_width=True)

# -------------------------------------------------------------------------
# TAB 2: SUD TREATMENT & RECOVERY PROGRAMS
# -------------------------------------------------------------------------
with tab2:
    st.markdown("""
    <div class="tab-header-card"
         style="background:#ECFDF5;border-left:6px solid #10B981;">
    <h2> Recovery Programs</h2>
    <p>
    Substance use treatment pathways, recovery services,
    behavioral health programs, and care coordination.
    </p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander(" Direct Intake Pathways & Dedicated Perinatal Programs", expanded=False):
        t2_col1, t2_col2 = st.columns(2)

        with t2_col1:
            cm_ties_img = get_image_base64("Children’s Mercy TIES Program.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{cm_ties_img}"></div>
                        <div class="card-title">Children’s Mercy TIES Program</div>
                        <div class="card-meta">✨ Service Area: Bi-State / KC Metro | Status: Active Intake Pathway</div>
                        <div class="card-body">
                            <span style="color:#EC4899; font-weight:bold;">🚨 Direct Action Referral:</span> Team for Infants Exposed to Substance use home visiting support program. Connects navigating parents with early care teams.
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource",
                           "https://www.childrensmercy.org/your-visit/family-support-and-resources/social-work/home-based-family-support-programs/",
                           use_container_width=True)

        with t2_col2:
            uh_ember_img = get_image_base64("University Health - EMBER Program.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{uh_ember_img}"></div>
                        <div class="card-title">University Health - EMBER Program</div>
                        <div class="card-meta">✨ Service Area: Missouri (KC) | Focus: Behavioral Health & Recovery</div>
                        <div class="card-body">Comprehensive multidisciplinary hub mapping out perinatal behavioral support, medical management, case navigation, and localized community training networks.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Watch EMBER Video", "https://youtu.be/N6EGIIYlmbY?si=BLp41JoKz2TJeZWf",
                            use_container_width=True)

    with st.expander(" Clinical Perinatal SUD Programs (Regional Models)", expanded=False):
        t2_col3, t2_col4 = st.columns(2)

        with t2_col3:
            slu_wish_img = get_image_base64("Saint Louis University_SSM Health - WISH Program.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{slu_wish_img}"></div>
                        <div class="card-title">Saint Louis University / SSM Health - WISH Program</div>
                        <div class="card-meta">✨ Service Area: Eastern Missouri | Focus: Prenatal Addiction Treatment</div>
                        <div class="card-body">The WISH Center provides comprehensive, multi-disciplinary prenatal care, specialized high-risk obstetrics, and evidence-based substance treatment plans.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource",
                            "https://www.ssmhealth.com/locations/location-details/wish-center",
                            use_container_width=True)

        with t2_col4:
            wustl_care_img = get_image_base64("Washington University in St. Louis - CARE Clinic.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{wustl_care_img}"></div>
                        <div class="card-title">Washington University in St. Louis - CARE Clinic</div>
                        <div class="card-meta">✨ Service Area: Eastern Missouri | Focus: Multi-disciplinary Perinatal Support</div>
                        <div class="card-body">Integrates targeted obstetric medical interventions, intensive psychiatric consultation, and substance tracking blueprints configured for pregnant individuals.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://sites.wustl.edu/stlcare4us/", use_container_width=True)

        t2_col5, t2_col6 = st.columns(2)
        with t2_col5:
            brave_img = get_image_base64("Mercy Health System - BRAVE Program.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{brave_img}"></div>
                        <div class="card-title">Mercy Health System - BRAVE Program</div>
                        <div class="card-meta">✨ Service Area: Regional Missouri | Focus: Perinatal Recovery Pathways</div>
                        <div class="card-body">Mercy Clinic Perinatal Substance Use Recovery program providing localized behavioral health mappings, outpatient medical support, and long-term stabilization.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource",
                            "https://www.mercy.net/practice/mercy-clinic-perinatal-substance-use-recovery-st-louis-tower-b/",
                            use_container_width=True)

        with t2_col6:
            usf_prism_img = get_image_base64("University of South Florida - PRISM_PEDI Program.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{usf_prism_img}"></div>
                        <div class="card-title">University of South Florida - PRISM / PEDI Program</div>
                        <div class="card-meta">✨ Service Area: National Model | Focus: Families Impacted by Substance Use</div>
                        <div class="card-body">Center for Families Impacted by Substance Use running cross-disciplinary clinical structures focusing heavily on complex pediatric and maternal recovery strategies.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource",
                            "https://health.usf.edu/care/pediatrics/services-specialties/center-families-substance-use",
                            use_container_width=True)

    with st.expander(" Supportive Infrastructure, Crisis Coordination & Education", expanded=False):
        t2_col7, t2_col8 = st.columns(2)

        with t2_col7:
            amethyst_img = get_image_base64("Amethyst Place.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{amethyst_img}"></div>
                        <div class="card-title">Amethyst Place</div>
                        <div class="card-meta">✨ Service Area: Missouri (KC) | Focus: Long-term Supportive Housing</div>
                        <div class="card-body">Provides supportive housing architectures, visual recovery tracking, family reunification support, and systemic counseling frameworks.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://amethystplace.org/", use_container_width=True)

        with t2_col8:
            epicc_img = get_image_base64("EPICC by CommCARE.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{epicc_img}"></div>
                        <div class="card-title">EPICC by CommCARE</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Crisis Case Coordination</div>
                        <div class="card-body">Engaging Patients in Care Coordination. Facilitates fast deployment, immediate emergency navigation, and critical linkages to substance use networks.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://commcare1.org/epicc-2/", use_container_width=True)

        t2_col9, t2_col10 = st.columns(2)
        with t2_col9:
            orn_img = get_image_base64("Opioid Response Network.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{orn_img}"></div>
                        <div class="card-title">Opioid Response Network (ORN)</div>
                        <div class="card-meta">✨ Service Area: National Network | Focus: Free SUD Education & Training</div>
                        <div class="card-body">Provides custom education and technical training resources tailored directly for medical institutions, clinicians, and regional community systems at no cost.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://opioidresponsenetwork.org/", use_container_width=True)

        with t2_col10:
            mo_mhan_img = get_image_base64("Missouri Maternal Health Action Network.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mo_mhan_img}"></div>
                        <div class="card-title">Missouri Maternal Health Action Network</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: System Collaboration</div>
                        <div class="card-body">A strategic multi-agency alliance resolving clinical equity barriers, refining policy rules, and stabilizing cross-system perinatal networks.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://moactionnetwork.org/", use_container_width=True)

        t2_col11, t2_col12 = st.columns(2)
        with t2_col11:
            heartland_img = get_image_base64("Heartland Center for Behavioral Change.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{heartland_img}"></div>
                        <div class="card-title">Heartland Center for Behavioral Change</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Substance Use Disorder Treatment</div>
                        <div class="card-body">Offers intensive inpatient and outpatient rehabilitation networks, detoxification medical units, and continuing recovery tracking.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.heartlandcbc.org/", use_container_width=True)

        with t2_col12:
            rediscover_img = get_image_base64("ReDiscover.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{rediscover_img}"></div>
                        <div class="card-title">ReDiscover</div>
                        <div class="card-meta">✨ Service Area: Missouri (KC) | Focus: Community Mental Health Center</div>
                        <div class="card-body">Nonprofit hub delivering highly structured substance use therapies, specialized stabilization services, and immediate behavioral case tracking.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://rediscovermh.org/", use_container_width=True)

        t2_col13, t2_col14 = st.columns(2)
        with t2_col13:
            bhg_img = get_image_base64("Behavioral Health Group (BHG).png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{bhg_img}"></div>
                        <div class="card-title">Behavioral Health Group (BHG)</div>
                        <div class="card-meta">✨ Service Area: Multi-State | Focus: Expert Addiction Care</div>
                        <div class="card-body">Outpatient medical tracking clinics specializing in pharmacotherapy (MAT), counseling assistance, and localized case stabilization infrastructure.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.bhgrecovery.com/", use_container_width=True)

        with t2_col14:
            confluence_img = get_image_base64("Confluence HRKC.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{confluence_img}"></div>
                        <div class="card-title">Confluence</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Naloxone & Harm Reduction Supply</div>
                        <div class="card-body">The primary distributor of lifesaving naloxone and harm reduction kits across Missouri, filling critical safety infrastructure gaps.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.confluencehrkc.org/", use_container_width=True)

# -------------------------------------------------------------------------
# TAB 3: COMMUNITY HEALTH, EQUITY & SUPPORT
# -------------------------------------------------------------------------
with tab3:
    st.markdown("""
    <div class="tab-header-card"
         style="background:#FFF7ED;border-left:6px solid #F97316;">
    <h2> Community Support</h2>
    <p>
    Community partnerships, maternal equity initiatives,
    family support resources, legal services, and public health programs.
    </p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander(" Maternal Equity & Community Care Coordination", expanded=False):
        t3_col1, t3_col2 = st.columns(2)

        with t3_col1:
            uzazi_img = get_image_base64("Uzazi Village.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{uzazi_img}"></div>
                        <div class="card-title">Uzazi Village</div>
                        <div class="card-meta">✨ Service Area: Bi-State Metro | Focus: Perinatal Equity & Community Health</div>
                        <div class="card-body">Nonprofit hub dedicating custom advocacy programs, specialized doula services, and health education to improve outcomes for Black and Brown families.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://uzazivillage.org/", use_container_width=True)

        with t3_col2:
            ivanhoe_img = get_image_base64("Ivanhoe Neighborhood Council.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{ivanhoe_img}"></div>
                        <div class="card-title">Ivanhoe Neighborhood Council</div>
                        <div class="card-meta">✨ Service Area: Missouri (KC) | Focus: Community Thriving & Advocacy</div>
                        <div class="card-body">A resident-led advocacy matrix running neighborhood-level care assistance, public health programs, and localized safety alignments.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://incthrives.org/", use_container_width=True)

        t3_col3, t3_col4 = st.columns(2)
        with t3_col3:
            innerworth_img = get_image_base64("Innerworth Psychology.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{innerworth_img}"></div>
                        <div class="card-title">Innerworth Psychology</div>
                        <div class="card-meta">✨ Service Area: Regional | Focus: Goal-focused Evidence Therapy</div>
                        <div class="card-body">Short-term, evidence-based cognitive therapy models integrating strength-based toolkits to support maternal mental health.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://Innerworthpsychology.com", use_container_width=True)

        with t3_col4:
            healthforward_img = get_image_base64("Health Forward Foundation.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{healthforward_img}"></div>
                        <div class="card-title">Health Forward Foundation</div>
                        <div class="card-meta">✨ Service Area: Regional Bi-State | Focus: Health Equity Philanthropy</div>
                        <div class="card-body">A purpose-driven philanthropic organization driving funding models and system advocacy to eliminate health disparities across the region.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://healthforward.org/", use_container_width=True)

    with st.expander(" Crisis Interventions, Legal Support & Public Health Departments", expanded=False):
        t3_col5, t3_col6 = st.columns(2)

        with t3_col5:
            dv_train_img = get_image_base64("Intimate Partner Violence_DV Training.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{dv_train_img}"></div>
                        <div class="card-title">Intimate Partner Violence / DV Training</div>
                        <div class="card-meta">✨ Service Area: Multi-State Training | Focus: Professional Education</div>
                        <div class="card-body">Specialized curriculum focused on "Responding to Domestic Violence with Pregnant and Postpartum Patients" hosted directly inside the MOCADSV portal systems.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource",
                            "https://mocadsv.coalitionmanager.org/eventmanager/onlinetraining/details/2588",
                            use_container_width=True)

        with t3_col6:
            newhouse_img = get_image_base64("NewHouse.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{newhouse_img}"></div>
                        <div class="card-title">NewHouse</div>
                        <div class="card-meta">✨ Service Area: Missouri (KC) | Focus: Domestic Violence Shelter</div>
                        <div class="card-body">Kansas City's oldest dedicated protective ecosystem providing safe housing, legal navigation help, emergency tracking, and therapy for survivors.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://newhousekc.org/#", use_container_width=True)

        t3_col7, t3_col8 = st.columns(2)
        with t3_col7:
            casa_img = get_image_base64("Jackson County CASA.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{casa_img}"></div>
                        <div class="card-title">Jackson County CASA</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Court Appointed Special Advocates</div>
                        <div class="card-body">Deploys court-appointed child advocates to manage family navigation blueprints and champion child safety across judicial networks.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://casakc.org/", use_container_width=True)

        with t3_col8:
            court_img = get_image_base64("16th Judicial Court of Missouri_Jackson County.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{court_img}"></div>
                        <div class="card-title">16th Judicial Court of Missouri: Jackson County</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Family Court Systems</div>
                        <div class="card-body">Direct operational resource portal outlining case management, procedural regulations, and family court safety links.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.16thcircuit.org/family-court",
                            use_container_width=True)

        t3_col9, t3_col10 = st.columns(2)
        with t3_col9:
            muni_court_img = get_image_base64("Kansas City Municipal Court.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{muni_court_img}"></div>
                        <div class="card-title">Kansas City Municipal Court</div>
                        <div class="card-meta">✨ Service Area: Missouri (KC) | Focus: Public Safety & Judicial Systems</div>
                        <div class="card-body">Provides public entry links to city hall municipal compliance programs, legal fine support tools, and alternative court programs.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://www.kcmo.gov/city-hall/departments/municipal-court",
                            use_container_width=True)

        with t3_col10:
            mo_doc_img = get_image_base64("Missouri Department of Corrections.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mo_doc_img}"></div>
                        <div class="card-title">Missouri Department of Corrections</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Corrections Programs & Re-entry</div>
                        <div class="card-body">Details rehabilitative family networks, re-entry intervention blueprints, and structural educational models within state parameters.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://doc.mo.gov/programs", use_container_width=True)

        t3_col11, t3_col12 = st.columns(2)
        with t3_col11:
            mo_dss_img = get_image_base64("Missouri Department of Social Services.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mo_dss_img}"></div>
                        <div class="card-title">Missouri Department of Social Services</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Children's Division Support</div>
                        <div class="card-body">The primary state management link for temporary child assistance programs, family safety services, and community resource tracking.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://dss.mo.gov/cd/", use_container_width=True)

        with t3_col12:
            mo_dhss_img = get_image_base64("Missouri DHSS & KC Health Department.png")
            st.markdown(f"""
                <div class="custom-card">
                    <div class="card-content">
                        <div class="img-container"><img class="logo" src="{mo_dhss_img}"></div>
                        <div class="card-title">Missouri DHSS & KC Health Department</div>
                        <div class="card-meta">✨ Service Area: Missouri | Focus: Public Health Infrastructure</div>
                        <div class="card-body">Combined wellness networks routing to the Department of Health and Senior Services and KCMO injury prevention portals.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("Explore Resource", "https://health.mo.gov/living/wellness/index.php",
                            use_container_width=True)