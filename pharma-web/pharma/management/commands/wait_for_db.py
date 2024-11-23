from django.core.management.base import BaseCommand
import time
import mysql.connector

class Command(BaseCommand):
    help = "Aguarda o banco de dados MySQL estar pronto antes de iniciar o servidor."

    def handle(self, *args, **kwargs):
        self.stdout.write("Aguardando o banco de dados...")
        while True:
            try:
                conn = mysql.connector.connect(
                    host="db",  # Nome do serviço no docker-compose
                    user="user",
                    password="password",
                    database="mydatabase"
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Banco de dados disponível!"))
                break
            except mysql.connector.Error:
                self.stdout.write("Banco de dados indisponível, tentando novamente...")
                time.sleep(1)
