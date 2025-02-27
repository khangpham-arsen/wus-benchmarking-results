import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import numpy as np
from datetime import datetime
import seaborn as sns

# Define a custom pastel color palette that's visible on white background
PASTEL_COLORS = [
    '#FF9999',  # Pastel Red
    '#66B2FF',  # Pastel Blue
    '#99FF99',  # Pastel Green
    '#FFCC99',  # Pastel Orange
    '#FF99CC',  # Pastel Pink
    '#99CCFF',  # Light Blue
    '#FFB366',  # Pastel Brown
    '#FF99FF',  # Pastel Purple
    '#99FFCC',  # Pastel Mint
    '#FFE5CC',  # Light Peach
]

# Define a custom diverging color scale for heatmaps
DIVERGING_COLORS = [
    [0, '#FF9999'],      # Pastel Red
    [0.5, '#FFFFFF'],    # White
    [1, '#66B2FF']       # Pastel Blue
]

def load_benchmark_data(report_dir):
    """Load benchmark results and metadata from a report directory."""
    results_file = Path(report_dir) / "benchmark_results.json"
    with open(results_file) as f:
        data = json.load(f)
    return data

def load_metadata():
    """Load metadata configuration."""
    with open("metadata.json") as f:
        return json.load(f)

def get_available_reports():
    """Get list of available benchmark reports."""
    results_dir = Path("results")
    return sorted([d for d in results_dir.iterdir() if d.is_dir()], reverse=True)

def create_metrics_df(data):
    """Convert benchmark metrics to DataFrame."""
    return pd.DataFrame(data["metrics"])

def plot_duration_distribution(df):
    """Plot distribution of query durations."""
    fig = px.histogram(
        df,
        x="duration",  # Changed back to x for traditional orientation
        nbins=30,
        title="Distribution of Query Durations",
        labels={"duration": "Duration (seconds)"},
        color_discrete_sequence=PASTEL_COLORS,
    )
    fig.update_traces(marker_line_color='white', marker_line_width=0.5)
    # Update layout with correct axis titles
    fig.update_layout(
        xaxis_title="Duration (seconds)",
        yaxis_title="Count"
    )
    return fig

def plot_operation_times(df):
    """Plot average operation times."""
    op_times = pd.json_normalize(df["operation_times"].apply(lambda x: x if isinstance(x, dict) else {}))
    avg_times = op_times.mean()
    
    fig = go.Figure(data=[
        go.Bar(
            x=avg_times.values,
            y=avg_times.index,
            orientation="h",
            marker_color=PASTEL_COLORS[0],
        )
    ])
    fig.update_layout(
        title="Average Operation Times",
        xaxis_title="Time (seconds)",
        yaxis_title="Operation",
    )
    return fig

def plot_operation_time_by_complexity(df):
    """Plot operation times by complexity."""
    op_times = pd.json_normalize(df["operation_times"].apply(lambda x: x if isinstance(x, dict) else {}))
    op_times["complexity"] = df["complexity"]
    
    melted = op_times.melt(id_vars=["complexity"], var_name="Operation", value_name="Duration")
    fig = px.box(
        melted,
        x="complexity",
        y="Duration",
        color="Operation",
        title="Operation Times by Complexity",
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_operation_time_by_language(df):
    """Plot operation times by language."""
    op_times = pd.json_normalize(df["operation_times"].apply(lambda x: x if isinstance(x, dict) else {}))
    op_times["language"] = df["language"]
    
    melted = op_times.melt(id_vars=["language"], var_name="Operation", value_name="Duration")
    fig = px.box(
        melted,
        x="language",
        y="Duration",
        color="Operation",
        title="Operation Times by Language",
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_error_heatmap(df, row_col, col_col):
    """Plot error heatmap."""
    error_matrix = pd.crosstab(df[row_col], df[col_col])
    
    fig = px.imshow(
        error_matrix,
        title=f"Error Heatmap: {row_col} vs {col_col}",
        labels=dict(x=col_col, y=row_col, color="Count"),
        aspect="auto",
        color_continuous_scale=DIVERGING_COLORS,
    )
    return fig

def plot_performance_by_context_depth(df):
    """Plot performance metrics by context depth."""
    depth_stats = df.groupby("chat_context_depth").agg({
        "duration": ["mean", "std"],
        "error_type": lambda x: (~x.isna()).mean()
    }).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Mean Duration",
        x=depth_stats["chat_context_depth"],
        y=depth_stats["duration"]["mean"],
        error_y=dict(type="data", array=depth_stats["duration"]["std"]),
        marker_color=PASTEL_COLORS[0],
    ))
    fig.add_trace(go.Scatter(
        name="Error Rate",
        x=depth_stats["chat_context_depth"],
        y=depth_stats["error_type"]["<lambda>"],
        yaxis="y2",
        line=dict(color=PASTEL_COLORS[1]),
        marker=dict(color=PASTEL_COLORS[1]),
    ))
    
    fig.update_layout(
        title="Performance by Context Depth",
        xaxis_title="Context Depth",
        yaxis_title="Duration (s)",
        yaxis2=dict(
            title="Error Rate",
            overlaying="y",
            side="right",
        ),
    )
    return fig

