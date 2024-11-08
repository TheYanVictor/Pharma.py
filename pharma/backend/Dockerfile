# Use a imagem oficial do Python como base
FROM python:3.8

# Defina variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo
COPY . /app/

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
