echo "Run migrations"
python manage.py migrate
echo "Done migrations"
python manage.py create_db_meters
echo "Create db"