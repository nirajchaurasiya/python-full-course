Niraj Chaurasiya@ROBOTICS-DESKTOP MINGW64 /p/python-full-course
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec 7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > chai_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
> > > chai_types["Spicy"]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > KeyError: 'Spicy'
> > > chai_types["Masala"]
> > > 'Spicy'
> > > chai_types.get("Ginger")
> > > 'Zesty'
> > > chai_types.get("Gingery")
> > > chai_types.get("Masalaa")
> > > chai_types  
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
> > > chai_types["Green"] = "Fresh"
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
> > > for chai in chai_types:
> > > ... print(chai)  
> > > ...
> > > Masala
> > > Ginger
> > > Green
> > > for chai in chai_types:
> > > ... print(chai,chai_types[chai])
> > > ...
> > > Masala Spicy
> > > Ginger Zesty
> > > Green Fresh
> > > for chai in chai_types:
> > > ... for chai in chai_types:
> > > KeyboardInterrupt
> > >
> > > KeyboardInterrupt
> > > for key, values in chai_types:
> > > ...  
> > > KeyboardInterrupt
> > >
> > > KeyboardInterrupt
> > > for key, values in chai_types.items():
> > > ... print(key,values)
> > > ...
> > > Green Fresh
> > > for key, value in chai_types.items():
> > > ... print(key,value)
> > > ...
> > > Masala Spicy
> > > Ginger Zesty
> > > Green Fresh
> > > if "Masala" in chai_types:
> > > ... print("I have masala chai")
> > > ...
> > > I have masala chai
> > > print(len(chai_types))
> > > 3
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
> > > chai_types["Earl Grey"] = "Citrus"
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
> > > chai_types.pop("Earl Grey")
> > > 'Citrus'
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
> > > chai_types.popitem()
> > > ('Green', 'Fresh')
> > > chai_types
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty'}
> > > del chai_types["Ginger"]
> > > chai_types
> > > {'Masala': 'Spicy'}
> > > chai_types_copy = chai_types.copy()
> > > chai_types_copy
> > > {'Masala': 'Spicy'}
> > > tea_shop = {
> > > ... "chai":{"Masala":"Spicy","Ginger":"Zesty"},
> > > ... "Tea":{"Green":"Mild","Black":"Strong"}
> > > ... }
> > > tea_shop
> > > {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}  
> > > print(tea_shop)
> > > {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}  
> > > print(tea_shop("Masala"))
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: 'dict' object is not callable
> > > print(tea_shop["Masala"])
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > KeyError: 'Masala'
> > > tea_shop["Masala"]  
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > KeyError: 'Masala'
> > > tea_shop["Masala"]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > KeyError: 'Masala'
> > > tea_shop["chai"]  
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty'}
> > > tea_shop["chai"]["Tea"]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > KeyError: 'Tea'
> > > tea_shop["chai"]["Ginger"]
> > > 'Zesty'
> > > square_nums = [x**2 for x in range(10)]
> > > square_nums
> > > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> > > square_nums = {x**2 for x in range(10)}
> > > square_nums
> > > {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
> > > square_nums = {x:x**2 for x in range(10)}
> > > square_nums
> > > {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
> > > square_nums.clear()
> > > square_nums
> > > {}
> > > keys = ["Masala","Ginger","Lemon"]
> > > keys
> > > ['Masala', 'Ginger', 'Lemon']
> > > default_value = "Delicious"
> > > new_dict = dict.fromkeys(keys,default_value)
> > > new_dict  
> > > {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
> > > new_dict = dict.fromkeys(keys,keys\)  
> > >  File "<stdin>", line 1

    new_dict = dict.fromkeys(keys,keys\)
                                       ^

SyntaxError: unexpected character after line continuation character

> > > new_dict = dict.fromkeys(keys,keys)  
> > > new_dict
> > > {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
