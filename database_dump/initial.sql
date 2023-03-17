CREATE DATABASE airflow_db;
CREATE USER 'masbro' IDENTIFIED BY 'mantap';
GRANT ALL PRIVILEGES ON airflow_db.* TO 'masbro';