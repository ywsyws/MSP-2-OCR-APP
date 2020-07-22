# MSP-2
MSP-2 Preparation

Vous êtes une entreprise qui possède une grande quantité d'images retraçant des opérations de vente passées (par exemple). Vous avez besoin d'obtenir les informations de texte contenues dans ces fichiers. Vous décidez pour cela d'utiliser une api d'OCR (Reconnaissance Optique de Caractères) afin d'extraire le texte des images.

[Application 2](https://ibb.co/R9JyvZF)
<br>
<a href="https://ibb.co/R9JyvZF"><img src="https://i.ibb.co/R9JyvZF/Capture-d-e-cran-de-2020-07-20-09-50-26.png" alt="Capture-d-e-cran-de-2020-07-20-09-50-26" border="0"></a>


<br>

## User Manual for Docker

1. If you you have your own Flask app, copy only the Dockerfile to your work directory
2. Open Dockerfile 
    * Change Git a/c information with yours (line 13, 14)
    * **Optional:** Replace the volume directory path `/app` that needs to be mounted with yours (line 37)
    * Replace the flask app name `main.py` to yours (line 40)
3. If you have your own Flask app, create requirements.txt file by typing `pip freeze > requirements.txt` in your work directory terminal where you flask app is
4. If you have your own Flask app, go to [gitignore.io] to create .gitignore file in your work directory
<br>

### In your work directory terminal:

5. Type `docker image build -t <image_name> .` to build the image
6. Use `docker images` to check if the image is successfully built
7. To create a container, type the command below and modify accordingly the `-v` tag arguments in the format of `host_path:container_path` <br>
   `docker container run -it --name <container_name> -p 8004:5000 -v "$(PWD):/app" -d <image_name>` 
e.g.: docker container run (--rm) -it --name "azure-ml" -p 8004:5000 -v "$(PWD):/app" (-d) jupyter-python  
explaination: containers name / hostPC port: service port in container / $(PWD) = projects directory

<br>

### Open your broswer

8. Go to <http://127.0.0.1:8004> to see the page. If neccessary, replace `127.0.0.1` with your localhost IP address. 
<br>
<br>

#### If your container is stopped

1. Type `docker start container_name` to restart it
2. To execute the container, type `docker exec -it <container_name> bash`

#### Once you are inside the docker container

3. Type `flask run --host=0.0.0.0` to run the application

4. Go to <http://127.0.0.1:8004> to see the page. If neccessary, replace `127.0.0.1` with your localhost IP address.

Note: You can type `docker ps` in your work dorectory terminal to check if the container is successfuly created

[gitignore.io]: https://gitignore.io/