def plot_feature_analysis(df):
    """Plot feature analysis."""
    feature_stats = df.groupby("features").agg({
        "duration": "mean",
        "error_type": lambda x: (~x.isna()).mean()
    }).reset_index()
    
    fig = px.scatter(
        feature_stats,
        x="duration",
        y="error_type",
        text="features",
        title="Feature Analysis: Duration vs Error Rate",
        labels={
            "duration": "Mean Duration (s)",
            "error_type": "Error Rate",
        },
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_retry_analysis(df):
    """Plot retry analysis."""
    retry_stats = df.groupby("retry_attempt").agg({
        "duration": "mean",
        "error_type": lambda x: (~x.isna()).mean()
    }).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Mean Duration",
        x=retry_stats["retry_attempt"],
        y=retry_stats["duration"],
        marker_color=PASTEL_COLORS[0],
    ))
    fig.add_trace(go.Scatter(
        name="Error Rate",
        x=retry_stats["retry_attempt"],
        y=retry_stats["error_type"],
        yaxis="y2",
        line=dict(color=PASTEL_COLORS[1]),
        marker=dict(color=PASTEL_COLORS[1]),
    ))
    
    fig.update_layout(
        title="Performance by Retry Attempt",
        xaxis_title="Retry Attempt",
        yaxis_title="Duration (s)",
        yaxis2=dict(
            title="Error Rate",
            overlaying="y",
            side="right",
        ),
    )
    return fig

def plot_ai_search_analysis(df):
    """Plot AI search pattern analysis."""
    # Create base figure
    fig = go.Figure()
    
    # Calculate statistics
    pattern_stats = df[df["ai_search_pattern"].notna()].groupby("ai_search_pattern").agg({
        "duration": ["mean", "std"],
        "error_type": lambda x: (~x.isna()).mean()
    }).reset_index()
    
    # Fix the column names after reset_index
    pattern_stats.columns = ["ai_search_pattern", "duration_mean", "duration_std", "error_rate"]
    
    # Add bar plot for duration
    fig.add_trace(go.Bar(
        name="Mean Duration",
        x=pattern_stats["ai_search_pattern"],
        y=pattern_stats["duration_mean"],
        error_y=dict(type="data", array=pattern_stats["duration_std"]),
        marker_color=PASTEL_COLORS[0],
    ))
    
    # Add line plot for error rate
    fig.add_trace(go.Scatter(
        name="Error Rate",
        x=pattern_stats["ai_search_pattern"],
        y=pattern_stats["error_rate"] * 100,
        yaxis="y2",
        mode="lines+markers",
        line=dict(color=PASTEL_COLORS[1]),
        marker=dict(color=PASTEL_COLORS[1]),
    ))
    
    # Update layout
    fig.update_layout(
        title="Performance by AI Search Pattern",
        xaxis_title="Search Pattern",
        yaxis_title="Duration (s)",
        yaxis2=dict(
            title="Error Rate (%)",
            overlaying="y",
            side="right",
        ),
        showlegend=True,
        barmode="group"
    )
    
    return fig

def plot_complexity_distribution(df):
    """Plot distribution of query complexity."""
    counts = df["complexity"].value_counts()
    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Query Complexity Distribution",
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_language_distribution(df):
    """Plot distribution of query languages."""
    counts = df["language"].value_counts()
    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Query Language Distribution",
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_error_distribution(df):
    """Plot distribution of error types."""
    counts = df["error_type"].value_counts(dropna=False).rename({np.nan: "Success"})
    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title="Error Type Distribution",
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def load_multiple_runs(report_dirs):
    """Load and combine data from multiple benchmark runs."""
    all_data = []
    for report_dir in report_dirs:
        data = load_benchmark_data(report_dir)
        df = create_metrics_df(data)
        df["run_id"] = report_dir.name
        df["timestamp"] = datetime.strptime(report_dir.name.split("_")[1], "%Y%m%d")
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

