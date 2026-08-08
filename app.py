import gradio as gr
import os
from datetime import datetime

from workflow import run_strategy, run_analytics


# =========================================================
# STORE THE LATEST GENERATED REPORT
# =========================================================

latest_report = {
    "business_name": "",
    "report": "",
}


# =========================================================
# GENERATE MARKETING STRATEGY
# =========================================================

def generate_strategy(
    business_name,
    product,
    industry,
    target_audience,
    budget,
    goal,
):
    """
    Generate a complete marketing strategy using
    the multi-agent workflow.
    """

    try:

        # -------------------------------------------------
        # Input validation
        # -------------------------------------------------

        if not business_name or not business_name.strip():
            return (
                "❌ Please enter a business name.",
                "",
                "",
                "",
                "",
                "",
                "",
            )

        if not product or not product.strip():
            return (
                "❌ Please enter a product or service.",
                "",
                "",
                "",
                "",
                "",
                "",
            )

        if not industry or not industry.strip():
            return (
                "❌ Please enter an industry.",
                "",
                "",
                "",
                "",
                "",
                "",
            )

        if not target_audience or not target_audience.strip():
            return (
                "❌ Please enter the target audience.",
                "",
                "",
                "",
                "",
                "",
                "",
            )

        if budget is None or budget <= 0:
            return (
                "❌ Please enter a valid marketing budget.",
                "",
                "",
                "",
                "",
                "",
                "",
            )

        if not goal or not goal.strip():
            return (
                "❌ Please enter a marketing goal.",
                "",
                "",
                "",
                "",
                "",
                "",
            )

        # -------------------------------------------------
        # Run multi-agent workflow
        # -------------------------------------------------

        results = run_strategy(
            business_name,
            product,
            industry,
            target_audience,
            budget,
            goal,
        )

        # -------------------------------------------------
        # Store final report for Human Approval
        # -------------------------------------------------

        latest_report["business_name"] = business_name
        latest_report["report"] = results["final_report"]

        return (
            "✅ Marketing strategy generated successfully.",
            results["market_research"],
            results["competitor_analysis"],
            results["campaign_plan"],
            results["content_strategy"],
            results["optimization"],
            results["final_report"],
        )

    except Exception as e:

        return (
            f"❌ Error: {str(e)}",
            "",
            "",
            "",
            "",
            "",
            "",
        )


# =========================================================
# HUMAN APPROVAL
# =========================================================

def approve_strategy():
    """
    Human approval step.

    The final marketing strategy is saved only after
    the user clicks the Approve Strategy button.
    """

    try:

        # -------------------------------------------------
        # Make sure a strategy exists
        # -------------------------------------------------

        if not latest_report["report"]:
            return (
                "⚠️ Generate a marketing strategy "
                "before approving it."
            )

        # -------------------------------------------------
        # Create outputs folder
        # -------------------------------------------------

        os.makedirs(
            "outputs",
            exist_ok=True,
        )

        # -------------------------------------------------
        # Prepare safe business name
        # -------------------------------------------------

        business_name = latest_report[
            "business_name"
        ].strip()

        safe_name = "".join(
            character
            if character.isalnum()
            or character in (" ", "-", "_")
            else "_"
            for character in business_name
        )

        # -------------------------------------------------
        # Generate timestamp
        # -------------------------------------------------

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = (
            f"{safe_name}_{timestamp}.txt"
        )

        file_path = os.path.join(
            "outputs",
            file_name,
        )

        # -------------------------------------------------
        # Save approved report
        # -------------------------------------------------

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                "AI MARKETING STRATEGY MANAGER\n"
            )

            file.write(
                "========================================\n\n"
            )

            file.write(
                f"Business: {business_name}\n"
            )

            file.write(
                "Approval Status: APPROVED\n"
            )

            file.write(
                "Approved On: "
                + datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
                + "\n\n"
            )

            file.write(
                "FINAL MARKETING STRATEGY\n"
            )

            file.write(
                "========================================\n\n"
            )

            file.write(
                str(latest_report["report"])
            )

        return f"""
### ✅ Strategy approved successfully.

**Report saved to:**

`{file_path}`
"""

    except Exception as e:

        return (
            f"❌ Approval Error: {str(e)}"
        )


