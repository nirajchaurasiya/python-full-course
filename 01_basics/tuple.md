Niraj Chaurasiya@ROBOTICS-DESKTOP MINGW64 /p/python-full-course
$ python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec 7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > tea_types = ("Black","Green","Oolong")
> > > tea_types
> > > ('Black', 'Green', 'Oolong')
> > > tea_types[0]
> > > 'Black'
> > > tea_types[-1]
> > > 'Oolong'
> > > tea_types[-2]
> > > 'Green'
> > > tea_types[-3]
> > > 'Black'
> > > tea_types[-4]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > IndexError: tuple index out of range
> > > tea_types[-1]
> > > 'Oolong'
> > > tea_types[0]  
> > > 'Black'
> > > tea_types[0] = "Lemon"
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: 'tuple' object does not support item assignment
> > > len(tea_types)
> > > 3
> > > more_tea = ("Herbal","Earl Grey")
> > > all_tea = more_tea + tea_types
> > > all_tea
> > > ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
> > > if "Green" in all_tea:
> > > ... print("Green is there in the list")
> > > ...
> > > Green is there in the list
> > > more_tea = ("Herbal","Earl Gray","Herbal")
> > > more_tea.count("Herbal")
> > > 2
> > > more_tea.count("Herb")  
> > > 0
> > > tea_types
> > > ('Black', 'Green', 'Oolong')
> > > (black,green,Oolong) = tea_types
> > > black
> > > 'Black'
> > > green
> > > 'Green'
> > > Oolong
> > > 'Oolong'
> > > type(tea_types)
> > > <class 'tuple'>
> > > ("",(1,2,3),"")
> > > ('', (1, 2, 3), '')
