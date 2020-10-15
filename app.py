from flask import Flask, render_template, request, url_for, Response, jsonify
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# read movies data
data = pd.read_csv('imdb_movies_data.csv')

app = Flask(__name__)

# this is for search box suggestion and autocomplete
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    name = list(data['movies_name'].str.capitalize())
    return Response(json.dumps(name), mimetype='application/json')


l_id = []    # list_movies_id
l_i = []     # list_image
l_m_n = []   # list_movie_name
l_m_y = []   # list_movie_year
l_m_d = []   # list_movie_duration
l_m_g = []   # list_movie_genre
l_m_r = []   # list_movie_rating

# top 50 movies details from data...
sub_data = data.iloc[0:50,:]

for i in range(50):
    l_id.append(sub_data['movies_id'][i])
    l_i.append(sub_data['Image_url'][i])
    l_m_n.append(sub_data['movies_name'][i])
    l_m_y.append(sub_data['released_year'][i])
    l_m_d.append(sub_data['duration'][i])
    l_m_g.append(sub_data['genres'][i])
    l_m_r.append(sub_data['rating'][i])

def create_similarity():
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['genres'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return similarity


def recomendation(movie_name):
    # find similar movies of searched movie
    similarity = create_similarity()
    if movie_name not in list(data['movies_name']):
        return('Sorry! The movie you requested is not in our database.')
    else:
        i = data.loc[data['movies_name']==movie_name].index[0] 
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:13] # excluding first item since it is the requested movie itself
        l = []    # movies name
        # tid = []  # ids of movies
        y = []    # movie's released year
        d = []    # movie's runtime duration
        r = []    # movie's rating
        url = []  # movie's poster image url
        g = []    # movie's genrea
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movies_name'][a])
            # tid.append(data['movies_id'][a])
            y.append(data['released_year'][a])
            d.append(data['duration'][a])
            r.append(data['rating'][a])
            url.append(data['Image_url'][a])
            g.append(data['genres'][a]) 

        return l, y, d, r, url, g


