# Rassam Yazdi
# 1006019425
# Section 0102
# ESC180 Lab 4

import utilities

def parse_story(file_name):
    #code ordered list of words and valid punctuations
    myfile = open(file_name, "r")
    content = myfile.read().lower()
    
    content.replace("\n",' ')
 
    for d in utilities.BAD_CHARS:
        content = content.replace(d," ")
                                  
    for v in utilities.VALID_PUNCTUATION:
        content = content.replace(v, " "+v+" ")
    
    return content.split()
    
 
def get_prob_from_count(counts):
    sum = 0
    for i in range(len(counts)):
        sum += counts[i]
    
    probs = counts
    
    for i in range(len(counts)):
        probs[i] = counts[i]/sum 
    
    return probs



def build_ngram_counts(words, n):
    dic = {}
    for i in range(len(words)-(n)):
        key  = []
        for j in range(i, i+n):
            key.append(words[j])
        if tuple(key) in dic.keys():
            newvalue = words[i+n]
            if newvalue in dic[tuple(key)][0]:
                dic[tuple(key)][1][dic[tuple(key)][0].index(newvalue)] = dic[tuple(key)][1][dic[tuple(key)][0].index(newvalue)]+1
                dic[tuple(key)] = [dic[tuple(key)][0],dic[tuple(key)][1]]
    
            else:
                value_list =  list(dic[tuple(key)][0])
                value_list.append(newvalue)
                count_list  = list(dic[tuple(key)][1])
                count_list.append(1)
                d1  = {tuple(key): (value_list,count_list)}
                dic.update(d1)
        else:
            dic[tuple(key)] = [[words[i+n]],[1]]
    return dic
    

    
def prune_ngram_counts(counts, prune_len):
    ngram_counts = {}
    for key in counts:
        if len(counts[key][0])> prune_len:
            zippo = zip(counts[key][1], counts[key][0])
            sortedzippo = list(sorted(zippo, reverse = True))
            
            cutline = prune_len
            
            for j in range(prune_len-1, len(counts)):
                if sortedzippo[j][0] == sortedzippo[cutline][0]:
                    cutline+=1
            
            sortedzippo = sortedzippo[0:cutline]
            
            updatedvalue = [[],[]]
            
            for k in range(0,len(sortedzippo)):
                updatedvalue[1].append(sortedzippo[k][0])
                updatedvalue[0].append(sortedzippo[k][1])
            
            ngram_counts.update({key:updatedvalue})
        else:
            ngram_counts.update({key:counts[key]})            
                           
    return ngram_counts       
                
def probify_ngram_counts(counts):
    for key in counts:
        prob = get_prob_from_count(counts[key][1])
        updatedvalue = [[],[]]
        updatedvalue[1].extend(prob)
        updatedvalue[0].extend(counts[key][0])
        counts.update({key:updatedvalue})
        
    return counts
    
   
def build_ngram_model(words, n): 
    output = probify_ngram_counts(prune_ngram_counts(build_ngram_counts(words, n), 15))
    return output
    
def gen_bot_list(ngram_model, seed, num_tokens=0):
    bot_list = []
    bot_list.extend(list(seed))
    strings = list(seed)
    counter = 0
    
    while 1:
        if tuple(strings) in ngram_model.keys():
            bot_list.append(utilities.gen_next_token(tuple(strings),ngram_model))
            counter+=1
            strings = []
            for i in range(counter,len(bot_list)):
                strings.append(bot_list[i])
        else:
            break
    
    if len(bot_list) > num_tokens:
        bot_list = bot_list[0:num_tokens]
        
    return bot_list
    
def gen_bot_text(token_list, bad_author):
    if bad_author == False:
        string = ""
        capslock = True
        
        for i in range(0,len(token_list)):
            if (token_list[i][0].upper()+token_list[i][1:].lower()) in utilities.ALWAYS_CAPITALIZE:
                capslock = True
                
            if capslock == True:
                token_list[i] = token_list[i][0].upper() + token_list[i][1:].lower()
                capslock = False
            
            if i == 0 or token_list[i] in utilities.END_OF_SENTENCE_PUNCTUATION or token_list[i] in utilities.VALID_PUNCTUATION:
                token_list[i] = token_list[i][0].upper() + token_list[i][1:].lower()
                string += token_list[i]
            else:
                string += (' '+ token_list[i])
                
            if token_list[i] in utilities.END_OF_SENTENCE_PUNCTUATION:
                capslock = True             
                
    else:
        string = ""
        for i in range(0,len(token_list)):
            if i == len(token_list)-1:
                string += token_list[i]
            else:
                string += (token_list[i] + " ")        
            
    return string
      


