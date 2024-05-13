> > > tea_varieties = ["Lemon","Masala","Mint","White","Oolong"]
> > > print(tea_varieties)
> > > ['Lemon', 'Masala', 'Mint', 'White', 'Oolong']
> > > print(tea_varieties[0])
> > > Lemon
> > > print(tea_varieties[1])
> > > Masala
> > > print(tea_varieties[-1])
> > > Oolong
> > > print(tea_varieties[1])
> > > Masala
> > > print(tea_varieties[1:3])
> > > ['Masala', 'Mint']
> > > print(tea_varieties[:2])
> > > ['Lemon', 'Masala']
> > > print(tea_varieties[2:])
> > > ['Mint', 'White', 'Oolong']
> > > tea_varieties[3]
> > > 'White'
> > > tea_varieties[3] = "Herbal"
> > > tea_varieties
> > > ['Lemon', 'Masala', 'Mint', 'Herbal', 'Oolong']
> > > print(tea_varieties)
> > > ['Lemon', 'Masala', 'Mint', 'Herbal', 'Oolong']
> > > tea_varieties[1:2] = "Black"
> > > print(tea_varieties)
> > > ['Lemon', 'B', 'l', 'a', 'c', 'k', 'Mint', 'Herbal', 'Oolong']
> > > tea_varieties = ["Lemon","Masala","Mint","White","Oolong"]
> > > tea_varieties[1:2]
> > > ['Masala']
> > > tea_varieties[1:2] = ["Lemon"]
> > > print(tea_varieties)
> > > ['Lemon', 'Lemon', 'Mint', 'White', 'Oolong']
> > > tea_varieties[1:3]
> > > ['Lemon', 'Mint']
> > > tea_varieties[1:3] = ["Black","Masala"]
> > > print(tea_varieties)
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong']
> > > tea_varieties
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong']
> > > tea_varieties[1:1  
> > > ...
> > > KeyboardInterrupt
> > > tea_varieties[1:1]
> > > []
> > > tea_varieties[1:1] = ["Test","Test"]
> > > tea_varieties[1:1]
> > > []
> > > tea_varieties  
> > > ['Lemon', 'Test', 'Test', 'Black', 'Masala', 'White', 'Oolong']
> > > tea_varieties[1:2]
> > > ['Test']
> > > tea_varieties[1:3]
> > > ['Test', 'Test']
> > > tea_varieties[1:3] = []
> > > tea_varieties  
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong']
> > > tea_varieties  
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong']
> > > for tea in tea_varieties:
> > > ... print(tea)
> > > ...
> > > Lemon
> > > Black
> > > Masala
> > > White
> > > Oolong
> > > for tea in tea_varieties:
> > > ... print(tea, end="-")
> > > ...
> > > Lemon-Black-Masala-White-Oolong->>>
> > > tea_varieties
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong']
> > > if "Oolong" in tea_varieties:
> > > ... print("I have Oolong tea")
> > > ...
> > > I have Oolong tea
> > > tea_varieties.append("Test")
> > > tea_varieties
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong', 'Test']
> > > tea_varieties
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong', 'Test']
> > > tea_varieties.pop()
> > > 'Test'
> > > tea_varieties
> > > ['Lemon', 'Black', 'Masala', 'White', 'Oolong']
> > > tea_varieties.remove("black")
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > ValueError: list.remove(x): x not in list
> > > tea_varieties.remove("Black")
> > > tea_varieties
> > > ['Lemon', 'Masala', 'White', 'Oolong']
> > > tea_varieties
> > > ['Lemon', 'Masala', 'White', 'Oolong']
> > > tea_varieties.insert(1,"Green")
> > > tea_varieties
> > > ['Lemon', 'Green', 'Masala', 'White', 'Oolong']
> > > tea_varieties_copy = tea_varieties.copy()
> > > tea_varieties_copy
> > > ['Lemon', 'Green', 'Masala', 'White', 'Oolong']
> > > tea_varieties_copy.append("Ginger")
> > > tea_varieties_copy
> > > ['Lemon', 'Green', 'Masala', 'White', 'Oolong', 'Ginger']  
> > > tea_varieties
> > > ['Lemon', 'Green', 'Masala', 'White', 'Oolong']
> > > squared_nums = [x**2 for x in range(10)]
> > > squared_nums
> > > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
