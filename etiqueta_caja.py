import os
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
# The following imports are necessary for reportlab to work properly
from reportlab.graphics.barcode import code93
from reportlab.graphics.barcode import code39
from reportlab.graphics.barcode import usps
from reportlab.graphics.barcode import usps4s
from reportlab.graphics.barcode import ecc200datamatrix

def create_box_label_pdf(label_data):
    page_size = (100 * mm, 55 * mm)

    directory = "Etiquetas Generadas"
    filename = "Etiqueta caja.pdf"
    full_path = os.path.join(directory, filename)

    # Create a new PDF file
    c = canvas.Canvas(full_path, pagesize=page_size)

    # Label dimensions - THIS ARE THE GENERAL DIMENSIONS FOR THE WHOLE LABEL
    label_width = 100 * mm
    label_height = 55 * mm

    # The following are the elements for the label in order
    # Code
    # Barcode
    # Description
    # UTM CANTIDAD
    # PRES W X Y Z
    # DERIVADA PESO

    # Draw label border
    c.rect(0, 0, label_width, label_height)

    # Marca
    c.setFont("Helvetica", 20)
    text = label_data[0]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 8 * mm, format(text))

    # Text1
    # Draw the barcode number
    c.setFont("Helvetica-Bold", 20)
    text = label_data[1]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 17 * mm, format(text))
    c.drawString

    # Draw the barcode
    barcode_number = label_data[0]
    barcode = code128.Code128(barcode_number, barHeight=8 * mm, barWidth=2.0)
    barcode.drawOn(c, (label_width - barcode.width) / 2, label_height - 27 * mm)

    # Text2
    c.setFont("Helvetica", 13)
    text = label_data[2]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 32 * mm, format(text))

    # Text3 and Text4
    c.setFont("Helvetica", 13)
    text = label_data[3] + "     " + label_data[4]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 37 * mm, format(text))

    # Text5 and Text6
    c.setFont("Helvetica", 13)
    text = label_data[5] + "     " + label_data[6]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 42 * mm, format(text))

    # Text7 and Text8
    c.setFont("Helvetica", 13)
    text = label_data[7] + "     " + label_data[8]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 47 * mm, format(text))

    # Text9
    c.setFont("Helvetica", 13)
    text = label_data[9]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - 52 * mm, format(text))

    # Save the PDF and close the canvas
    c.save()
"""
# Test data
label_data = ["BRAND",
              "12345678901",
              "Item name example",
              "UTM: 1",
              "Quantity: 4",
              "Pres:",
              "W: 000   X: 000   Y: 004   Z: 001",
              "Derivada: 1234567890",
              "Peso: 10 kg"]

create_box_label_pdf(label_data)
"""
