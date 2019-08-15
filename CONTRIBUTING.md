# For contributors

Comments, criticisms, and concerns are always welcome! If you would like to help with development, please follow the steps below.

## Clone the repo 

```bash
git clone https://github.com/rbpatt2019/studious-happiness.git
cd studiouos-happiness
```

## Make a new environment

Follow your own protocol! I use pyenv for all my env/venv control, so I would do:

```bash
pyenv virtualenv studious-happiness
pyenv local studious-happiness
```

Regardless of how you do it, run the following once its created:

```bash
make develop
```

## Start developing

Checkout the [Makefile](Makefile) for lots of useful commands for testing, linting, and many others! Before committing any changes, I'd strongly recommend creating a new branch:

```bash
git checkout -b new_feature
```

## And contribute!

Once you're ready to share your changes, fork the repository on github. Then, add it as a remote to the repo and push the changes there. 

```bash
git remote add origin https://github.com/YOUR_USER/studious-happiness.git
git push origin new_feature
```

Finally, open a pull request, and I'll review it as soon as I can!

If you're a command line nut like me, this can all be done from the command line using `hub`, a CLI for interacting with the github api. See their [repo](https://github.com/github/hub) for installation instructions. Then run:

```bash
hub fork --remote-name=origin
git push origin new_feature
hub pull-request```