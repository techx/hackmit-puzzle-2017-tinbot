# Tinbot

_Where bots find their true love™_

<p align="center">
	<img src="https://github.com/techx/hackmit-puzzle-2017-tinbot/raw/master/screenshot.png" alt="screenshot" width="400" />
</p>

**Warning:** This repository consists of server side secrets that are _not_ in the `.gitignore`. Do not push from deployment sites.

## Setup

Resolve dependencies,

```bash
pip install -r requirements.txt
```

The server will run with any Keras backend, but tensorflow is prefered for faster boot up time. The solution file only works with tensorflow.

We now need to generate and train the models we'll use. First edit the `generate_models.py` file. And set `NUM_MODELS` to the desired number of models to train. Then run,

```bash
python generate_models.py
```

## Deploy

The repository has all client side dependencies pre-built and bundled. For local debugging, use,

```bash
python runserver.py
```

Production,

```bash
gunicorn -b 0.0.0.0:80 -w 1 tfb:app
```

You can only use 1 worker thread with gunicorn, because I suck at programming.

## Puzzle Mechanics

_**(Spoiler Warning: Everything below this line gives away the solution to the puzzle)**_

The puzzle presents you with a website where you can edit your profile. The only thing you can change about your profile is your profile picture. When you do this, the site runs a neural network in your browser and on the server, predicting a specific class.

You can now start swiping bots on the Find Bots page. Your job is to get the `Puzzler` bot to swipe you back. The user should now notice that the preference of the `Puzzler` bot happens to only be class 1. This means that the user's profile picture must result in class 1 on the neural network.

The user at this point must implement a "gradient ascent" algorithm that maximizes the activation of the predicted class, solving for an input image that activates class 1.

Now the user must engage in conversation with the `Puzzler` bot in order to extract the solution of the puzzle. _This part is still in progress_

### Example Solution

There are many different ways of solving this puzzle. The one I could come up with is at `tfb/trainer/solve.py`

### Development

The `FIXME` in the template `tfb/templates/wrapper.html` is part of the puzzle.