def plot_duration_trend(df):
    """Plot duration trends across runs."""
    run_stats = df.groupby("run_id").agg({
        "duration": ["mean", "std"],
        "timestamp": "first"
    }).sort_values(("timestamp", "first"))

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=run_stats[("timestamp", "first")],
        y=run_stats[("duration", "mean")],
        error_y=dict(type="data", array=run_stats[("duration", "std")]),
        mode="lines+markers",
        name="Mean Duration",
        line=dict(color=PASTEL_COLORS[0]),
        marker=dict(color=PASTEL_COLORS[0]),
    ))
    
    fig.update_layout(
        title="Duration Trend Across Runs",
        xaxis_title="Run Date",
        yaxis_title="Duration (seconds)",
    )
    return fig

def plot_error_rate_trend(df):
    """Plot error rate trends across runs."""
    run_stats = df.groupby("run_id").agg({
        "error_type": lambda x: (~x.isna()).mean(),
        "timestamp": "first"
    }).sort_values("timestamp")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=run_stats["timestamp"],
        y=run_stats["error_type"] * 100,
        mode="lines+markers",
        name="Error Rate",
        line=dict(color=PASTEL_COLORS[0]),
        marker=dict(color=PASTEL_COLORS[0]),
    ))
    
    fig.update_layout(
        title="Error Rate Trend Across Runs",
        xaxis_title="Run Date",
        yaxis_title="Error Rate (%)",
    )
    return fig

