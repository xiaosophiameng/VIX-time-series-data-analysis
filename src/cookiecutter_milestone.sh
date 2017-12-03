# the codes below generate a project file
# and directory structure template for my data science project
#create a readme file
touch README.md
#create a LICENSE file
touch LICENSE.md
#create a citation file
touch CITATION.md
#create a contributing file
touch CONTRIBUTING.md
#create a conduct file
touch CONDUCT.md
#make a folder named data
mkdir data
#go to data folder and create the birds_count_table.csv file in the folder
cd data
touch birds_count_table.csv
#go out of data folder
cd ..
#make a folder named doc
mkdir doc
#go to doc folder and create notebook and manuscript files in the folder
cd doc
touch notebook.md
touch manuscript.md
#go out of doc folder
cd ..
#make a folder named results
mkdir results
#make a folder named src
mkdir src
#go to src folder and create the following two py files in the folder
cd src
touch sightings_analysis.py
touch runall.py
#go out of src folder
cd ..

#move cookiecutter file to src folder
mv cookiecutter_milestone.sh src
#make a folder named from_joe
mkdir from_joe
