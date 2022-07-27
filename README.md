# image_augmentation
augment image data by using different augmentation techniques and save for training.


1. create an environment with conda and install the dependencies using:
    `pip install requirements.txt`

2. run python main.py with 4 arguments to start augmentation:
   
    1. img_type: (str), choose from: "jpg", "png".
   
    2. generate: (int) how many image per sample.
    
    3. choose_augment_methods_randomly: (str), choose from: "T","F".
    
    4. specify method(if 'choose_augment_methods_randomly' is "F"): (str), choose from:"rotate","blur","occlusion","brightness","contrast","distortion". If the 3rd argument is "T" or True then the pipeline will use all the available augmentation techniques.
    

