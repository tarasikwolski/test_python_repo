from oop_training_1_290820.my_cat import MyCat

def make_cat_list():
    cat1 = MyCat("Mruczek")
    cat2 = MyCat("Patus")
    cat3 = MyCat("Puszek")
    cats = [cat1,cat2, cat3]

    for cat in cats:
        cat.make_sound()