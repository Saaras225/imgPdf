import os
import img2pdf

with open("imagesToPdF.pdf","wb") as file:
	file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\saray\\Documents\\PROYECTOS\\imgPdf") if i.endswith(".jpeg")]))