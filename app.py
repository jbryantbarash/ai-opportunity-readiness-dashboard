import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="AI Opportunity & Change Readiness Evaluator",
    layout="wide",
)

# ---------- Helpers ----------

DATA_PATH = Path(__file__).parent / "sample_use_cases.csv"


def load_initial_data() -> pd.DataFrame:
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH)
    else:
        # Fallback seed data if CSV is missing
        df = pd.DataFrame(
            [
                {
                    "Use Case": "Intelligent document triage for claims",
                    "Business Value (1-5)": 5,
                    "Technical Feasibility (1-5)": 3,
                    "Data Readiness (1-5)": 3,
                    "Change Impact (1-5)": 4,
                    "Risk (1-5)": 3,
                    "Owner": "Operations",
                    "Notes": "High cost savings; requires integration with core systems.",
                },
                {
                    "Use Case": "Member services AI copilot",
                    "Business Value (1-5)": 4,
                    "Technical Feasibility (1-5)": 4,
                    "Data Readiness (1-5)": 4,
                    "Change Impact (1-5)": 3,
                    "Risk (1-5)": 3,
                    "Owner": "Customer Service",
                    "Notes": "GenAI-based; frontline adoption is key.",
                },
                {
                    "Use Case": "Provider data cleansing & matching",
                    "Business Value (1-5)": 4,
                    "Technical Feasibility (1-5)": 3,
                    "Data Readiness (1-5)": 2,
                    "Change Impact (1-5)": 2,
                    "Risk (1-5)": 2,
                    "Owner": "Data Management",
                    "Notes": "Improves downstream analytics & reporting.",
                },
                {
                    "Use Case": "Internal knowledge retrieval assistant",
                    "Business Value (1-5)": 3,
                    "Technical Feasibility (1-5)": 5,
                    "Data Readiness (1-5)": 4,
                    "Change Impact (1-5)": 2,
                    "Risk (1-5)": 2,
                    "Owner": "Enterprise",
                    "Notes": "RAG-based Q&A over policies, SOPs, and training materials.",
                },
            ]
        )
    return df


def compute_scores(
    df: pd.DataFrame,
    w_value: float,
    w_feas: float,
    w_data: float,
    w_change: float,
    w_risk: float,
) -> pd.DataFrame:
    df = df.copy()

    # Ensure numeric types
    for col in [
        "Business Value (1-5)",
        "Technical Feasibility (1-5)",
        "Data Readiness (1-5)",
        "Change Impact (1-5)",
        "Risk (1-5)",
    ]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Change impact & risk are "costs" so we flip them in the scoring
    # (higher impact/risk reduces priority)
    weights_sum = w_value + w_feas + w_data + w_change + w_risk
    if weights_sum == 0:
        weights_sum = 1.0

    df["Priority Score"] = (
        df["Business Value (1-5)"] * w_value
        + df["Technical Feasibility (1-5)"] * w_feas
        + df["Data Readiness (1-5)"] * w_data
        - df["Change Impact (1-5)"] * w_change
        - df["Risk (1-5)"] * w_risk
    ) / weights_sum

    # Readiness Score – how ready we are to start:
    # Higher feasibility, higher data readiness, lower change impact, lower risk.
    df["Readiness Score"] = (
        df["Technical Feasibility (1-5)"]
        + df["Data Readiness (1-5)"]
        + (5 - df["Change Impact (1-5)"])
        + (5 - df["Risk (1-5)"])
    ) / 4.0

    return df


# ---------- App State ----------

if "use_cases" not in st.session_state:
    st.session_state.use_cases = load_initial_data()


# ---------- Sidebar Controls ----------

st.sidebar.title("Scoring Weights")

st.sidebar.markdown("Adjust how much each factor influences **Priority Score**:")

w_value = st.sidebar.slider("Business Value weight", 0.0, 5.0, 3.0, 0.5)
w_feas = st.sidebar.slider("Technical Feasibility weight", 0.0, 5.0, 2.5, 0.5)
w_data = st.sidebar.slider("Data Readiness weight", 0.0, 5.0, 2.5, 0.5)
w_change = st.sidebar.slider("Change Impact weight (penalty)", 0.0, 5.0, 2.0, 0.5)
w_risk = st.sidebar.slider("Risk weight (penalty)", 0.0, 5.0, 2.0, 0.5)

