# Movies-Recomendation-System

Content based recommendation system recommends similar movies which you searched. When you will be search any movies the details of movie display and this details comes from
imdb website with the process of web-scraping.
<br/><br/>
You can check out the demo: https://movie-recommender-system00.herokuapp.com/

# Screenshots of project

<img src='https://user-images.githubusercontent.com/48127972/96625938-75285b80-132c-11eb-95b0-9195073c1d8d.png' width='700px' height='400px'>

<img src='https://user-images.githubusercontent.com/48127972/96625943-78234c00-132c-11eb-8f8c-2e27760facf7.png' width='700px' height='400px'>

<img src='https://user-images.githubusercontent.com/48127972/96625953-7a85a600-132c-11eb-96e5-5bb52fbdc48d.png' width='700px' height='400px'>

<img src='https://user-images.githubusercontent.com/48127972/96625967-7e192d00-132c-11eb-9323-090f7d7cb245.png' width='700px' height='400px'>

# How to run the project?

1. Clone this repository and install the requirements.txt
2. Open the command prompt and run app.py file
3. After run the python file, copy the url from command promt and paste in browser press enter then the project will be start on browser.

# Cosine Similarity

Cosine similarity is used to measure the similarity between documents. It is the matrix and it measures the cosine of angle between to vectors projected in the multi-dimensional 
space.

<img src='https://user-images.githubusercontent.com/48127972/96173558-ab896380-0f45-11eb-98f5-5f701b758e17.png' >

# Requirements

1. Flask
2. pandas
3. sklearn
4. bs4 (BeautifulSoup4)
5. josn
6. requests

# Dataset source

For this project I have create our own dataset using web-scraping of imdb website. All method have done in my python notebook file given in this repo.
I have scrap top 5000 movies and detailes of movies and make csv file and use.