def plot_operation_time_comparison(df):
    """Plot operation time comparison across runs."""
    op_times = pd.json_normalize(df["operation_times"].apply(lambda x: x if isinstance(x, dict) else {}))
    op_times["run_id"] = df["run_id"]
    
    melted = op_times.melt(id_vars=["run_id"], var_name="Operation", value_name="Duration")
    fig = px.box(
        melted,
        x="run_id",
        y="Duration",
        color="Operation",
        title="Operation Times Comparison Across Runs",
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_success_rate_by_category(df, category_col):
    """Plot success rate comparison by category across runs."""
    success_rates = df.groupby(["run_id", category_col])["error_type"].apply(
        lambda x: (~x.isna()).mean() * 100
    ).reset_index()
    
    fig = px.line(
        success_rates,
        x="run_id",
        y="error_type",
        color=category_col,
        title=f"Success Rate by {category_col} Across Runs",
        labels={"error_type": "Success Rate (%)"},
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_performance_comparison_heatmap(df, metric="duration"):
    """Plot performance comparison heatmap across runs and categories."""
    if metric == "duration":
        pivot_data = df.pivot_table(
            values="duration",
            index="complexity",
            columns="run_id",
            aggfunc="mean"
        )
    else:  # error rate
        pivot_data = df.pivot_table(
            values="error_type",
            index="complexity",
            columns="run_id",
            aggfunc=lambda x: (~x.isna()).mean() * 100
        )
    
    fig = px.imshow(
        pivot_data,
        title=f"{'Duration' if metric == 'duration' else 'Error Rate'} Comparison Heatmap",
        labels=dict(
            x="Run ID",
            y="Complexity",
            color="Seconds" if metric == "duration" else "Error Rate (%)"
        ),
        aspect="auto",
        color_continuous_scale=DIVERGING_COLORS,
    )
    return fig

def plot_ai_search_duration_by_complexity(df):
    """Plot duration comparison between AI Search and Normal Flow by complexity."""
    # Add ai_search flag
    df = df.copy()
    df["ai_search"] = df["ai_search_pattern"].apply(
        lambda x: "AI Search" if x and not pd.isna(x) else "Normal Flow"
    )
    
    fig = px.box(
        df,
        x="complexity",
        y="duration",
        color="ai_search",
        title="Query Duration: AI Search vs Normal Flow by Complexity",
        labels={
            "complexity": "Complexity",
            "duration": "Duration (seconds)",
            "ai_search": "Mode"
        },
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def plot_ai_search_error_rates(df):
    """Plot error rate comparison between AI Search and Normal Flow."""
    # Add ai_search flag
    df = df.copy()
    df["ai_search"] = df["ai_search_pattern"].apply(
        lambda x: "AI Search" if x and not pd.isna(x) else "Normal Flow"
    )
    
    # Calculate error rates
    error_rates = df.groupby(["ai_search", "complexity"])["error_type"].apply(
        lambda x: (x.notna().sum() / len(x)) * 100
    ).reset_index()
    error_rates.columns = ["Mode", "Complexity", "Error Rate"]
    
    # Handle empty data case
    if error_rates.empty:
        fig = go.Figure()
        fig.update_layout(
            title="Error Rates: AI Search vs Normal Flow (No Data)",
            xaxis_title="Complexity",
            yaxis_title="Error Rate (%)"
        )
        return fig
    
    fig = px.bar(
        error_rates,
        x="Complexity",
        y="Error Rate",
        color="Mode",
        title="Error Rates: AI Search vs Normal Flow",
        barmode="group",
        labels={
            "Error Rate": "Error Rate (%)"
        },
        color_discrete_sequence=PASTEL_COLORS,
    )
    
    # Add value labels only if there's data
    for data in fig.data:
        if len(data.x) > 0 and len(data.y) > 0:  # Check if there's data to plot
            fig.add_traces(
                go.Scatter(
                    x=data.x,
                    y=data.y,
                    mode="text",
                    text=[f"{y:.1f}%" for y in data.y],
                    textposition="top center",
                    showlegend=False,
                    textfont=dict(size=10)
                )
            )
    
    # Update layout
    fig.update_layout(
        yaxis=dict(range=[0, max(100, error_rates["Error Rate"].max() * 1.2)]),  # Add some padding for labels
        showlegend=True
    )
    
    return fig

def calculate_query_times(df):
    """Calculate total query times for AI Search and Normal Flow."""
    query_times = []
    for _, row in df.iterrows():
        operation_times = row.get("operation_times", {})
        if not operation_times:
            continue

        # Calculate total query time
        exec_times = sum(
            float(operation_times.get(op, 0))
            for op in [
                "Query Execution",
                "Query Execution 1",
                "Query Execution 2",
                "Query Fixing",
            ]
        )

        if row["ai_search_pattern"]:
            # AI Search: VannaAI SQL Generation + Query Executions
            total_time = exec_times + float(
                operation_times.get("VannaAI SQL Generation", 0)
            )
            mode = "AI Search"
        else:
            # Normal Flow: Initial Query Generation + Query Executions
            total_time = (
                exec_times
                + float(operation_times.get("Initial Query Generation", 0))
                + float(operation_times.get("Table Retrieval", 0))
                + float(operation_times.get("Column Extraction", 0))
                + float(operation_times.get("Query Optimization", 0))
            )
            mode = "Normal Flow"

        query_times.append({
            "Mode": mode,
            "Complexity": row["complexity"],
            "Total Query Time": total_time,
        })
    
    return pd.DataFrame(query_times)

def plot_query_time_comparison(df):
    """Plot query time comparison between AI Search and Normal Flow."""
    query_time_df = calculate_query_times(df)
    
    fig = px.box(
        query_time_df,
        x="Complexity",
        y="Total Query Time",
        color="Mode",
        title="Total Query Time: AI Search vs Normal Flow",
        labels={
            "Total Query Time": "Total Query Time (seconds)"
        },
        color_discrete_sequence=PASTEL_COLORS,
    )
    return fig

def generate_ai_search_stats(df):
    """Generate statistical analysis for AI Search vs Normal Flow."""
    # Add ai_search flag
    df = df.copy()
    df["ai_search"] = df["ai_search_pattern"].apply(
        lambda x: "AI Search" if x and not pd.isna(x) else "Normal Flow"
    )
    
    # Overall statistics
    overall_stats = df.groupby("ai_search").agg({
        "duration": ["mean", "std", "min", "max"],
        "error_type": lambda x: (x.notna().sum() / len(x)) * 100,
    }).round(3)
    
    overall_stats.columns = [
        "Mean Duration",
        "Std Duration",
        "Min Duration",
        "Max Duration",
        "Error Rate (%)",
    ]
    
    # Query time statistics
    query_time_df = calculate_query_times(df)
    query_time_stats = query_time_df.groupby(["Mode", "Complexity"])["Total Query Time"].agg([
        "mean", "std", "min", "max"
    ]).round(3)
    
    # Calculate key findings
    ai_mean = overall_stats.loc["AI Search", "Mean Duration"]
    normal_mean = overall_stats.loc["Normal Flow", "Mean Duration"]
    diff_pct = ((ai_mean - normal_mean) / normal_mean) * 100
    
    ai_error = overall_stats.loc["AI Search", "Error Rate (%)"]
    normal_error = overall_stats.loc["Normal Flow", "Error Rate (%)"]
    error_diff = ai_error - normal_error
    
    ai_query_time = query_time_df[query_time_df["Mode"] == "AI Search"]["Total Query Time"].mean()
    normal_query_time = query_time_df[query_time_df["Mode"] == "Normal Flow"]["Total Query Time"].mean()
    query_time_diff = ((ai_query_time - normal_query_time) / normal_query_time) * 100
    
    findings = {
        "Duration Comparison": f"AI Search is {abs(diff_pct):.1f}% {'slower' if diff_pct > 0 else 'faster'} than Normal Flow",
        "Error Rate Comparison": f"AI Search has {abs(error_diff):.1f}% {'higher' if error_diff > 0 else 'lower'} error rate than Normal Flow",
        "Query Time Comparison": f"AI Search is {abs(query_time_diff):.1f}% {'slower' if query_time_diff > 0 else 'faster'} than Normal Flow"
    }
    
    return overall_stats, query_time_stats, findings

def export_to_pdf(df, selected_report):
    """Export all visualizations and statistics to PDF."""
    import matplotlib.pyplot as plt
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, landscape
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, ListFlowable, ListItem
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    import io
    import markdown2
    from pathlib import Path
    import re
    
    # Create PDF in memory
    pdf_buffer = io.BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(letter))
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    styles.add(ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.HexColor('#1f77b4'),  # Plotly's default blue
        alignment=TA_CENTER
    ))
    
    styles.add(ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceBefore=6,
        spaceAfter=6
    ))
    
    styles.add(ParagraphStyle(
        'CustomBold',
        parent=styles['CustomBody'],
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        'CustomList',
        parent=styles['CustomBody'],
        leftIndent=20,
        firstLineIndent=0,
        bulletIndent=10,
        spaceBefore=0,
        spaceAfter=3
    ))
    
    # Title
    story.append(Paragraph(f"Benchmark Report: {selected_report.name}", styles['CustomTitle']))
    story.append(Spacer(1, 20))

    # Try to load existing summary report
    summary_path = Path(selected_report) / "visualizations" / "summary_report.md"
    if summary_path.exists():
        with open(summary_path) as f:
            summary_content = f.read()
            
            # Convert markdown to HTML using markdown2
            html = markdown2.markdown(summary_content, extras=['tables', 'fenced-code-blocks'])
            
            # Split content into sections based on headers
            sections = []
            current_header = None
            current_content = []
            
            for line in html.split('\n'):
                header_match = re.search(r'<h(\d)[^>]*>(.*?)</h\1>', line)
                if header_match:
                    # If we have previous content, add it to sections
                    if current_header is not None:
                        sections.append((current_header, '\n'.join(current_content)))
                    # Start new section
                    current_header = (header_match.group(1), header_match.group(2))
                    current_content = []
                else:
                    current_content.append(line)
            
            # Add last section if exists
            if current_header is not None and current_content:
                sections.append((current_header, '\n'.join(current_content)))
            
            # Process sections
            for (header_level, header_text), content in sections:
                # Add header
                story.append(Paragraph(header_text.strip(), styles[f'Heading{header_level}']))
                
                # Process content
                content = content.strip()
                if not content:
                    continue
                
                # Handle lists
                if '<ul>' in content or '<ol>' in content:
                    list_items = re.findall(r'<li>(.*?)</li>', content)
                    bullets = []
                    for item in list_items:
                        # Handle bold text in list items
                        item = re.sub(r'<strong>(.*?)</strong>', r'<b>\1</b>', item)
                        bullets.append(ListItem(Paragraph(item, styles['CustomList'])))
                    story.append(ListFlowable(bullets, bulletType='bullet'))
                
                # Handle tables
                elif '<table>' in content:
                    # Extract table data
                    rows = []
                    for row in re.findall(r'<tr>(.*?)</tr>', content):
                        cells = re.findall(r'<t[dh]>(.*?)</t[dh]>', row)
                        rows.append(cells)
                    
                    if rows:
                        table = Table(rows)
                        table.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 11),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f8ff')),
                            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 1), (-1, -1), 10),
                            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
                        ]))
                        story.append(table)
                
                # Handle regular paragraphs
                else:
                    # Handle bold text
                    content = re.sub(r'<strong>(.*?)</strong>', r'<b>\1</b>', content)
                    story.append(Paragraph(content, styles['CustomBody']))
                
                story.append(Spacer(1, 10))
            
            story.append(PageBreak())

    # Overview Statistics with colors
    story.append(Paragraph("Overview Statistics", styles["Heading2"]))
    overview_data = [
        ["Metric", "Value"],
        ["Total Test Cases", str(len(df))],
        ["Average Duration (s)", f"{df['duration'].mean():.2f}"],
        ["Success Rate", f"{(df['error_type'].isna().mean() * 100):.1f}%"],
        ["Languages", str(len(df['language'].unique()))],
        ["Complexity Levels", str(len(df['complexity'].unique()))],
        ["Error Types", str(len(df['error_type'].dropna().unique()))]
    ]
    overview_table = Table(overview_data)
    overview_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f77b4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f8ff')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(overview_table)
    story.append(Spacer(1, 20))
    
    # Function to save plotly figure as image with better quality
    def fig_to_img(fig, width=1000, height=500):
        # Update figure template for better colors
        fig.update_layout(
            template="plotly",  # Use the default plotly template for better colors
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot area
            colorway=PASTEL_COLORS,  # Use a colorful palette
        )
        img_bytes = fig.to_image(format="png", width=width, height=height, scale=2)
        img_io = io.BytesIO(img_bytes)
        return Image(img_io, width=9*inch, height=4.5*inch)
    
    # Add all visualizations with sections
    sections = [
        ("Performance Analysis", [
            ("Duration Distribution", plot_duration_distribution(df)),
            ("Operation Times", plot_operation_times(df)),
            ("Operation Times by Complexity", plot_operation_time_by_complexity(df)),
            ("Operation Times by Language", plot_operation_time_by_language(df))
        ]),
        ("AI Search Analysis", [
            ("Duration Analysis", plot_ai_search_duration_by_complexity(df)),
            ("Error Rate Analysis", plot_ai_search_error_rates(df)),
            ("Query Time Analysis", plot_query_time_comparison(df)),
            ("AI Search Patterns", plot_ai_search_analysis(df))
        ]),
        ("Error Analysis", [
            ("Error Distribution", plot_error_distribution(df)),
            ("Retry Analysis", plot_retry_analysis(df)),
            ("Error by Complexity", plot_error_heatmap(df, "complexity", "error_type")),
            ("Error by Language", plot_error_heatmap(df, "language", "error_type"))
        ]),
        ("Context Analysis", [
            ("Context Depth Performance", plot_performance_by_context_depth(df)),
            ("Context vs Complexity", plot_error_heatmap(df, "complexity", "chat_context_depth")),
            ("Context vs Language", plot_error_heatmap(df, "language", "chat_context_depth"))
        ]),
        ("Distribution Analysis", [
            ("Complexity Distribution", plot_complexity_distribution(df)),
            ("Language Distribution", plot_language_distribution(df)),
            ("Error Type Distribution", plot_error_distribution(df))
        ])
    ]
    
    for section_title, plots in sections:
        # Add section header with color
        section_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            textColor=colors.HexColor('#1f77b4'),
            spaceBefore=20,
            spaceAfter=10
        )
        story.append(Paragraph(section_title, section_style))
        story.append(Spacer(1, 10))
        
        for plot_title, fig in plots:
            # Add plot title with color
            plot_style = ParagraphStyle(
                'PlotTitle',
                parent=styles['Heading3'],
                textColor=colors.HexColor('#2c3e50'),
                spaceBefore=15,
                spaceAfter=5
            )
            story.append(Paragraph(plot_title, plot_style))
            story.append(fig_to_img(fig))
            story.append(Spacer(1, 10))
        
        story.append(PageBreak())

    # Build PDF
    doc.build(story)
    
    # Get the PDF content
    pdf_content = pdf_buffer.getvalue()
    pdf_buffer.close()
    
    return pdf_content

