from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = "keys coding competetive development Python webscraping automation getsetpython projects cool awesome blockchain data machinelearning  regex loops datascience opencv ML list dictionary analysis sentiment variable set counter enumerate try except if-else for function class object instance GUI encryption security"

our_mask = np.array(Image.open('./resources/twitter_mask.png'))

cloud = WordCloud(
    font_path ="./resources/cabin-sketch.bold.ttf", 
    background_color ="white", 
    height = 1800,
    width = 1400,
    mask = our_mask
    ).generate(text)

plt.imshow(cloud)
plt.axis("off")
plt.savefig('./output/wordcloud2.png', dpi=300)
plt.show()