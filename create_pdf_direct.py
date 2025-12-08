#!/usr/bin/env python3
"""Create PDF directly using reportlab"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_pdf():
    doc = SimpleDocTemplate("submission_midterm_simple.pdf", pagesize=A4,
                           rightMargin=2.5*cm, leftMargin=2.5*cm,
                           topMargin=2.5*cm, bottomMargin=2.5*cm)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='black',
        spaceAfter=5,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    story.append(Paragraph("Insurance Claim Timeline Retrieval System", title_style))
    
    # Subtitle
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#333333',
        spaceAfter=15,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    story.append(Paragraph("GenAI Multi-Agent Systems — Midterm", subtitle_style))
    
    # Student info
    student_style = ParagraphStyle(
        'Student',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    story.append(Paragraph("<b>Student:</b> Nitzan Nossery", student_style))
    
    # Date
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#666666',
        spaceAfter=25,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    story.append(Paragraph("Date: December 2025", date_style))
    
    # System Overview
    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=8,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    story.append(Paragraph("System Overview", heading_style))
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        fontName='Times-Roman'
    )
    
    overview_text = """This project implements a multi-agent GenAI system for querying an insurance claim timeline. A ManagerAgent routes user queries to a SummarizationAgent for high-level timeline questions, or to a NeedleAgent for precise factual retrieval. The system uses hierarchical RAG indexing with an Auto-Merging Retriever over a synthetic, time-stamped claim dataset, and integrates MCP-style tools for date differences and rental cost computation."""
    story.append(Paragraph(overview_text, normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Evaluation Results
    story.append(Paragraph("Evaluation Results", heading_style))
    story.append(Paragraph("<b>Achieved Full Score Across All Quality Metrics</b>", normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=normal_style,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=5
    )
    story.append(Paragraph("• Correctness: 5.0 / 5.0", bullet_style))
    story.append(Paragraph("• Relevancy: 5.0 / 5.0", bullet_style))
    story.append(Paragraph("• Recall: 5.0 / 5.0", bullet_style))
    story.append(Spacer(1, 0.3*cm))
    
    checkmark_style = ParagraphStyle(
        'Checkmark',
        parent=normal_style,
        textColor='#00AA00',
        spaceAfter=15
    )
    story.append(Paragraph("✔ All 8 evaluation queries scored 5/5 across all metrics.", checkmark_style))
    
    # MCP Usage
    story.append(Paragraph("MCP Usage", heading_style))
    mcp_text = """MCP-style tools are used to extend the LLM beyond pure text reasoning by delegating precise, auditable computations (date differences and rental cost calculations) to explicit tools, while the agents focus on retrieval, routing, and explanation."""
    story.append(Paragraph(mcp_text, normal_style))
    story.append(Spacer(1, 1*cm))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#666666',
        spaceAfter=0,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    story.append(Paragraph("Submission Document — Midterm Assignment", footer_style))
    
    doc.build(story)
    print("✅ PDF created successfully: submission_midterm_simple.pdf")

if __name__ == "__main__":
    try:
        create_pdf()
    except ImportError:
        print("❌ reportlab not installed. Installing...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
        create_pdf()