# =========================================================
# CAMPAIGN PERFORMANCE ANALYTICS
# =========================================================

def analyze_campaign(
    impressions,
    clicks,
    conversions,
    cost,
    revenue,
):
    """
    Analyze real campaign performance data using
    the Marketing Analytics Agent.
    """

    try:

        # -------------------------------------------------
        # Input validation
        # -------------------------------------------------

        if impressions is None or impressions <= 0:
            return (
                "❌ Impressions must be greater than 0."
            )

        if clicks is None or clicks < 0:
            return (
                "❌ Clicks cannot be negative."
            )

        if conversions is None or conversions < 0:
            return (
                "❌ Conversions cannot be negative."
            )

        if cost is None or cost < 0:
            return (
                "❌ Advertising cost cannot be negative."
            )

        if revenue is None or revenue < 0:
            return (
                "❌ Revenue cannot be negative."
            )

        if clicks > impressions:
            return (
                "❌ Clicks cannot be greater "
                "than impressions."
            )

        if conversions > clicks:
            return (
                "❌ Conversions cannot be greater "
                "than clicks."
            )

        # -------------------------------------------------
        # Run Analytics Agent
        # -------------------------------------------------

        result = run_analytics(
            impressions,
            clicks,
            conversions,
            cost,
            revenue,
        )

        return result

    except Exception as e:

        return (
            f"❌ Analytics Error: {str(e)}"
        )


# =========================================================
# GRADIO APPLICATION
# =========================================================

