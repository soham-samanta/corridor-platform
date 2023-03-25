import aspose.words as aw

def doccreate():

    doc = aw.Document()

    builder = aw.DocumentBuilder(doc)

    builder.insert_image(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\chakravyuh\extract\conf_mat.png")
    # builder.insert_image(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\extract\hist.png")
    # builder.insert_image(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\extract\scatter.png")


    doc.save(r"C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\chakravyuh\toword\out.docx")
