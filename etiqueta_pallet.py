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

def create_pallet_label_pdf(label_data):
    page_size = (100 * mm, 149 * mm)

    directory = "Etiquetas Generadas"
    filename = "Etiqueta Pallet.pdf"
    full_path = os.path.join(directory, filename)

    # Create a new PDF file
    c = canvas.Canvas(full_path, pagesize=page_size)

    # Label dimensions - THIS ARE THE GENERAL DIMENSIONS FOR THE WHOLE LABEL
    label_width = 100 * mm
    label_height = 149 * mm

    # Draw label border
    #c.rect(0, 0, label_width, label_height)

    # Draw the image
    image_path = label_data[0]
    image_width = 100 * mm
    image_height = 20 * mm
    c.drawImage(image_path, 0, label_height - image_height, width=image_width, height=image_height)

    # Text1
    c.setFont("Helvetica-Bold", 13)
    text = label_data[1]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width)/2, label_height - image_height - 5 * mm, format(text))
    # Text2
    c.setFont("Helvetica", 13)
    text = label_data[2]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - image_height - 13 * mm, format(text))
    # Text3
    c.setFont("Helvetica", 13)
    text = label_data[3]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - image_height - 21 * mm, format(text))

    # Draw the separating line
    horizontal_margin = 2 * mm
    top_margin = 45 * mm
    c.line(horizontal_margin, label_height - top_margin, label_width - horizontal_margin, label_height - top_margin)

    # Marca
    c.setFont("Helvetica", 14)
    text = label_data[11]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 10 * mm, format(text))

    # Text4
    # Draw the barcode number
    c.setFont("Helvetica-Bold", 20)
    text = label_data[4]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 20 * mm, format(text))

    # Draw the barcode
    barcode_number = label_data[4]
    barcode = code128.Code128(barcode_number, barHeight=8 * mm, barWidth=2.0)
    barcode.drawOn(c, (label_width - barcode.width)/2, label_height - top_margin - 30 * mm)

    # Text5
    c.setFont("Helvetica", 13)
    text = label_data[5]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 37 * mm, format(text))

    # Text6 and Text7
    c.setFont("Helvetica", 13)
    text = label_data[6] + "     " + label_data[7]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 50 * mm, format(text))

    # Text8
    c.setFont("Helvetica", 13)
    text = label_data[8]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 63 * mm, format(text))

    # Text9
    c.setFont("Helvetica", 13)
    text = label_data[9]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 76 * mm, format(text))

    # Text10
    c.setFont("Helvetica", 13)
    text = label_data[10]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 89 * mm, format(text))

    # Text11
    c.setFont("Helvetica", 13)
    text = label_data[12]
    text_width = c.stringWidth(format(text))
    c.drawString((label_width - text_width) / 2, label_height - top_margin - 99 * mm, format(text))

    # Save the PDF and close the canvas
    c.save()
