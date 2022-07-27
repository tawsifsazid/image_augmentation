import sys
from definitions import ROOT_DIR, load_img_path, save_img_path, save_label_path # configure all the paths here
from preprocessing import augment

def help():
    print('\n\ncommand formats/options:\nmain.py \nimg_type: (str), choose from: "jpg", "png" \ngenerate: (int) how many image per sample\nchoose_augment_methods_randomly: (str), choose from: "T","F" '
    '\nspecify method(if ''choose_augment_methods_randomly'' is "F"): (str), choose from:"rotate","blur","occlusion","brightness","contrast","distortion"\n')

if __name__ == '__main__':
    print('number of arguments = {}'.format(len(sys.argv)))
    print(sys.argv)
    if len(sys.argv) != 5:
        print('error number of arguments must be 5')
        help()
        sys.exit()
    load_img = sys.argv[1]
    generate_number = sys.argv[2]
    choose_method_randomly = sys.argv[3]
    specify = sys.argv[4]
    #print(type(generate_number))
    if load_img != 'jpg' and load_img != 'png':
        print('error: "img_type" image format should be "jpg" or "png"')
        help()
        sys.exit()
    load_img = '*.{}'.format(load_img)
    if not str.isdigit(generate_number):
        print('error: "generate" must be an integer')
        help()
        sys.exit()
    generate_number = int(generate_number)
    if choose_method_randomly != 'T' and choose_method_randomly != 'F':
        print('error: "choose_augment_methods_randomly" must be "T"/"F"')
        help()
        sys.exit()
    methods = []
    if choose_method_randomly != 'T':
        if specify == 'rotate':
            methods = [1]
        elif specify == 'occlusion':
            methods = [2]
        elif specify == 'brightness':
            methods = [3]
        elif specify == 'contrast':
            methods = [4]
        elif specify == 'blur':
            methods = [5]
        elif specify == 'distortion':
            methods = [6]
        else:
            print('error: "specify method" must be "rotate","blur","occlusion","brightness","contrast" or "distortion"')
            help()
            sys.exit()
    else:
        methods = [1, 2, 3, 4, 5, 6]
    augment.run_augmentation(load_img_path, save_img_path, save_label_path, load_img, generate_number, methods)

# img type loading, koyta img generate korbe, randomly choose method: false hole, Specify