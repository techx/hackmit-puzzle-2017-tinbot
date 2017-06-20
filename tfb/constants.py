MODELS_DIRECTORY = 'tfb/models'
MODEL_PREFIX = 'model_{model_index}.model'
RANDOM_PREFIX = 'random_{model_index}.png'

BOT_JOBS = [line.rstrip('\n') for line in open('tfb/meta/bot_jobs.txt')]
BOT_NAMES = [line.rstrip('\n') for line in open('tfb/meta/bot_names.txt')]

CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']