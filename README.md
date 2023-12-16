### **Portfolio**

I had several projects that I wanted to show but I didn't like the idea of using one existent website because all the alternatives that I was trying didn't have some of the features I thought were a must in my portfolio or were not flexible to customize it or were not beautiful (or what I consider beautiful for a portfolio).

Using one of those platforms would be the best option since I have a full-time job and two little girls born during the pandemic years, but I decided to go for it through the complicated path (sometimes hell path) and create my portfolio from scratch.

I know that one portfolio is not a good example for a data analytics project, actually is not related to data analytics, but this project was a great opportunity to show my determination, creative problem solving, adaptability and to learn a lot along the time I would dedicate to this project.

The features I wanted in my portfolio include:

1. Multi-language
2. Responsive website
3. Light/Dark mode
4. Customizable
5. Containerized
6. Elasticsearch

The first four were mandatory, the other two I wanted to learn and practice.

So let's explain the path from the beginning.

#### **The path**

Since I am not a UX/Designer or web developer, and my knowledge of HTML, CSS, and JavaScript was limited, the challenge started being super hard for me. 

##### **The website**

When I started to investigate my options to create one website, the beginning was very discouraging. Only when I discovered [**Hugo**](https://gohugo.io/) I started to see the light at the end of the tunnel. Hugo is a framework for building websites with a lot of beautiful templates for websites and a great community. So I was researching Hugo and his templates for quite a while until I found some templates that could fit my requirements. The problem was that Hugo is fantastic for building static websites which is the opposite of my idea of one portfolio.

So in the end when I chose the [**iWriter**](https://github.com/statichunt/iwriter-hugo) template arrived at the moment to adapt it to a dynamic website.

##### **Flask**

One technology that I wanted to explore and improve my skills in was [**Python**](https://www.python.org/) because has tons of libraries, frameworks, and an impressive community behind it. So, when I thought about dynamic websites, [**Flask**](https://flask.palletsprojects.com/en/3.0.x/) came quickly to my mind. Since I worked with it in my [*Lyrics*](https://github.com/oiroqueiro/mid-bootcamp-project) project, I knew about his capabilities but the hard work had just started.

I had to adapt the iWriter template to be a dynamic template with [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/) without losing any functionality I liked about this template.

After spending many, many, many hours understanding the HTML, CSS, javascript, and Bootstrap (and other technologies) that my template was used to have such features and more hours cleaning the code and adapting, I had some templates quite cleaned and ready to use with the logic of my website.

At this point I want to share with all of you [**this fantastic tutorial of Flask**](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), by *Miguel Grinberg*. I also use this one, in Spanish, of [**j2logo**](https://j2logo.com/tutorial-flask-espanol/) by *Juan José Lozano Gómez*. I learned a lot with them and with all the features that I had to face.

##### **Customizable**

I wanted a customizable website so after evaluating different options, I decided to use one Excel file to store all the texts of my website in addition to the content of my portfolio. The menus texts, buttons, images, ... can be adapted easily.

At the beginning I thought to manage the creation of the content within the website, but soon I realized that I didn't have time if I wanted to finish the project this year. Nevertheless, I did investigate and in the end, I could create one part that makes me feel a little proud of, it is that I could make the URLs to the login and logout pages of my website customizable via environment variables. The option of editing the content would be a future feature.

And how could I make the content of my portfolio customizable? Firstly I thought about the use of HTML, then the use of [**Markdown**](https://www.markdownguide.org/), and in the end, I thought what's better than allowing the use of both? So, we can write our content using Markdown and HTML labels and use both at the same time.

##### **DDBB**

I have been working with Microsoft SQL Server for more than 15 years and lately, I have been working with MySQL, at the beginning of my career I was using for years Oracle. So for this project, I decided to try a new one and the choice for developing was [**SQLite**](https://www.sqlite.org/index.html) but to use it in production once I deploy the project I went for [**PostgreSQL**](https://www.postgresql.org/). The good part is that the portfolio works perfectly with both so only changing the environment variables can use SQLite, PostgreSQL, or another different.

##### **The search**

In the beginning, my portfolio would have very few projects, so a searching function would not be too important but I wanted to create one project alive for a long time and easily maintainable so in the end I implemented a simple search function using the queries of the extension [**FlaskSQLAlchemy**](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) which was the library that I was using to work with the databases. But in the last months I have been reading quite often about NoSQL databases, and the capabilities of [**Elasticsearch**](https://www.elastic.co/) for searching, so I decided to start working with this kind of databases using Elasticsearch in my project.

Finally, the option of search in my portfolio is powered by Elasticsearch and, in case this engine is not present in our enviroment, will be powered by FlaskSQLAlchemy.

I also have a search of keywords, this is much simpler and it will find only the keyword we are searching but with the characteristic of bringing the keywords that share the projects where our keyword search is present too.

##### **Containerization**

And, if all the technologies I had to explore, learn, and implement for my project were not enough, I decided that I should containerize my app. So I started to learn **Docker** since this is one of the most popular platforms. During my learning path, I was able to create a docker container with my Flask app, so I had one docker container with my portfolio working but I wanted to create all my whole project with containers. In the end, I finished with a docker network with 3 containers: 

- The first one, and more important because has all the data, one PostgreSQL docker
- The second one, if present, is the Elasticsearch docker for the searching functionality
- The third one is my Flask app which has even the HTTP Server powered by [**Gunicorn**](https://gunicorn.org/)

##### **Deployment**

(I am still working on this part)

As the last step of my project, I need to deploy it. During this path, I was working always with opensource or free-of-charge options (except the domain name that I had to pay) and the option I found that could work for me was the use of [**OCI**](https://www.oracle.com/es/cloud/), the **Oracle Cloud Infrastructure** that has one Free Tier (Always Free Services) which I could use for the deployment.

In addition to this, I created one [**Google Analytics**](https://analytics.google.com/) account to monitor and analyze my website.