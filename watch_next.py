import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')

movie_file = open('movies.txt', 'r')
movie_list = []
movie_title_list = []
similarity_list = []

#for each line of movies, split out the title and then save both the title and the description in a list
for line in movie_file:
    line = line.strip('\n')
    line_list = line.split(' :')
    movie_title_list.append(line_list[0])
    movie_list.append(line_list[1])



#find the similarity of all sentences with the movie description of Hulk
Planet_Hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
for sentence in movie_list:
    similarity_list.append(nlp(sentence).similarity(nlp(Planet_Hulk)))


#find the highest similarity in the list by comparing similarity index
similarity_rating = 0
count = 0
index_val = 0

for num in similarity_list:
    if num > similarity_rating:
        similarity_rating = num
        index_val = count
    count += 1

#print the recommendation for the user
print('-------------------------------------------')
print(f'It is recommended you watch {movie_title_list[index_val]}')
