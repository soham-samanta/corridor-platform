import aspose.words as aw

doc = aw.Document()

builder = aw.DocumentBuilder(doc)

builder.insert_image(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\extract\conf_mat.png")
builder.insert_image(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\extract\hist.png")
builder.insert_image(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\extract\scatter.png")


doc.save("out.docx")
