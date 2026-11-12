def main():
    # Remove pass with your answer.
        num = int(input("input a int:"))
        if num % 10 == 0 and num % 3 != 0:
            print(str(num) + " is divisible by 10 and not divisible by 3.")
        else :
            print(str(num) + " is not divisible by 10 or divisible by 3.") 

if __name__ == "__main__":
    # execute only if run as a script
    main()
