from xml.etree import ElementTree as ET


def panbie(polarity):
    if polarity == 'positive':
        polarity= '1'
    else:
        if polarity == 'negative':
            polarity = '-1'
        else:
            if polarity == 'neutral':
                polarity = '0'
    return polarity

def chuli_category(category):
    for i in category:
        if i=='/':
            flag = 1
            break
        else:
            flag = 0
    return flag

f = open('G:\\shijiewenjian\\Restaurants_Train_v2.txt','w')
node = ET.parse('Restaurants_Train_v2.xml')
root =node.findall('./sentence') 
for wenben in root: 
    text_ = wenben.find('text').text 
    
    firstchild = wenben.find('aspectTerms')
    if firstchild  is not None:
        for termn in firstchild.findall('aspectTerm'):
            term = termn.get('term')
            polarity = termn.get('polarity')
            polarity = panbie(polarity)
        f.write(text_+'\n')
        f.write('term =  '+term+'\n') 
        f.write(polarity+'\n')
for wenben in root:
    text_ = wenben.find('text').text
    secondchild = wenben.find('aspectCategories')
    if secondchild is not None:
        for categoryn in secondchild.findall('aspectCategory'):
            category = categoryn.get('category')
            polarity = categoryn.get('polarity')
            polarity = panbie(polarity)
            flag = chuli_category(category)
            if flag == 1:
                category1 = 'anecdotes'
                catagory2 = 'miscellaneous'
                f.write(text_+'\n')
                f.write('catagory =  '+category1+'\n')
                f.write(polarity+'\n')
                f.write(text_+'\n')
                f.write('catagory =  '+catagory2+'\n')
                f.write(polarity+'\n')
            if flag == 0:
                f.write(text_+'\n')
                f.write('catagory =  '+category+'\n') 
                f.write(polarity+'\n')
f.close()
#第二篇文档处理

f2 = open('G:\\shijiewenjian\\Laptop_Train_v2.txt','w',encoding='utf-8')
node = ET.parse('Laptop_Train_v2.xml')
root =node.findall('./sentence') 
for wenben in root: 
    text_ = wenben.find('text').text 
    firstchild = wenben.find('aspectTerms')
    if firstchild  is not None:
        for termn in firstchild.findall('aspectTerm'):
            term = termn.get('term')
            polarity = termn.get('polarity')
            polarity = panbie(polarity)
        f2.write(text_+'\n')
        f2.write('term =  '+term+'\n') 
        f2.write(polarity+'\n')
f2.close()