def main():
    st.set_page_config(page_title="Benchmark Results Viewer", layout="wide")
    st.title("Benchmark Results Viewer")

    # Sidebar - Report Selection
    st.sidebar.header("Report Selection")
    reports = get_available_reports()
    
    # Single run selection
    selected_report = st.sidebar.selectbox(
        "Select Benchmark Report",
        reports,
        format_func=lambda x: x.name
    )

    if not selected_report:
        st.warning("No benchmark reports found.")
        return

    # Load data for single run analysis
    data = load_benchmark_data(selected_report)
    df = create_metrics_df(data)

    # Multiple runs selection for comparison
    st.sidebar.header("Run Comparison")
    selected_runs = st.sidebar.multiselect(
        "Select Runs to Compare",
        reports,
        format_func=lambda x: x.name
    )

    # Export button - Moved after data loading
    if st.sidebar.button("Export Report to PDF"):
        with st.spinner("Generating PDF report..."):
            pdf_content = export_to_pdf(df, selected_report)
            
            # Create download button
            st.sidebar.download_button(
                label="📥 Download PDF Report",
                data=pdf_content,
                file_name=f"benchmark_report_{selected_report.name}.pdf",
                mime="application/pdf"
            )
            st.sidebar.success("PDF report generated successfully!")

    # Create tabs for different analyses - Reordered and grouped logically
    tab_overview, tab_performance, tab_ai_search, tab_errors, tab_context, tab_features, tab_comparison, tab_details = st.tabs([
        "Overview",                  # High-level summary
        "Performance Analysis",      # Core performance metrics
        "AI Search Analysis",        # AI-specific analysis
        "Error Analysis",           # Error patterns and retry analysis
        "Context Analysis",         # Context-related metrics
        "Feature Analysis",         # Feature-specific analysis
        "Run Comparison",           # Multi-run comparison
        "Detailed Results"          # Individual test case details
    ])

    with tab_overview:
        st.header("Report Overview")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Test Cases", len(df))
        with col2:
            st.metric("Avg Duration (s)", f"{df['duration'].mean():.2f}")
        with col3:
            st.metric("Success Rate", f"{(df['error_type'].isna().mean() * 100):.1f}%")
        with col4:
            st.metric("Languages", len(df["language"].unique()))

        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(plot_complexity_distribution(df), use_container_width=True)
        with col2:
            st.plotly_chart(plot_language_distribution(df), use_container_width=True)
        with col3:
            st.plotly_chart(plot_error_distribution(df), use_container_width=True)

    with tab_performance:
        st.header("Performance Analysis")
        
        # Duration Distribution
        st.subheader("Query Duration Analysis")
        st.plotly_chart(plot_duration_distribution(df), use_container_width=True)
        
        # Operation Times
        st.subheader("Operation Time Analysis")
        st.plotly_chart(plot_operation_times(df), use_container_width=True)
        
        # Operation Times by Complexity and Language
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(plot_operation_time_by_complexity(df), use_container_width=True)
        with col2:
            st.plotly_chart(plot_operation_time_by_language(df), use_container_width=True)

    with tab_ai_search:
        st.header("AI Search vs Normal Flow Analysis")
        
        # Overall Statistics
        overall_stats, query_time_stats, findings = generate_ai_search_stats(df)
        
        # Key Findings
        st.subheader("Key Findings")
        for metric, finding in findings.items():
            st.write(f"- **{metric}:** {finding}")
        
        # Duration Analysis
        st.subheader("Duration Analysis")
        st.plotly_chart(plot_ai_search_duration_by_complexity(df), use_container_width=True)
        
        # Error Rate Analysis
        st.subheader("Error Rate Analysis")
        st.plotly_chart(plot_ai_search_error_rates(df), use_container_width=True)
        
        # Query Time Analysis
        st.subheader("Query Time Analysis")
        st.plotly_chart(plot_query_time_comparison(df), use_container_width=True)
        
        # Detailed Statistics
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Overall Performance Statistics")
            st.dataframe(overall_stats, use_container_width=True)
        
        with col2:
            st.subheader("Query Time Statistics by Complexity")
            st.dataframe(query_time_stats, use_container_width=True)

    with tab_errors:
        st.header("Error Analysis")
        
        # Retry Analysis
        st.subheader("Retry Performance")
        st.plotly_chart(plot_retry_analysis(df), use_container_width=True)
        
        # Error Correlations
        st.subheader("Error Correlations")
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                plot_error_heatmap(df, "complexity", "error_type"),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                plot_error_heatmap(df, "language", "error_type"),
                use_container_width=True
            )

    with tab_context:
        st.header("Context Analysis")
        
        # Context Depth Analysis
        st.plotly_chart(plot_performance_by_context_depth(df), use_container_width=True)
        
        # Error Heatmap
        st.subheader("Error Analysis by Context")
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                plot_error_heatmap(df, "complexity", "chat_context_depth"),
                use_container_width=True
            )
        with col2:
            st.plotly_chart(
                plot_error_heatmap(df, "language", "chat_context_depth"),
                use_container_width=True
            )

    with tab_features:
        st.header("Feature Analysis")
        
        # Feature Performance
        st.plotly_chart(plot_feature_analysis(df), use_container_width=True)
        
        # AI Search Patterns
        if "ai_search_pattern" in df.columns:
            st.plotly_chart(plot_ai_search_analysis(df), use_container_width=True)

    with tab_comparison:
        st.header("Run Comparison Analysis")
        
        if len(selected_runs) < 2:
            st.warning("Please select at least 2 runs to compare in the sidebar.")
        else:
            # Load data for all selected runs
            comparison_df = load_multiple_runs(selected_runs)
            
            # Overall Trends
            st.subheader("Performance Trends")
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(plot_duration_trend(comparison_df), use_container_width=True)
            with col2:
                st.plotly_chart(plot_error_rate_trend(comparison_df), use_container_width=True)
            
            # Operation Time Comparison
            st.subheader("Operation Time Comparison")
            st.plotly_chart(plot_operation_time_comparison(comparison_df), use_container_width=True)
            
            # Success Rate Comparisons
            st.subheader("Success Rate Comparisons")
            category = st.selectbox(
                "Select Category for Success Rate Comparison",
                ["complexity", "language", "scenario_type"]
            )
            st.plotly_chart(plot_success_rate_by_category(comparison_df, category), use_container_width=True)
            
            # Performance Heatmaps
            st.subheader("Performance Comparison Heatmaps")
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(
                    plot_performance_comparison_heatmap(comparison_df, "duration"),
                    use_container_width=True
                )
            with col2:
                st.plotly_chart(
                    plot_performance_comparison_heatmap(comparison_df, "error_rate"),
                    use_container_width=True
                )
            
            # Statistical Analysis
            st.subheader("Statistical Analysis")
            run_stats = comparison_df.groupby("run_id").agg({
                "duration": ["mean", "std", "min", "max"],
                "error_type": lambda x: (~x.isna()).mean() * 100,
                "timestamp": "first"
            }).sort_values(("timestamp", "first"))
            
            st.dataframe(run_stats, use_container_width=True)

    with tab_details:
        st.header("Detailed Results")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            complexity_filter = st.multiselect(
                "Complexity",
                df["complexity"].unique()
            )
        with col2:
            language_filter = st.multiselect(
                "Language",
                df["language"].unique()
            )
        with col3:
            scenario_filter = st.multiselect(
                "Scenario Type",
                df["scenario_type"].unique()
            )

        # Apply filters
        filtered_df = df.copy()
        if complexity_filter:
            filtered_df = filtered_df[filtered_df["complexity"].isin(complexity_filter)]
        if language_filter:
            filtered_df = filtered_df[filtered_df["language"].isin(language_filter)]
        if scenario_filter:
            filtered_df = filtered_df[filtered_df["scenario_type"].isin(scenario_filter)]

        # Display filtered results
        st.dataframe(
            filtered_df[[
                "test_case_id",
                "question",
                "complexity",
                "language",
                "scenario_type",
                "duration",
                "error_type"
            ]],
            use_container_width=True
        )

        # Detailed Test Case View
        st.header("Test Case Details")
        selected_case = st.selectbox(
            "Select Test Case",
            filtered_df["test_case_id"],
            format_func=lambda x: f"{x} - {filtered_df[filtered_df['test_case_id'] == x]['question'].iloc[0][:50]}..."
        )

        if selected_case:
            case_data = filtered_df[filtered_df["test_case_id"] == selected_case].iloc[0]
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Question & Answer")
                st.write("**Question:**")
                st.write(case_data["question"])
                st.write("**Answer:**")
                st.write(case_data["answer"])
            
            with col2:
                st.subheader("SQL & Results")
                st.write("**SQL Query:**")
                st.code(case_data["sql"], language="sql")
                st.write("**Results:**")
                st.write(case_data["sql_result"])

            st.subheader("Performance Breakdown")
            st.write("**Operation Times:**")
            op_times = pd.Series(case_data["operation_times"])
            st.bar_chart(op_times)

            if case_data["error_type"]:
                st.error(f"Error Type: {case_data['error_type']}")
                st.error(f"Error Details: {case_data['error']}")

if __name__ == "__main__":
    main() 