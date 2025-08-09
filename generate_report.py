from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import os

# Paths
graphs_folder = "graphs"
output_pdf = "titanic_report.pdf"
insights_file = os.path.join(graphs_folder, "insights.txt")

# Create PDF
doc = SimpleDocTemplate(output_pdf, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b>Titanic Data Analysis Report</b>", styles['Title']))
elements.append(Spacer(1, 20))

# Add insights
if os.path.exists(insights_file):
    elements.append(Paragraph("<b>Insights:</b>", styles['Heading2']))
    with open(insights_file, 'r') as f:
        for line in f:
            elements.append(Paragraph(line.strip(), styles['Normal']))
    elements.append(Spacer(1, 20))

# Add images
for img_name in os.listdir(graphs_folder):
    if img_name.endswith(".png"):
        img_path = os.path.join(graphs_folder, img_name)
        elements.append(Paragraph(f"<b>{img_name}</b>", styles['Heading3']))
        elements.append(Image(img_path, width=400, height=300))
        elements.append(Spacer(1, 20))

# Build PDF
doc.build(elements)
print(f"PDF report generated: {output_pdf}")