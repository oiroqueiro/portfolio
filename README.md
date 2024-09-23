### **Portfolio**

Portfolio built from scratch, from website planning with no idea of web development to deployment with docker without idea of containers.

I had several projects that I wanted to show but I didn't like the idea of using one existent website because all the alternatives that I was trying didn't have some of the features I thought were a must in my portfolio or were not flexible to customize it or were not beautiful (or what I consider beautiful for a portfolio).

Using one of those platforms would be the best option since I have a full-time job and two little girls born during the pandemic years, but I decided to go for it through the complicated path (sometimes hell path) and <u>create my portfolio from scratch</u>.

I know that one portfolio is not a good example for a data analytics project, actually is not related to data analytics, but this project was a great opportunity to show my determination, creative problem solving, adaptability and to learn a lot along the time I would dedicate to this project.

The features I wanted in my portfolio include:

1. Multi-language
2. Responsive website
3. Light/Dark mode
4. Customizable
5. Containerized
6. Index Search

The first four were mandatory, the other two I wanted to learn and practice.

**Demo/My portfolio**

You can see ~~a live demo~~ my portfolio working in  [**Oscarlytics**](https://oscarlytics.com).

*2024/09 Update*
*The following features have been added:*  
*- Robots.txt to allow web crawlers to index the portfolio. Since this is a static file, I decided to serve the file using Nginx instead of serving it from within the portfolio.*  
*- sitemap.xml to help the indexing of the webpages. At this moment I have only few projects so was easy to create one static file. In the future, if keep adding projects at a slow pace, this method will be easy to mantain. If I have more time to add more projects, I will implement a dynamic sitemap.xml*  
*- reCaptcha v3 to prevent spam. I was receiving few messages that were clearly spam, so I decided to implement this method of Google in his free tier.*  


So let's explain the path from the beginning.

#### **The path**

Since I am not a UX/Designer or web developer, and my knowledge of HTML, CSS, and JavaScript was limited, the challenge started being super hard for me. 

##### **Multi-language**

One thing that I was sure would not happen was the use of a library to translate all the texts automatically. I know that there are fantastic options out there that could make my portfolio accessible to almost everyone, but I think that a feature made like this would run against the nature of one portfolio.

A portfolio should be a presentation card of the work of someone to show the skills of the owner, using an automated tool, which is quite easy to implement (I know what I'm talking about because I used it in 2 of my previous projects and of course, I am not against this), is not what I wanted, so the choice I took to implement the multi-language was translated by myself the texts and store them in the database making easy to the users to change between the languages that the owner knows (or decide to show).

##### **The website**

When I started to investigate my options to create one website, the beginning was very discouraging. Only when I discovered [**Hugo**](https://gohugo.io/) I started to see the light at the end of the tunnel. Hugo is a framework for building websites with a lot of beautiful templates for websites and a great community. So I was researching Hugo and his templates for quite a while until I found some templates that could fit my requirements. The problem was that Hugo is fantastic for building static websites which is the opposite of my idea of one portfolio.

So in the end when I chose the [**iWriter**](https://github.com/statichunt/iwriter-hugo) template arrived at the moment to adapt it to a dynamic website.

##### **Flask**

One technology that I wanted to explore and improve my skills in was [**Python**](https://www.python.org/) because has tons of libraries, frameworks, and an impressive community behind it. So, when I thought about dynamic websites, [**Flask**](https://flask.palletsprojects.com/en/3.0.x/) came quickly to my mind. Since I worked with it in my [*Lyrics*](https://github.com/oiroqueiro/mid-bootcamp-project) project, I knew about his capabilities but the hard work had just started.

I had to adapt the iWriter template to be a dynamic template with [Jinja](https://jinja.palletsprojects.com/en/3.1.x/templates/) without losing any functionality I liked about this template.

After spending many, many, many hours understanding the HTML, CSS, javascript, and Bootstrap (and other technologies) that my template was used to have such features and more hours cleaning the code and adapting, I had some templates quite cleaned and ready to use with the logic of my website.

At this point I want to share with all of you [**this fantastic tutorial of Flask**](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), by *Miguel Grinberg*. I also use this one, in Spanish, of [**j2logo**](https://j2logo.com/tutorial-flask-espanol/) by *Juan José Lozano Gómez*. I learned a lot with them and with all the features that I had to face.

In the end, I added one chart in the about me section, created with [**cutecharts**](https://github.com/cutecharts/cutecharts.py), which will show a summary of the keywords present on the portfolio.

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

And, if all the technologies I had to explore, learn, and implement for my project were not enough, I decided that I should containerize my app. So I started to learn **Docker** since this is one of the most popular platforms. During my learning path, I was able to create a docker container with my Flask app, so I had one docker container with my portfolio working but I wanted to create all my whole project with containers. In the end, I finished with a docker network with ~~3 containers~~ 4 containers: 

- The first one, and more important because has all the data, one PostgreSQL docker
- The second one, if present, is the Elasticsearch docker for the searching functionality
- The third one is my Flask app which has even the WSGI HTTP Server powered by [**Gunicorn**](https://gunicorn.org/)
- The fourth is the real Web Server and Reverse Proxy, the [**Nginx**](https://www.nginx.com/) docker

##### **Deployment**

As the last step of my project, I need to deploy it. During this path, I was working always with opensource or free-of-charge options (except the domain name that I had to pay) and the option I found that could work for me was the use of [**OCI**](https://www.oracle.com/es/cloud/), the **Oracle Cloud Infrastructure** that has one Free Tier (Always Free Services) which I could use for the deployment.

The problem arose when I couldn't run all the containers, I could push my flask to the docker hub, but when I pulled it I faced a lot of problems with the architecture of the hardware. After a lot of tests and updates of my container (even though I tried to recompile everything for the new platform), I gave up and decided to try another VPS provider.

This time I decided to go for a paid provider with a platform that I could manage without so many problems, the result was that after configuring a new Ubuntu Server in [**Ginernet**](https://ginernet.com/en/vps/), a Spanish provider (since I am based in Spain) with reasonable prices, I could deploy my website without problems.

The new problems arrived when I tried to access my website from my Android mobile.
The browser changes always the *HTTP* protocol to *HTTPS* which I didn't implement in my Flask app, so I needed to change my docker-compose and add the fourth container (Nginx).
Then was the turn of the ***HTTPS\*** protocol implementation, which requires ***SSL\*** certificates but not only signed by my server because web browsers only like certificates signed by a well-known certificate authority (if our certificate is not like this, the web browser will show an ugly page before our beautiful website), so with the help of [**Let's Encrypt**](https://letsencrypt.org/) and few tests (like creating a new container that I had to drop in the end) I could give to my website a good enough and free *SSL* certificate.And how I could have this? In the end was quite easy, in the command line of my Ubuntu Server (the host of the dockers), I typed this:

`sudo apt-get update`

`sudo apt-get install certbot python3-certbot-nginx`

and then:

`sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com`

After that, only needed to restart the Nginx container to get the generated certificates. Certbot also creates one cron job to renew the certificates when needed. 

Right now, the quality of my server is grade **A** in [**Qualys. SSL Labs**](https://www.ssllabs.com/), but I will keep trying to get the **A+** grade soon.

In addition to this, I created one [**Google Analytics**](https://analytics.google.com/) account to monitor and analyze my website, which is working fine.

**Installing**

And now I will explain how you can use this project.

First, need to say that I use Linux (Ubuntu) at home, and my project was created using this operating system, so if you are using Windows at least the paths need to be changed, I think that all the paths are in the environment variables or configuration files (docker compose, nginx.conf, ...), which are in the docker folder.

- Python needs to be installed, can be downloaded [here](https://www.python.org/downloads/).

- If you will clone this repository, install Git downloading from [here](https://git-scm.com/downloads)

- Clone this repository in the folder where you will work

  `git clone https://github.com/oiroqueiro/portfolio.git`

- Create one environment to work, for instance, inside your project, type

  `python3 -m venv test`

  where test is the name that you want for your environment

- Activate the new environment

  `source test/bin/activate`

  or in windows:

  `test\Srcripts\activate.bat`

  if you see something like this, with the environment name between parentheses at the beginning of the line, it's activated:

  `(temp) user@pc:/portfolio$`

- Then install all the requirements typing:

  `pip install -r requirements.txt`

  and it should be ready to work

- Create the folder structure for the personal content, in my case I have the project in one folder named *portfolio* and at the same level *portfolio_production* with this structure:

  ```
  ├── docker-compose.yml
  ├── dockerfile.nginx
  ├── env_elastic
  ├── env_portfolio
  ├── env_postgres
  ├── nginx.bak.conf
  ├── nginx.conf
  └── portfolio_content
      ├── content.xlsx
      └── portfolio
          └── static
              └── img
                  ├── Favicon144x.png
                  ├── Favicon16x.png
                  ├── Favicon180x.png
                  ├── Favicon192x.png
                  ├── Favicon32x.png
                  ├── Favicon48x.png
                  ├── Favicon512x.png
                  ├── Favicon72x.png
                  ├── Favicon96x.png
                  ├── Logo_black_240x.png
                  ├── Logo_black_240x.webp
                  ├── Logo_white_120x.png
                  ├── Logo_white_240x.webp
                  ├── og-image.jpg
                  ├── ProfilePicture1110x.jpg
                  ├── ProfilePicture1110x_lost.jpg
                  ├── ProfilePicture1110x_lost.webp
                  ├── ProfilePicture1110x.webp
                  ├── ProfilePicture40x_lost.jpg
                  ├── ProfilePicture40x_smudged_lost.jpg
                  ├── ProfilePicture545x.webp
                  ├── ProfilePicture600x_lost.webp
                  ├── ProfilePicture600x.webp
                  ├── ProfilePicture700x_lost.webp
                  ├── ProfilePicture700x.webp
                  ├── ProfilePictureAbout_1110x.jpg
                  ├── ProfilePictureAbout_1110x.webp
                  ├── ProfilePictureAbout_545x.webp
                  ├── ProfilePictureAbout_600x.webp
                  ├── ProfilePictureAbout_700x.webp
                  ├── ProfilePicture.webp
                  └── projects
                      ├── project0101_1110x.jpg
                      ├── project0101_1110x.webp
                      ├── project0101_545x.webp
                      ├── project0101_600x.webp
                      ├── project0101_700x.webp
                      ├── project0101.jpg
                      ├── project0102_1110x.jpg
                      ├── project0102_1110x.webp
                      ├── project0102_545x.webp
                      ├── project0102_600x.webp
                      ├── project0102_700x.webp
                      ├── project0102.jpg
                      ├── project0103_1110x.jpg
                      ├── project0103_1110x.webp
                      ├── project0103_545x.webp
                      ├── project0103_600x.webp
                      ├── project0103_700x.webp
                      ├── project0103.jpg
                      ├── project0201_1110x.jpg
                      ├── project0201_1110x.webp
                      ├── project0201_545x.webp
                      ├── project0201_600x.webp
                      ├── project0201_700x.webp
                      ├── project0201.jpg
                      ├── project0202_1110x.jpg
                      ├── project0202_1110x.webp
                      ├── project0202_545x.webp
                      ├── project0202_600x.webp
                      ├── project0202_700x.webp
                      ├── project0202.jpg
                      ├── project0203_1110x.jpg
                      ├── project0203_1110x.webp
                      ├── project0203_545x.webp
                      ├── project0203_600x.webp
                      ├── project0203_700x.webp
                      ├── project0203.jpg
                      ├── project0204_1110x.jpg
                      ├── project0204_1110x.webp
                      ├── project0204_545x.webp
                      ├── project0204_600x.webp
                      ├── project0204_700x.webp
                      ├── project0204.jpg
  ```

  What you need to know about it:

  - These are the files that need to be modified to run the containers:

    ```
    ├── docker-compose.yml
    ├── dockerfile.nginx
    ├── env_elastic
    ├── env_portfolio
    ├── env_postgres
    ├── nginx.bak.conf
    ├── nginx.conf
    ```

  - the env* files are the files with the environment variables (users, passwords, emails, number of projects per page, ...) that are used by the containers

  - This is the file with the content of the portfolio (texts of the portfolio itself and personal content like about, projects, personal texts, ...). When you want to change or add something, just modify the Excel file, upload it to the production environment, and restart the portfolio docker. Is there a content_template.xlsx in the main folder of the project where can see some data:

    ```
        ├── content.xls
    ```

    In it you can see 4 sheets:

    - languages: Using the [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) codes, in my case:

      | **language** |
      | ------------ |
      | en           |
      | es           |

  - portfolio: The texts of the website itself, you can modify them on your own or add more languages. For example:

    | **template** | **variable**  | **language** | **value** |
    | ------------ | ------------- | ------------ | --------- |
    |              | menu_home     | en           | Home      |
    |              | menu_about    | en           | About     |
    |              | menu_projects | en           | Projects  |
    |              | menu_contact  | en           | Contact   |

    Notice that the template column needs to be empty

  - content: The personal texts needed to be modified for every template (but projects that have their own). In my case, the first rows look like this:

    | **template** | **variable** | **language** | **value**                                                    |
    | ------------ | ------------ | ------------ | ------------------------------------------------------------ |
    | index        | hello        | en           | Hey, I’m                                                     |
    | index        | name         | en           | Oscar Iglesias                                               |
    | index        | subtitle     | en           | Data Analyst & ERP Developer Analyst. Welcome to my Portfolio. |
    | index        | hello        | es           | Hola, soy                                                    |
    | index        | name         | es           | Oscar Iglesias                                               |
    | index        | subtitle     | es           | Analista de Datos & Analista Desarrollador de ERP. Bienvenid@ a mi Portfolio. |
    | about        | hello        | en           | Hi,I’m Oscar Iglesias, Data Analyst and ERP Analyst Developer |
    | about        | parragraph1  | en           | I'm living in ...                                            |
    | about        | parragraph2  | en           | I love working with data. During my professional experience, I got the chance to work with many types of databases and acquire a great experience helping stakeholders to get more information and discover good insights because of my skills in visualisation as well. |

  - projects: The content of the projects with these columns:

    | **date** | **project_n** | **language** | **title** | **resume** | **exposition** | **action** | **resolution** | **keywords** | **link1** | **link2** | **link3** | **link4** | **link5** | **image_title** | **image1** | **image2** | **image3** |      |
    | -------- | ------------- | ------------ | --------- | ---------- | -------------- | ---------- | -------------- | ------------ | --------- | --------- | --------- | --------- | --------- | --------------- | ---------- | ---------- | ---------- | ---- |

    - date: is the date when the project was released

    - project_n: the number of the project in that day (if you are super productive and don't have litle daughters... )

    - language: the ISO 639-1 code of the language used in this row

    - title: the title that appears in the list of projects

    - resume: the text that appears in the list of projects

    - exposition, action, resolution: the 3 blocks I divided the projects, can use how you want, to me is easier to work like this, or use only one it's up to you. In these blocks, you can use references to the images. 

    - keywords: separated by commas (,)

    - links: this column has no use in the project, I created but in the end, the use of Markdown and HTML was enough to reach what I wanted to get. But I keep them just in case in the future I need them

    - image_title, image1, image2, image3: I thought to create more columns but in the end were enough for me, one image for the header and one for each block, they can be referenced in the blocks of the content (exposition, action, resolution) like this:

      ` <img>image1</img>`

      ` <img>image2</img>`

      ` <img>image3</img>`

  - These are the images of the portfolio (the images for the projects are not at this level):

                └── img
                    ├── Favicon144x.png
                    ├── Favicon16x.png
                    ├── Favicon180x.png
                    ├── Favicon192x.png
                    ├── Favicon32x.png
                    ├── Favicon48x.png
                    ├── Favicon512x.png
                    ├── Favicon72x.png
                    ├── Favicon96x.png
                    ├── Logo_black_240x.png
                    ├── Logo_black_240x.webp
                    ├── Logo_white_120x.png
                    ├── Logo_white_240x.webp
                    ├── og-image.jpg
                    ├── ProfilePicture1110x.jpg
                    ├── ProfilePicture1110x_lost.jpg
                    ├── ProfilePicture1110x_lost.webp
                    ├── ProfilePicture1110x.webp
                    ├── ProfilePicture40x_lost.jpg
                    ├── ProfilePicture40x_smudged_lost.jpg
                    ├── ProfilePicture545x.webp
                    ├── ProfilePicture600x_lost.webp
                    ├── ProfilePicture600x.webp
                    ├── ProfilePicture700x_lost.webp
                    ├── ProfilePicture700x.webp
                    ├── ProfilePictureAbout_1110x.jpg
                    ├── ProfilePictureAbout_1110x.webp
                    ├── ProfilePictureAbout_545x.webp
                    ├── ProfilePictureAbout_600x.webp
                    ├── ProfilePictureAbout_700x.webp
                    ├── ProfilePicture.webp

    What you need to know is that if you want to use your images, only be careful to set the corresponding name (ProfilePicture1110x.jpg for example), I think that is quite self-explainable the names to know what they are for. Just tell you that the 1110x, 700x, ... are the horizontal pixels of the pictures.

  - These are the images of the projects:

                    └── projects
                        ├── project0101_1110x.jpg
                        ├── project0101_1110x.webp
                        ├── project0101_545x.webp
                        ├── project0101_600x.webp
                        ├── project0101_700x.webp
                        ├── project0101.jpg
                        ├── project0102_1110x.jpg
                        ├── project0102_1110x.webp
                        ├── project0102_545x.webp
                        ├── project0102_600x.webp
                        ├── project0102_700x.webp
                        ├── project0102.jpg
                        ├── project0103_1110x.jpg
                        ├── project0103_1110x.webp
                        ├── project0103_545x.webp
                        ├── project0103_600x.webp
                        ├── project0103_700x.webp
                        ├── project0103.jpg
                        ├── project0201_1110x.jpg
                        ├── project0201_1110x.webp
                        ├── project0201_545x.webp
                        ├── project0201_600x.webp
                        ├── project0201_700x.webp
                        ├── project0201.jpg
                        ├── project0202_1110x.jpg
                        ├── project0202_1110x.webp
                        ├── project0202_545x.webp
                        ├── project0202_600x.webp
                        ├── project0202_700x.webp
                        ├── project0202.jpg
                        ├── project0203_1110x.jpg
                        ├── project0203_1110x.webp
                        ├── project0203_545x.webp
                        ├── project0203_600x.webp
                        ├── project0203_700x.webp
                        ├── project0203.jpg
                        ├── project0204_1110x.jpg
                        ├── project0204_1110x.webp
                        ├── project0204_545x.webp
                        ├── project0204_600x.webp
                        ├── project0204_700x.webp
                        ├── project0204.jpg

    The project is ready to use up to 4 images, one of them for the header. To configure them, in the content.txt only need to type the name of the image without the underscore, pixels, and extensions, for example:

    | **image_title** | **image1**  | **image2**  | **image3**  |
    | --------------- | ----------- | ----------- | ----------- |
    | project0101     | project0102 | project0103 |             |
    | project0101     | project0102 | project0103 |             |
    | project0201     | project0202 | project0203 | project0204 |
    | project0201     | project0202 | project0203 | project0204 |

    

- If you want to run locally without containers, you need to fill the content of the environment variables in the file **.env** in the main folder of the project and run it to load them in memory. The PROJECTS_PAGE will show this number of projects in the index of projects, you can adjust as you want. UPDATE_DATA if is True, will execute the insert_data.py on the load of the **boot.sh** file. PORTFOLIO_LOGIN_URL AND PORTFOLIO_LOGOUT_URL are the names for the routes in the URL of the web browser to be logged in or logged out, which are customizable. At the moment they only work on creating new menu options but in the future, I plan to add and modify the content from inside the portfolio instead of using an Excel file:

​        export FLASK_APP=portfolio.py

​	export MAIL_SERVER=

​	export MAIL_PORT=465

​	export MAIL_USE_SSL=True

​	export MAIL_USE_TLS=False

​	export MAIL_USERNAME=

​	export MAIL_PASSWORD=

​	export MAIL_RECIPIENT=

​	export PORTFOLIO_LOGIN_URL=login

​	export PORTFOLIO_LOGOUT_URL=end

​	export PROJECTS_PAGE=4

​	export UPDATE_DATA=True

​	export DATABASE_URL=

​	export ELASTICSEARCH_URL=



- To run the containers, first need to install docker, you can download it from [here](https://www.docker.com/products/docker-desktop/?_gl=1*1o5ji3v*_ga*MTA2Mzg1NDYyMy4xNjg4ODM4Mjc3*_ga_XJWPQMJYHQ*MTcwNDAzODk3OC42Ny4xLjE3MDQwMzkwMjEuMTcuMC4w).

  Then, you have to modify the paths and your domain in the files inside the *docker* folder. Then you have 2 options:

  - run like this, then you can use:

    `docker compose -f docker-compose_pulling.yml -p portfolio up -d`

    or

    `docker-compose -f docker-compose_pulling.yml -p portfolio up -d`

    depending on your system.

    This will pull the image that I have created which is in the [**docker hub**](https://hub.docker.com/repository/docker/roqueou/portfolio/general)

    If the setup is ok (all the configurations are well), will have 4 containers running your portfolio.

  - modify your portfolio on your own and create one docker for your portfolio with your modifications:

    `docker compose -f docker-compose_builder.yml`

    or

    `docker-compose -f docker-compose_builder.yml`

    depending on your system.

    After that you have your image that can run with the other 3 containers.

- If you want to push your image to docker hub and then use the pulling method, then you have to:

  - create one account in the hub of docker, [here](https://hub.docker.com/)

  - tag your image:

    `docker tag your_image_name yourusername/name_of_your_image:version`

    first, use your local image name and then the name that you want to publish in your hub with the version (usually: latest)

  - push it:

    `docker push yourusername/name_of_your_image:version`

  - then modify the docker-compose_pulling.yml to download your image and that's it.

- And if you want to monitor is your server is Up or Down, and even the days that your ssl certificate would be valid, I can recommend install the docker of [**Uptime Kuma**](https://github.com/louislam/uptime-kuma), with just this line of code:

  `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1`

  Then, you can configure and analyze your website using the url: http://localhost:3001/
