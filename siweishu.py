with open("四位数.txt", "w") as f:
    for i in range(10000):
        f.write(f"{i:04d}
")
