# Arabic Tacotron TTS
An implementation of Tacotron speech synthesis in TensorFlow for Arabic. 


### Audio Samples
Check **[Audio Samples](https://youssefsharief.github.io/arabic-tacotron-tts/)** from models trained using this repo on [Nawar Halabi's speech corpus](http://en.arabicspeechcorpus.com/)


## Background
In April 2017, Google published a paper, [Tacotron: Towards End-to-End Speech Synthesis](https://arxiv.org/pdf/1703.10135.pdf),
where they present a neural text-to-speech model that learns to synthesize speech directly from
(text, audio) pairs. However, they didn't release their source code or training data. This is an attempt to provide an open-source implementation of the model described in their paper.

This implementation is pretty much the same as [Keithito's implemetation](https://github.com/keithito/tacotron). Here are [changes](#changes) I made.

Check this article to know more about this project [Arabic-Tacotron-TTS](https://yousof.net/Arabic-Tacotron-Text-To-Speech/)


## Quick Start
### Installing dependencies

1. Install Python 3. Use version 3.5 instead of newer python versions for tensorflow support. You could use anaconda to create a new environment by 
    1. `conda create  -n myenv python=3.5 `
    2. `activate myenv`

2. Install requirements:
   `pip install -r requirements.txt`

3. Install tensorflow   
   * `pip install tensorflow` or `pip install tensorflow-gpu`
  
### Using a pre-trained model

1. **Download and unpack the [pretrained model](https://drive.google.com/file/d/1c8VaKKKBdhqiwQWvC2K5ut18RKoNfpgg/view?usp=sharing)**
   
2. Extract the model files into a folder in a destination of your choice
   
3. **Run the demo server**:
   `python demo_server.py --checkpoint .\{folder_in_a_destination_of_your_choice}\model.ckpt-200000`

4. **Point your browser at localhost:9200**
   * Type what you want to synthesize. Use only diacritised Arabic text.

### Training
*Note: you need 40GB (more or less) of free disk space to train a model.*
1. **Download a speech dataset.**
   The following are supported out of the box:
    * [Nawar Halabi](http://en.arabicspeechcorpus.com/)
   You can use other datasets if you convert them to the right format. See [TRAINING_DATA.md](TRAINING_DATA.md) for more info.

2. Preprocess
    *  **Unpack the [dataset](http://en.arabicspeechcorpus.com/)`**
    * Add a folder called nawar_without_hag9 in `~/tacotron`
        * Download [temp_filtered.csv](https://drive.google.com/open?id=1oAXqIDRVN8wNPuq83ZlV02Z7qWRTJ1TA) and add it there.
        * Add a folder called wavs there in which all wav files are there
    Your tree should look like this
    ```
    tacotron
        |- nawar_without_hag9
            |- temp_filtered.csv
            |- wavs
    ```
    * Run `python .\preprocess.py --dataset nawar`
    * Update max_iters to 400 if not already set to that number

3. Train
    * `python .\train.py`

4. **Monitor with Tensorboard** (optional)
    The trainer dumps audio and alignments every 1000 steps. You can find these in `~/tacotron/logs-tacotron`. You could use tensorboard to make sense out of these data using the following command.
   `tensorboard --logdir ~/tacotron/logs-tacotron`

## <a name="changes"></a> Changes from the original repo
1. Added Arabic speech corpus preprocessing code and created temp_filtered.csv
2. Hosted Arabic trained model based on Nawar Halabi's Speech Corpus
3. Updated hparams to work with the Arabic speech corpus
4. Added an instructional explanation on how to reproduce
5. Added Arabic specific tests
6. Removed some of the unused code
7. Updated symbols to match the Arabic phonetic language
8. Adjusted data-feeder so that all input text are phonetised by [arabic_pronounce](https://github.com/youssefsharief/arabic_pronounce)

## Areas of Improvement
* Add cleaners
* Add embedded diacritiser

## Summary of important commands 
* python .\preprocess.py --dataset nawar
* python .\train.py --restore_step 201000
* python .\demo_server.py --checkpoint C:\Users\User\tacotron\logs-tacotron\model.ckpt-70000
* python -m pytest

## Notes
Remember to delete the files in the training folder then preprocess again if you changed the config


## Thanks to
Suhail Kwailat, Dr. Taha Zerrouki, Dr. Motaz Saad, Dr. Nawar Halabi, Keith Ito, Dr. Basem Ahmed, and Leo Ma for their detailed feedback and recommendations.
