from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize  
from reportlab.lib.units import cm  
PAGE_HEIGHT=defaultPageSize[1]  
PAGE_WIDTH=defaultPageSize[0]  
styles = getSampleStyleSheet()

Title = "Korrektur Zeitaufzeichnung"  
pageinfo = "platypus example"

text = [ "Dienstbeginn\t zu korrigierende Zeit  -  Zeit", "Dienstende zu korrigierende Zeit  -  Zeit", "Sonderurlaub zu korrigierende Zeit  -  Zeit", "Vergessene Buchung zu korrigierende Zeit  -  Zeit", "Dienstreise zu korrigierende Zeit  -  Zeit"]


def myFirstPage(canvas, doc):  
    canvas.saveState()  
    canvas.setFont('Helvetica-Bold',16)  
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)  
    canvas.setFont('Helvetica',9)  
    canvas.drawString(cm, 0.75 * cm,"First Page / %s" % pageinfo)  
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawString(cm, 0.75 * cm,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def go():
    doc = SimpleDocTemplate("zeitkarte.pdf")
    Story = [Spacer(1,2*cm)]
    style = styles["Normal"]
    Name = "Name"
    Story.append(Paragraph("name", style))
    for line in text:
        bogustext = (line)
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*cm))
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)





if __name__ == "__main__":
    print("Hello World")
    go()
