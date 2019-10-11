from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "keys coding competetive development Python webscraping automation getsetpython projects cool awesome blockchain data machinelearning  regex loops datascience opencv ML list dictionary analysis sentiment variable set counter enumerate try except if-else for function class object instance GUI encryption security"
cloud = WordCloud(background_color = "yellow").generate(text)

plt.imshow(cloud)
plt.axis("off")
plt.savefig("./output/wordcloud1.png", dpi=600)
plt.show()