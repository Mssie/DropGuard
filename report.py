from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf(name, risk, explanation, plan):
    filename = f"{name}_DropGuard_Report.pdf"
    doc = SimpleDocTemplate(filename)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("DROP GUARD AI REPORT", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph(f"Student: {name}", styles["Normal"]))
    elements.append(Paragraph(f"Risk Score: {risk}%", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph("AI Explanation:", styles["Heading2"]))
    elements.append(Paragraph(explanation, styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(Paragraph("Intervention Plan:", styles["Heading2"]))
    elements.append(Paragraph(plan, styles["Normal"]))

    doc.build(elements)
    return filename
