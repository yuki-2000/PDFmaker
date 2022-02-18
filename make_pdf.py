import img2pdf
from pathlib import Path

#単処理
def ImageToPdf(outputpath, imagepath):
    '''
    outputpath: pathlib.Path()
    imagepath: pathlib.Path()
    '''
    lists = list(imagepath.glob("**/*"))#単フォルダ内を検索
    #pdfを作成
    with open(outputpath,"wb") as f:
        #jpg,pngファイルだけpdfに結合
        #Pathlib.WindowsPath()をstring型に変換しないとエラー
        #jpegにも対応
        f.write(img2pdf.convert([str(i) for i in lists if i.match("*.jpg") or i.match("*.png") or i.match("*.jpeg")]))
    print(outputpath.name + " :Done")

#複数フォルダをループ処理する
while True:
    #作業フォルダ
    base_path = input("PDFに変換したいファルダが入った親フォルダをd&Pしてください")
    base_path = base_path.strip(" \' ")
    #作業フォルダ内のディレクトリだけを抽出する
    glob = Path(base_path).glob("*")
    imagefolderlist = list([item for item in list(glob) if item.is_dir()])
    #outputpathに指定ディレクトリと同名を指定する
    outputpathlist = list([item.with_name(item.name + ".pdf") for item in imagefolderlist])
    #ループ処理を行う
    for outputpath,imagepath in zip(outputpathlist,imagefolderlist):
        try:
            ImageToPdf(outputpath,imagepath)
        except:
            pass
