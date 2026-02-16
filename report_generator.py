from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def generate_pdf(student_name, risk, explanation, plan, filename="report.pdf"):

    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    elements.append(Paragraph("DROP GUARD - AI RISK REPORT", title_style))
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph(f"Student: {student_name}", normal_style))
    elements.append(Paragraph(f"Risk Score: {risk}%", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("AI Narrative:", styles["Heading2"]))
    elements.append(Paragraph(explanation, normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("Intervention Plan:", styles["Heading2"]))
    elements.append(Paragraph(plan, normal_style))

    doc.build(elements)
    return filename
