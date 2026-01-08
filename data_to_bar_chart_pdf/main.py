from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart


def build_pdf(output_path="styled_document.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()

    title = Paragraph("Styled PDF Document", styles["Title"])

    sales_data = {
        "Alpha": [1200, 1500, 1700],
        "Beta": [1100, 1300, 1600],
        "Gamma": [1000, 1400, 1800],
    }

    table_data = [
        ["Product", "Q1 Sales", "Q2 Sales", "Q3 Sales"],
        ["Alpha"] + sales_data["Alpha"],
        ["Beta"] + sales_data["Beta"],
        ["Gamma"] + sales_data["Gamma"],
    ]

    table = Table(
        table_data,
        style=[
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ],
    )

    chart = Drawing(400, 200)
    bar_chart = VerticalBarChart()
    bar_chart.data = [
        sales_data["Alpha"],
        sales_data["Beta"],
        sales_data["Gamma"],
    ]
    bar_chart.categoryAxis.categoryNames = ["Q1", "Q2", "Q3"]
    bar_chart.valueAxis.valueMin = 0
    max_val = max(max(values) for values in bar_chart.data)
    bar_chart.valueAxis.valueMax = max_val * 1.1
    bar_chart.valueAxis.valueStep = 100

    chart.add(bar_chart)

    story = [title, Spacer(1, 12), table, Spacer(1, 24), chart]
    doc.build(story)


if __name__ == "__main__":
    build_pdf()