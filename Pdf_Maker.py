from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def create_pdf_from_csv(filtered_df, pdf_file, title="Report"):
    pdf = SimpleDocTemplate(pdf_file, pagesize=landscape(letter))
    elements = []
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading = Paragraph(title, title_style)
    elements.append(heading)
    elements.append(Spacer(1, 12))
    data = [filtered_df.columns.tolist()] + filtered_df.values.tolist()
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)
    elements.append(table)
    pdf.build(elements)


if __name__ == "__main__":
    print('ERROR')
