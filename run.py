import numpy as np
import matplotlib.image as mpimg

#figura 4.24

#lendo a imagem
imagem = mpimg.imread('pegada.png')

#figura 4.19
#processing
x = np.hstack((imagem,imagem,imagem,imagem))
#saving image
mpimg.imsave('figura1.png',x)

#figura 4.20
#processing
x = imagem.shape
#setting the image height
height = x[0]
#setting the image width
width = x[1]
#setting the image rbga
rgba = x[2]
#processing
imagem_branca = np.zeros([height,width,rgba], dtype = np.uint8)
imagem_branca[:,:height] = [0.1,0.1,0.1,0.1]
imagem_branca[:,height] = [0.1,0.1,0.1,0.1]
juncao = np.vstack((imagem,imagem_branca))
imagem_rotacionada = np.rot90(juncao,2)
imagem_refletida = np.fliplr(imagem_rotacionada)
x = np.hstack((juncao,imagem_refletida,juncao,imagem_refletida,))
#saving image
mpimg.imsave('figura2.png', x)

#figura 4.21
#processing
reflexao = np.fliplr(imagem)
x = np.hstack((reflexao,imagem,reflexao,imagem))
#saving image
mpimg.imsave('figura3.png',x)

#figura 4.22
#processing
reflexao = np.flipud(imagem)
x = np.vstack((imagem,reflexao))
x = np.hstack((x,x,x,x))
#saving image
mpimg.imsave('figura4.png',x)

#figura 4.23
#processing
x = imagem.shape
#setting the image height
height = x[0]
#setting the image width
width = x[1]
#setting the image rbga
rgba = x[2]
#processing
imagem_branca = np.zeros([height,width,rgba], dtype = np.uint8)
imagem_branca[:,:height] = [0.1,0.1,0.1,0.1]
imagem_branca[:,height] = [0.1,0.1,0.1,0.1]
x = np.vstack((imagem,imagem_branca))
y = np.rot90(x,2)
x = np.hstack((x,y,x,y))
mpimg.imsave('figura5.png',x)

#figura 4.24
reflexao = np.fliplr(imagem)
z = np.hstack((reflexao,imagem))
x = z.shape
#setting the image height
height = x[0]
#setting the image width
width = x[1]
#setting the image rbga
rgba = x[2]
imagem_branca = np.zeros([height,width,rgba], dtype = np.uint8)
imagem_branca[:,:height] = [0.1,0.1,0.1,0.1]
imagem_branca[:,height] = [0.1,0.1,0.1,0.1]
x = np.vstack((z,imagem_branca))
y = np.rot90(x,2)
r = np.hstack((x,y,x,y))
#saving image
mpimg.imsave('figura6.png',r)

#figura 4.25
#processing
reflexao = np.flipud(imagem)
x = np.vstack((imagem,reflexao))
y = np.fliplr(x)
saida = np.hstack((y,x,y,x))
#saving image
mpimg.imsave('figura7.png',saida)