@app.route('/')
def home():
    # render the details of top 50 movies to index.html file
    return render_template('index.html', i1 = l_i[0], i2 = l_i[1], i3 = l_i[2], i4 = l_i[3],
                                        n1 = l_m_n[0], n2 = l_m_n[1], n3 = l_m_n[2], n4 = l_m_n[3],
                                        y1 = l_m_y[0], y2 = l_m_y[1], y3 = l_m_y[2], y4 = l_m_y[3],
                                        d1 = l_m_d[0], d2 = l_m_d[1], d3 = l_m_d[2], d4 = l_m_d[3],
                                        g1 = l_m_g[0], g2 = l_m_g[1], g3 = l_m_g[2], g4 = l_m_g[3],
                                        r1 = l_m_r[0], r2 = l_m_r[1], r3 = l_m_r[2], r4 = l_m_r[3],
                                        i5 = l_i[4], i6 = l_i[5], i7 = l_i[6], i8 = l_i[7],
                                        n5 = l_m_n[4], n6 = l_m_n[5], n7 = l_m_n[6], n8 = l_m_n[7],
                                        y5 = l_m_y[4], y6 = l_m_y[5], y7 = l_m_y[6], y8 = l_m_y[7],
                                        d5 = l_m_d[4], d6 = l_m_d[5], d7 = l_m_d[6], d8 = l_m_d[7],
                                        g5 = l_m_g[4], g6 = l_m_g[5], g7 = l_m_g[6], g8 = l_m_g[7],
                                        r5 = l_m_r[4], r6 = l_m_r[5], r7 = l_m_r[6], r8 = l_m_r[7],
                                        i9 = l_i[8], i10 = l_i[9], i11 = l_i[10], i12 = l_i[11],
                                        n9 = l_m_n[8], n10 = l_m_n[9], n11 = l_m_n[10], n12 = l_m_n[11],
                                        y9 = l_m_y[8], y10 = l_m_y[9], y11 = l_m_y[10], y12 = l_m_y[11],
                                        d9 = l_m_d[8], d10 = l_m_d[9], d11 = l_m_d[10], d12 = l_m_d[11],
                                        g9 = l_m_g[8], g10 = l_m_g[9], g11 = l_m_g[10], g12 = l_m_g[11],
                                        r9 = l_m_r[8], r10 = l_m_r[9], r11 = l_m_r[10], r12 = l_m_r[11],
                                        i13 = l_i[12], i14 = l_i[13], i15 = l_i[14], i16 = l_i[15],
                                        n13 = l_m_n[12], n14 = l_m_n[13], n15 = l_m_n[14], n16 = l_m_n[15],
                                        y13 = l_m_y[12], y14 = l_m_y[13], y15 = l_m_y[14], y16 = l_m_y[15],
                                        d13 = l_m_d[12], d14 = l_m_d[13], d15 = l_m_d[14], d16 = l_m_d[15],
                                        g13 = l_m_g[12], g14 = l_m_g[13], g15 = l_m_g[14], g16 = l_m_g[15],
                                        r13 = l_m_r[12], r14 = l_m_r[13], r15 = l_m_r[14], r16 = l_m_r[15],
                                        i17 = l_i[16], i18 = l_i[17], i19 = l_i[18], i20 = l_i[19],
                                        n17 = l_m_n[16], n18 = l_m_n[17], n19 = l_m_n[18], n20 = l_m_n[19],
                                        y17 = l_m_y[16], y18 = l_m_y[17], y19 = l_m_y[18], y20 = l_m_y[19],
                                        d17 = l_m_d[16], d18 = l_m_d[17], d19 = l_m_d[18], d20 = l_m_d[19],
                                        g17 = l_m_g[16], g18 = l_m_g[17], g19 = l_m_g[18], g20 = l_m_g[19],
                                        r17 = l_m_r[16], r18 = l_m_r[17], r19 = l_m_r[18], r20 = l_m_r[19],
                                        i21 = l_i[20], i22 = l_i[21], i23 = l_i[22], i24 = l_i[23],
                                        n21 = l_m_n[20], n22 = l_m_n[21], n23 = l_m_n[22], n24 = l_m_n[23],
                                        y21 = l_m_y[20], y22 = l_m_y[21], y23 = l_m_y[22], y24 = l_m_y[23],
                                        d21 = l_m_d[20], d22 = l_m_d[21], d23 = l_m_d[22], d24 = l_m_d[23],
                                        g21 = l_m_g[20], g22 = l_m_g[21], g23 = l_m_g[22], g24 = l_m_g[23],
                                        r21 = l_m_r[20], r22 = l_m_r[21], r23 = l_m_r[22], r24 = l_m_r[23],
                                        i25 = l_i[24], i26 = l_i[25], i27 = l_i[26], i28 = l_i[27],
                                        n25 = l_m_n[24], n26 = l_m_n[25], n27 = l_m_n[26], n28 = l_m_n[27],
                                        y25 = l_m_y[24], y26 = l_m_y[25], y27 = l_m_y[26], y28 = l_m_y[27],
                                        d25 = l_m_d[24], d26 = l_m_d[25], d27 = l_m_d[26], d28 = l_m_d[27],
                                        g25 = l_m_g[24], g26 = l_m_g[25], g27 = l_m_g[26], g28 = l_m_g[27],
                                        r25 = l_m_r[24], r26 = l_m_r[25], r27 = l_m_r[26], r28 = l_m_r[27],
                                        i29 = l_i[28], i30 = l_i[29], i31 = l_i[30], i32 = l_i[31],
                                        n29 = l_m_n[28], n30 = l_m_n[29], n31 = l_m_n[30], n32 = l_m_n[31],
                                        y29 = l_m_y[28], y30 = l_m_y[29], y31 = l_m_y[30], y32 = l_m_y[31],
                                        d29 = l_m_d[28], d30 = l_m_d[29], d31 = l_m_d[30], d32 = l_m_d[31],
                                        g29 = l_m_g[28], g30 = l_m_g[29], g31 = l_m_g[30], g32 = l_m_g[31],
                                        r29 = l_m_r[28], r30 = l_m_r[29], r31 = l_m_r[30], r32 = l_m_r[31],
                                        i33 = l_i[32], i34 = l_i[33], i35 = l_i[34], i36 = l_i[35],
                                        n33 = l_m_n[32], n34 = l_m_n[33], n35 = l_m_n[34], n36 = l_m_n[35],
                                        y33 = l_m_y[32], y34 = l_m_y[33], y35 = l_m_y[34], y36 = l_m_y[35],
                                        d33 = l_m_d[32], d34 = l_m_d[33], d35 = l_m_d[34], d36 = l_m_d[35],
                                        g33 = l_m_g[32], g34 = l_m_g[33], g35 = l_m_g[34], g36 = l_m_g[35],
                                        r33 = l_m_r[32], r34 = l_m_r[33], r35 = l_m_r[34], r36 = l_m_r[35],
                                        i37 = l_i[36], i38 = l_i[37], i39 = l_i[38], i40 = l_i[39],
                                        n37 = l_m_n[36], n38 = l_m_n[37], n39 = l_m_n[38], n40 = l_m_n[39],
                                        y37 = l_m_y[36], y38 = l_m_y[37], y39 = l_m_y[38], y40 = l_m_y[39],
                                        d37 = l_m_d[36], d38 = l_m_d[37], d39 = l_m_d[38], d40 = l_m_d[39],
                                        g37 = l_m_g[36], g38 = l_m_g[37], g39 = l_m_g[38], g40 = l_m_g[39],
                                        r37 = l_m_r[36], r38 = l_m_r[37], r39 = l_m_r[38], r40 = l_m_r[39],
                                        i41 = l_i[40], i42 = l_i[41], i43 = l_i[42], i44 = l_i[43],
                                        n41 = l_m_n[40], n42 = l_m_n[41], n43 = l_m_n[42], n44 = l_m_n[43],
                                        y41 = l_m_y[40], y42 = l_m_y[41], y43 = l_m_y[42], y44 = l_m_y[43],
                                        d41 = l_m_d[40], d42 = l_m_d[41], d43 = l_m_d[42], d44 = l_m_d[43],
                                        g41 = l_m_g[40], g42 = l_m_g[41], g43 = l_m_g[42], g44 = l_m_g[43],
                                        r41 = l_m_r[40], r42 = l_m_r[41], r43 = l_m_r[42], r44 = l_m_r[43],
                                        i45 = l_i[44], i46 = l_i[45], i47 = l_i[46], i48 = l_i[47],
                                        n45 = l_m_n[44], n46 = l_m_n[45], n47 = l_m_n[46], n48 = l_m_n[47],
                                        y45 = l_m_y[44], y46 = l_m_y[45], y47 = l_m_y[46], y48 = l_m_y[47],
                                        d45 = l_m_d[44], d46 = l_m_d[45], d47 = l_m_d[46], d48 = l_m_d[47],
                                        g45 = l_m_g[44], g46 = l_m_g[45], g47 = l_m_g[46], g48 = l_m_g[47],
                                        r45 = l_m_r[44], r46 = l_m_r[45], r47 = l_m_r[46], r48 = l_m_r[47],
                                        i49 = l_i[48], i50 = l_i[49],
                                        n49 = l_m_n[48], n50 = l_m_n[49],
                                        y49 = l_m_y[48], y50 = l_m_y[49],
                                        d49 = l_m_d[48], d50 = l_m_d[49],
                                        g49 = l_m_g[48], g50 = l_m_g[49],
                                        r49 = l_m_r[48], r50 = l_m_r[49]
                                        
                                        )



