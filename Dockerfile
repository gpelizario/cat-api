FROM python:3.6



# Instalacao de pacotes
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install requests


# Copiando o requirements                                        
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

#instalando tudo que tem no requirements

RUN pip install -r requirements.txt

COPY . /app

#coloquei pra ele entender que sempre deve usar python3                  

ENTRYPOINT [ "python3" ]

#script a ser iniciado

CMD ["img_cat_dashboard.py"]