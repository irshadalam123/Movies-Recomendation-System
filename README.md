# Movies-Recomendation-System

Content based recommendation system recommends similar movies which you searched. When you will be search any movies the details of movie display and this details comes from
imdb website with the process of web-scraping.
<br/><br/>
You can check out the demo: https://movie-recommender-system00.herokuapp.com/

# Screenshots of project

<img src='https://user-images.githubusercontent.com/48127972/96168839-f9e73400-0f3e-11eb-90b6-f4c36b0e503c.png' width='700px' height='400px'>

<img src='https://user-images.githubusercontent.com/48127972/96168899-0c616d80-0f3f-11eb-91cf-42f6949f51cd.png' width='700px' height='400px'>

<img src='https://user-images.githubusercontent.com/48127972/96169238-767a1280-0f3f-11eb-8e7c-ed7b75d4e97b.png' width='700px' height='400px'>

<img src='https://user-images.githubusercontent.com/48127972/96169249-7b3ec680-0f3f-11eb-84c0-1d0618c67b8f.png' width='700px' height='400px'>

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
