{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#importing necessary libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.image as mpimg\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "\n",
    "np.random.seed(2)\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix\n",
    "import itertools\n",
    "\n",
    "from keras.utils.np_utils import to_categorical \n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2d\n",
    "from keras.optimizers import RMSprop\n",
    "from keras.preprocessing.image import ImageDataGenerator\n",
    "from keras.callbacks import ReduceLROnPLateau\n",
    "\n",
    "sns.set(style='white',context='notebook',palette='deep')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#let's load our data\n",
    "train = pd.read_csv()\n",
    "test = pd.read_csv()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
