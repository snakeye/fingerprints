# Fingerprints

## Fingerprints database

FVC2004 Database http://bias.csr.unibo.it/fvc2004/download.asp

## Run the pipeline

```bash
 pipenv shell 
 python src/read.py data/example.png | python src/step1.py | python src/write.py data/result.png
 ```