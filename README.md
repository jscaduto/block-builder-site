block-builder-site
==================
a website that helps create phrases out of lettered blocks.

background
==================
I built this site to help solve the question of whether a phrase could be build from a set of lettered blocks.
Each block has a different set of 6 letters on its faces. There are two original sets that have been added to the config for the site, but other sets ccould also be added.
The block sets both are comprised of 16 blocks.  Some blocks share the same letters, although no block is identical.
There is also logic in place to calculate the difficulty of the phrase based on how many possible ways the phrase can be created using a given block set.

install
==================
checkout and build this project like any django projects
git clone repo
pip install -r requirements.txt
cd block-builder-site
python manage.py runserver

