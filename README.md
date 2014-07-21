block-builder-site
==================
a web app that helps create phrases out of lettered blocks.

background
==================
I built this site to help solve the question of whether a phrase could be build from a set of lettered blocks.

Block Sets Description:
Each block has a different set of 6 letters on its faces. 
The block sets both are comprised of 16 blocks.
Blocks share some of the same letters
No two blocks are identical (share all 6 letters in common).
Each block is numbered as a reference.

There are two original sets that have been added to the config for the site, but other sets could also be added.

features
==================
Shows whether a phrase is possible.
Option to show the solution to build the phrase by displaying the ordered list of block reference numbers.
Lists links last 5 possible phrases created (updated via ajax)

There is also logic in place to calculate the difficulty of the phrase based on how many possible ways the phrase can be created using a given block set.

install
==================
checkout and build this project like any django projects
* git clone repo
* pip install -r requirements.txt
* cd block-builder-site
* python manage.py runserver

