FROM python:3.12-slim

# set working directory inside the container
WORKDIR /app

# copy requirements first, install, then copy the rest
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# now copy everything else (app.py, pkl files, templates/)
COPY . .

# document which port the app listens on (informational, doesn't actually publish it)
EXPOSE 5000

# run with gunicorn instead of the Flask dev server
# "app:app" means: in the file app.py, use the object named "app" (your Flask instance)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]