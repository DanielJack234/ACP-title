input("Double loop at n = 4 took 10 steps. Watch it grow. press Enter")
for  n in [10, 100, 1000]
    input("n = " + str(n) + ". Press Enter to run")
    print("step =", n * (n + 1) // 2)
    