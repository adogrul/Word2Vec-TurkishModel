from wiki_dump_reader import Cleaner, iterate
import time 

def clean(sentence):
    table = str.maketrans("ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZWXQ","abcçdefgğhiıjklmnoöprsştuüvyzwxq")
    if "==" not in sentence and  "|" not in sentence and "!" in sentence and "ISBN" not in sentence and  ". Bölüm" not in sentence and "≈" not in sentence and "=" not in sentence and "http" not in sentence:
        sentence_ = sentence.strip().split()
        if sentence_[0] != "InDesign" and sentence_[0] != "Dosya" and sentence_[0] != "Image" and sentence_[0] != "YÖNLENDİRME" and sentence_[0] != "bar:" and sentence_[0] != "TextData=" and      sentence_[0] != "fontsize:" and sentence_[0] != "id" and sentence_[0] != "ImageSize" and sentence_[0] != "PlotArea" and sentence_[0] != "DateFormat" and sentence_[0] != "Period"            and sentence_[0] != "TimeAxis" and sentence_[0] != "AlignBars" and sentence_[0] != "ScaleMajor" and sentence_[0] != "ScaleMinor" and sentence_[0] != "BackgroundColors" and sentence_[0] != "BarData" and sentence_[0] != "REDIRECT" and sentence_[0] != "@":
            if len(sentence.split()) > 4:
                sentence = sentence.replace("\n"," ").replace("\t"," ").replace("Hicrî","Hicrî ").replace("Rumi","Rumi ")
                sentence = sentence.translate(table)
                return sentence
            
cleaner = Cleaner()

w = open("cleanWikiText_.txt","w",encoding="utf8")

start = time.time()
for title, text in iterate('trwiki-20230901-pages-articles-multistream.xml'):
    text = cleaner.clean_text(text)

    text, links = cleaner.build_links(text)

    cleaned_text = clean(text)
    try:
        w.writelines(text+"\n")
    except: pass
print(time.time()- start)  

w.close()