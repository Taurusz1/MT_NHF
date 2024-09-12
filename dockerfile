FROM python:3.12
RUN pip install pandas numpy scikit-learn mathplotlib 
WORKDIR /work
ADD main.py .
CMD ["python", "./main.py"] 
# Or enter the name of your unique directory and parameter set.
