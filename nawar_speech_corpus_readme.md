* Preprocess 
    * Add a folder called nawar in the tacotron directory in your user folder
        * Add temp.csv there
        * Add a folder called wavs there in which all wav files are there
    * Run `python .\preprocess.py --dataset nawar`
* Update max_iters to 400 if not already set to that number
* Train
    * `python .\train.py`