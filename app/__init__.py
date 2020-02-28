import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config

LOG_DIR = 'LOG_DIR'
LOG_BACKUP_COUNT = 'LOG_BACKUP_COUNT'
MAX_LOG_BYTES = 'MAX_LOG_BYTES'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.views import views_bp
    app.register_blueprint(views_bp, url_prefix="/reviewAnalysis")

    if not os.path.exists(app.config[LOG_DIR]):
        os.mkdir(app.config[LOG_DIR])
    
    log_file = os.path.join(app.config[LOG_DIR], 'app.log')
    file_handler = RotatingFileHandler(log_file)

    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s ')
        )   
    
    file_handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    
    app.logger.addHandler(file_handler)
    app.logger.info("App started")

    return app