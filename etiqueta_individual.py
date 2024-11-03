from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib import utils

def create_individual_label_pdf(label_data):
    page_size = (50 * mm, 25 * mm)

    # Create a new PDF file
    c = canvas.Canvas("Etiqueta Individual Simple.pdf", pagesize=page_size)

    # Set the font and font size
    c.setFont("Helvetica", 10)

    # Calculate the label dimensions
    label_width = 50 * mm
    label_height = 25 * mm

    # Draw the label border
    #c.rect(0, 0, label_width, label_height)

    # Text1
    # Draw the barcode number
    c.setFont("Helvetica-Bold", 8)
    text = label_data[0]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, 22 * mm, format(text))

    # Draw the barcode
    barcode_number = label_data[0]
    barcode = code128.Code128(barcode_number, barHeight=8 * mm, barWidth=1.0)
    barcode.drawOn(c, (label_width - barcode.width)/2, 13 * mm)

    # Text2
    c.setFont("Helvetica", 7)
    text = label_data[1]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, 10 * mm, format(text))

    # Text3 and Text4
    c.setFont("Helvetica", 7)
    text = label_data[2] + "                       " + label_data[3]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, 6 * mm, format(text))

    # Text5 and Text6
    c.setFont("Helvetica", 7)
    text = label_data[4] + "   " + label_data[5]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, 2 * mm, format(text))

    # Save the PDF and close the canvas
    c.save()

label_data = ["10202520338",
              "ITEM NAME",
              "UTM: 1",
              "Cantidad: 1",
              "DERIVADA: 1234567890",
              "Peso: 2,5 kg"]

create_individual_label_pdf(label_data)