st.sidebar.markdown("---")
st.sidebar.markdown("**Tips**")
st.sidebar.caption(
    "- Increase *Business Value* weight for value-first strategy\n"
    "- Increase *Feasibility* & *Data* for quick wins\n"
    "- Increase *Change Impact* & *Risk* to de-prioritize hard or risky bets"
)

# ---------- Main Layout ----------

st.title("AI Opportunity & Change Readiness Evaluator")
st.caption(
    "Prioritize AI and automation use cases based on value, feasibility, data readiness, "
    "change impact, and risk."
)

tab_data, tab_visuals, tab_details = st.tabs(["Use Case Table", "Visuals", "Summary & Insights"])

# ---------- Tab 1: Data Table ----------

with tab_data:
    st.subheader("Use Cases")

    st.markdown(
        "Edit existing rows or add new ones. Use 1–5 scales for all scoring columns."
    )

    edited_df = st.data_editor(
        st.session_state.use_cases,
        num_rows="dynamic",
        key="use_case_editor",
    )

    st.session_state.use_cases = edited_df

    st.info(
        "Hint: Use this view during workshops to co-create and score use cases with stakeholders."
    )

# ---------- Compute Scores ----------

scored_df = compute_scores(
    st.session_state.use_cases, w_value, w_feas, w_data, w_change, w_risk
)

# ---------- Tab 2: Visualizations ----------

with tab_visuals:
    st.subheader("Prioritization View")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Ranked by Priority Score")

        sorted_df = scored_df.sort_values("Priority Score", ascending=False)

        fig_bar = px.bar(
            sorted_df,
            x="Use Case",
            y="Priority Score",
            hover_data=[
                "Business Value (1-5)",
                "Technical Feasibility (1-5)",
                "Data Readiness (1-5)",
                "Change Impact (1-5)",
                "Risk (1-5)",
                "Readiness Score",
            ],
        )
        fig_bar.update_layout(
            xaxis_title="Use Case",
            yaxis_title="Priority Score",
            xaxis_tickangle=-35,
            margin=dict(b=120),
        )

        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.markdown("#### Value vs Feasibility (Bubble = Priority)")

        fig_scatter = px.scatter(
            scored_df,
            x="Technical Feasibility (1-5)",
            y="Business Value (1-5)",
            size="Priority Score",
            color="Readiness Score",
            hover_name="Use Case",
            hover_data=[
                "Owner",
                "Data Readiness (1-5)",
                "Change Impact (1-5)",
                "Risk (1-5)",
                "Priority Score",
                "Readiness Score",
            ],
        )
        fig_scatter.update_layout(
            xaxis_title="Technical Feasibility (1–5)",
            yaxis_title="Business Value (1–5)",
        )

        st.plotly_chart(fig_scatter, use_container_width=True)

# ---------- Tab 3: Summary & Insights ----------

with tab_details:
    st.subheader("Summary & Insights")

    top_n = st.slider("Show top N opportunities", 1, len(scored_df), min(5, len(scored_df)))
    top_df = scored_df.sort_values("Priority Score", ascending=False).head(top_n)

    st.markdown("#### Top Opportunities")
    st.table(
        top_df[
            [
                "Use Case",
                "Owner",
                "Priority Score",
                "Readiness Score",
                "Business Value (1-5)",
                "Technical Feasibility (1-5)",
                "Data Readiness (1-5)",
                "Change Impact (1-5)",
                "Risk (1-5)",
            ]
        ]
    )

    st.markdown("#### Narrative")
    if not top_df.empty:
        highest = top_df.iloc[0]
        st.write(
            f"- **Highest priority:** `{highest['Use Case']}` (Owner: {highest['Owner']}) "
            f"with Priority Score **{highest['Priority Score']:.2f}** and Readiness "
            f"Score **{highest['Readiness Score']:.2f}**."
        )
        st.write(
            "- Consider these as **POC candidates**: they balance strong business value "
            "with reasonable feasibility and data readiness."
        )
        st.write(
            "- Use the weights in the sidebar live with stakeholders to show how "
            "**strategy changes** (e.g. risk-averse vs. aggressive) alter the roadmap."
        )
    else:
        st.warning("No use cases available. Please add at least one in the table.")
