import os
from PIL import Image


errojpge = []
erropng = []
errogif = []

convertidasjpge = []
convertidaspng = []
convertidasgif = []


def create_log(log_text):
    with open("conversion_log.txt", "a") as log_file:
        log_file.write('\n' + log_text)


def del_filetext():
    with open("conversion_log.txt", "w") as log_file:
        log_file.write('')


def to_jpeg(path):
    create_log('='*20)
    create_log('\nCONVERSÂO PARA JPGE:\n')
    create_log('='*20)
    global errojpge, list_img, i
    list_files = os.listdir(path)
    list_img = [i for i in list_files if i.split(
        '.')[-1] != 'jpeg' or 'JPEG']

    i = 1
    for img in list_img:

        try:
            input = path + '/' + img
            output = path + '/jpge/' + img.replace(img.split('.')[-1], '.jpeg')
            if os.path.exists(path + '/jpge'):
                im = Image.open(input).convert("RGB")
                im.save(output)
                convertidasjpge.append(img)
            else:
                os.mkdir(path + '/jpge')
                im = Image.open(input).convert("RGB")
                im.save(output)
                convertidasjpge.append(img)
            i += 1

        except:
            errojpge.append(img)
            create_log(f'\n Desculpa, não posso converter o arquivo {img}\n ')
            continue
    if len(errojpge) == 0:
        create_log(
            "\n Todas as imagens foram convertidas com sucesso para Jpeg ;)\n ")

    else:
        create_log('\nARQUIVOS CONVERTIDOS PARA JPEG:\n')
        for n in range(0, (len(convertidasjpge))):
            if len(convertidasjpge) != 0:
                img_convertidas = str(convertidasjpge[n])
                create_log((img_convertidas))
        create_log('\nARQUIVOS NÃO CONVERTIDoS PARA JPEG: \n')
        for j in range(0, len(errojpge)):
            img_erro = str(errojpge[j])
            create_log((img_erro))


def to_png(path):
    create_log('='*20)
    create_log('\nCONVERSÂO PARA PNG:\n')
    create_log('='*20)
    global erropng, list_img, i
    list_files = os.listdir(path)
    list_img = [i for i in list_files if i.split(
        '.')[-1] != 'png' or 'PNG']

    i = 1
    for img in list_img:

        try:
            input = path + '/' + img
            output = path + '/png/' + img.replace(img.split('.')[-1], '.png')
            if os.path.exists(path + '/png'):
                im = Image.open(input).convert("RGB")
                im.save(output)
                convertidaspng.append(img)

            else:
                os.mkdir(path + '/png')
                im = Image.open(input).convert("RGB")
                im.save(output)
                convertidaspng.append(img)

            i += 1

        except:
            erropng.append(img)
            create_log(f'\n Desculpa, não posso converter o arquivo {img}\n ')
            continue
    if len(erropng) == 0:
        create_log(
            "\n Todas as imagens foram convertidas com sucesso para png ;)\n ")

    else:
        create_log('\nARQUIVOS CONVERTIDOS PARA PNG:\n')
        for n in range(0, (len(convertidaspng))):
            if len(convertidaspng) != 0:
                img_convertidas = str(convertidaspng[n])
                create_log((img_convertidas))
        create_log('\nARQUIVOS NÃO CONVERTIDAS PARA PNG: \n')
        for j in range(0, len(erropng)):
            img_erro = str(erropng[j])
            create_log((img_erro))


def to_gif(path):

    create_log('='*20)
    create_log('\nCONVERSÂO PARA GIF:\n')
    create_log('='*20)
    global errogif, list_img, i
    list_files = os.listdir(path)
    list_img = [i for i in list_files if i.split(
        '.')[-1] != 'gif' or 'GIF']

    i = 1
    for img in list_img:

        try:
            input = path + '/' + img
            output = path + '/gif/' + img.replace(img.split('.')[-1], '.gif')
            if os.path.exists(path + '/gif'):
                im = Image.open(input).convert("RGB")
                im.save(output)
                convertidasgif.append(img)

            else:
                os.mkdir(path + '/gif')
                im = Image.open(input).convert("RGB")
                im.save(output)
                convertidasgif.append(img)

            i += 1

        except:
            errogif.append(img)
            create_log(f'\n Desculpa, não posso converter o arquivo {img}\n ')
            continue
    if len(errogif) == 0:
        create_log(
            "\n Todas as imagens foram convertidas com sucesso para gif ;)\n ")

    else:
        create_log('\nARQUIVOS CONVERTIDOS PARA GIF:\n')
        for n in range(0, (len(convertidasgif))):
            if len(convertidasgif) != 0:
                img_convertidas = str(convertidasgif[n])
                create_log((img_convertidas))
        create_log('\nARQUIVOS NÂO CONVERTIDOS PARA GIF: \n')
        for j in range(0, len(errogif)):
            img_erro = str(errogif[j])
            create_log((img_erro))
