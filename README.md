



* python .\preprocess.py --dataset nawar
* python .\train.py --restore_step 201000
* python .\demo_server.py --checkpoint C:\Users\User\tacotron\logs-tacotron\model.ckpt-70000
* python -m pytest

Remember to delete the files in training folder then preprocess again if you changed the config