@app.route('/search', methods=['GET', 'POST'])
def search_movies():
    if request.method == 'POST':
        d = request.form['autocomplete']
    else:
        d = request.args.get('m_name')
        print(d)

    movie_name, movie_year, movie_duration, movie_rating, movie_img_url, movie_genre = recomendation(d)

    indx = data.index[data['movies_name'] == d]

    m_id = list(data['movies_id'][indx])       # movie's id from data
    m_year = list(data['released_year'][indx]) # movie's released year
    m_rating = list(data['rating'][indx])      # movie's rating
    m_duration = list(data['duration'][indx])  # movie's runtime duration
    m_genre = list(data['genres'][indx])       # movie's genres

    # search movie for getting more details
    m_url = 'https://www.imdb.com/title/'+m_id[0]

    # #     if t_id == title_id[0]:

    cast_image = []   # cast image of searched movie
    cast_name = []    # cast name

    res = requests.get(m_url)
    result = res.text
    msoop = BeautifulSoup(result, 'html.parser')

    # poster image of searched movie
    img_div = msoop.find_all('div', {'class':'poster'})
    main_img = img_div[0].select('img')

    # story about movie
    story_line_div = msoop.find_all('div', {'class':'inline canwrap'})
    story_line = story_line_div[0].select('span')

    # scraping screen shots of searched movie
    screen_shot = msoop.find_all('div', {'class':'mediastrip'})
    ss_img = screen_shot[0].select('img')

    # find director name of searched movie
    credit_cast_summary = msoop.find_all('div', {'class':'credit_summary_item'})
    credit_cast = credit_cast_summary[0].select('a')

    # scraping cast details
    cast_img_tr = msoop.find_all('td', {'class':'primary_photo'})

    for c in cast_img_tr:
        cast_img = c.select('img')
        try:
            cast_image.append(cast_img[0].attrs['loadlate'])
        except:
            cast_image.append(cast_img[0].attrs['src'])
        cast_name.append(cast_img[0].attrs['alt'])


    # render all details to html file
    return render_template('recomendation.html', img = main_img[0].attrs['src'], story = story_line[0].text, movie_name = d,
                                                movie_year = m_year[0], m_rating = m_rating[0], m_dur = m_duration[0], m_gen = m_genre[0],

                                                m_director = credit_cast[0].text,

                                                ss1 = ss_img[0].attrs['loadlate'], ss2 = ss_img[1].attrs['loadlate'], ss3 = ss_img[2].attrs['loadlate'],
                                                ss4 = ss_img[3].attrs['loadlate'], ss5 = ss_img[4].attrs['loadlate'], ss6 = ss_img[5].attrs['loadlate'],

                                                c_img1 = cast_image[0], c_img2 = cast_image[1], c_img3 = cast_image[2], c_img4 = cast_image[3],
                                                c_img5 = cast_image[4], c_img6 = cast_image[5], c_img7 = cast_image[6], c_img8 = cast_image[7],
                                                c_img9 = cast_image[8], c_img10 = cast_image[9], c_img11 = cast_image[10], c_img12 = cast_image[11],
                                                
                                                c_name1 = cast_name[0], c_name2 = cast_name[1], c_name3 = cast_name[2], c_name4 = cast_name[3],
                                                c_name5 = cast_name[4], c_name6 = cast_name[5], c_name7 = cast_name[6], c_name8 = cast_name[7],
                                                c_name9 = cast_name[8], c_name10 = cast_name[9], c_name11 = cast_name[10], c_name12 = cast_name[11],

                                                i1 = movie_img_url[0], i2 = movie_img_url[1],
                                                i3 = movie_img_url[2], i4 = movie_img_url[3], i5 = movie_img_url[4],
                                                i6 = movie_img_url[5], i7 = movie_img_url[6], i8 = movie_img_url[7],
                                                i9 = movie_img_url[8], i10 = movie_img_url[9], i11 = movie_img_url[10],
                                                i12 = movie_img_url[11],

                                                n1 = movie_name[0], n2 = movie_name[1], n3 = movie_name[2], n4 = movie_name[3],
                                                n5 = movie_name[4], n6 = movie_name[5], n7 = movie_name[6], n8 = movie_name[7],
                                                n9 = movie_name[8], n10 = movie_name[9], n11 = movie_name[10], n12 = movie_name[11],

                                                y1 = movie_year[0], y2 = movie_year[1], y3 = movie_year[2], y4 = movie_year[3],
                                                y5 = movie_year[4], y6 = movie_year[5], y7 = movie_year[6], y8 = movie_year[7],
                                                y9 = movie_year[8], y10 = movie_year[9], y11 = movie_year[10], y12 = movie_year[11],

                                                d1 = movie_duration[0], d2 = movie_duration[1], d3 = movie_duration[2], d4 = movie_duration[3],
                                                d5 = movie_duration[4], d6 = movie_duration[5], d7 = movie_duration[6], d8 = movie_duration[7],
                                                d9 = movie_duration[8], d10 = movie_duration[9], d11 = movie_duration[10], d12 = movie_duration[11],

                                                r1 = movie_rating[0], r2 = movie_rating[1], r3 = movie_rating[2], r4 = movie_rating[3],
                                                r5 = movie_rating[4], r6 = movie_rating[5], r7 = movie_rating[6], r8 = movie_rating[7],
                                                r9 = movie_rating[8], r10 = movie_rating[9], r11 = movie_rating[10], r12 = movie_rating[11],

                                                g1 = movie_genre[0], g2 = movie_genre[1], g3 = movie_genre[2], g4 = movie_genre[3],
                                                g5 = movie_genre[4], g6 = movie_genre[5], g7 = movie_genre[6], g8 = movie_genre[7],
                                                g9 = movie_genre[8], g10 = movie_genre[9], g11 = movie_genre[10], g12 = movie_genre[11]
                                                
                                                )
    
    
    # return render_template('recomendation.html')

if __name__ == '__main__':
    app.run(debug=True)