def write_story(file_name, text, title, student_name, author, year):
    file = open(file_name, 'w')
    file.write("\n"*10)
    file.write(title+ ": "+str(year)+ ", UNLEASHED\n")
    file.write(student_name+ ", inspired by "+ author+"\n")
    file.write("Copyright year published ("+str(year)+"), publisher: EngSci press\n")
    file.write("\n"*17)
    content = text.split()
    linestring1 = ""
    pagestring = ''
    i = 0
    pagenumber = 1
    chapternumber = 1
    bookstring = ''
    while i < len(content) :
        k = 0
        while k in range(12) and i <len(content):
            chapterstring = ''
            pagestring = ""
            if k == 0:
                print(k)
                pagestring += "CHAPTER " +str(chapternumber)+"\n\n"
                for j in range(26):
                    linestring1 = ""
                    while i<len(content):
                        if len(linestring1+" "+content[i]) > 90:
                            break
                        else:
                            if len(linestring1) == 0:
                                linestring1 += content[i]
                            else:
                                linestring1 += " "+content[i]
                            i +=1
                    linestring1 += "\n"
                    pagestring += linestring1
                chapterstring+=pagestring
                if len(linestring1.split()) != 0:
                    chapterstring += '\n' +str(pagenumber)+"\n"
                else:
                    chapterstring += '\n' +str(pagenumber)
                pagenumber += 1              
            else:
                for j in range(28):
                    linestring1 = ""
                    while i<len(content):
                        if len(linestring1+" "+content[i]) > 90:
                            break
                        else:
                            if len(linestring1) == 0:
                                linestring1 += content[i]
                            else:
                                linestring1 += " "+content[i]
                            i +=1
                    linestring1 += "\n"
                    pagestring += linestring1
                chapterstring += pagestring
                if len(linestring1) != 0:
                    chapterstring +=  '\n' + str(pagenumber)+"\n"
                else:
                    chapterstring += '\n' + str(pagenumber)
                pagenumber += 1
            k+=1
            bookstring += chapterstring
        chapternumber += 1
    file.write(bookstring)      
    file.close()





if (__name__ == "__main__"):
    #print(parse_story("test_text_parsing.txt"))
    
    build_ngram_model(['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may','go', 'home', '.'],2)
        
    lame = ['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may','go', 'home', '.']
    
    #print(build_ngram_counts(['the', 'child', 'will', 'go', 'out', 'to', 'play', ',', 'and', 'the', 'child', 'can', 'not', 'be', 'sad', 'anymore', '.'],2))
    #print(build_ngram_counts(['the', 'child','will','the', 'child','will','the', 'child','can','the', 'child','can'],2))
    
    ngram_counts= {('i', 'love'): [['js', 'py3', 'c'], [20, 20, 10]],('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],('toronto', 'is'): [['six', 'drake'], [2, 3]]}
    
    #print(probify_ngram_counts(ngram_counts))
    
    
    
    model = {('the', 'child'): [['will', 'can', 'may'], [0.5, 0.25, 0.25]], ('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]], ('can', 'the'): [['child'], [1.0]], ('child', 'may'): [['go'], [1.0]], ('may', 'go'): [['home'], [1.0]], ('go', 'home'): [['.'], [1.0]]}

    
    #print(gen_bot_list(model,('hello','world'),5))
    
    token_list = ['this', 'j', 'string', 'of', 'george', '.', 'which', 'needs', 'to', 'be', 'created', '.']
    #print(gen_bot_text(token_list, False))
                 
    #write_story("112.txt", "text text hduvfbwilevbl dhwbkvleiqow bhvdhjvdbbfkbhs dvhebhqelclibc  bhekvlqibccbilc dhvdbqlq fhvhdsks f ds d d kb", "title", "Rassam", "Fitzgerald", 2019)
    #write_story("113.txt", parse_story("308.txt"),"title", "Rassam", "Fitzgerald", 2019)
    token_list = parse_story("308.txt")
    text = gen_bot_text(token_list, False)
    file = open('308.txt', 'r')
    #text  = ' '.join(parse_story(file.name))
    write_story('testicles.txt', text, 'Three Men in a Boat', 'Jerome K. Jerome', 'Jerome K. Jerome', 1889)    