# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /srv

# Copy the entire project into the container
COPY . .

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry --version

# Install project dependencies using Poetry
RUN poetry install


# Run your tests (adjust the command as needed)
# CMD ["poetry", "run", "pytest", "tests/"]
CMD ["cat"]
