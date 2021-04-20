{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['\\n\\nI reached my favorite spot in my home, THE TERRACE',\n",
       " ' The only place which has proved to be my best friend for all those past years',\n",
       " ' Sun was not up yet, so was I',\n",
       " ' Waiting for the sun, I saw some leftover rice 4 to 5 feet away from me',\n",
       " ' I began to weave my own thought web that how many tons of food get waste on a daily basis and how many people go to bed hungry each night',\n",
       " ' Those rice were making me feel guilty inside',\n",
       " '\\n\\nGuilt-ridden  I hopelessly sat there',\n",
       " ' I saw a squirrel , a little furry cute squirrel',\n",
       " ' She was full of life, full of bubbling energy',\n",
       " ' She came up there searching for food and upon finding those rice, she looked so satisfied as it was everything she needed',\n",
       " ' She rolled up some grains of rice into a holdable ball and then sat on its back paws',\n",
       " ' She grabbed that riceball with her tiny front paws and gnawed',\n",
       " ' Not only she looked adorable but for around 10 to 15 minutes I forgot all my problems and kept gazing at her awestruck beauty',\n",
       " ' Nature never forgets to keep its food cycle smoothly running']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file1=open(\"article1.txt\",\"r\")\n",
    "text1=file1.readlines()\n",
    "text1\n",
    "\n",
    "file2=open(\"article2.txt\",\"r\")\n",
    "text2=file2.readlines()\n",
    "text2\n",
    "\n",
    "import nltk\n",
    "str1=''.join(text1)\n",
    "str2=''.join(text2)\n",
    "\n",
    "str1\n",
    "\n",
    "str2\n",
    "\n",
    "# Split the string\n",
    "\n",
    "sent_text1=str1.split('.')\n",
    "sent_text2=str2.split('.')\n",
    "\n",
    "sent_text1\n",
    "\n",
    "sent_text2\n",
    "\n",
    "# Create a for loop that compares two lists\n",
    "final_list=[]\n",
    "for z in sent_text1:\n",
    "    for y in sent_text2:\n",
    "        if z == y:\n",
    "            final_list.append(z)\n",
    "\n",
    "final_list\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
