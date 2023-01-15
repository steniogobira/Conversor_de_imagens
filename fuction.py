import os
from PIL import Image

path = '\\Users\\steni\\Desktop\\TESTE\\'
erro = []


def to_jpeg(path):
    global erro
    list_files = os.listdir(path)
    list_img = [i for i in list_files if i.split(
        '.')[-1] != 'jpeg' or 'JPEG']

    i = 1
    for img in list_img:
        print(
            f'Convertendo imagem {img}. \n{i}/{len(list_img)} imagens'
        )
        try:
            input = path + img
            output = path + img.replace(img.split('.')[-1], '.jpeg')
            im = Image.open(input).convert("RGB")
            im.save(output)
            i += 1

        except:
            erro.append(img.split(".")[-1])
            print(
                f'Desculpa, não posso converter o arquivo om extensão {img.split(".")[-1]}'
            )

        else:
            continue


def arquivos_in(path):

    global erro
    os.chdir(path)
    lista_arquivos = os.listdir()

    for arquivos in lista_arquivos:
        if os.path.isfile(arquivos):
            extensoes = arquivos.split('.')[-1]
            if extensoes not in erro:
                if os.path.exists(os.getcwd() + '/' + extensoes):
                    os.rename(arquivos, os.getcwd() + '/' +
                              extensoes + '/' + arquivos)
                else:
                    os.mkdir(arquivos.split('.')[-1])
                    os.rename(arquivos, os.getcwd() + '/' +
                              extensoes + '/' + arquivos)


to_jpeg(path)

arquivos_in(path)