with gr.Blocks(
    title="AI Marketing Strategy Manager"
) as demo:

    # =====================================================
    # HEADER
    # =====================================================

    gr.Markdown(
        """
# 🚀 AI Marketing Strategy Manager

### Multi-Agent Marketing Intelligence Platform

This system uses specialized AI agents to:

- Research the market
- Analyze competitors
- Plan marketing campaigns
- Create marketing content
- Analyze campaign performance
- Recommend improvements
- Generate a final professional marketing strategy
- Allow human approval before saving the strategy
"""
    )

    gr.Markdown("---")

    # =====================================================
    # BUSINESS INFORMATION
    # =====================================================

    gr.Markdown(
        "## 🏢 Business Information"
    )

    with gr.Row():

        business_name = gr.Textbox(
            label="Business Name",
            placeholder="Example: Urban Setup",
        )

        product = gr.Textbox(
            label="Product / Service",
            placeholder=(
                "Example: Affordable sneakers "
                "for college students"
            ),
        )

    with gr.Row():

        industry = gr.Textbox(
            label="Industry",
            placeholder=(
                "Example: Fashion / Footwear"
            ),
        )

        target_audience = gr.Textbox(
            label="Target Audience",
            placeholder=(
                "Example: College students "
                "aged 18-24"
            ),
        )

    with gr.Row():

        budget = gr.Number(
            label="Marketing Budget (INR)",
            value=50000,
        )

        goal = gr.Textbox(
            label="Marketing Goal",
            value="Increase online sales",
        )

    # =====================================================
    # GENERATE STRATEGY BUTTON
    # =====================================================

    generate_button = gr.Button(
        "🚀 Generate Marketing Strategy",
        variant="primary",
    )

    # =====================================================
    # STATUS
    # =====================================================

    gr.Markdown("### Status")

    status_output = gr.Markdown()

    # =====================================================
    # MARKET RESEARCH
    # =====================================================

    gr.Markdown("---")

    gr.Markdown(
        "## 🔎 Market Research"
    )

    market_output = gr.Textbox(
        label="Market Research",
        lines=12,
        interactive=False,
    )

    # =====================================================
    # COMPETITOR ANALYSIS
    # =====================================================

    gr.Markdown(
        "## 🏢 Competitor Analysis"
    )

    competitor_output = gr.Textbox(
        label="Competitor Analysis",
        lines=12,
        interactive=False,
    )

    # =====================================================
    # CAMPAIGN PLAN
    # =====================================================

    gr.Markdown(
        "## 📢 Campaign Plan"
    )

    campaign_output = gr.Textbox(
        label="Campaign Plan",
        lines=15,
        interactive=False,
    )

    # =====================================================
    # CONTENT STRATEGY
    # =====================================================

    gr.Markdown(
        "## ✍️ Content Strategy"
    )

    content_output = gr.Textbox(
        label="Content Strategy",
        lines=15,
        interactive=False,
    )

    # =====================================================
    # OPTIMIZATION ADVISOR
    # =====================================================

    gr.Markdown(
        "## ⚙️ Optimization Advisor"
    )

    optimization_output = gr.Textbox(
        label="Optimization Recommendations",
        lines=12,
        interactive=False,
    )

    # =====================================================
    # FINAL MARKETING STRATEGY
    # =====================================================

    gr.Markdown("---")

    gr.Markdown(
        "# 📋 Final Marketing Strategy"
    )

    final_output = gr.Markdown()

    # =====================================================
    # CONNECT GENERATE BUTTON
    # =====================================================

    generate_button.click(
        fn=generate_strategy,

        inputs=[
            business_name,
            product,
            industry,
            target_audience,
            budget,
            goal,
        ],

        outputs=[
            status_output,
            market_output,
            competitor_output,
            campaign_output,
            content_output,
            optimization_output,
            final_output,
        ],
    )

    # =====================================================
    # HUMAN APPROVAL
    # =====================================================

    gr.Markdown("---")

    gr.Markdown(
        """
## 👤 Human Approval

Review the complete strategy before approving it.

The final report will only be saved after you click
**Approve Strategy**.
"""
    )

    approve_button = gr.Button(
        "✅ Approve Strategy"
    )

    approval_output = gr.Markdown()

    approve_button.click(
        fn=approve_strategy,
        inputs=[],
        outputs=approval_output,
    )

    # =====================================================
    # CAMPAIGN PERFORMANCE ANALYTICS
    # =====================================================

    gr.Markdown("---")

    gr.Markdown(
        """
# 📊 Campaign Performance Analytics

Enter actual campaign performance data below.

The **Marketing Analytics Agent** will calculate
campaign metrics, analyze the results, and recommend
possible improvements.
"""
    )

    # =====================================================
    # ANALYTICS INPUTS
    # =====================================================

    with gr.Row():

        impressions_input = gr.Number(
            label="Impressions",
            value=100000,
            precision=0,
        )

        clicks_input = gr.Number(
            label="Clicks",
            value=5000,
            precision=0,
        )

        conversions_input = gr.Number(
            label="Conversions",
            value=250,
            precision=0,
        )

    with gr.Row():

        cost_input = gr.Number(
            label="Advertising Cost (INR)",
            value=20000,
        )

        revenue_input = gr.Number(
            label="Revenue Generated (INR)",
            value=60000,
        )

    # =====================================================
    # ANALYTICS BUTTON
    # =====================================================

    analyze_button = gr.Button(
        "📊 Analyze Campaign Performance",
        variant="primary",
    )

    # =====================================================
    # ANALYTICS OUTPUT
    # =====================================================

    gr.Markdown(
        "## 📈 Analytics Report"
    )

    analytics_output = gr.Markdown()

    # =====================================================
    # CONNECT ANALYTICS BUTTON
    # =====================================================

    analyze_button.click(
        fn=analyze_campaign,

        inputs=[
            impressions_input,
            clicks_input,
            conversions_input,
            cost_input,
            revenue_input,
        ],

        outputs=[
            analytics_output,
        ],
    )


# =========================================================
# START GRADIO APPLICATION
# =========================================================

if __name__ == "__main__":

    demo.launch()