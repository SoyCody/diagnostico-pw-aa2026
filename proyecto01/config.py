import os

DEFECTO_PUERTO = 5000
PORT = int(os.getenv('PORT', DEFECTO_PUERTO))