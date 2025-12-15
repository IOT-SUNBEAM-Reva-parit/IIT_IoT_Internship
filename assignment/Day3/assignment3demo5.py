def great(name="user"):
    print("Hello", name)
    freet("Reva")
    greet()
    
    
    def calculate(amount, rate=5):
        interest = (amount * rate) / 100
        print("Interest:", interest)
        
        calculate(1000)
        calculate(1000, 10)
        
        def student(name, age, city):
            print(name, age, city)
            student(name="Akash", age=25, city="Pune")
            student(city="Mumbai", name="Reva", age=20)
            
            def display(a,b,c):
                print(a,b,c)
                display(10, c=30, b=20)
                
                def add(a,b):
                    return a + b
                def operate(func, x, y):
                    result = func, (x, y)
                    print("Result:", result)
                    operate(add, 5, 3)
                    
                    def multiply(a,b):
                        return a * b
                    operate(multiply, 4, 6)
                    
    